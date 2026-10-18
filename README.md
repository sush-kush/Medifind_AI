# 🏥 Medifind AI — Kolar Healthcare Discovery

**IBM Z Datathon 2026 | SSF2026 | Team Nuvyra**

Medifind AI is a healthcare discovery prototype built with **Python and Streamlit**. It brings hospital and doctor directory information into one place and uses AI-assisted text search to help users discover potentially relevant healthcare records more easily.

> **Responsible use:** Medifind AI is a directory and discovery prototype. It does not diagnose, prescribe, guarantee live availability, or replace professional medical advice or emergency services.

---

## 👥 Team Nuvyra

- **Sushmitha M**
- **Rudranamma A S**
- **Hemavathi D S**
- **S Vikas**

---

# 🚨 The Real-World Problem

Imagine a family member suddenly needs medical attention.

In a stressful situation, the family may need to quickly find a suitable hospital, locate a specialist such as a dermatologist or cardiologist, or understand which healthcare services may be available nearby.

But healthcare information can be scattered across different listings and sources.

People may have to spend time searching through multiple pages just to find basic information about hospitals, doctors, specializations, services, operating hours, or capacity.

When someone is already under pressure, **time spent searching for information can add to the stress of the situation.**

The problem is not always the absence of healthcare resources. Sometimes, it is the difficulty of **discovering the relevant information quickly and in one place.**

This inspired our team to ask:

> **What if healthcare information discovery could be simpler, more organised, and faster?**

---

# 💡 Our Solution — Medifind AI

**Medifind AI** provides a single interface for exploring the healthcare directory data available to the project.

Users can:

- 🏥 Explore hospital information
- 👨‍⚕️ Search doctor records
- 🩺 Explore medical specializations
- 🔎 Search healthcare information using natural text queries
- 🎯 Apply filters to narrow down available records
- 📊 View charts and data-completeness summaries
- 🕒 Explore operating-hours and capacity information where available

Instead of manually searching through separate lists, users can explore relevant healthcare records through one organised interface.

Our goal is to **reduce the time spent searching for healthcare information and make relevant records easier to discover.**

---

# 🤖 AI-Assisted Search

Medifind AI combines **keyword matching with text similarity** to identify potentially relevant records.

### How it works

**User Query → Text Processing → TF-IDF → Cosine Similarity + Keyword Matching → Relevant Records**

### TF-IDF

**TF-IDF (Term Frequency–Inverse Document Frequency)** converts text into numerical representations based on the importance of words within the available records.

### Cosine Similarity

Cosine similarity compares the numerical representation of the user's query with available healthcare records and provides a similarity measure.

This allows the system to identify potentially relevant records without depending entirely on exact keyword matches.

### Example

A user can search:

> **"dermatologist in Kolar"**

The system uses the available healthcare data to identify records that may be relevant to the query.

The search result is a **relevance signal**, not a medical recommendation or guarantee that a doctor or service is currently available.

---

# 🖥️ Key Features

- Searchable hospital and doctor directories
- AI-assisted text search
- TF-IDF and cosine-similarity text matching
- Keyword matching
- Filters for exploring available records
- Hospital information
- Related capacity and operating-hours information where available
- Charts and data-completeness summaries
- Missing-data handling
- Responsible-use notices

---

# 🏗️ Solution Architecture

```text
                    USER
                      │
                      ▼
             ┌─────────────────┐
             │ Streamlit UI    │
             │ Search + Filters│
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Search Logic    │
             │                 │
             │ Keyword Match   │
             │ TF-IDF          │
             │ Cosine Similarity│
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Healthcare Data │
             │                 │
             │ Hospitals       │
             │ Doctors         │
             │ Hours/Capacity  │
             │ Data Dictionary │
             │ Quality Notes   │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Relevant Records│
             │ + Visualizations│
             └─────────────────┘
```

---

# ☁️ IBM Z / LinuxONE

Medifind AI was **developed and tested in an IBM LinuxONE environment** as part of the IBM Z Datathon 2026.

LinuxONE provided the computing environment used for developing and testing our Python-based healthcare discovery application.

The prototype uses open-source technologies including:

- Python
- Streamlit
- Pandas
- scikit-learn
- Plotly

The current prototype does **not** claim production deployment, IBM watsonx API integration, or specialized hardware acceleration.

Future development could explore IBM Z/LinuxONE capabilities for:

- Secure and scalable hosting
- Access control
- Enterprise-grade deployment
- Monitoring and reliability
- Integration with verified healthcare data sources

This provides a potential path from a prototype toward a more reliable healthcare information platform.

---

# 📊 Data and Evaluation

The current prototype uses structured CSV datasets.

The repository currently contains:

- `hospitals.csv`
- `doctors.csv`
- `hospital_hours_capacity.csv`
- `data_dictionary.csv`
- `data_quality_notes.csv`

### Data Quality

Search quality depends strongly on the quality of the underlying data.

Important areas for improvement include:

- Missing-value detection
- Duplicate-record detection
- Consistent naming and categories
- Source verification
- Regular data updates
- Tracking data provenance and update dates

### Precision and Recall

Future evaluation will use labelled search queries to measure:

**Precision:** How many returned records are actually relevant?

**Recall:** How many of the relevant records were successfully retrieved?

Testing multiple similarity thresholds can help identify an appropriate balance between returning useful results and reducing irrelevant matches.

We do not claim measured precision, recall, or a validated threshold unless supported by actual evaluation results.

---

# 🛡️ Responsible AI

Healthcare information requires careful handling.

Our responsible-AI approach includes:

### 1. Data Verification

Healthcare records should come from trusted sources and be regularly reviewed and updated.

### 2. Transparency

Users should understand that search results are generated from the available dataset and may be incomplete or outdated.

### 3. Privacy

The system should avoid collecting unnecessary personal or sensitive health information.

### 4. Human Oversight

Search results should support information discovery, while healthcare decisions should remain with qualified healthcare professionals.

### 5. Avoiding Medical Claims

Medifind AI does not diagnose diseases, prescribe treatments, or recommend medical procedures.

### 6. Emergency Safety

Medifind AI is not an emergency-response system. During a medical emergency, users should contact appropriate local emergency services and seek professional medical assistance.

---

# ⚠️ Current Limitations

- The prototype depends on the healthcare data available in the repository.
- The information may be incomplete or require independent verification.
- The application does not provide verified real-time hospital or doctor availability.
- Search relevance depends on query wording, available text, and the similarity threshold.
- A separate `services.csv` file is not currently included in the repository, so service-search results may be limited or empty.
- The prototype is not intended for diagnosis, treatment decisions, or emergency response.

---

# 🚀 Future Improvements

We plan to improve Medifind AI by:

- Adding a validated healthcare-services dataset
- Integrating verified provider availability through authorised data sources
- Improving data validation and update tracking
- Evaluating search performance using labelled queries
- Reporting precision and recall
- Optimising the similarity threshold using evaluation results
- Improving accessibility and user experience
- Strengthening privacy and responsible-AI safeguards
- Exploring secure and scalable deployment on IBM Z/LinuxONE

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Application and search logic |
| **Streamlit** | Interactive web interface |
| **Pandas** | Data loading and processing |
| **scikit-learn** | TF-IDF and cosine similarity |
| **Plotly** | Data visualization |
| **CSV** | Structured healthcare datasets |
| **IBM LinuxONE** | Development and testing environment |

---

# 📁 Project Structure

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

---

# ▶️ Run Locally

**Python 3.10–3.12 is recommended.**

### 1. Clone or download the repository

```bash
git clone https://github.com/sush-kush/Medifind_AI.git
cd Medifind_AI
```

### 2. Create a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

---

# 🧪 Run Tests

```bash
pytest -q
```

---

# 🌐 Project Links

**GitHub Repository:**  
https://github.com/sush-kush/Medifind_AI

**Pitch Video:**  
https://youtu.be/VGg--Y4wg38

---

# 👥 Team Nuvyra

**Sushmitha M | Rudranamma A S | Hemavathi D S | S Vikas**

### IBM Z Datathon 2026 — SSF2026

> **“In healthcare, every second matters — let technology make finding the right help simpler.”**

---
