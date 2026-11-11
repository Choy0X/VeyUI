#!/usr/bin/env python3
"""Retrieve pre-extracted screen knowledge offline, without loading source images."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/ready-screens.json'
PROVENANCE=ROOT/'data/screen-provenance.json'
RECIPES=ROOT/'data/screen-recipes.json'
CONCEPTS=ROOT/'data/reference-library.json'
ALIASES={'signin': 'authentication', 'login': 'authentication', 'signup': 'onboarding', 'billing': 'payment', 'checkout': 'payment', 'preferences': 'settings', 'inbox': 'messages', 'dashboard': 'overview', 'todos': 'tasks', 'todo': 'tasks', 'kanban': 'board', 'profile': 'account', 'filtering': 'filter', 'searching': 'search', 'editor': 'editing', 'notifications': 'notification', 'permission': 'permissions', 'errors': 'error', 'validation': 'error', 'validate': 'error', 'paywall': 'pricing', 'tiers': 'pricing', 'plans': 'pricing', 'onboard': 'onboarding', 'edit': 'editing', 'filters': 'filter', 'failed':'error', 'failure':'error', 'invalid':'error'}
STOPWORDS={'a','an','the','for','of','and','or','with','to','in','ui','screen','design','app','please','me','create','build','implement','new'}
# High-risk purpose words must be evidenced by the record's explicit tags/pattern.
PURPOSES={'authentication','onboarding','pricing','error','permissions'}

def words(value):
    return {ALIASES.get(t,t) for t in re.findall(r'[a-z0-9]+',value.lower().replace('sign in','signin').replace('sign up','signup').replace('log in','login')) if t not in STOPWORDS}

def load():
    data=json.loads(DATA.read_text(encoding='utf-8'))
    recipes=json.loads(RECIPES.read_text(encoding='utf-8'))
    if data.get('schema_version')!=1:raise ValueError('Unsupported ready-screen schema')
    return data['screens'],recipes['recipes']

def validate(screens,recipes,provenance):
    ids=set();sources=set();state_keys=set()
    for s in screens:
        for field in ('id','product','platform','name','pattern','tags','layout','evidence_ref'):
            if not s.get(field):raise ValueError('Missing '+field+' in '+s.get('id','record'))
        if s['id'] in ids:raise ValueError('Duplicate screen ID')
        ids.add(s['id'])
        if s['platform'] not in {'web','mobile','desktop'}:raise ValueError('Unknown platform')
        if s['pattern'] not in recipes:raise ValueError('Unknown recipe '+s['pattern'])
        if s['evidence_ref'] not in provenance:raise ValueError('Missing provenance')
        p=provenance[s['evidence_ref']]
        if p.get('classification') not in {'publisher_ui_screen','official_documentation_screen'}:raise ValueError('Not a shipped-product UI screen')
        if p.get('review')!='layout_inspected':raise ValueError('Unreviewed screen')
        if not re.fullmatch(r'[a-f0-9]{64}',p.get('image_sha256','')) or not p.get('source_url','').startswith('https://'):raise ValueError('Missing source evidence')
        if not isinstance(s['tags'],list) or not all(isinstance(t,str) for t in s['tags']):raise ValueError('Invalid tags')
        key=(s['product'],s['name'])
        if key in state_keys:raise ValueError('Duplicate product state: '+str(key))
        state_keys.add(key)
        if p['image_sha256'] in sources:raise ValueError('Duplicate image evidence counted as another screen')
        sources.add(p['image_sha256'])
        if re.search(r'https?://|#[0-9a-fA-F]{6}\b',' '.join([s['layout'],s.get('lesson','')])):raise ValueError('Link or source palette in design payload')
    return {'ready_screens':len(screens),'products':len({s['product'] for s in screens}),'platforms':dict(Counter(s['platform'] for s in screens)),
            'source_types':dict(Counter(provenance[s['evidence_ref']]['classification'] for s in screens)),
            'reference_image_reads_required':0,'reference_network_requests_required':0,
            'scope':'Pre-extracted layout knowledge from screenshots of released products; not live-tested flows or exact pixel specifications.'}

def search(screens,query,platform=None,limit=3):
    terms=words(query);ranked=[]
    if not terms:return []
    purposes=terms & PURPOSES
    for s in screens:
        if platform and s['platform']!=platform:continue
        tags=words(' '.join(s['tags'])+' '+s['pattern'])
        if purposes and not purposes <= tags:continue
        if {'error','payment'}<=terms and 'payment' not in tags:continue
        fields=[words(' '.join(s['tags'])+' '+s['name']),words(s['layout']),words(s['product']),words(s['pattern'])]
        matches=set().union(*fields)&terms
        if not matches:continue
        score=30*len(matches)+12*len(terms&fields[0])+5*len(terms&fields[3])+2*len(terms&fields[1])+len(terms&fields[2])
        ranked.append((score,s))
    # Diversity breaks equal-relevance ties; it never promotes a weaker match.
    chosen=[];products=set()
    while ranked and len(chosen)<limit:
        ranked.sort(key=lambda x:(-x[0],x[1]['product'] in products,x[1]['id']))
        _,s=ranked.pop(0);chosen.append(s);products.add(s['product'])
    return chosen

def packet(screens,recipes,budget=5000):
    if budget<500:raise ValueError('Budget must be at least 500 characters')
    result={'library':'pre-extracted-screens-v1','mode':'offline_pre_extracted','palette':'Use the target brand; source palette is excluded.','screens':[],'implementation_rules':{},
            'boundary':'Layout is observed. Adaptation rules are original recommendations; behavior must be implemented and tested in your project.'}
    omitted=[]
    for s in screens:
        item={k:s[k] for k in ('id','product','platform','operating_system','name','pattern','capture_kind','layout','lesson') if k in s}
        rule_key=s['pattern'];previous=dict(result['implementation_rules'])
        result['screens'].append(item);result['implementation_rules'][rule_key]=recipes[rule_key]
        if len(json.dumps(result,ensure_ascii=False))+200>budget:
            result['screens'].pop();result['implementation_rules']=previous;omitted.append(s['id'])
    result['omitted_for_budget']=omitted
    if not result['screens'] and screens:raise ValueError('Budget too small for a complete screen; increase --budget-chars')
    return result

def load_support():
    flows=json.loads((ROOT/'data/documented-flows.json').read_text(encoding='utf-8'))['flows']
    guides=json.loads((ROOT/'data/decision-guides.json').read_text(encoding='utf-8'))['guides']
    return flows,guides

def validate_support(screens):
    flows,guides=load_support();provenance=json.loads((ROOT/'data/flow-provenance.json').read_text(encoding='utf-8'))['records']
    screen_ids={s['id'] for s in screens};ids=set()
    for row in flows+guides:
        if row['id'] in ids:raise ValueError('Duplicate supporting knowledge ID')
        ids.add(row['id'])
        if not row.get('tags') or not all(isinstance(t,str) for t in row['tags']):raise ValueError('Invalid supporting tags')
        if re.search(r'https?://|#[0-9a-fA-F]{6}\b',json.dumps(row)):raise ValueError('Source URL or palette in default support payload')
    for f in flows:
        if f['platform'] not in {'web','desktop','mobile'}:raise ValueError('Invalid flow platform')
        if len(f['steps'])<2 or any(not step.get('action') or not step.get('result') or step.get('evidence')!='documented' for step in f['steps']):raise ValueError('Invalid documented flow')
        if not set(f['related_screens'])<=screen_ids:raise ValueError('Unknown related screen')
        p=provenance.get(f['evidence_ref'],{})
        if p.get('review')!='official_text_inspected' or not p.get('source_url','').startswith('https://'):raise ValueError('Missing documented flow evidence')
        if p.get('runtime_tested') is not False:raise ValueError('Unsupported runtime-tested flow claim')
    for g in guides:
        if any(not g.get(k) for k in ('title','decision','tradeoff','avoid','verify','evidence')):raise ValueError('Incomplete decision guide')
    return {'documented_flows':len(flows),'decision_guides':len(guides),'independently_operated_flows':0}

def support_search(rows,query,platform=None,limit=2):
    terms=words(query)
    if not terms:return []
    ranked=[]
    for row in rows:
        if platform and row.get('platform') and row['platform']!=platform:continue
        labels=words(' '.join(row['tags'])+' '+row.get('name',row.get('title',''))+' '+row['id'])
        score=len(terms&labels)
        if score:ranked.append((score,row))
    return [r for _,r in sorted(ranked,key=lambda x:(-x[0],x[1]['id']))[:limit]]

def concept_search(query, platform=None, limit=2):
    """Return only compact, inspected art direction notes."""
    terms = words(query)
    if not terms:
        return []
    records = json.loads(CONCEPTS.read_text(encoding='utf-8'))['records']
    purposes = terms & PURPOSES
    ranked = []
    for record in records:
        if record['kind'] != 'concept' or record['evidence'] != 'image_inspected':
            continue
        if platform and platform not in record['platforms']:
            continue
        pattern_hits = terms & words(' '.join(record['patterns']))
        title_hits = terms & words(record['title'])
        if purposes and not (pattern_hits | title_hits) & purposes:
            continue
        if pattern_hits or title_hits:
            ranked.append((3 * len(pattern_hits) + len(title_hits), record))

    selected = []
    families = set()
    for _, record in sorted(ranked, key=lambda pair: (-pair[0], pair[1]['id'])):
        family = record.get('concept_family', record['id'])
        if family in families:
            continue
        families.add(family)
        selected.append({
            key: record[key] for key in
            ('id', 'title', 'platforms', 'observations', 'adaptation', 'transfer_check')
            if key in record
        })
        if len(selected) == limit:
            break
    return selected


def bounded(out,budget):
    # Drop complete lowest-priority records, never truncate an observation mid-sentence.
    for field in ('decision_guides','documented_flows','concept_references','screens'):
        while len(json.dumps(out,ensure_ascii=False,separators=(',',':')))>budget and out.get(field):
            removed=out[field].pop();out.setdefault('omitted_for_budget',[]).append(removed['id'])
            if field=='screens':
                remaining={x['pattern'] for x in out['screens']}
                out['implementation_rules']={k:v for k,v in out['implementation_rules'].items() if k in remaining}
    if len(json.dumps(out,ensure_ascii=False,separators=(',',':')))>budget:
        raise ValueError('Budget too small for complete output')
    return out

def brief(screens,recipes,query,platform=None,budget=7500):
    flows,guides=load_support();found=search(screens,query,platform,3)
    purposes=words(query)&PURPOSES
    if not found and len(purposes)>1:
        # Mixed-state tasks need separate precedents; never imply one image proves every state.
        for purpose in sorted(purposes):
            narrowed=' '.join((words(query)-purposes)|{purpose})
            for row in search(screens,narrowed,platform,1):
                if row['id'] not in {x['id'] for x in found}:found.append(row)
    out=packet(found,recipes,max(budget,5000))
    out['documented_flows']=support_search(flows,query,platform,1)
    out['decision_guides']=support_search(guides,query,None,2)
    out['concept_references'] = concept_search(query, platform)
    covered=set().union(*(words(' '.join(x['tags'])+' '+x['pattern']) for x in found))
    out['screen_purpose_gaps']=sorted(purposes-covered)
    out['evidence_types']={'screens':'Observed static layout','documented_flows':'Publisher-described behavior, not independently operated','decision_guides':'Original target-design recommendations','concept_references':'Inspected static visual studies; shipped status and behavior unverified'}
    if not found:out['coverage_gap']='No matching reviewed screen; use labeled guidance and record the gap. No automatic source browsing.'
    out=bounded(out,budget)
    remaining_ids={x['id'] for x in out['screens']}
    remaining_tags=set().union(*(words(' '.join(x['tags'])+' '+x['pattern']) for x in found if x['id'] in remaining_ids))
    out['screen_purpose_gaps']=sorted(purposes-remaining_tags)
    return bounded(out,budget)

def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    for name in ('stats','validate'):sub.add_parser(name)
    for name in ('brief','flows','decisions','concepts'):
        a=sub.add_parser(name);a.add_argument('query');a.add_argument('--platform',choices=['web','mobile','desktop']);a.add_argument('--budget-chars',type=int,default=7500 if name=='brief' else 5000)
    a=sub.add_parser('guidance');a.add_argument('patterns',nargs='*',help='Recipe names; omit to list available names. These are original guidance, not shipped screens.')
    a=sub.add_parser('search');a.add_argument('query');a.add_argument('--platform',choices=['web','mobile','desktop']);a.add_argument('--limit',type=int,default=3);a.add_argument('--budget-chars',type=int,default=5000)
    a=sub.add_parser('get');a.add_argument('ids',nargs='+');a.add_argument('--budget-chars',type=int,default=8000)
    a=sub.add_parser('provenance');a.add_argument('ids',nargs='+')
    args=p.parse_args()
    try:
        screens,recipes=load()
        if args.command in {'stats','validate'}:
            out=validate(screens,recipes,json.loads(PROVENANCE.read_text(encoding='utf-8'))['records']);out.update(validate_support(screens))
            out['capture_kinds']=dict(Counter(s.get('capture_kind','not_separately_classified') for s in screens))
        elif args.command=='brief':out=brief(screens,recipes,args.query,args.platform,args.budget_chars)
        elif args.command == 'concepts':
            out = bounded({
                'concept_references': concept_search(args.query, args.platform, limit=4),
                'boundary': 'Inspected static art direction. Adaptation and checks are target proposals. Shipped status, behavior and motion are unverified.',
            }, args.budget_chars)
        elif args.command in {'flows','decisions'}:
            flows,guides=load_support();key='documented_flows' if args.command=='flows' else 'decision_guides'
            out=bounded({key:support_search(flows if args.command=='flows' else guides,args.query,args.platform,2),'boundary':'Flows are documented, not runtime-tested. Decision guides are original recommendations.'},args.budget_chars)
        elif args.command=='guidance':
            if len(set(args.patterns))>3:p.error('Read at most three recipes at once')
            missing=set(args.patterns)-recipes.keys()
            if missing:p.error('Unknown recipes: '+', '.join(sorted(missing)))
            out={'evidence':'Original implementation guidance, not observed shipped screens or verified flows','recipes':{k:recipes[k] for k in args.patterns}} if args.patterns else {'available_original_recipes':sorted(recipes)}
        elif args.command=='search':
            if not 1<=args.limit<=8:p.error('limit must be 1–8; retrieve a small working set')
            found=search(screens,args.query,args.platform,args.limit);out=packet(found,recipes,args.budget_chars)
            out['query_coverage']={'query':args.query,'unmatched_terms':sorted(words(args.query)-set().union(*(words(' '.join(s['tags'])+' '+s['name']+' '+s['layout']+' '+s['product']+' '+s['pattern']) for s in found)))}
            if len(json.dumps(out,ensure_ascii=False,separators=(',',':')))>args.budget_chars:out.pop('query_coverage')
            if not found:out['coverage_gap']='No matching compiled screen. Broaden the task terms or use original design principles; do not automatically browse.'
        else:
            if len(set(args.ids))>8:p.error('Retrieve at most eight records at a time')
            lookup={s['id']:s for s in screens};missing=set(args.ids)-lookup.keys()
            if missing:p.error('Unknown IDs: '+', '.join(sorted(missing)))
            selected=[lookup[i] for i in dict.fromkeys(args.ids)]
            if args.command=='get':out=packet(selected,recipes,args.budget_chars)
            else:
                prov=json.loads(PROVENANCE.read_text(encoding='utf-8'))['records'];out={s['id']:prov[s['evidence_ref']] for s in selected}
        serialized=json.dumps(out,ensure_ascii=False,separators=(',',':'))
        if hasattr(args,'budget_chars') and len(serialized)>args.budget_chars:p.exit(1,'Budget too small for complete output; increase --budget-chars\n')
        print(serialized)
    except (ValueError,OSError,KeyError,TypeError) as e:p.exit(1,str(e)+'\n')
if __name__=='__main__':main()
