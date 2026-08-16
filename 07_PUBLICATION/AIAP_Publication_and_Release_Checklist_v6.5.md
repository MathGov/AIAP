# AIAP v6.5 Publication and Release Checklist

## SSRN / working-paper release

- [ ] Upload `AIAP_Core_Working_Paper_v6.5.pdf`.
- [ ] Use the version-matched title, abstract, keywords, and declarations.
- [ ] Classify the work as a methodological working paper, not as an empirically validated intervention.
- [ ] Preserve the canonical version identifier in the citation.
- [ ] After an identifier is assigned, update the repository citation metadata without altering the frozen manuscript bytes.

## Website

- [ ] Publish the canonical page at `https://ripplelogic.org/aiap/`.
- [ ] Use `07_PUBLICATION/AIAP_RippleLogic_Page_v6.5.html` or the matching website copy as the source, preserving the empirical-status boundary.
- [ ] Keep the Core, Standard, implementation tools, and empirical-status boundary visibly distinct.
- [ ] Confirm all public buttons resolve after the GitHub release is created: Core PDF, Normative Standard PDF, complete ZIP, release page, and release guide.
- [ ] Publish the final ZIP SHA-256 digest beside the download.
- [ ] Do not represent machine validation as institutional authority.

## GitHub / repository

- [ ] In the existing `MathGov/ripple-logic` monorepo, place the extracted package under `aiap/v6.5/`; do **not** overwrite repository-root MathGov metadata.
- [ ] Preserve filenames and relative figure paths inside the AIAP subtree.
- [ ] Create GitHub release tag `AIAP-v6.5`.
- [ ] Attach these canonical release assets: `AIAP_v6.5_COMPLETE_READY_FINAL.zip`, `AIAP_Core_Working_Paper_v6.5.pdf`, and `AIAP_Normative_Assurance_Standard_v6.5.pdf`.
- [ ] Run `python -B -m unittest -v test_validate_aiap_record.py` from `06_MACHINE_READABLE`.
- [ ] Run `python -B verify_release.py ..` from `08_VERIFICATION`.
- [ ] Confirm the verifier reports `10 / 10 PASS` even if ordinary runtime debris such as `__pycache__` or `.git` is present; governed release files must still match the manifests exactly.
- [ ] Publish the version manifest, explicit rights notice, file manifest, and SHA-256 manifest.
- [ ] Add DOI/SSRN metadata only after assignment.

## Pilot preparation

- [ ] Declare Phase 1 or Phase 2 and complete the Pilot Readiness Pack locally.
- [ ] Obtain ethics, assessment, data-governance, accessibility, and institutional authority.
- [ ] Configure local workload and comparator assumptions.
- [ ] Pass all thirteen Assurance Capacity Gate conditions.
- [ ] Preregister estimands, thresholds, sampling, analysis, and continuation/withdrawal rules before data collection.
