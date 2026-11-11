#!/usr/bin/env python3
"""Isolated review infrastructure; never generates designs or certifies taste.

init ROOT [--count N] [--kind landing|app]; build ROOT;
check ROOT [--stage review|implement]
Only public/ is meant to be served. Manifest declarations need actual evidence.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path
import sys
from urllib.parse import urlparse, quote


def text(value):
    return html.escape(str(value), quote=True)


def local_file(public, value):
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError("Expected a nonempty public-relative file path")
    candidate = (public / value).resolve()
    if not candidate.is_relative_to(public.resolve()):
        raise ValueError("File path escapes public directory")
    if any(part.startswith('.') for part in Path(value).parts):
        raise ValueError("Hidden paths are not public assets")
    return candidate


def http_url(value):
    try:
        p = urlparse(value)
        return p.scheme in ('http', 'https') and bool(p.hostname) and not p.username and not p.password
    except (TypeError, ValueError):
        return False


def digest(data):
    # Selection does not alter the review gallery; visual/review declarations do.
    visible = {k: v for k, v in data.items() if k != 'selection'}
    return hashlib.sha256(json.dumps(visible, sort_keys=True).encode()).hexdigest()


def read(root):
    data = json.loads((root / 'studio.json').read_text(encoding='utf-8'))
    if not isinstance(data, dict) or not isinstance(data.get('candidates'), list):
        raise ValueError('Expected an object with candidates array')
    if not all(isinstance(c, dict) for c in data['candidates']):
        raise ValueError('Each candidate must be an object')
    ids = [c.get('id') for c in data['candidates']]
    if any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids)):
        raise ValueError('Candidate IDs must be nonempty and unique')
    return data


def initialize(root, count, kind='landing'):
    if root.exists():
        raise ValueError('Choose a new isolated directory; init never overwrites existing work')
    root.mkdir(parents=True)
    (root / 'public').mkdir()
    (root / 'reviews').mkdir()
    views = (['wide-opening', 'compact-opening', 'wide-complete', 'compact-complete']
             if kind == 'landing' else ['entry', 'primary-action', 'outcome', 'alternate-or-recovery', 'compact'])
    candidates = []
    for i in range(count):
        ident = chr(97 + i)
        (root / 'public' / ident).mkdir()
        candidates.append({
            'id': ident, 'version': '1', 'title': f'Concept {ident.upper()} — draft',
            'premise': '', 'tradeoff': '', 'entry': f'{ident}/index.html',
            'preview_url': '', 'runtime_reviewed': False, 'access_checked': False,
            'main_action_tested': False, 'reference_fit': '',
            'reference_links': [],
            'scope_complete': False, 'scope_summary': '', 'limitations': '', 'runtime': '',
            'known_material_defects': [],
            'captures': [{'view': view, 'artifact_version': '1', 'path': '', 'inspected': False, 'observation': ''} for view in views],
            'reviews': [{'perspective': role, 'reviewer': '', 'artifact_version': '1',
                         'status': 'unverified', 'path': f'reviews/{ident}-{role}.md'}
                        for role in ['visual', 'ux-engineering']]
        })
    data = {'schema_version': 2, 'title': 'Design concepts', 'kind': kind,
            'required_views': views, 'lead_id': '', 'review_method': 'pending', 'review_fallback_reason': '',
            'requested_count': count,
            'reference_links_required': True, 'reference_exception_reason': '',
            'count_reason': '' if count != 3 else 'Default material-design exploration',
            'gallery_url': '', 'gallery_access_checked': False, 'access_lifetime': '',
            'candidates': candidates, 'selection': None}
    (root / 'studio.json').write_text(json.dumps(data, indent=2) + '\n')
    print(f'Created draft workspace: {root}. Author concepts; no designs or hosting created.')


def coverage(root, data, stage, check_gallery=True):
    errors = []
    public = root / 'public'
    if data.get('schema_version') != 2:
        errors.append('Use schema_version 2 and record scope coverage plus reviewer evidence')
    required = data.get('required_views')
    if (not isinstance(required, list) or len(required) < 2 or
            not all(isinstance(v, str) and v for v in required)):
        errors.append('Record required complete-page or end-to-end task views')
        required = []
    elif len(required) != len(set(required)):
        errors.append('Required view names must be unique')
    core_views = {'landing': {'wide-opening', 'compact-opening', 'wide-complete', 'compact-complete'},
                  'app': {'entry', 'primary-action', 'outcome', 'alternate-or-recovery', 'compact'}}
    kind = data.get('kind')
    if kind not in core_views:
        errors.append('Specify kind landing or app')
    elif not core_views[kind].issubset(set(required)):
        errors.append('Required views omit core complete-experience coverage for ' + kind)
    if not data.get('lead_id'):
        errors.append('Record the design lead')
    method = data.get('review_method')
    if method not in ('independent', 'self-review'):
        errors.append('Record independent review or an explicit self-review fallback')
    if method == 'self-review' and not data.get('review_fallback_reason'):
        errors.append('Explain why independent review is unavailable')
    if data.get('requested_count') != len(data['candidates']) or not data['candidates']:
        errors.append('Candidate count differs from requested_count or is empty')
    if data.get('requested_count') != 3 and not data.get('count_reason'):
        errors.append('Record the user-requested count or specific scope exception')
    if data.get('reference_links_required') is False and not data.get('reference_exception_reason'):
        errors.append('Record the explicit scope/user exception to existing-example links')
    if not http_url(data.get('gallery_url')) or data.get('gallery_access_checked') is not True:
        errors.append('Gallery needs an actual HTTP(S) URL and declared access check')
    urls = [c.get('preview_url') for c in data['candidates'] if c.get('preview_url')]
    if len(urls) != len(set(urls)):
        errors.append('Candidates must have distinct direct preview URLs')
    if not data.get('access_lifetime'):
        errors.append('Record access lifetime (local session, preview expiry, or persistent)')
    if check_gallery:
        gallery = public / 'index.html'
        receipt = root / 'gallery-receipt.json'
        if not gallery.is_file() or not receipt.is_file():
            errors.append('Build the review gallery and its freshness receipt')
        else:
            try:
                built = json.loads(receipt.read_text(encoding='utf-8'))
                if (built.get('manifest_digest') != digest(data) or
                        built.get('gallery_digest') != hashlib.sha256(gallery.read_bytes()).hexdigest()):
                    errors.append('Gallery is stale or modified: rebuild after updating the manifest')
            except (OSError, ValueError, AttributeError):
                errors.append('Invalid gallery receipt: rebuild the gallery')
    for c in data['candidates']:
        prefix = str(c['id']) + ': '
        refs = c.get('reference_links', [])
        if not isinstance(refs, list):
            errors.append(prefix + 'reference_links must be a list')
            refs = []
        if data.get('reference_links_required') is True and not refs:
            errors.append(prefix + 'missing existing-example link for this concept')
        for ref in refs:
            if not isinstance(ref, dict):
                errors.append(prefix + 'invalid existing-example record')
                continue
            if not http_url(ref.get('url')):
                errors.append(prefix + 'existing example needs a public HTTP(S) URL without credentials')
            for key in ('title', 'surface', 'where_to_look', 'adaptation', 'evidence_basis', 'checked_at'):
                if not isinstance(ref.get(key), str) or not ref[key].strip():
                    errors.append(prefix + 'existing example missing ' + key)
            if ref.get('access_checked') is not True:
                errors.append(prefix + 'existing-example access check not recorded')
        for key in ('title', 'version', 'premise', 'tradeoff', 'reference_fit', 'scope_summary', 'limitations', 'runtime'):
            if not isinstance(c.get(key), str) or not c[key].strip():
                errors.append(prefix + 'missing ' + key)
        try:
            entry = local_file(public, c.get('entry'))
            if not entry.is_file() or not entry.stat().st_size:
                errors.append(prefix + 'missing nonempty entry/build output')
        except ValueError as e:
            errors.append(prefix + str(e))
        if not http_url(c.get('preview_url')):
            errors.append(prefix + 'missing actual preview URL')
        for key in ('runtime_reviewed', 'access_checked', 'main_action_tested', 'scope_complete'):
            if c.get(key) is not True:
                errors.append(prefix + key + ' not declared complete')
        if c.get('known_material_defects') != []:
            errors.append(prefix + 'unresolved or unspecified material defects')
        captures = c.get('captures')
        if not isinstance(captures, list) or len(captures) < 2:
            errors.append(prefix + 'need at least two relevant views/device classes')
            continue
        views = set()
        for cap in captures:
            if not isinstance(cap, dict):
                errors.append(prefix + 'invalid capture record')
                continue
            if cap.get('view'):
                views.add(str(cap['view']))
            try:
                f = local_file(public, cap.get('path'))
                if not f.is_file() or not f.stat().st_size:
                    errors.append(prefix + 'missing capture file')
            except ValueError as e:
                errors.append(prefix + str(e))
            if cap.get('inspected') is not True or not cap.get('observation'):
                errors.append(prefix + 'capture needs personal inspection and observation')
            if cap.get('artifact_version') != c.get('version'):
                errors.append(prefix + 'capture version does not match current candidate')
        if len(views) < 2:
            errors.append(prefix + 'capture view labels must identify different review views')
        for view in required:
            if view not in views:
                errors.append(prefix + 'missing required view: ' + view)
        reviews = c.get('reviews')
        if not isinstance(reviews, list) or not all(isinstance(r, dict) for r in reviews):
            errors.append(prefix + 'missing valid review records')
            continue
        assigned = []
        for role in ('visual', 'ux-engineering'):
            records = [r for r in reviews if r.get('perspective') == role]
            if len(records) != 1:
                errors.append(prefix + 'need one current review record for ' + role)
                continue
            review = records[0]
            reviewer = review.get('reviewer')
            assigned.append(reviewer)
            if not isinstance(reviewer, str) or not reviewer.strip():
                errors.append(prefix + 'missing reviewer identity for ' + role)
            if review.get('artifact_version') != c.get('version'):
                errors.append(prefix + 'stale review version for ' + role)
            if review.get('status') != 'clear':
                errors.append(prefix + 'material findings not declared resolved for ' + role)
            try:
                report = local_file(root, review.get('path'))
                if not report.is_file() or not report.stat().st_size:
                    errors.append(prefix + 'missing review report for ' + role)
            except ValueError as e:
                errors.append(prefix + str(e))
        if method == 'independent' and (data.get('lead_id') in assigned or len(set(assigned)) != 2):
            errors.append(prefix + 'independent review requires two reviewers distinct from the lead')
    if stage == 'implement':
        choice = data.get('selection')
        if not isinstance(choice, dict):
            errors.append('No recorded concept selection; application integration remains blocked')
        else:
            candidate = next((c for c in data['candidates'] if c['id'] == choice.get('id')), None)
            if not candidate or choice.get('version') != candidate.get('version'):
                errors.append('Selection must identify a current reviewed candidate version')
            if choice.get('authority') not in ('user-selected', 'explicitly-delegated') or not choice.get('evidence'):
                errors.append('Record actual selection/delegation evidence, not inferred approval')
    return errors


def build(root, data):
    public = root / 'public'
    cards = []
    for c in data['candidates']:
        entry = local_file(public, c.get('entry'))
        url = c.get('preview_url')
        if url and not http_url(url):
            raise ValueError('preview_url must be HTTP(S) without embedded credentials')
        href = url or quote(entry.relative_to(public.resolve()).as_posix(), safe='/')
        refs = c.get('reference_links', [])
        if not isinstance(refs, list):
            raise ValueError('reference_links must be a list')
        reference_items = []
        for ref in refs:
            if not isinstance(ref, dict) or not http_url(ref.get('url')):
                raise ValueError('existing-example URL must be HTTP(S) without embedded credentials')
            access = ('Access check recorded: ' + str(ref.get('checked_at', 'date missing'))
                      if ref.get('access_checked') is True else 'Access not checked')
            reference_items.append(f'<li><a href="{text(ref["url"])}" rel="noopener noreferrer">View existing example: {text(ref.get("title", "Reference"))}</a><p>{text(ref.get("surface", ""))} — {text(access)}</p><p><b>Where to look:</b> {text(ref.get("where_to_look", ""))}</p><p><b>Adaptation:</b> {text(ref.get("adaptation", ""))}</p><p><b>Evidence:</b> {text(ref.get("evidence_basis", ""))}</p></li>')
        reference_section = '<h3>Existing inspiration</h3><ul>' + ''.join(reference_items) + '</ul>' if reference_items else ''
        captures = []
        for cap in c.get('captures', []):
            if not cap.get('path'):
                continue
            f = local_file(public, cap['path'])
            if f.is_file():
                src = quote(f.relative_to(public.resolve()).as_posix(), safe='/')
                captures.append(f'<figure><a href="{text(src)}"><img src="{text(src)}" alt="{text(cap.get("view", "Capture"))}"></a><figcaption>{text(cap.get("view", ""))}: {text(cap.get("observation", "Not inspected"))}</figcaption></figure>')
        cards.append(f'<article><h2>{text(c.get("title", c["id"]))}</h2><p>{text(c.get("premise", ""))}</p><p><b>Scope:</b> {text(c.get("scope_summary", ""))}</p><p><b>Runtime:</b> {text(c.get("runtime", ""))}</p><p><b>Limitations:</b> {text(c.get("limitations", ""))}</p><p><b>Tradeoff:</b> {text(c.get("tradeoff", ""))}</p><a class="open" href="{text(href)}">Open concept {text(c["id"].upper())}</a>{reference_section}<div class="captures">{"".join(captures)}</div></article>')
    errors = coverage(root, data, 'review', check_gallery=False)
    status = 'Draft — review declarations incomplete' if errors else 'Review evidence recorded — assess the actual designs'
    page = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{text(data.get('title', 'Design concepts'))}</title>
<style>body{{font:16px/1.5 system-ui,sans-serif;background:#f7f7f8;color:#171719;max-width:1400px;margin:0 auto;padding:32px}}h1{{font-size:32px}}main{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:20px}}article{{background:white;border:1px solid #ddd;border-radius:16px;padding:24px;min-width:0}}.open{{display:inline-block;background:#171719;color:white;padding:10px 16px;border-radius:8px}}figure{{margin:24px 0}}img{{display:block;width:100%;height:240px;object-fit:contain;object-position:top;background:#eee}}figcaption{{font-size:13px;margin-top:8px}}a:focus-visible{{outline:3px solid #205dde;outline-offset:4px}}footer{{margin-top:32px}}</style>
<header><h1>{text(data.get('title', 'Design concepts'))}</h1><p>{text(status)}</p><p>Open each direction at full size. Captures document reviewed views; they do not replace interaction review.</p></header><main>{''.join(cards)}</main><footer>{text(data.get('access_lifetime', 'Preview access has not been verified.'))}</footer></html>'''
    public.mkdir(parents=True, exist_ok=True)
    (public / 'index.html').write_text(page, encoding='utf-8')
    (root / 'gallery-receipt.json').write_text(json.dumps({
        'manifest_digest': digest(data),
        'gallery_digest': hashlib.sha256((public / 'index.html').read_bytes()).hexdigest()
    }, indent=2) + '\n')
    print(f'Built {public / "index.html"}. This command does not host or inspect the pages.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('init', 'build', 'check'))
    parser.add_argument('root', type=Path)
    parser.add_argument('--count', type=int, choices=range(1, 7), default=3)
    parser.add_argument('--kind', choices=('landing', 'app'), default='landing')
    parser.add_argument('--stage', choices=('review', 'implement'), default='review')
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == 'init':
            initialize(root, args.count, args.kind)
        else:
            data = read(root)
            if args.command == 'build':
                build(root, data)
            else:
                errors = coverage(root, data, args.stage)
                for error in errors:
                    print('INCOMPLETE: ' + error)
                print('Declaration/file coverage only; no visual-quality or URL-reachability certification.')
                return bool(errors)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
