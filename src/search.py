from __future__ import annotations
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .data import text, join_hospitals

ALIASES = {"paediatrician": "paediatrics", "paediatricians": "paediatrics", "pediatrician": "paediatrics", "pediatricians": "paediatrics", "gynaecology": "obstetrics and gynaecology", "gynecology": "obstetrics and gynaecology", "radiology": "radiodiagnosis", "government hospitals": "government", "children": "paediatrics"}
STOP = {"find", "show", "list", "me", "which", "are", "is", "the", "a", "an", "in", "at", "for", "with", "related", "to", "please", "hospital", "hospitals", "doctor", "doctors", "service", "services"}

def normalize_query(query: str) -> str:
    q = re.sub(r"[^\w\s-]", " ", (query or "").lower())
    for old, new in ALIASES.items():
        q = re.sub(rf"\b{re.escape(old)}\b", new, q)
    return re.sub(r"\s+", " ", q).strip()

def _combined(frame: pd.DataFrame, columns: list[str]) -> list[str]:
    return [" ".join(text(row.get(c, "")) for c in columns if c in frame.columns) for _, row in frame.iterrows()]

def _score(query: str, docs: list[str]):
    if not docs or not query.strip():
        return []
    try:
        vec = TfidfVectorizer(ngram_range=(1, 2), strip_accents="unicode", sublinear_tf=True)
        matrix = vec.fit_transform(docs + [query])
        return cosine_similarity(matrix[-1], matrix[:-1]).ravel().tolist()
    except ValueError:
        return [0.0] * len(docs)

def _search(frame: pd.DataFrame, query: str, columns: list[str], threshold: float = .12, limit: int = 30) -> pd.DataFrame:
    if frame.empty or not query:
        return pd.DataFrame()
    docs = _combined(frame, columns)
    q = normalize_query(query)
    scores = _score(q, docs)
    terms = [t for t in re.findall(r"[\w-]+", q) if t not in STOP and len(t) > 1]
    rows = []
    for idx, (doc, score) in enumerate(zip(docs, scores)):
        low = doc.lower()
        hits = [t for t in terms if t in low]
        # Keyword overlap helps short queries and is shown transparently alongside TF-IDF.
        keyword = len(hits) / max(1, len(terms))
        final = max(score, keyword * .72)
        if final >= threshold:
            item = frame.iloc[idx].copy()
            item["_score"] = float(final)
            item["_tfidf"] = float(score)
            item["_matched_terms"] = hits
            rows.append(item)
    if not rows:
        return pd.DataFrame()
    out = pd.DataFrame(rows).sort_values(["_score", "_tfidf"], ascending=False)
    return out.head(limit).reset_index(drop=True)

def search_hospitals(data: dict, query: str, limit: int = 30) -> pd.DataFrame:
    f = data.get("hospitals", pd.DataFrame()).copy()
    cols = ["hospital_name", "hospital_type", "city", "district", "state", "address", "data_status", "notes"]
    return _search(f, query, cols, limit=limit)

def search_doctors(data: dict, query: str, limit: int = 30) -> pd.DataFrame:
    doctors = data.get("doctors", pd.DataFrame()).copy()
    if doctors.empty: return doctors
    doctors = join_hospitals(doctors, data.get("hospitals", pd.DataFrame()))
    cols = ["doctor_name", "qualifications", "specializations", "additional_training", "hospital_name", "verification_status", "notes"]
    return _search(doctors, query, cols, limit=limit)

def search_services(data: dict, query: str, limit: int = 30) -> pd.DataFrame:
    services = data.get("services", pd.DataFrame()).copy()
    if services.empty: return services
    services = join_hospitals(services, data.get("hospitals", pd.DataFrame()))
    cols = ["service_name", "category", "availability_status", "hospital_name", "hospital_type", "notes"]
    return _search(services, query, cols, limit=limit)

def infer_entity(query: str) -> str:
    q = normalize_query(query)
    if any(x in q for x in ["doctor", "paediatrics", "orthopaedics", "qualification", "specialization", "physician"]): return "doctors"
    if any(x in q for x in ["service", "facility", "radiodiagnosis", "diagnostic", "blood bank", "icu", "laboratory"]): return "services"
    return "hospitals"

def ai_search(data: dict, query: str) -> tuple[str, pd.DataFrame]:
    kind = infer_entity(query)
    funcs = {"hospitals": search_hospitals, "doctors": search_doctors, "services": search_services}
    return kind, funcs[kind](data, query)
