import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('reference_library',ROOT/'scripts/reference_library.py')
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)

def record(**changes):
    r=dict(id='A001',title='Calendar event',kind='app_store_preview',platforms=['mobile'],patterns=['calendar'],evidence='unreviewed',source='Publisher',observations=[],adaptation='Inspect first.',limitations=['Static image only.'],rights='Link only.',checked_on='2026-11-07',image_url='https://example.org/image.png')
    r.update(changes);return r

def catalog(*records):return dict(schema_version=1,records=list(records))

class ReferenceLibraryTests(unittest.TestCase):
    def test_canonical_catalog_and_separate_counts(self):
        data=lib.validate(json.loads((ROOT/'data/reference-library.json').read_text()))
        stats=lib.stats(data['records'])
        self.assertEqual(stats['records'],sum(stats['by_kind'].values()))
        self.assertEqual(stats['records'],sum(stats['by_evidence'].values()))
        self.assertGreater(stats['apps_with_publisher_previews'],1)

    def test_unreviewed_not_shipped_evidence(self):
        with self.assertRaises(ValueError):lib.validate(catalog(record(kind='shipped_screen')))

    def test_inspected_needs_locator_and_observation(self):
        for changes in [dict(image_url=None,observations=['Observed.']),dict(observations=[])]:
            with self.subTest(changes=changes),self.assertRaises(ValueError):
                lib.validate(catalog(record(evidence='image_inspected',**changes)))

    def test_duplicate_ids_and_non_https_rejected(self):
        for data in [catalog(record(),record()),catalog(record(url='javascript:alert(1)'))]:
            with self.assertRaises(ValueError):lib.validate(data)

    def test_local_hash_and_escape(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);p=root/'a.png';p.write_bytes(b'fixture')
            r=record(asset='a.png',sha256=hashlib.sha256(p.read_bytes()).hexdigest())
            lib.validate(catalog(r),root)
            with self.assertRaises(ValueError):lib.validate(catalog(r,dict(r,id='A002')),root)
            with self.assertRaises(ValueError):lib.validate(catalog(dict(r,sha256='bad')),root)
            with self.assertRaises(ValueError):lib.safe_asset(root,'../outside.png')
            outside=root.parent/'outside-reference-fixture.png';outside.write_bytes(b'fixture')
            try:
                (root/'link.png').symlink_to(outside)
                with self.assertRaises(ValueError):lib.safe_asset(root,'link.png')
            finally:outside.unlink()

    def test_search_filters_and_all_terms(self):
        rs=[record(category='Productivity'),record(id='A002',platforms=['web'],title='Calendar history')]
        self.assertEqual([r['id'] for r in lib.query(rs,'calendar productivity',platform='mobile')],['A001'])
        self.assertFalse(lib.query(rs,'calendar checkout'))
        self.assertFalse(lib.query(rs,evidence='image_inspected'))

    def test_script_breakout_escaped(self):
        result=lib.gallery(catalog(record(title='</script><script>alert(1)</script>')))
        self.assertNotIn('</script><script>alert(1)</script>',result)
        self.assertIn('\\u003c/script\\u003e',result)

    def test_task_evidence_precedes_brand_name(self):
        rs=[record(title='Todoist Calendar',patterns=['preview awaiting inspection']),record(id='S001',title='Event editor',patterns=['calendar'],evidence='image_inspected',observations=['Labeled event fields.'])]
        self.assertEqual(lib.query(rs,'calendar')[0]['id'],'S001')

    def test_external_images_opt_in(self):
        result=lib.gallery(catalog(record()))
        self.assertIn('remote=false',result)
        self.assertIn('remote&&r.image_url',result)
        self.assertNotIn('<img src="https://example.org',result)

    def test_custom_asset_root_and_overwrite_refusal(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);image=root/'image.png';image.write_bytes(b'fixture')
            d=catalog(record(asset='image.png',sha256=hashlib.sha256(image.read_bytes()).hexdigest()))
            cat=root/'catalog.json';cat.write_text(json.dumps(d));out=root/'gallery.html'
            cmd=[sys.executable,str(ROOT/'scripts/reference_library.py'),'--catalog',str(cat),'--asset-root',str(root),'gallery','--output',str(out)]
            result=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertIn('data:image/png;base64,',out.read_text())
            prior=out.read_bytes();result=subprocess.run(cmd,capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0);self.assertEqual(prior,out.read_bytes())

    def test_shortlist_unknown_and_dated_review(self):
        with tempfile.TemporaryDirectory() as td:
            cat=Path(td)/'catalog.json';cat.write_text(json.dumps(catalog(record(checked_on='2026-01-01'))))
            prefix=[sys.executable,str(ROOT/'scripts/reference_library.py'),'--catalog',str(cat)]
            result=subprocess.run(prefix+['show','A999'],capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0)
            result=subprocess.run(prefix+['review-due','--today','2026-11-07','--days','90'],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(len(json.loads(result.stdout)),1)

if __name__=='__main__':unittest.main()
