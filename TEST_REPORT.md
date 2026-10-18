# Test report

Executed in the Manus Sandbox on Python 3.12.3, `x86_64`, with dependencies installed from `requirements.txt` into a local virtual environment.

## Results

- **Automated tests:** 7 passed (`pytest -q`). Covers real CSV loading/counts, `hospital_id` joins, hospital/doctor/service searches, query aliasing, unmatched and empty queries, missing files, and provisional warning labels.
- **Demo-query smoke checks:** 4 passed. Government hospitals, orthopaedics doctors, paediatricians, and radiodiagnosis listings each returned matching records; an invented/unmatched test phrase returned no results.
- **Streamlit AppTest:** passed. The home screen rendered; all six navigation destinations loaded without app exceptions; home quick-search callback worked; AI query entry and demo query button completed without app exceptions.
- **Running application:** Streamlit started on port 8517; `GET /_stcore/health` returned HTTP 200 with `ok`; `GET /` returned HTTP 200.
- **Python syntax check:** `py_compile` passed for `app.py`, `src/data.py`, and `src/search.py`.
- **Packaged-project check:** the ZIP extracted into a clean temporary directory and all 7 tests passed from that extracted copy.

## Fixes made during validation

- Fixed pytest import path so tests work from the project root.
- Corrected a provisional label rule so ordinary transcribed profiles with a caveat about unverified credentials are not mislabeled as provisional; explicit provisional/needs-verification records remain visibly flagged.
- Fixed a demo rendering failure caused by joining CSV cells containing missing values; demo examples now use the dataset-grounded set directly.
- Fixed home quick-search state handling using the supported Streamlit callback lifecycle.
- Added plural paediatrician/pediatrician query aliases after a demo smoke check showed plural entity routing was incorrect.
- Tightened the minimum similarity threshold to suppress weak incidental matches.

## Not tested / known limitations

- The available machine is `x86_64`, not IBM LinuxONE `s390x`; Docker is not installed in this sandbox. No container build, s390x dependency resolution, or target-host runtime test was performed. Use the exact LinuxONE instructions in `README.md` and validate on the target server.
- Streamlit AppTest and HTTP health checks were used; no separate interactive browser session or visual screenshot review was performed.
- Streamlit emitted a non-blocking deprecation warning for `use_container_width`; it still runs successfully in the tested version. Future Streamlit upgrades may require replacing it with `width="stretch"`.
- Search is local lexical similarity, not clinical or human-validated semantic reasoning. Supplied source records may be incomplete, stale, or provisional; verify operational details with providers.
