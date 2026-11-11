#!/usr/bin/env python3
"""Offline reference retrieval and a portable visual catalog. No paid service or model training."""
import argparse
import base64
import hashlib
import json
import mimetypes
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'data/reference-library.json'
EVIDENCE = {'image_inspected', 'image_overview_inspected', 'text_inspected', 'discovery_lead', 'unreviewed'}
KINDS = {'concept', 'shipped_screen', 'app_store_preview', 'site_reference', 'documented_flow'}

def safe_asset(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError('Missing or unsafe asset: ' + value)
    if path.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp'}:
        raise ValueError('Unsupported image: ' + value)
    return path

def validate(data, root=ROOT):
    if data.get('schema_version') != 1 or not isinstance(data.get('records'), list):
        raise ValueError('Unsupported catalog schema')
    ids, hashes = set(), set()
    for r in data['records']:
        for key in ('id','title','kind','platforms','patterns','evidence','source','observations','adaptation','limitations','rights','checked_on'):
            if key not in r:
                raise ValueError('Missing field: ' + key)
        if not re.fullmatch(r'[A-Z][0-9]{3,6}',r['id']) or r['id'] in ids:
            raise ValueError('Invalid/duplicate ID: ' + r['id'])
        ids.add(r['id'])
        if r['kind'] not in KINDS or r['evidence'] not in EVIDENCE:
            raise ValueError('Unknown kind/evidence: ' + r['id'])
        if not r['platforms'] or not set(r['platforms']) <= {'web','mobile','desktop'}:
            raise ValueError('Invalid platform: ' + r['id'])
        for field in ('patterns','observations','limitations'):
            if not isinstance(r[field],list) or not all(isinstance(v,str) for v in r[field]):
                raise ValueError('Expected text list: ' + field)
        date.fromisoformat(r['checked_on'])
        for key in ('url','image_url'):
            if r.get(key) and (urlsplit(r[key]).scheme != 'https' or not urlsplit(r[key]).netloc):
                raise ValueError('Only HTTPS reference URLs: ' + r['id'])
        if r['kind']=='shipped_screen' and r['evidence']!='image_inspected':
            raise ValueError('A screen record requires inspected image evidence')
        # asset_withheld marks a record whose image was inspected but is intentionally not distributed.
        if r['evidence'] in {'image_inspected','image_overview_inspected'} and not (r.get('asset') or r.get('image_url') or r.get('asset_withheld')):
            raise ValueError('Image evidence needs a locator')
        if r.get('asset_withheld') and r.get('asset'):
            raise ValueError('A record cannot both bundle and withhold its image: '+r['id'])
        if r['evidence'] in {'image_inspected','image_overview_inspected'} and not r['observations']:
            raise ValueError('Inspected image needs observations: '+r['id'])
        if r.get('content_role') not in {None,'promotional_art','ui_presentation','unknown'}:
            raise ValueError('Unknown content role: '+r['id'])
        if r.get('asset'):
            path=safe_asset(root,r['asset']); digest=hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != r.get('sha256') or digest in hashes:
                raise ValueError('Hash mismatch/duplicate asset: ' + r['id'])
            hashes.add(digest)
    return data

def query(records, text='', platform=None, kind=None, evidence=None, pattern=None):
    terms=set(re.findall(r'\w+',text.casefold()))
    result=[]
    for r in records:
        if platform and platform not in r['platforms']: continue
        if kind and kind!=r['kind']: continue
        if evidence and evidence!=r['evidence']: continue
        if pattern and pattern not in r['patterns']: continue
        words=set(re.findall(r'\w+', ' '.join([r['title'],r.get('category',''),r.get('app',''),*r['patterns'],*r['observations'],r['adaptation']]).casefold()))
        matched=terms & words
        if terms and matched!=terms: continue
        # Prefer observed task patterns over product-name/category-only matches.
        def hits(value):return len(terms & set(re.findall(r'\w+',value.casefold())))
        relevance=12*hits(' '.join(r['patterns']))+4*hits(' '.join(r['observations']))+2*hits(r['title'])
        evidence_rank={'image_inspected':4,'image_overview_inspected':3,'text_inspected':2,'discovery_lead':1,'unreviewed':0}[r['evidence']]
        result.append((relevance+evidence_rank,r))
    return [r for _,r in sorted(result,key=lambda x:(-x[0],x[1]['id']))]

def stats(records):
    return {'records':len(records),'by_kind':dict(Counter(r['kind'] for r in records)),
            'by_evidence':dict(Counter(r['evidence'] for r in records)),
            'bundled_images':sum(bool(r.get('asset')) for r in records),
            'withheld_images':sum(bool(r.get('asset_withheld')) for r in records),
            'linked_images':sum(bool(r.get('image_url')) for r in records),
            'apps_with_publisher_previews':len({r['app_id'] for r in records if r.get('app_id')}),
            'by_content_role':dict(Counter(r.get('content_role','not_classified') for r in records)),
            'notice':'Records, images, documented flows and original pattern cards are different counts. No training or automatic updates.'}

def gallery(data, root=ROOT):
    records=[]
    for r in data['records']:
        item=dict(r)
        if r.get('asset'):
            p=safe_asset(root,r['asset'])
            item['preview']='data:'+mimetypes.guess_type(p.name)[0]+';base64,'+base64.b64encode(p.read_bytes()).decode()
        records.append(item)
    payload=json.dumps(records,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    template=(ROOT/'assets/reference-gallery.template.html').read_text(encoding='utf-8')
    return template.replace('/*REFERENCE_DATA*/',payload)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--catalog',type=Path,default=CATALOG)
    p.add_argument('--asset-root',type=Path,default=ROOT,help='Root for local images in a project-owned catalog')
    sub=p.add_subparsers(dest='command',required=True)
    for name in ('stats','validate'):sub.add_parser(name)
    s=sub.add_parser('search');s.add_argument('query',nargs='?',default='')
    s.add_argument('--platform',choices=['web','mobile','desktop']);s.add_argument('--kind',choices=sorted(KINDS))
    s.add_argument('--evidence',choices=sorted(EVIDENCE));s.add_argument('--pattern');s.add_argument('--limit',type=int,default=8)
    s=sub.add_parser('show');s.add_argument('ids',nargs='+')
    s=sub.add_parser('gallery');s.add_argument('--output',type=Path,required=True)
    s=sub.add_parser('shortlist');s.add_argument('ids',nargs='+');s.add_argument('--output',type=Path,required=True)
    s=sub.add_parser('review-due');s.add_argument('--days',type=int,default=90);s.add_argument('--today',default=date.today().isoformat())
    args=p.parse_args()
    try:
        data=validate(json.loads(args.catalog.read_text(encoding='utf-8')),args.asset_root);records=data['records']
        if args.command in ('stats','validate'):result=stats(records)
        elif args.command=='search':
            if not 1<=args.limit<=100:p.error('limit must be 1–100')
            result=query(records,args.query,args.platform,args.kind,args.evidence,args.pattern)[:args.limit]
        elif args.command=='review-due':
            if args.days<1:p.error('days must be positive')
            today=date.fromisoformat(args.today)
            result=[r for r in records if (today-date.fromisoformat(r['checked_on'])).days>=args.days]
        elif args.command=='gallery':
            if args.output.exists():p.error('Output exists; choose a new path to preserve prior exports')
            args.output.write_text(gallery(data,args.asset_root),encoding='utf-8');result={'output':str(args.output),'records':len(records),'browser_review':'not performed by this command'}
        else:
            lookup={r['id']:r for r in records}
            missing=set(args.ids)-lookup.keys()
            if missing:p.error('Unknown IDs: '+', '.join(sorted(missing)))
            result=[lookup[i] for i in dict.fromkeys(args.ids)]
            if args.command=='shortlist':
                if args.output.exists():p.error('Output exists; choose a new path')
                result={'palette_policy':'exclude source palette','selection':result,'next':'Inspect selected evidence, translate principles, then build complete concepts.'}
                args.output.write_text(json.dumps(result,indent=2),encoding='utf-8')
        print(json.dumps(result,indent=2,ensure_ascii=False));return 0
    except (ValueError,OSError,KeyError,TypeError) as e:
        p.exit(1,str(e)+'\n')

if __name__=='__main__':raise SystemExit(main())
