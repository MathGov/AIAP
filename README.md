# Artificial Intelligence Assurance Protocol (AIAP) v6.5

**From Task Design to Claim-Level Assurance**

**Open-publication edition 1 · 28 September 2026.** Original code/schemas are Apache-2.0; author-owned research materials are CC-BY-4.0. [License scope and grant](OPEN_LICENSE_GRANT.md) supersede the original package’s restrictive notices for author-controlled material. Research/specification version: **6.5**, unchanged.

[Read and download](https://ripplelogic.org/aiap/) · [Open release](https://github.com/MathGov/AIAP/releases/tag/AIAP-v6.5-open.1) · [Core paper PDF](01_CORE_PAPER/)


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

For the original frozen ZIP, run `python -B verify_release.py ..` from `08_VERIFICATION` after extraction. The verifier remains fail-closed for governed release files while ignoring only a narrow allow-list of runtime/editor debris that can be created by Python, Git, the operating system, or Office.

## Publication identity

- Project page: https://ripplelogic.org/aiap/
- Standalone repository: https://github.com/MathGov/AIAP
- Current publication tag: `AIAP-v6.5-open.1`
- Original scientific/specification release: `AIAP-v6.5`, build `AIAP-v6.5+2026.08.15.1`
- Original release ZIP remains unchanged. The open bundle adds current licensing and repository guidance without changing the normative research files.

Earlier documents refer to a planned `ripple-logic/aiap/v6.5` monorepo location. That is historical publishing guidance, not the current repository. Use the standalone project above.

## Verification scope

Run `python scripts/verify_publication.py` from this repository to verify preserved governed files and the original archive's checksum. Run the original full verifier against the **original extracted ZIP**, not this maintained repository overlay: repository-level licensing, navigation and automation files have intentionally changed. CI verifies both the frozen original package and preserved research payload. Passing checks does not establish empirical effectiveness or authorization to deploy.

## Status boundary

AIAP v6.5 is specification-complete for scholarly evaluation and governed pilot preparation. It is not empirically validated as an integrated institutional intervention. Publication, conformance documentation, schema validation, or workbook completion does not itself authorize high-stakes use or certify a programme.

## Citation

McGaughran, J. (2026). *From task design to claim-level assurance: The Artificial Intelligence Assurance Protocol for AI-mediated higher education* (AIAP Core Working Paper v6.5).

## Rights

See [OPEN_LICENSE_GRANT.md](OPEN_LICENSE_GRANT.md), [LICENSE.md](LICENSE.md) and [RIGHTS_AND_LICENSING.md](RIGHTS_AND_LICENSING.md). The author has now explicitly issued the open licenses described there.
