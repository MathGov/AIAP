# AIAP v6.5 Feedback Adjudication and Final Change Log

## Decision boundary

Claude's review was treated as a set of defect hypotheses, not as an instruction to enlarge AIAP. A change was accepted only when it corrected a demonstrable scholarly, cross-format, operational, or publication defect. The four lanes, six-stage protocol, R0–R6 provisional role vocabulary, thirteen-condition Assurance Capacity Gate, five-figure visual system, and validation boundary remain unchanged.


## Final full-system audit adjudication

The Claude/Genspark cross-artifact audit correctly found that the conceptual architecture was already complete, while three operational artifacts still required bounded repair. The accepted changes below do not alter a lane, stage, role, gate count, taxonomy, empirical proposition, or authority boundary.

| Audit finding | Determination | Final v6.5 action |
|---|---|---|
| Pilot Data Dictionary did not carry the minimum dataset needed for RQ2 incremental validity and RQ3 equity analysis | **Accurate and release-material.** | Expanded the dictionary to 73 defined fields, including programme/module, lane, modality, occasion, product score/decision, authentication duration, unseen/perturbed status, criterion timing/blinding, equity variables, itemized student burden, role-specific staff burden, capacity incidents, and governance fields. `independent_criterion_score` is now conditional for all participants where feasible or a prespecified validation sample. |
| Local Comparator multiplied invigilation by cohort size | **Accurate and potentially misleading.** | Replaced the model with `(number of sittings × duration per sitting × invigilators) + setup`; added a `Number of sittings` input. The default comparator now yields 8 invigilation hours, 113 recurring hours, and approximately 0.377 staff-hours per student rather than 1,309 hours and 4.363 hours per student. |
| Normative Standard §11 described a different set of thirteen conditions | **Accurate.** | Replaced the prose list with the canonical labelled G01–G13 set, matching the Core, Feasibility Model, Pilot Readiness Pack, schema, and crosswalk. |
| Standard lacked the individual-certification rule | **Accurate.** | Added a SHALL rule: every student completes the declared minimum authentication when an individual consequential claim depends on it; sampling may support moderation, calibration, audit, or research but may not substitute for individual certification evidence. |
| Core evidence-verification date differed between DOCX and Markdown | **Accurate.** | Synchronized the DOCX to 14 August 2026 and re-rendered the final PDF. |
| Core glossary omitted `verify` from competence authentication | **Accurate, minor.** | Restored the five-component formulation: explain, defend, verify, adapt, or transfer. |
| Table 16A did not distinguish Phase 1 and Phase 2 work | **Accurate, useful navigation improvement.** | Added explicit phase labels to each proposition-to-test pathway without changing any empirical priority or estimand. |
| Pilot Readiness Pack overall formula could be read ambiguously | **Accurate.** | Rewrote it as three explicit clauses for PASS, PASS_WITH_CONTROLS, and NOT_READY. |
| Prompt Construct Blueprint defaulted unreviewed components to `No` | **Accurate fail-open default.** | Changed all blank-template defaults to `Not assessed` and expanded the dropdown to `Yes / No / Not assessed`. |
| Feasibility workbook mapping omitted some display-to-JSON tokens | **Accurate, mechanical.** | Added the complete PASS, PASS_WITH_CONTROLS, FAIL, NOT READY/NOT_READY, and Not assessed/NOT_ASSESSED mapping. |
| Programme Assurance Map example could be mistaken for a recommended composition | **Accurate, low-cost safeguard.** | Added a visible notice that the distribution is illustrative and not a recommended default. |
| Canonical Markdown had lost all non-ASCII characters | **Not an artifact defect.** | Direct byte-level verification confirms valid UTF-8, non-ASCII bytes, and the exact surnames/symbols. The recurring loss occurs in a transport/extraction representation. No content was transliterated. |
| Validator tests should be rerun with inspectable inputs | **Accurate as verification discipline; already structurally present.** | Re-ran the two schema examples, semantic validator, and nine published adversarial unit tests. Their test inputs remain in `test_validate_aiap_record.py`. |
| Simplify the four lanes or R0–R6, add a gate/status, shorten the canonical paper, or add more literature | **Rejected.** | These proposals either pre-empt the registered comparator programme, duplicate existing controls, or confuse the canonical public/study edition with a venue-specific derivative. |
| Adopt a reuse licence for figures/templates | **Authorial strategic option, not a defect.** | No licence change was made. The explicit all-rights-reserved position remains controlling. |

## Additional release hygiene

Final OOXML inspection found unused hyperlink relationships attached to an empty footnotes part in the Core DOCX. They were not visible or active, but contained stale builder-era targets. The orphan relationships were removed, the Core was re-rendered, and the 87-page visual output remained pixel-identical.

## Earlier paper-only feedback adjudication

| Review finding | Determination | v6.5 action |
|---|---|---|
| Markdown had lost diacritics, dashes, quotation marks, multiplication signs, section symbols, and copyright symbols | **Not accurate for the actual v6.0.2 bytes.** Direct UTF-8 decoding and byte-level token checks found the named characters and surnames intact. The pattern arose in a rendered/extracted transport view, not the release source. | Preserved the canonical UTF-8 source and added exact regression checks for `Kılınç`, `Gašević`, `Raković`, `Foltýnek`, `Šigut`, `Levels 2–5`, `R0–R6`, `×`, `§`, `©`, and curly quotation marks. |
| Correspondence was populated in Markdown but blank in DOCX | **Partly inaccurate.** The DOCX contained a live mail hyperlink, but its visible text was `mailto:james.mg@buv.edu.vn`, which was inelegant and could extract inconsistently. | Rebuilt the line so the visible address is `james.mg@buv.edu.vn` while the mailto target remains functional. |
| Appendix D3 placement diverged across DOCX and Markdown | **Already repaired in v6.0.2.** The Markdown contains `<a id="app-d3">` and a nested D3 Contents entry; DOCX/PDF navigation also resolves. | Retained and reverified. |
| A double blank gap remained before Ali and Maroulis in the Markdown references | **Accurate, minor.** | Removed the residual gap. |
| Section 15 and Appendix G gave two competing "first" pilots | **Accurate and material.** | Defined a two-phase empirical sequence: Phase 1 bounded feasibility/measurement; Phase 2 multi-institution comparison and transportability over at least two cycles. Synchronized the Core, Pilot Protocol, Pilot Readiness Pack, release manifest, and public materials. |
| The early misconduct definition could be read as contradicting the later Lane 2A rule | **Accurate.** | Rewrote the early rule: deception, fabricated evidence, Lane 1 breach, or outsourcing contrary to an explicit production/authorship constraint is misconduct; weak authentication remains a validity concern unless independent misconduct evidence exists. |
| The evidence-plan authority rule appeared widened merely to preserve Lane 2B | **A strong reviewer objection; clarification warranted.** | Added the functional rationale: claim status changes decision authority, programme mapping, progression/public wording, assured-elsewhere duties, and promotion review even when it adds no positive evidence object. The simpler certifying/non-certifying flag remains a preregistered comparator. |
| Luo (2024) should be added | **Accurate and directly relevant.** | Added a bounded discussion of how policy problem representations center contested originality, linked to AIAP's competence/provenance/public-claim separation. |
| Dawson and Sutherland-Smith (2018) should be added | **Accurate and directly relevant.** | Added the small blinded pilot and its 62% sensitivity / 96% specificity findings, with explicit non-generalization language. |
| The canonical paper is too long for a conventional journal submission | **Likely true for many venues but not a defect in the canonical public/study edition.** | No compression of the canonical edition. Any journal derivative must be generated from v6.5 after a venue and current house limits are selected. |
| "All rights reserved" required a decision before public release | **Accurate as a release-governance point.** Prior authorial position was cautious rather than openly licensed. | Added root-level `LICENSE.md` and clarified that GitHub/RippleLogic.org publication is source-visible but does not grant an open-source or Creative Commons licence. |

## Additional defect found during the v6.5 audit

The Workload Calculator's number formats were misapplied to several rows: the 10-minute alternative-format allowance displayed as 1000%, the 3-hour recording-review input displayed as 300%, and two proportion rows displayed as decimals. The underlying values and formulas were correct, but the presentation was not. v6.5 corrects each affected number format and re-renders the workbook.

## Earlier v6.0.2 corrections retained

- Live AIAS FAQ path and correct Advisor/Level-3 attribution.
- Exact thirteen-condition G01–G13 Core/Standard/workbook/schema alignment.
- Four positive assurance objects reconciled with Lane 1 and Lane 2B machine-routing values.
- Single alphabetized, non-duplicated glossary.
- Canonical `submission_authentication_interval_minutes` field name.
- Group-attribution, lane/object, competence-key, composition-arithmetic, and gate-status semantic validation.
- Affirmative fail-closed feasibility formula: PASS is possible only when all thirteen gates explicitly pass.
- Four-route machine-readable example, semantic validator, and adversarial tests.
- Version-matched Core-to-Standard crosswalk and Pilot Readiness Pack.

## Rejected or deliberately deferred

| Proposal | Decision | Reason |
|---|---|---|
| Add new lanes, objects, roles, gates, figures, or statuses | Rejected | No unresolved distinction earned the additional cognitive or governance cost. |
| Replace Lane 2B now with a flag | Deferred to evidence | v6.5 states the functional rationale and retains the simpler flag model as a direct comparator. |
| Simplify R0–R6 now | Deferred to reliability and utility testing | The Role Coding Manual explicitly requires comparison with a simpler alternative. |
| Treat schema/workbook validation as authority or empirical validation | Rejected | Structural coherence cannot establish substantive validity, institutional authority, legal compliance, or programme conformance. |
| Add more graphics | Rejected | The five retained figures perform distinct cognitive functions; another would be redundant. |
| Convert the canonical paper into a journal-length derivative without a selected venue | Rejected | Venue-specific derivatives must not define or supersede the canonical edition. |
| Adopt a Creative Commons or open-source licence without an explicit author decision | Rejected | v6.5 makes the current all-rights-reserved position explicit rather than inventing a broader licence. |

## Final freeze rule

AIAP v6.5 is frozen as the publication-ready specification baseline. The next legitimate source of architectural change is empirical evidence, a reproducible security/rights failure, a demonstrated interoperability defect, or new evidence that changes a load-bearing claim. Editorial motion without such a trigger should not reopen the framework.


## Final publication-engineering adjudication — 15 August 2026

| Audit finding | Determination | Final v6.5 build action |
|---|---|---|
| Running the published unit-test command created `__pycache__/*.pyc`, after which the exact-coverage verifier reported those runtime files as unauthorized release additions | **Accurate and release-material.** The verifier's strictness was correct, but the published workflow mutated its own verification surface. | Changed all published verification commands to `python -B` and hardened the verifier to ignore only a narrow allow-list of runtime/editor artifacts. Governed release files remain fail-closed and must match both manifests exactly. |
| Package instructions said to upload the AIAP release root at repository root | **Accurate deployment conflict in the existing MathGov monorepo.** Doing so could overwrite the canonical MathGov root `README.md`, licence, citation, and governance metadata. | Defined the monorepo publication path as `aiap/v6.5/`; package-level metadata governs that subtree without replacing MathGov Core metadata. |
| RippleLogic.org HTML used package-relative document links that were valid only inside the extracted ZIP | **Accurate website-deployment defect.** | Replaced them with canonical GitHub release-asset URLs, added a complete-release button, release-guide/release-page links, and social/Schema.org metadata. |
| Publication metadata named `AIAP_v6.5_COMPLETE_READY.zip` rather than the canonical final release asset | **Accurate naming drift.** | Synchronized metadata and the release checklist to `AIAP_v6.5_COMPLETE_READY_FINAL.zip` and release tag `AIAP-v6.5`. |

These changes are publication/reproducibility corrections only. No lane, stage, evidence object, gate, role vocabulary, scientific proposition, authority boundary, or empirical-status claim was altered.
