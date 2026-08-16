# AIAP v6.5 Core-to-Standard Crosswalk

**Purpose.** This version-matched crosswalk links the scholarly architecture in the Core Working Paper to the SHALL/SHOULD/MAY requirements in the Normative Assurance Standard, the operational instruments, the machine-readable layer, and the verification evidence.

**Boundary.** A crosswalk demonstrates traceability. It does not establish empirical validation, legal compliance, conformance for a real programme, or institutional authority.

| Principal rule / requirement | Core Working Paper | Normative Standard | Operational implementation | Machine-readable / workbook evidence | Verification evidence |
|---|---|---|---|---|---|
| Evidence-plan authority | §4; Core Governing Rules Register | §2.1 | Handbook §3; Toolkit §4 | `material_claims`, condition, lane, evidence, inference, use | Schema + semantic validator; claim-profile review |
| Claim boundedness and decomposition | §§4-5; Appendix C | §§2.2, 4 Stages 0-1 | Handbook §§1-3; Toolkit §4 | `claim_id`, capability, stakes, condition, programme use, public wording | Required-field validation; programme-map audit |
| Lane-modality separation | §4 | §§4 Stage 2, 9 | Handbook Step 5; Pilot Protocol §8 | `condition.openness`, `condition.modality`, `condition.materially_constrained` | Schema enums; modality threat-model review |
| Claim-level application | §§5.1, 6 | §4 Stage 0 | Handbook §1; Toolkit §4 | one `materialClaim` object per claim | Array-level schema validation; composite-example check |
| Lane 1 secured assurance | §§5, 7.7; Table 9 | §5.1 | Handbook Lane 1 card | `lane_1`, `independent_capability`, high-independence evidence | Semantic lane/object compatibility test |
| Lane 2A competence-authenticated open | §§5, 7.1-7.4; Table 8 | §§5.2, 6 | Handbook Lane 2A card; Toolkit; Prompt Bank | non-null authentication, prompt security, interval, competence profile | Schema conditional + semantic validator + pilot protocol |
| Lane 2B non-certifying discipline | §§5, 7; Table 15 | §5.3 | Handbook Lane 2B card; Toolkit wording | `lane_2b`, `non_certifying_learning_support`, `non_certifying`, `assured_elsewhere` | Semantic validator rejects illicit certification combinations |
| Lane 3 AI-integrated assurance | §§5-7, 10 | §5.4 | Handbook Lane 3 card; Role Manual R4-R6 | `lane_3`, `ai_integrated_capability`, workflow and authenticated judgement evidence | Schema/semantic validation; all-lanes example |
| Four positive assurance objects and routing values | Figure 1; §§5, 7.7; Appendix F | §§2.3, 4 Stage 1 | Toolkit §4; Programme Map Definitions | six operational enum values with explicit object/routing descriptions | Cross-artifact terminology scan; lane/object tests |
| Prompt security and form equivalence | §7.1.1 | §6.1 | Handbook §6.1; Toolkit §5; Prompt Bank workbook | `prompt_security`; Data Dictionary fields | G02/G03; exposure/form-equivalence records; validator |
| Submission-authentication interval | §§7.1.1, 10 | §6.1 | Handbook §6.1; Toolkit §4 | `submission_authentication_interval_minutes` | G04; Data Dictionary and JSON field-name synchronization |
| Individual attribution in group work | §§7, 11 | §6.2 | Handbook §10.1; Toolkit moderation checklist | `individual_attribution` | Root schema conditional for high/safety-critical group claims; semantic test |
| Individual certification | §7; Rules Register | §§6.2, 10 | Handbook §7 | per-student evidence and decision records | Programme-map and pilot-record review |
| Product-authentication combination | §7.3; Box 3 | §7 | Handbook Step 4; Toolkit §6 | `combination_model` | Lane 2B/non-certifying test; rubric/hurdle audit |
| Evidence dependence and dual independence | §7.4; Figure 3 | §8 | Handbook Step 5 | evidence independence groups and source/environment ratings | Schema required fields; semantic and moderation review |
| Least-intrusive evidence governance | §§7.5-7.6, 9 | §§9, 12 | Data Protection, Accessibility, and Evidence Governance | governance, retention, accessibility, challenge status | Data inventory, retention, appeal, and accessibility review |
| Public-claim accounting | §7.7; Table 9; Figure 4 | §10 | Programme Map workbook | `public_wording`, `publication_boundary`, assurance composition | Weight-sum validator; claim-evidence audit |
| Assurance Capacity Gate - G01-G13 | §§8.1, 14 | §11 | Pilot Readiness Pack; Feasibility Model | `capacity_gate.conditions` | exact G01-G13 validator; conservative workbook formula |
| Capacity-degradation rule | §14 | §11 | Handbook §10; Governance §8 | `degradation_plan` | incident scenario and fallback review |
| Minimum appeal rights | §7.1 | §§11-12 | Handbook §10.2; Toolkit FAQ; Governance §7 | `governance.appeal_rights` | Required booleans and rehearing rule; process audit |
| Temporal requalification | §§10, 14; Appendix I | §13 | Handbook §10 | review date, triggers, per-claim requalification date | version/date/trigger checks |
| Validation and falsification boundary | §§1.1, 15; Appendix G; declarations | §14 | Pilot Protocol §§1-12 | `status_boundary`, `publication_boundary` | validator disclaimer; preregistered continuation rules |
| Pilot-readiness and authority boundary | Appendix H | §§1, 14-15 | Pilot Readiness Pack | version, authority, gate, governance, scope | release verification; local sign-off required |

## Interpretation order

1. The **Core Working Paper** explains and limits the scholarly claims.
2. The **Normative Assurance Standard** controls any AIAP conformance claim.
3. The **implementation artifacts** operationalize but do not enlarge the Standard.
4. The **machine-readable artifacts** check structure and selected semantic rules but do not confer authority.
5. Real-world use requires local approvals, completed records, rights protection, capacity, and evidence that supports the exact claim.
