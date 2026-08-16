# AIAP v6.5 Verification Status

## Final result

**PASS — publication-ready, GitHub-ready, RippleLogic.org-ready release tree.**  
Publication build: **AIAP-v6.5+2026.08.15.1** (release-engineering hardening only; no semantic change).

AIAP v6.5 is specification-complete for scholarly evaluation and governed pilot preparation. This verification establishes artifact integrity, navigation, cross-artifact synchronization, computational operability, machine readability, and publication engineering. It does **not** establish empirical validity, legal compliance, accreditation, institutional authorization, or deployment authority.

## Verified release state

| Dimension | Result |
|---|---:|
| Release-tree files before archive | 59 |
| Automated verification dimensions | 10 / 10 PASS |
| DOCX files | 8 genuine OOXML |
| PDF files | 8 |
| Rendered pages visually inspected | 129 / 129 |
| Core paper | 87 pages |
| Materialized TOC entries | 171 / 171 synchronized to final PDF outlines |
| DOCX internal hyperlinks | 407 |
| DOCX bookmarks | 416 |
| PDF internal links | 411 |
| Distinct PDF internal destinations | 191 |
| Broken PDF destinations | 0 |
| PDF outline entries | 180 |
| External scholarly links | 83 |
| Embedded core figures | 5 / 5 |
| Figures with alternative text | 5 / 5 |
| Tracked changes / comments | 0 / 0 |
| Unresolved DOCX anchors | 0 |
| Externally linked images | 0 |
| Workbooks | 5 genuine OOXML |
| Formula cells with cached values | 61 / 61 |
| Cached formula errors | 0 |
| Machine-readable examples | 2 / 2 valid |
| Adversarial validator tests | 9 / 9 PASS |
| Accessibility findings | 0 high; 0 medium; 71 low raw-URL notices |

## Final operational-hardening verification

- The Pilot Data Dictionary now defines 73 fields and includes the product-score, lane, modality, occasion, authentication-duration, unseen/perturbed, criterion timing/blinding, equity, burden, capacity, and governance variables needed to execute the declared RQ1-RQ3 analyses.
- `independent_criterion_score` is conditional: collect it for all participants where feasible or for a prespecified validation sample sized to the criterion-related estimand.
- The Workload Calculator Local Comparator now uses `(sittings × duration per sitting × invigilators) + setup`. Its default values produce 8 invigilation hours, 113 recurring hours, and approximately 0.377 staff-hours per student.
- Normative Standard §11 now contains the exact canonical G01-G13 labelled gate set, and §6.2 carries the individual-certification SHALL rule.
- The Core DOCX and Markdown agree on the 14 August 2026 verification date; competence authentication uses all five components: explain, defend, verify, adapt, and transfer.
- Table 16A identifies the Phase 1, Phase 2, and cross-phase empirical pathways without changing any proposition or estimand.
- The Pilot Readiness Pack states separate PASS, PASS_WITH_CONTROLS, and NOT_READY rules.
- The Prompt Construct Blueprint defaults unreviewed rows to `Not assessed`, not `No`.
- Workbook display states map explicitly to machine tokens: PASS, PASS_WITH_CONTROLS, FAIL, NOT READY/NOT_READY, and Not assessed/NOT_ASSESSED.
- The Programme Assurance Map states that its exemplar distribution is illustrative and not a recommended default.
- The canonical Markdown passes direct UTF-8 byte decoding and retains `Kılınç`, `Gašević`, `Raković`, `Foltýnek`, `Šigut`, en dashes, `×`, `§`, `©`, and curly quotation marks.
- The Core DOCX contains no stale or malformed external hyperlink relationship; unused builder-era relationships in the empty footnotes part were removed.
- Both JSON examples, the semantic validator, and all nine published adversarial unit tests pass.

## Document and visual verification

All 87 Core pages and all 42 companion pages were rendered and visually inspected. The edited Core, Normative Standard, and Pilot Readiness Pack were re-rendered after their final changes. The Core render after OOXML relationship cleanup was pixel-identical across all 87 pages. No clipping, overlap, missing figure, broken glyph, stranded heading, or material layout defect was found.

All five workbooks were inspected through formula/value scans and rendered key-range previews. No formula errors were found. The Feasibility Model remains affirmative and fail-closed, with complete cached formula values.

## Reproducible checks

```bash
cd 06_MACHINE_READABLE
python -B -m unittest -v test_validate_aiap_record.py

cd ../08_VERIFICATION
python -B verify_release.py ..
```

The verifier is additionally hardened against a narrow set of non-release runtime/editor artifacts (`__pycache__`, `*.pyc`, `.git`, `.DS_Store`, `Thumbs.db`, Office lock files, and `.tmp`/`.bak` files). A deliberate post-test runtime-debris check confirms that these do not create false manifest failures, while every governed release artifact remains subject to exact file-manifest and SHA-256 coverage.

The final delivery ZIP is decompression-tested after sealing. Its SHA-256 digest is supplied with the download link.

## Scientific boundary

The next legitimate source of architectural change for AIAP is Phase 1 pilot evidence, a reproducible security or rights failure, a demonstrated interoperability defect, or new evidence that changes a load-bearing claim.
