# Responsible AI and safe use

Medifind AI is a healthcare information discovery directory. It is not a clinical decision-support system, diagnosis service, treatment recommender, or substitute for a qualified clinician.

## User recommendations

1. **Confirm details directly with the provider.** Contact the hospital before travel to check its address, contact number, doctor roster, service, hours, and current operational status.
2. **Do not use this app for emergencies.** Search relevance, records, and published/transcribed hours are not an emergency response. Contact local emergency services or go to an appropriate emergency facility.
3. **Treat qualifications and provisional records cautiously.** The app displays source status, notes, and provisional warnings but does not validate credentials. Ask the provider to confirm a clinician's current affiliation and qualifications.
4. **Do not infer live availability.** Listed services, hours, capacity, and equipment are not live feeds. Never infer an available doctor, bed, device, medicine, or appointment from these records.

## Application safeguards

- Search returns directory records; it does not prescribe, diagnose, triage symptoms, or make medical recommendations.
- Relevance is a text-similarity aid, not a quality ranking or endorsement. UI copy makes this distinction explicit.
- Low/no matches produce an empty state rather than an invented provider or unsupported answer.
- Source links, supplied verification fields, and record notes remain visible. Provisional records are labeled.
- Empty files, missing values, and absent records are handled without fabricating replacements.
- No fake reviews, testimonials, ratings, or performance claims are included.
- No paid service, external generative model, API key, or live provider integration is required.

## Known limitations

Similarity is lexical and may miss spelling variants or map terms imperfectly. Data quality and freshness depend on the supplied CSVs. The app does not verify source URLs, credentials, identities, or information changes. A future production release should establish a documented data-owner review process, date-stamped provenance and change history, accessibility/user testing, privacy/security review, and a governed correction channel before public healthcare use.
