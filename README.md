# Medifind AI — Kolar Healthcare Discovery

**IBM Z Datathon 2026 | SSF2026 | Team Nuvyra**

Medifind AI is a healthcare discovery prototype built with Python and Streamlit. It brings hospital and doctor directory information into one place and uses AI-assisted text search to help users discover relevant records more easily.

> **Responsible use:** Medifind AI is a directory and discovery prototype. It does not diagnose, prescribe, guarantee live availability, or replace professional medical advice or emergency services.

## Team Nuvyra

- Sushmitha M
- Rudranamma A S
- Hemavathi D S
- S Vikas

## Problem Statement

People may need to search multiple listings to find relevant hospitals, doctors, and healthcare services. Information can be incomplete, difficult to compare, or not updated in real time.

## Our Solution

Medifind AI provides a single interface for exploring the healthcare directory data available to the project. Users can browse records, apply filters, and use AI-assisted text search to find potentially relevant hospitals, doctors, and services.

## Key Features

- Searchable hospital and doctor directories.
- Filters for exploring available records.
- TF-IDF and cosine-similarity text search, combined with keyword matching.
- Hospital information and related capacity or operating-hours data where available.
- Charts and data-completeness summaries.
- Responsible-use notices and missing-data handling.

**Data limitation:** The current repository contains five CSV files. A separate `services.csv` file is not currently included, so service-search results may be empty. The application does not provide verified live availability.

## Technology Stack

- Python
- Streamlit
- Pandas
- scikit-learn
- Plotly
- CSV datasets

## Project Structure

```text
Medifind_AI/
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── data.py
│   └── search.py
├── data/
│   ├── hospitals.csv
│   ├── doctors.csv
│   ├── hospital_hours_capacity.csv
│   ├── data_dictionary.csv
│   └── data_quality_notes.csv
└── tests/
    └── test_app_core.py
```

## Run Locally

Python 3.10–3.12 is recommended.

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment.
4. Install the dependencies.
5. Start the application.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Run Tests

```bash
pytest -q
```

## Responsible AI and Limitations

- Search results are suggestions based on directory text, not medical recommendations.
- Missing or provisional data can affect the relevance of results.
- The app does not verify provider details or live availability.
- Users should confirm information directly with healthcare providers.
- The app is not intended for diagnosis, treatment decisions, or emergencies.

## Future Improvements

- Add a validated healthcare-services dataset.
- Integrate verified provider availability where an authorised data source is available.
- Evaluate search relevance using labelled examples and report precision and recall.
- Improve data validation, accessibility, and responsible-AI safeguards.
