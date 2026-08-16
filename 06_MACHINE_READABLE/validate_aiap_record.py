#!/usr/bin/env python3
"""AIAP v6.5 structural + semantic record validator.

Exit 0: all supplied records pass.
Exit 1: one or more structural or semantic errors.
This validator establishes machine coherence only. It does not establish substantive validity,
empirical validation, legal compliance, conformance, or institutional authority.
"""
from __future__ import annotations
import argparse, copy, json, math, sys
from datetime import date, datetime
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator, FormatChecker

GATE_IDS={f"G{i:02d}" for i in range(1,14)}
LANE_OBJECTS={
  "lane_1":{"artifact_quality","independent_capability","present_demonstrable_competence"},
  "lane_2a":{"artifact_quality","present_demonstrable_competence"},
  "lane_2b":{"artifact_quality","non_certifying_learning_support"},
  "lane_3":{"ai_integrated_capability"},
}
COMPONENTS={"explain","defend","verify","adapt","transfer"}

def derived_gate_status(conditions:list[dict[str,Any]])->str:
    statuses=[c.get("status") for c in conditions]
    if "FAIL" in statuses: return "FAIL"
    if "NOT_ASSESSED" in statuses: return "NOT_READY"
    if "PASS_WITH_CONTROLS" in statuses: return "PASS_WITH_CONTROLS"
    if statuses and all(s=="PASS" for s in statuses): return "PASS"
    return "NOT_READY"

def semantic_errors(record:dict[str,Any])->list[str]:
    errors=[]
    claims=record.get("material_claims",[])
    is_group=bool(record.get("assessment",{}).get("group_assessment",False))
    for i,c in enumerate(claims):
        loc=f"material_claims[{i}] ({c.get('claim_id','?')})"
        lane=c.get("lane"); obj=c.get("certification_object")
        if lane in LANE_OBJECTS and obj not in LANE_OBJECTS[lane]:
            errors.append(f"{loc}: certification_object {obj!r} is incompatible with {lane}; allowed={sorted(LANE_OBJECTS[lane])}")
        model=c.get("combination_model")
        if lane=="lane_2b":
            if model!="non_certifying": errors.append(f"{loc}: Lane 2B requires combination_model='non_certifying'")
            if not c.get("assured_elsewhere"): errors.append(f"{loc}: Lane 2B requires non-empty assured_elsewhere")
        elif model=="non_certifying":
            errors.append(f"{loc}: non_certifying combination_model is reserved for Lane 2B")
        if lane=="lane_2a":
            for field in ("authentication","prompt_security","submission_authentication_interval_minutes","competence_profile"):
                if c.get(field) is None: errors.append(f"{loc}: Lane 2A requires non-null {field}")
        if lane=="lane_3" and c.get("authentication") is None and c.get("stakes") in {"high","safety_critical"}:
            errors.append(f"{loc}: high-consequence Lane 3 requires authenticated judgement/transfer evidence")
        prof=c.get("competence_profile")
        if isinstance(prof,dict):
            declared=set(prof.get("load_bearing_components",[]))
            decisions=set((prof.get("component_decisions") or {}).keys())
            unknown=decisions-COMPONENTS
            if unknown: errors.append(f"{loc}: unknown competence component_decisions keys {sorted(unknown)}")
            if decisions!=declared: errors.append(f"{loc}: component_decisions keys {sorted(decisions)} must equal load_bearing_components {sorted(declared)}")
        if is_group and c.get("stakes") in {"high","safety_critical"}:
            ia=c.get("individual_attribution")
            if not isinstance(ia,dict) or not all(ia.get(k) is True for k in ("group_artifact","separate_evidence","separate_challenge","individual_decision_record")):
                errors.append(f"{loc}: high/safety-critical group claim requires true individual-attribution safeguards")
    comp=record.get("programme_assurance_composition",{})
    total=comp.get("total_mapped_weight")
    parts=[comp.get(k) for k in ("lane_1_weight","lane_2a_weight","lane_2b_weight","lane_3_weight")]
    if isinstance(total,(int,float)) and all(isinstance(x,(int,float)) for x in parts):
        if not math.isclose(sum(parts),total,rel_tol=1e-9,abs_tol=1e-9):
            errors.append(f"programme_assurance_composition: lane weights sum to {sum(parts)}, not total_mapped_weight {total}")
    gate=record.get("capacity_gate",{})
    conditions=gate.get("conditions",[])
    ids=[c.get("gate_id") for c in conditions if isinstance(c,dict)]
    if len(conditions)!=13: errors.append(f"capacity_gate.conditions: expected exactly 13, found {len(conditions)}")
    if len(ids)!=len(set(ids)): errors.append("capacity_gate.conditions: duplicate gate_id")
    if set(ids)!=GATE_IDS: errors.append(f"capacity_gate.conditions: IDs must be exactly G01-G13; missing={sorted(GATE_IDS-set(ids))}, extra={sorted(set(ids)-GATE_IDS)}")
    derived=derived_gate_status(conditions)
    if gate.get("status")!=derived: errors.append(f"capacity_gate.status={gate.get('status')!r} but condition statuses derive {derived!r}")
    for c in conditions:
        if c.get("status")=="PASS_WITH_CONTROLS":
            for f in ("control","owner","expiry"):
                if not c.get(f): errors.append(f"capacity_gate {c.get('gate_id')}: PASS_WITH_CONTROLS requires {f}")
    return errors

def validate_record(record:dict[str,Any],schema:dict[str,Any])->list[str]:
    v=Draft202012Validator(schema,format_checker=FormatChecker())
    structural=[]
    for e in sorted(v.iter_errors(record),key=lambda e:list(e.absolute_path)):
        p='.'.join(str(x) for x in e.absolute_path) or '$'
        structural.append(f"schema {p}: {e.message}")
    return structural+semantic_errors(record)

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument('records',nargs='+',type=Path)
    ap.add_argument('--schema',type=Path,default=Path(__file__).with_name('AIAP_Assessment_Assurance_Record_v6.5.schema.json'))
    ap.add_argument('--json',action='store_true',dest='as_json')
    args=ap.parse_args()
    schema=json.loads(args.schema.read_text(encoding='utf-8'))
    result=[]; ok=True
    for path in args.records:
        record=json.loads(path.read_text(encoding='utf-8'))
        errs=validate_record(record,schema); ok=ok and not errs
        result.append({'file':str(path),'valid':not errs,'errors':errs})
    if args.as_json: print(json.dumps(result,indent=2,ensure_ascii=False))
    else:
        for r in result:
            print(('PASS' if r['valid'] else 'FAIL')+': '+r['file'])
            for e in r['errors']: print('  - '+e)
    return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
