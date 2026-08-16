# AIAP v6.5 Machine-Readable Assurance Record

This directory contains the Draft 2020-12 JSON Schema, a Lane 2A worked example, a comprehensive four-route example, and a version-matched structural-plus-semantic validator.

## Validate

```bash
python -B validate_aiap_record.py AIAP_Assessment_Assurance_Record_v6.5.example.json
python -B validate_aiap_record.py AIAP_Assessment_Assurance_Record_v6.5.example_all_lanes.json
python -B -m unittest -v test_validate_aiap_record.py
```

The validator checks schema legality plus cross-field rules that portable JSON Schema cannot fully express: lane/object compatibility, exact G01-G13 coverage, affirmative gate status, assurance-composition arithmetic, Lane 2B non-certification, competence-profile key correspondence, and high-stakes group attribution.

A PASS establishes machine coherence only. It does not establish empirical validity, legal compliance, institutional authority, or conformance for a real programme.

`-B` suppresses Python bytecode output so verification does not mutate the extracted release tree. The independent release verifier additionally ignores only a narrow allow-list of runtime/editor artifacts while requiring exact coverage of every governed release file.
