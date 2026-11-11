import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('design_library',ROOT/'scripts/design_library.py')
lib=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(lib)

class OfflineLibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.screens,cls.recipes=lib.load()
        cls.provenance=json.loads(lib.PROVENANCE.read_text())['records']

    def test_reviewed_collection_has_over_300_unique_screens(self):
        stats=lib.validate(self.screens,self.recipes,self.provenance)
        self.assertGreater(stats['ready_screens'],300)
        self.assertEqual(set(stats['platforms']),{'mobile','web','desktop'})

    def test_default_lookup_needs_no_network_provenance_or_images(self):
        with patch('socket.socket',side_effect=AssertionError('Network forbidden')):
            screens,recipes=lib.load()
            out=lib.packet(lib.search(screens,'calendar event',platform='mobile'),recipes)
        data=json.dumps(out)
        self.assertNotIn('https://',data)
        self.assertNotIn('image_url',data)
        self.assertTrue(out['screens'])
        # Provenance is deliberately absent from the lookup inputs.
        self.assertNotIn('source_url',data)

    def test_specific_purpose_does_not_return_incidental_login_detail(self):
        results=lib.search(self.screens,'authentication login','mobile')
        self.assertTrue(results)
        self.assertIn('M298',[s['id'] for s in results])
        self.assertNotIn('M289',[s['id'] for s in results])
        for s in results:self.assertIn('authentication',lib.words(' '.join(s['tags'])+' '+s['pattern']))

    def test_permission_query_avoids_generic_settings(self):
        results=lib.search(self.screens,'settings permissions','desktop')
        self.assertTrue(results)
        self.assertTrue(all('permissions' in lib.words(' '.join(s['tags'])+' '+s['pattern']) for s in results))
        self.assertTrue(all(s['pattern']=='file-permissions' for s in results))
        self.assertIn('POSIX',self.recipes['file-permissions']['adaptation_and_states'])

    def test_pricing_coverage_and_missing_payment_error_evidence(self):
        self.assertIn('E003',[r['id'] for r in lib.search(self.screens,'pricing tiers checkout','web')])
        self.assertEqual(lib.search(self.screens,'payment error','web'),[])
        self.assertEqual(lib.search(self.screens,'error validation','mobile'),[])
        self.assertEqual(lib.search(self.screens,''),[])

    def test_budget_keeps_whole_observations_and_labels_omissions(self):
        selected=lib.search(self.screens,'calendar event editing','mobile',8)
        out=lib.packet(selected,self.recipes,1800)
        self.assertLessEqual(len(json.dumps(out,ensure_ascii=False)),1800)
        self.assertTrue(out['screens'])
        self.assertTrue(out['omitted_for_budget'])
        original={s['id']:s for s in selected}
        for s in out['screens']:self.assertEqual(s['layout'],original[s['id']]['layout'])
        with self.assertRaises(ValueError):lib.packet(selected,self.recipes,500)

    def test_invalid_provenance_and_duplicates_rejected(self):
        with self.assertRaises(ValueError):lib.validate(self.screens+[self.screens[0]],self.recipes,self.provenance)
        prov=copy.deepcopy(self.provenance)
        prov[self.screens[0]['evidence_ref']]['review']='unreviewed'
        with self.assertRaises(ValueError):lib.validate(self.screens,self.recipes,prov)
        prov=copy.deepcopy(self.provenance)
        prov[self.screens[1]['evidence_ref']]['image_sha256']=prov[self.screens[0]['evidence_ref']]['image_sha256']
        with self.assertRaises(ValueError):lib.validate(self.screens,self.recipes,prov)

    def test_product_diversity_does_not_promote_weaker_match(self):
        rows=[{'id':'1','product':'A','platform':'web','tags':['calendar','editing'],'name':'calendar editing','layout':'calendar editing','pattern':'editor'},
              {'id':'2','product':'A','platform':'web','tags':['calendar','editing'],'name':'calendar editing details','layout':'calendar editing','pattern':'editor'},
              {'id':'3','product':'B','platform':'web','tags':['calendar'],'name':'calendar','layout':'calendar','pattern':'calendar'}]
        self.assertEqual([s['id'] for s in lib.search(rows,'calendar editing',limit=2)],['1','2'])

    def test_cli_gap_and_guidance_are_honest(self):
        def run(*args):return json.loads(subprocess.check_output([sys.executable,str(ROOT/'scripts/design_library.py'),*args],text=True))
        out=run('search','payment error','--platform','web')
        self.assertIn('coverage_gap',out)
        self.assertEqual(out['screens'],[])
        advice=run('guidance','pricing','payment')
        self.assertIn('Original',advice['evidence'])
        self.assertEqual(set(advice['recipes']),{'pricing','payment'})
        self.assertNotIn('https://',json.dumps(advice))

class CoachingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.screens,cls.recipes=lib.load()

    def test_support_integrity(self):
        out=lib.validate_support(self.screens)
        self.assertEqual(out['documented_flows'],8)
        self.assertEqual(out['decision_guides'],19)
        self.assertEqual(out['independently_operated_flows'],0)

    def test_brief_separates_payment_from_email_validation(self):
        out=lib.brief(self.screens,self.recipes,'pricing failed payment','web')
        self.assertIn('E003',[s['id'] for s in out['screens']])
        self.assertNotIn('E076',[s['id'] for s in out['screens']])
        self.assertIn('error',out['screen_purpose_gaps'])
        self.assertEqual(out['documented_flows'][0]['id'],'FL01')
        self.assertIn('D02',[g['id'] for g in out['decision_guides']])
        self.assertLessEqual(len(json.dumps(out,ensure_ascii=False,separators=(',',':'))),7500)
        self.assertNotIn('https://',json.dumps(out))

    def test_error_screen_is_available_for_relevant_task(self):
        out=lib.search(self.screens,'email validation error','web')
        self.assertIn('E076',[s['id'] for s in out])

    def test_sharing_is_not_posix_permissions(self):
        rows={s['id']:s for s in self.screens}
        self.assertEqual(rows['E053']['pattern'],'sharing')
        self.assertEqual(rows['G081']['pattern'],'file-permissions')
        self.assertEqual(rows['F036']['platform'],'desktop')

    def test_combined_lookup_stays_offline(self):
        with patch('socket.socket',side_effect=AssertionError('No network')):
            out=lib.brief(self.screens,self.recipes,'settings search scope','desktop',7500)
        self.assertTrue(out['screens'])
        self.assertTrue(out['documented_flows'])
        self.assertTrue(out['decision_guides'])
        self.assertNotIn('image_url',json.dumps(out))

    def test_small_budget_preserves_complete_records_and_rule_references(self):
        out=lib.brief(self.screens,self.recipes,'settings search scope','desktop',2400)
        self.assertLessEqual(len(json.dumps(out,ensure_ascii=False,separators=(',',':'))),2400)
        self.assertTrue(out['omitted_for_budget'])
        self.assertEqual(set(out['implementation_rules']),{s['pattern'] for s in out['screens']})

if __name__=='__main__':unittest.main()
