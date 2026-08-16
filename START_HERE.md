# START HERE — AIAP v6.5

## Release identity

**Artificial Intelligence Assurance Protocol (AIAP) Release 6.5**  
Canonical date: **14 August 2026**  
Publication build: **AIAP-v6.5+2026.08.15.1** (release-engineering hardening only; no semantic change)  
Canonical paper: **From Task Design to Claim-Level Assurance**

AIAP v6.5 is the finalized canonical publication release. It preserves the four lanes, six-stage protocol, evidence-plan authority rule, five-figure visual system, and empirical-status boundary while completing the final cross-format, research-sequencing, pilot-instrument, workload, normative-gate, licensing, and publication-engineering corrections.

## Recommended reading order

1. `01_CORE_PAPER/AIAP_Core_Working_Paper_v6.5.pdf`
2. `02_NORMATIVE_STANDARD/AIAP_Normative_Assurance_Standard_v6.5.pdf`
3. `03_IMPLEMENTATION/AIAP_Implementation_Handbook_v6.5.pdf`
4. The version-matched implementation, pilot, and workbook instruments.
5. `06_MACHINE_READABLE/AIAP_Machine_Readable_Validation_README_v6.5.md`
6. `08_VERIFICATION/VERIFICATION_STATUS.md`

## Folder map

- `01_CORE_PAPER` — canonical scholarly paper, editable DOCX, canonical UTF-8 Markdown source, and five figures.
- `02_NORMATIVE_STANDARD` — conformance requirements and Core-to-Standard crosswalk.
- `03_IMPLEMENTATION` — handbook, toolkit, role manual, evidence-governance guide, and pilot-readiness pack.
- `04_PILOT_AND_VALIDATION` — preregistration-ready protocol, data dictionary, prompt bank, exposure log, and form-equivalence instruments.
- `05_WORKBOOKS` — workload, feasibility, and programme-assurance tools.
- `06_MACHINE_READABLE` — JSON Schema, two worked examples, semantic validator, and adversarial tests.
- `07_PUBLICATION` — SSRN metadata/abstract, RippleLogic.org copy, public explainer, website HTML, and release checklist.
- `08_VERIFICATION` — adjudication record, machine report, file manifest, cryptographic hashes, and release verifier.
- Repository metadata (`README.md`, `LICENSE.md`, `CITATION.cff`, `CONTRIBUTING.md`, `SECURITY.md`) is at the release root so the extracted folder can be uploaded directly to GitHub.

## Scientific and authority boundary

AIAP v6.5 is specification-complete for scholarly evaluation and governed pilot preparation. It is **not empirically validated as an integrated institutional intervention**. Machine validation, completed documents, publication, or a conformance claim does not itself authorize high-stakes assessment use, certification, accreditation, or degree/public claims.

## Empirical sequence

- **Phase 1:** bounded feasibility and measurement study, approximately 120 students across two or three modules, with final sample size determined by the primary estimand and precision target.
- **Phase 2:** multi-institution comparative study across at least two and preferably three or more institutions and at least two academic cycles.

## Fast verification

```bash
cd 06_MACHINE_READABLE
python -B -m unittest -v test_validate_aiap_record.py
cd ../08_VERIFICATION
python -B verify_release.py ..
```

`-B` prevents Python bytecode from being written into the extracted release tree. The verifier is also hardened to ignore a narrow allow-list of non-release runtime/editor artifacts (`__pycache__`, `*.pyc`, `.git`, `.DS_Store`, `Thumbs.db`, Office lock files, and `.tmp`/`.bak` files) while continuing to require exact manifest and SHA-256 coverage for every governed release artifact.

## Publication map

- Canonical public page: `https://ripplelogic.org/aiap/`
- GitHub monorepo path: `https://github.com/MathGov/ripple-logic/tree/main/aiap/v6.5`
- GitHub release tag: `AIAP-v6.5`
- Canonical release page: `https://github.com/MathGov/ripple-logic/releases/tag/AIAP-v6.5`
- Canonical ZIP asset: `AIAP_v6.5_COMPLETE_READY_FINAL.zip`

When publishing inside the MathGov `ripple-logic` repository, place the extracted AIAP package under `aiap/v6.5/`; do **not** overwrite the repository-root MathGov `README.md`, `LICENSE.md`, or other Core governance files.
