# Medifind AI — Kolar healthcare discovery

A functional, lightweight Streamlit directory app for exploring the supplied hospital, doctor, service, hours/capacity, data dictionary, and data-quality CSVs. Built for the **IBM Z Datathon 2026 / SSF2026** project context. It discovers and explains published records; it does not diagnose, prescribe, assess hospital quality, or provide live availability.

## Features

- Searchable hospital, doctor, and service directories with filters and source links.
- Natural-language-style AI Search using local TF-IDF/cosine similarity plus transparent keyword overlap; no API keys or network model dependency.
- Functional “Discover Medifind AI” demo with dataset-based queries.
- Dynamic record counts, data completeness summaries, and real-data charts.
- Hospital joins via `hospital_id`; source, verification, and provisional notes are retained and surfaced.
- Missing data and missing CSV files degrade gracefully.
- Responsive Streamlit UI with responsible-use notices.

## Run locally

Python 3.10–3.12 is recommended. From this project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Open `http://localhost:8501`. To use another port, replace `8501` in the command. The app binds to all interfaces; expose it only behind an appropriately secured network/reverse proxy.

## Docker (IBM LinuxONE / s390x)

The Dockerfile uses the official Python slim base image, supports build-platform architecture selection, and does not pull x86-only model packages. On the LinuxONE Ubuntu 24.04 host, from the extracted project directory:

```bash
docker build --platform linux/s390x -t medifind-ai:latest .
docker run -d --name medifind-ai --restart unless-stopped -p 127.0.0.1:8502:8501 medifind-ai:latest
```

Port `8502` on host is intentionally used as an example to avoid colliding with a JupyterLab service; change the left-hand port if needed. This maps only to localhost. Put a trusted reverse proxy in front if remote access is required; do not expose Streamlit's port publicly without security controls.

The container listens on internal port `8501` by default. To change it, pass both a `PORT` value and a matching container-side port mapping, for example: `docker run -d --name medifind-ai -e PORT=8600 -p 127.0.0.1:8502:8600 medifind-ai:latest`.

Logs and lifecycle:

```bash
docker logs -f medifind-ai
docker stop medifind-ai
docker start medifind-ai
docker restart medifind-ai
docker rm -f medifind-ai  # only when you intend to remove the container
```

Build dependencies are Python wheels resolved for the target platform at build time. LinuxONE/s390x build and runtime were **not available in this sandbox**, so validate the build on the target host; see `ARCHITECTURE.md`. No IBM-specific acceleration is claimed.

## Tests

```bash
pytest -q
```

Tests cover the supplied record counts, relationships, hospital/doctor/service searches, query alias handling, empty/unmatched queries, missing data files, and provisional labeling. See `TEST_REPORT.md` for the executed results and environment limitations.

## Project map

- `app.py` — Streamlit pages and user interface.
- `src/data.py` — CSV loading, relationship joins, and status labels.
- `src/search.py` — TF-IDF/keyword search and intent routing.
- `data/` — original six user-supplied CSV files.
- `tests/` — automated core tests.
- `DATA_SOURCES.md`, `RESPONSIBLE_AI.md`, `ARCHITECTURE.md` — provenance, safety and technical design.
- `DEMO_SCRIPT.md` — <=3-minute presentation outline, suggested queries and submission checklist.

## Important limitations

The source dataset itself notes missing phone/address fields, unverified/provisional doctor information, and transcribed hours. Verify details with providers. Service listings do not prove current operation; hours/capacity rows are not live. This project is not an emergency resource. If someone may be experiencing an emergency, use local emergency services rather than relying on this directory.
