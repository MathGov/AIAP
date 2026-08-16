#!/usr/bin/env python3
import copy, json, subprocess, sys, unittest
from pathlib import Path
from validate_aiap_record import validate_record
HERE=Path(__file__).resolve().parent
SCHEMA=json.loads((HERE/'AIAP_Assessment_Assurance_Record_v6.5.schema.json').read_text())
BASE=json.loads((HERE/'AIAP_Assessment_Assurance_Record_v6.5.example.json').read_text())
ALL=json.loads((HERE/'AIAP_Assessment_Assurance_Record_v6.5.example_all_lanes.json').read_text())
class TestAIAPValidator(unittest.TestCase):
  def assertValid(self,r): self.assertEqual(validate_record(r,SCHEMA),[])
  def assertInvalid(self,r,needle):
    errs=validate_record(r,SCHEMA); self.assertTrue(any(needle in e for e in errs),errs)
  def test_valid_examples(self): self.assertValid(BASE); self.assertValid(ALL)
  def test_lane2a_provenance_rejected(self):
    r=copy.deepcopy(BASE); r['material_claims'][0]['certification_object']='production_provenance'; self.assertInvalid(r,'incompatible')
  def test_lane2b_independent_rejected(self):
    r=copy.deepcopy(ALL); c=r['material_claims'][2]; c['certification_object']='independent_capability'; self.assertInvalid(r,'incompatible')
  def test_composition_arithmetic(self):
    r=copy.deepcopy(BASE); r['programme_assurance_composition']['lane_1_weight']=99; self.assertInvalid(r,'lane weights sum')
  def test_gate_status_consistency(self):
    r=copy.deepcopy(BASE); r['capacity_gate']['status']='PASS'; self.assertInvalid(r,'derive')
  def test_gate_ids_exact(self):
    r=copy.deepcopy(BASE); r['capacity_gate']['conditions'][0]['gate_id']='G02'; self.assertInvalid(r,'duplicate gate_id')
  def test_component_typo_schema(self):
    r=copy.deepcopy(BASE); r['material_claims'][0]['competence_profile']['component_decisions']['explane']='supported'; self.assertInvalid(r,'unknown competence component_decisions keys')
  def test_group_attribution(self):
    r=copy.deepcopy(BASE); r['assessment']['group_assessment']=True; r['material_claims'][0]['individual_attribution']=None; self.assertInvalid(r,'individual_attribution')
  def test_lane2b_model(self):
    r=copy.deepcopy(ALL); r['material_claims'][2]['combination_model']='hurdle'; self.assertInvalid(r,"requires combination_model='non_certifying'")
if __name__=='__main__': unittest.main(verbosity=2)
