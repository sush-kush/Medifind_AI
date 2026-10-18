from pathlib import Path
import pandas as pd
from src.data import load_data, join_hospitals, verification_label
from src.search import search_hospitals, search_doctors, search_services, ai_search, normalize_query

DATA = Path(__file__).resolve().parents[1] / "data"

def test_expected_files_and_real_records():
    d=load_data(DATA)
    assert len(d["hospitals"]) == 5
    assert len(d["doctors"]) == 17
    assert len(d["services"]) == 107
    assert set(["hospitals","doctors","services","hours","quality","dictionary"]).issubset(d)

def test_child_records_join_to_canonical_hospital():
    d=load_data(DATA)
    out=join_hospitals(d["doctors"],d["hospitals"])
    assert len(out)==len(d["doctors"])
    assert out["parent_hospital_name"].notna().all()

def test_search_by_real_terms():
    d=load_data(DATA)
    assert not search_hospitals(d,"government").empty
    assert not search_doctors(d,"orthopaedics").empty
    assert not search_services(d,"radiodiagnosis").empty

def test_natural_language_alias_and_entity():
    d=load_data(DATA)
    assert "paediatrics" in normalize_query("Find a paediatrician in Kolar")
    kind,results=ai_search(d,"Show doctors related to orthopaedics")
    assert kind=="doctors" and not results.empty

def test_empty_and_unmatched_queries_are_graceful():
    d=load_data(DATA)
    assert search_doctors(d,"").empty
    _, results=ai_search(d,"zzqxv non-existent specialty")
    assert results.empty

def test_missing_files_and_values_are_supported(tmp_path):
    d=load_data(tmp_path)
    assert all(frame.empty for frame in d.values())
    sparse={"hospitals":pd.DataFrame(),"doctors":pd.DataFrame(columns=["doctor_name"]),"services":pd.DataFrame()}
    assert search_hospitals(sparse,"Kolar").empty

def test_provisional_status_is_not_presented_as_verified():
    d=load_data(DATA)
    out=join_hospitals(d["doctors"],d["hospitals"])
    hope=out[out.parent_hospital_name.eq("Hope Hospital")]
    assert not hope.empty
    assert any("provisional" in verification_label(r).lower() or "verify" in verification_label(r).lower() for _,r in hope.iterrows())
