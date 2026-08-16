# AIAP Release Notes v6.5

## Release class

Final canonical publication release. No new lane, role, positive assurance object, gate, figure, or unsupported empirical claim has been added.

## Final scholarly corrections

1. Made the empirical sequence explicit: Phase 1 is the bounded feasibility/measurement study; Phase 2 is the multi-institution comparator and transportability study.
2. Harmonized the early misconduct definition with the Lane 2A certification boundary so production delegation is misconduct only when deception or an explicit production/authorship constraint is implicated.
3. Added the architectural rationale for treating non-certifying claim status as a first-class governed decision while retaining the simpler flag model as an empirical comparator.
4. Added two directly relevant sources: Luo (2024) on policy constructions of originality in GenAI assessment, and Dawson and Sutherland-Smith (2018) on the limits of marker detection of contract cheating.
5. Corrected the canonical DOCX correspondence display so the visible address no longer includes the `mailto:` prefix.
6. Removed the residual blank gap in the Markdown reference list.

## Cross-format and operational hardening

1. Confirmed the canonical Markdown source is valid UTF-8 and retains diacritics, en dashes, curly quotation marks, multiplication signs, section symbols, and the copyright symbol.
2. Preserved the Appendix D3 anchor, nested Contents entry, DOCX navigation, and PDF destinations.
3. Corrected percentage/number formatting in the Workload Calculator so accessibility, asynchronous-review, and recording-review inputs display in their intended units.
4. Recalculated all formula-bearing workbooks and verified complete cached formula values.
5. Synchronized all documents, workbooks, schemas, examples, validators, metadata, filenames, and release records to v6.5.
6. Moved GitHub metadata to the release root and added an explicit `LICENSE.md` while preserving the author-selected all-rights-reserved position.
7. Added RippleLogic.org-ready publication HTML and metadata alongside the existing website copy.


## Final cross-artifact operational corrections

1. Expanded the Pilot Data Dictionary so the shipped instrument can execute the declared RQ1-RQ3 analyses, including product-score incremental validity, subgroup equity, criterion timing/blinding, modality/occasion effects, and itemized burden.
2. Corrected the Local Comparator invigilation model by adding the number of sittings and removing the erroneous cohort multiplier. The default comparison is now on the same order of magnitude as AIAP rather than displaying an artificial fifteen-fold cost advantage.
3. Replaced Normative Standard §11 with the exact canonical G01-G13 gate set and added the individual-certification SHALL rule.
4. Synchronized the Core evidence-verification date to 14 August 2026, restored `verify` in the competence-authentication glossary definition, and added Phase 1/Phase 2 labels to the empirical crosswalk.
5. Rewrote the Pilot Readiness Pack decision formula as explicit PASS, PASS_WITH_CONTROLS, and NOT_READY clauses.
6. Changed the Prompt Construct Blueprint's unreviewed default from `No` to `Not assessed`; completed workbook-to-JSON status mappings; and marked the Programme Assurance Map distribution as illustrative rather than normative.
7. Re-ran the schema examples, semantic validator, nine adversarial tests, release verifier, OOXML/PDF navigation checks, spreadsheet formula-cache checks, and complete visual inspection.
8. Removed unused stale hyperlink relationships from the Core DOCX's empty footnotes part without changing its visible rendering.

## Deliberately unchanged

- Four-lane architecture.
- R0–R6 provisional role vocabulary.
- Six-stage protocol.
- Evidence-plan authority rule.
- Normative/implementation/machine artifact-role separation.
- Five-figure visual system.
- Empirical validation boundary.

## Current status

AIAP v6.5 is publication-ready and specification-complete for governed pilot preparation. It remains not empirically validated as an integrated institutional intervention.


## Publication-build hardening — 15 August 2026

This bounded build update does **not** change the AIAP v6.5 semantic specification.

1. Hardened `08_VERIFICATION/verify_release.py` so a normal test run or Git checkout cannot create false release failures from a narrow allow-list of non-release runtime/editor artifacts (`__pycache__`, `*.pyc`, `.git`, `.DS_Store`, `Thumbs.db`, Office lock files, `.tmp`, `.bak`). Governed release files still require exact manifest and SHA-256 coverage.
2. Changed documented Python commands to use `python -B`, preventing bytecode creation during the published verification workflow.
3. Corrected the GitHub deployment model for the existing MathGov monorepo: the AIAP package is published under `aiap/v6.5/` rather than overwriting repository-root MathGov metadata.
4. Defined canonical GitHub release tag `AIAP-v6.5` and canonical release assets for the Core PDF, Normative Standard PDF, and `AIAP_v6.5_COMPLETE_READY_FINAL.zip`.
5. Replaced package-relative website buttons with canonical GitHub release URLs and added OpenGraph, Twitter-card, and Schema.org scholarly metadata to the RippleLogic.org HTML.
6. Synchronized publication metadata, website copy, publication checklist, release guide, version manifest, verification status, and build report to the hardened publication build `AIAP-v6.5+2026.08.15.1`.
