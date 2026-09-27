# Artificial Intelligence Assurance Protocol (AIAP) v6.5

**From Task Design to Claim-Level Assurance**

AIAP is a claim-level assessment-assurance architecture for AI-mediated higher education. It asks what an assessment genuinely allows an institution to claim about a student, then aligns the claim, evidence-producing condition, assurance route, evidence, decision rule, and programme or public use.

## Start here

1. Read `START_HERE.md`.
2. Read the canonical Core Working Paper in `01_CORE_PAPER`.
3. Use the Normative Assurance Standard in `02_NORMATIVE_STANDARD` for any conformance claim.
4. Use the implementation and pilot instruments only within their stated authority and evidence boundaries.
5. Validate machine-readable records with the tools in `06_MACHINE_READABLE`.

## Four routes

- **Lane 1:** Secured
- **Lane 2A:** Competence-authenticated open
- **Lane 2B:** Open non-certifying
- **Lane 3:** AI-integrated open

The four lanes are assurance or claim-status routes. They are not a scale of increasing AI permission or educational value.

## Validation

```bash
cd 06_MACHINE_READABLE
python -B validate_aiap_record.py AIAP_Assessment_Assurance_Record_v6.5.example.json
python -B validate_aiap_record.py AIAP_Assessment_Assurance_Record_v6.5.example_all_lanes.json
python -B -m unittest -v test_validate_aiap_record.py
```

Run `python -B verify_release.py ..` from `08_VERIFICATION` after extraction. The verifier remains fail-closed for governed release files while ignoring only a narrow allow-list of runtime/editor debris that can be created by Python, Git, the operating system, or Office.

## Publication identity

- Canonical page: `https://ripplelogic.org/aiap/`
- Repository: `https://github.com/MathGov/ripple-logic`
- Monorepo path: `aiap/v6.5/`
- GitHub release tag: `AIAP-v6.5`
- Canonical release asset: `AIAP_v6.5_COMPLETE_READY_FINAL.zip`
- Publication build: `AIAP-v6.5+2026.08.15.1` (release-engineering hardening only; no semantic change)

When AIAP is published in the existing MathGov monorepo, the contents of this package belong under `aiap/v6.5/`. The package-level `README.md`, `LICENSE.md`, and `CITATION.cff` govern the AIAP release subtree; they must not replace repository-root MathGov metadata.

## Status boundary

AIAP v6.5 is specification-complete for scholarly evaluation and governed pilot preparation. It is not empirically validated as an integrated institutional intervention. Publication, conformance documentation, schema validation, or workbook completion does not itself authorize high-stakes use or certify a programme.

## Citation

McGaughran, J. (2026). *From task design to claim-level assurance: The Artificial Intelligence Assurance Protocol for AI-mediated higher education* (AIAP Core Working Paper v6.5).

## Rights

See `RIGHTS_AND_LICENSING.md`. No open-source or Creative Commons license is granted by this release unless the author later issues one explicitly.
