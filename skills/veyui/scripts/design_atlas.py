#!/usr/bin/env python3
"""Offline design playbook retrieval. Python standard library, no network or paid service."""
import argparse
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))

def terms(value):
    tokens = re.findall(r'[a-z0-9]+', value.lower())
    return [t[:-1] if t.endswith('s') and not t.endswith('ss') and len(t) > 4 else t for t in tokens]

def validate():
    cards = load('patterns.json')['patterns']
    sources = load('sources.json')['sources']
    benchmarks = load('user-benchmarks.json')['benchmarks']
    known = {s['id'] for s in sources + benchmarks}
    errors = []
    for label, values in [('patterns', cards), ('sources', sources), ('benchmarks', benchmarks)]:
        ids = [v['id'] for v in values]
        if len(ids) != len(set(ids)):
            errors.append(f'Duplicate IDs in {label}')
    required = ('id', 'title', 'category', 'platforms', 'job', 'composition', 'avoid', 'review', 'provenance')
    for card in cards:
        for field in required:
            if not card.get(field):
                errors.append(f"{card.get('id')}: missing {field}")
        for source in card.get('related_sources', []):
            if source not in known:
                errors.append(f"{card['id']}: unknown source {source}")
        if card.get('provenance') != 'original_synthesis' or card.get('visual_evidence') != 'none':
            errors.append(f"{card['id']}: unexpected provenance, review manually")
    return cards, sources, benchmarks, errors

def search(cards, query, platform, category, limit):
    q = set(terms(query))
    if platform:
        q.discard(platform)
    corpus = [set(terms(' '.join(str(c.get(f, '')) for f in ('title','job','composition','avoid','review','category')))) for c in cards]
    idf = {t: math.log(1 + len(cards) / (1 + sum(t in doc for doc in corpus))) for t in q}
    ranked = []
    for c, doc in zip(cards, corpus):
        if platform and platform not in c['platforms'] and 'all' not in c['platforms']:
            continue
        if category and category != c['category']:
            continue
        title = set(terms(c['title']))
        job = set(terms(c['job']))
        category_words = set(terms(c['category']))
        score = sum(idf[t] * (4 if t in title or t in category_words else 2 if t in job else 1) for t in q if t in doc)
        if q and score == 0:
            continue
        ranked.append((score,c))
    ranked.sort(key=lambda p:(-p[0],p[1]['id']))
    return [dict(c, retrieval_score=round(score,3)) for score,c in ranked[:limit]]

def markdown(cards):
    out=['# Retrieved design patterns', '', 'Original guidance, not observed product screenshots. Retrieval rank is relevance, not quality.', '']
    for c in cards:
        out += [f"## {c['id']} · {c['title']}", '', f"- Use for: {c['job']}", f"- Compose: {c['composition']}", f"- Avoid: {c['avoid']}", f"- Review: {c['review']}", f"- Platform: {', '.join(c['platforms'])}", f"- Further study IDs: {', '.join(c['related_sources'])}", '']
    return '\n'.join(out)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p=sub.add_parser('search'); p.add_argument('query'); p.add_argument('--platform',choices=['web','mobile','desktop']); p.add_argument('--category'); p.add_argument('--limit',type=int,default=6); p.add_argument('--format',choices=['json','md'],default='md')
    p=sub.add_parser('show'); p.add_argument('ids',nargs='+'); p.add_argument('--format',choices=['json','md'],default='md')
    p=sub.add_parser('sources'); p.add_argument('--ids',nargs='*'); p.add_argument('--kind'); p.add_argument('--available-only',action='store_true')
    sub.add_parser('benchmarks'); sub.add_parser('stats'); sub.add_parser('validate')
    args=parser.parse_args()
    cards,sources,benchmarks,errors=validate()
    if errors:
        print(json.dumps({'valid':False,'errors':errors},indent=2)); return 1
    if args.command in ('validate','stats'):
        print(json.dumps({'schema_valid':True,'patterns':len(cards),'categories':sorted({c['category'] for c in cards}),'sources':len(sources),'source_status_counts':{k:sum(s['status']==k for s in sources) for k in sorted({s['status'] for s in sources})},'user_reference_observations':len(benchmarks),'external_screen_captures_in_original_atlas':0,'additional_reference_library':'data/reference-library.json (run reference_library.py stats)' ,'model_training_performed':False,'notice':'Schema validity is not visual quality approval.'},indent=2)); return 0
    if args.command=='benchmarks':
        print(json.dumps(load('user-benchmarks.json'),indent=2)); return 0
    if args.command=='sources':
        pool=sources+benchmarks
        result=[s for s in pool if (not args.ids or s['id'] in args.ids) and (not args.kind or s['kind']==args.kind) and (not args.available_only or s.get('status','').startswith('text_verified'))]
        if args.ids:
            missing=set(args.ids)-{s['id'] for s in result}
            if missing:
                parser.error('Unknown or filtered source IDs: '+', '.join(sorted(missing)))
        print(json.dumps(result,indent=2)); return 0
    if args.command=='show':
        lookup={c['id']:c for c in cards}
        missing=set(args.ids)-set(lookup)
        if missing: parser.error('Unknown pattern IDs: '+', '.join(sorted(missing)))
        result=[lookup[i] for i in args.ids]
    else:
        if not 1<=args.limit<=30: parser.error('--limit must be between 1 and 30')
        if args.category and args.category not in {c['category'] for c in cards}: parser.error('Unknown category; run stats')
        result=search(cards,args.query,args.platform,args.category,args.limit)
    print(json.dumps(result,indent=2) if args.format=='json' else markdown(result))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
