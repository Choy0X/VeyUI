import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('studio', ROOT / 'scripts/concept_studio.py')
studio = importlib.util.module_from_spec(spec)
spec.loader.exec_module(studio)


class ConceptReferences(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'studio'
        with contextlib.redirect_stdout(io.StringIO()):
            studio.initialize(self.root, 3)
        self.data = studio.read(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def ref(self, url='https://example.com/product'):
        return dict(title='<Studio & sample>', url=url, surface='public tour',
                    where_to_look='Project list', adaptation='Row hierarchy',
                    evidence_basis='Fixture only; not a verified real source',
                    checked_at='2026-11-07', access_checked=True)

    def errors(self):
        return studio.coverage(self.root, self.data, 'review', check_gallery=False)

    def build(self):
        with contextlib.redirect_stdout(io.StringIO()):
            studio.build(self.root, self.data)
        return (self.root / 'public/index.html').read_text()

    def test_new_studio_requires_example_for_every_candidate(self):
        self.assertEqual(sum('missing existing-example link' in e for e in self.errors()), 3)

    def test_missing_access_check_is_not_accepted(self):
        ref = self.ref(); ref['access_checked'] = False
        self.data['candidates'][0]['reference_links'] = [ref]
        self.assertTrue(any('access check not recorded' in e for e in self.errors()))

    def test_gallery_keeps_reference_and_generated_preview_distinct(self):
        c = self.data['candidates'][0]
        c['reference_links'] = [self.ref()]
        c['preview_url'] = 'https://example.com/generated/a'
        page = self.build()
        self.assertIn('href="https://example.com/product"', page)
        self.assertIn('href="https://example.com/generated/a"', page)
        self.assertIn('View existing example: &lt;Studio &amp; sample&gt;', page)
        self.assertIn('Open concept A', page)
        self.assertNotIn('<Studio & sample>', page)

    def test_unsafe_reference_links_are_rejected(self):
        for url in ['javascript:alert(1)', 'https://name:secret@example.com/', 'file:///private']:
            with self.subTest(url=url):
                self.data['candidates'][0]['reference_links'] = [self.ref(url)]
                with self.assertRaises(ValueError): self.build()

    def test_exception_requires_reason(self):
        self.data['reference_links_required'] = False
        self.assertTrue(any('scope/user exception' in e for e in self.errors()))

    def test_reference_change_invalidates_gallery_receipt(self):
        self.data['candidates'][0]['reference_links'] = [self.ref()]
        self.build()
        self.data['candidates'][0]['reference_links'][0]['adaptation'] = 'Different relationship'
        errors = studio.coverage(self.root, self.data, 'review')
        self.assertTrue(any('Gallery is stale' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
