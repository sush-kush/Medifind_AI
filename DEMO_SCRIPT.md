# Datathon demo script (maximum 3 minutes)

**0:00–0:20 — Problem and solution**  
“Healthcare information is spread across sources, and incomplete data can look more certain than it is. Medifind AI organizes the supplied Kolar directory records and keeps their source and verification context visible.”

**0:20–0:45 — Home and transparency**  
Show the live record counts and search. Point out the notice: no diagnosis or treatment, and no live doctor, bed, or equipment availability.

**0:45–1:25 — Discovery workflows**  
Open Find Hospitals and search “government”. Open a result and show its source, recorded details, related services/hours if present. Then search doctors for “orthopaedics”; explain that a result is a text match, not a quality rank, and point out the verification status.

**1:25–2:00 — AI Search / demo**  
Ask “Which hospitals list radiodiagnosis services?” or click the corresponding example in Discover Medifind AI. Explain that local TF-IDF/cosine similarity and keyword overlap locate matching records without an external AI key or an unsupported recommendation.

**2:00–2:30 — Data quality**  
Show missing-field counts and the data-quality notes. Highlight provisional Hope Hospital doctor information and transcribed hours as information requiring confirmation.

**2:30–2:50 — Architecture and impact**  
Briefly describe CSV → hospital_id join → local search → sourced results. Emphasize locality-first information discovery, modest CPU/resource needs, and a LinuxONE-ready build procedure that still needs validation on actual s390x hardware.

## Suggested dataset-grounded queries

- `Show government hospitals`
- `Find doctors related to orthopaedics`
- `Find a paediatrician`
- `Hospitals with radiodiagnosis services`

All should be run against the included CSVs; visible results depend on the actual records and search routing.

## Screenshot checklist

- Home branding, counts, search field, and safety notice.
- Hospital results with source/status context.
- Doctor result showing qualifications/specialization and verification label.
- Service result showing recorded listing status and non-live warning.
- Discover Medifind AI demo query selected and real result visible.
- Dashboard chart and missing-information summary.

## Submission checklist

- [ ] Include project ZIP and README with local setup and Docker commands.
- [ ] Include all six supplied CSVs, unchanged, plus data provenance documentation.
- [ ] Include test report and note that LinuxONE build/runtime was not tested in the sandbox.
- [ ] Demonstrate information-quality and emergency-use notices.
- [ ] Do not claim live availability, medical recommendations, credential verification, or IBM/Telum acceleration.
- [ ] Verify source pages/records independently before public or operational use.
