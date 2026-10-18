# Data sources and limitations

## Supplied source files

The six CSVs in `data/` are included unchanged from the archive provided for this project:

| File | Rows in supplied copy | Purpose |
|---|---:|---|
| `hospitals.csv` | 5 | Hospital profiles, types, place fields, website/source fields, notes and data status |
| `doctors.csv` | 17 | Doctor names, qualifications, specializations, profile/source URLs, verification status and notes |
| `services.csv` | 107 | Hospital-linked service records, categories, listing statuses, source types/URLs and notes |
| `hospital_hours_capacity.csv` | 7 | Reported hours/capacity-style entries with transcription/verification context |
| `data_dictionary.csv` | 7 | Field definitions supplied with the project data |
| `data_quality_notes.csv` | 8 | Known issues, risks, actions and their status |

Rows/counts refer to the delivered archive and are recomputed by the app when loaded. Child tables are linked using `hospital_id`. Hospital names are joined from the canonical hospital table when possible; supplied notes and source fields are retained.

## Provenance and interpretation

This application does not independently validate source pages or conduct field verification. Doctor profile details are marked with their supplied `verification_status` and notes. Hope Hospital doctor records are explicitly provisional in the supplied data and the app labels them as needing verification. Government hospital doctor names are absent when no source record supplies them; the app does not invent names. A dataset value such as `listed_on_website`, a transcribed board detail, or a source URL means only that the project data records that status/source.

No live API is connected. In particular, a service listing is not a confirmation that the service is operational now. Published/transcribed hours, beds/capacity notes, and equipment references do not represent live status, vacancy, stock, or duty rosters. Missing contact details remain missing; no phone numbers or addresses are inferred.

Use the source URLs displayed on each record to perform your own confirmation before visiting or relying on any operational detail. Always contact the hospital directly for current information.
