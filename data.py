from __future__ import annotations
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
FILES = {
    "hospitals": "hospitals.csv", "doctors": "doctors.csv", "services": "services.csv",
    "hours": "hospital_hours_capacity.csv", "dictionary": "data_dictionary.csv",
    "quality": "data_quality_notes.csv",
}

def load_data(data_dir: str | Path = DATA_DIR) -> dict[str, pd.DataFrame]:
    """Load each available project CSV. Missing files return empty frames gracefully."""
    root = Path(data_dir)
    result = {}
    for key, filename in FILES.items():
        path = root / filename
        try:
            result[key] = pd.read_csv(path, keep_default_na=True) if path.is_file() else pd.DataFrame()
        except (OSError, pd.errors.ParserError, UnicodeDecodeError):
            result[key] = pd.DataFrame()
    return result

def text(value) -> str:
    return "" if pd.isna(value) else str(value).strip()

def join_hospitals(frame: pd.DataFrame, hospitals: pd.DataFrame) -> pd.DataFrame:
    """Enrich child records through hospital_id; use canonical hospital name where available."""
    if frame.empty or hospitals.empty or "hospital_id" not in frame or "hospital_id" not in hospitals:
        return frame.copy()
    h = hospitals[[c for c in ["hospital_id", "hospital_name", "hospital_type", "city", "website", "source_url", "data_status", "notes"] if c in hospitals]].copy()
    h = h.rename(columns={c: f"parent_{c}" for c in h.columns if c != "hospital_id"})
    out = frame.drop(columns=["hospital_name"], errors="ignore").merge(h, how="left", on="hospital_id", validate="many_to_one")
    if "parent_hospital_name" in out:
        out["hospital_name"] = out["parent_hospital_name"].fillna("")
    return out

def is_provisional(record: pd.Series) -> bool:
    values = " ".join(text(record.get(c, "")) for c in ["verification_status", "data_status", "notes", "parent_data_status"]).lower()
    return any(term in values for term in ["provisional", "needs_source_verification", "pending"])

def verification_label(record: pd.Series) -> str:
    if is_provisional(record):
        return "Provisional — verify before relying"
    value = text(record.get("verification_status", "")) or text(record.get("data_status", ""))
    if not value:
        return "Not specified"
    if any(x in value.lower() for x in ["verified", "handled"]):
        return f"Source status: {value} (not a live verification)"
    return f"Published/source status: {value}"

def available(value) -> bool:
    return bool(text(value))
