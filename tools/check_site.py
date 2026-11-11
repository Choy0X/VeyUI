#!/usr/bin/env python3
"""Static checks for the landing page in site/. Run from the repository root:

    python tools/check_site.py

Checks: authored files are plain ASCII, JSON-LD parses, the FAQPage JSON-LD equals the
visible FAQ, every local href/src/url() resolves, no third-party loads (scripts, styles,
fonts, images, frames), absolute canonical and social image URLs, social images have the
right pixel size, no leftover files from the retired UI kit. Exits 1 on any failure.
"""
import json
import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'site'
BASE = 'https://choy0x.github.io/VeyUI/'
errors = []


def fail(msg):
    errors.append(msg)


# 1. ASCII in authored text files (vendored libraries and licence texts are exempt)
authored = [p for p in SITE.rglob('*') if p.is_file() and p.suffix in ('.html', '.css', '.js', '.txt', '.xml', '.svg')]
for p in authored:
    rel = p.relative_to(SITE).as_posix()
    if rel.startswith('assets/vendor/') or p.name.upper().startswith('LICENSE'):
        continue
    text = p.read_text(encoding='utf-8')
    bad = sorted({c for c in text if ord(c) > 127})
    if bad:
        fail('non-ASCII characters in %s: %s' % (rel, ' '.join('U+%04X' % ord(c) for c in bad[:8])))

# 2. retired kit files must be gone
for rel in ['assets/system.css', 'assets/system.js', 'assets/veyui.css', 'assets/veyui.js',
            'assets/layout', 'assets/moments', 'assets/motion', 'assets/ui']:
    if (SITE / rel).exists():
        fail('retired kit path still present: site/' + rel)

index = (SITE / 'index.html').read_text(encoding='utf-8')


# 3. parse the page
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []          # (tag, attr, value)
        self.ldjson = []
        self._ld = False
        self.faq = []           # (question, answer)
        self._stack = []
        self._cur = None
        self.h1 = 0
        self.meta = {}
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ('href', 'src', 'srcset', 'data-src', 'data-path'):
            if k in a and a[k]:
                self.refs.append((tag, k, a[k]))
        if tag == 'h1':
            self.h1 += 1
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self._ld = True
            self.ldjson.append('')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href')
        if tag == 'meta':
            key = a.get('property') or a.get('name')
            if key:
                self.meta[key] = a.get('content', '')
        if tag == 'button' and 'acc__btn' in (a.get('class') or ''):
            self._cur = ['q', '']
        if tag == 'div' and 'acc__p' in (a.get('class') or ''):
            self._cur = ['a', '']
            self._depth = 1
        elif tag == 'div' and self._cur and self._cur[0] == 'a':
            self._depth += 1

    def handle_endtag(self, tag):
        if tag == 'script':
            self._ld = False
        if tag == 'button' and self._cur and self._cur[0] == 'q':
            self.faq.append([self._cur[1].strip(), ''])
            self._cur = None
        if tag == 'div' and self._cur and self._cur[0] == 'a':
            self._depth -= 1
            if self._depth == 0:
                if self.faq:
                    self.faq[-1][1] = re.sub(r'\s+', ' ', self._cur[1]).strip()
                self._cur = None

    def handle_data(self, data):
        if self._ld:
            self.ldjson[-1] += data
        elif self._cur:
            self._cur[1] += data


page = Page()
page.feed(index)

if page.h1 != 1:
    fail('index.html must have exactly one h1, found %d' % page.h1)
if page.canonical != BASE:
    fail('canonical must be ' + BASE + ', found %s' % page.canonical)
for key in ('og:image', 'twitter:image'):
    if not page.meta.get(key, '').startswith(BASE + 'assets/'):
        fail(key + ' must be an absolute URL under ' + BASE + 'assets/')

docs = []
for raw in page.ldjson:
    try:
        docs.append(json.loads(raw))
    except ValueError as e:
        fail('JSON-LD does not parse: %s' % e)
faq_ld = next((d for d in docs if d.get('@type') == 'FAQPage'), None)
if not faq_ld:
    fail('FAQPage JSON-LD missing')
else:
    ld = [(q['name'], q['acceptedAnswer']['text']) for q in faq_ld['mainEntity']]
    vis = [tuple(x) for x in page.faq]
    if ld != vis:
        fail('FAQPage JSON-LD differs from the visible FAQ (%d vs %d entries)' % (len(ld), len(vis)))
if not any(d.get('@type') in ('SoftwareApplication', ['SoftwareApplication', 'SoftwareSourceCode']) for d in docs):
    fail('SoftwareApplication JSON-LD missing')

# 4. local references resolve, nothing third-party is loaded
loaders = {('link', 'href'), ('script', 'src'), ('img', 'src'), ('source', 'srcset'), ('iframe', 'src'), ('iframe', 'data-src')}
for tag, attr, val in page.refs:
    if attr == 'srcset':
        val = val.split()[0]
    if val.startswith(('#', 'mailto:', 'data:')):
        continue
    if re.match(r'^[a-z]+://', val):
        if val.startswith(BASE):
            continue
        if (tag, attr) in loaders and tag != 'a':
            fail('third-party load in index.html: %s' % val)
        continue
    if val.startswith('/'):
        fail('root-absolute URL (breaks under /VeyUI/): ' + val)
        continue
    target = SITE / val.split('#')[0].split('?')[0]
    if val.split('#')[0].endswith('/') or target.is_dir():
        target = target / 'index.html'
    if not target.exists():
        fail('missing local file referenced by index.html: ' + val)

for p in list(SITE.rglob('*.css')) + list(SITE.rglob('*.js')) + list(SITE.glob('examples/*/index.html')):
    rel = p.relative_to(SITE).as_posix()
    if rel.startswith('assets/vendor/'):
        continue
    text = p.read_text(encoding='utf-8')
    for m in re.finditer(r'''(?:url\(\s*|src=["']|href=["']|@import\s+["']|import\(?\s*["'])(https?:)?//[^"')\s]+''', text):
        if m.group(0).startswith(('href="http', "href='http")):
            continue
        fail('third-party load in %s: %s' % (rel, m.group(0)[:80]))
    for m in re.finditer(r'''url\(\s*["']?(?!data:|https?:|#|%23)([^"')]+)''', text) if p.suffix == '.css' else []:
        ref = (p.parent / m.group(1).split('?')[0].split('#')[0]).resolve()
        if not ref.exists():
            fail('missing file referenced by %s: %s' % (rel, m.group(1)))

# 5. example pages: local refs resolve
for ex in sorted((SITE / 'examples').glob('*/index.html')):
    html = ex.read_text(encoding='utf-8')
    for m in re.finditer(r'''(?:src|href)=["']([^"'#:]+)["']''', html):
        val = m.group(1)
        if val.startswith(('http', '//', 'data:', 'mailto:')):
            continue
        if not (ex.parent / val).resolve().exists():
            fail('missing file referenced by %s: %s' % (ex.relative_to(SITE), val))

# 5b. the before and after section: five named fixes, both static frames, controls, no removed-example leftovers
if index.count('class="ba__fix"') != 5:
    fail('the #choice section must list exactly 5 named fixes, found %d' % index.count('class="ba__fix"'))
if index.count('class="ba__fig"') != 2:
    fail('the #choice section must have a before and an after frame')
for needle in ('id="ba-range"', 'role="radiogroup"', 'fictional product', 'sample data'):
    if needle not in index:
        fail('before and after section is missing: ' + needle)
for stale in ('examples/', 'Ledgerline', 'Hushloop', 'Tracewell', 'poster-m-'):
    if stale in index or stale in (SITE / 'assets' / 'js' / 'main.js').read_text(encoding='utf-8'):
        fail('stale reference to a removed example: ' + stale)

# 5c. the hero: before and after teaser with a real range control, no generic-card deck
m = re.search(r'<section class="hero".*?</section>', index, re.S)
if not m:
    fail('hero section missing')
else:
    hero = m.group(0)
    for needle in ('type="range"', 'Typical agent output', 'Designed with veyUI', 'href="#choice"', 'hero-after', 'hero-before'):
        if needle not in hero:
            fail('hero is missing: ' + needle)
    for stale in ('class="deck"', 'class="slot"', 'g__t', 'face--gen', 'hero__field', 'hero-field-poster'):
        if stale in index:
            fail('retired hero markup still present: ' + stale)
    if len(re.findall(r'<h1[ >]', hero)) != 1:
        fail('hero must contain exactly one h1')

# 6. social images have the declared size
def png_size(path):
    with open(path, 'rb') as f:
        head = f.read(24)
    if head[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    return struct.unpack('>II', head[16:24])


for name, size in (('og-image.png', (1200, 630)), ('social-preview.png', (1280, 640))):
    path = SITE / 'assets' / name
    got = png_size(path) if path.exists() else None
    if got != size:
        fail('%s must be %dx%d PNG, found %s' % (name, size[0], size[1], got))

# 7. sitemap and robots point at the project URL
if BASE not in (SITE / 'sitemap.xml').read_text(encoding='utf-8'):
    fail('sitemap.xml does not list ' + BASE)
if 'sitemap.xml' not in (SITE / 'robots.txt').read_text(encoding='utf-8'):
    fail('robots.txt does not reference the sitemap')

if errors:
    print('site check failed:')
    for e in errors:
        print(' -', e)
    sys.exit(1)
print('site check ok: %d authored files, %d FAQ entries match, %d JSON-LD blocks' % (len(authored), len(page.faq), len(docs)))
