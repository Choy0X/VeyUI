#!/usr/bin/env python3
"""Check declared review coverage and files. Does not inspect images or certify design quality."""
import argparse
import json
from pathlib import Path

def check(path):
    data=json.loads(path.read_text(encoding='utf-8'))
    issues=[]
    if not isinstance(data,dict): raise ValueError('Review record must be an object')
    for field in ('required_views','views','findings','required_interactions','interactions'):
        if field in data and not isinstance(data[field],list): raise ValueError(field+' must be a list')
    for field in ('views','findings','interactions'):
        if any(not isinstance(v,dict) for v in data.get(field,[])): raise ValueError(field+' must contain objects')
    for field in ('required_views','required_interactions'):
        if any(not isinstance(v,str) or not v.strip() for v in data.get(field,[])): raise ValueError(field+' must contain nonempty IDs')
    expected=data.get('required_views',[])
    versions=data.get('expected_versions',{})
    task_versions=data.get('expected_interaction_versions',{})
    if not isinstance(versions,dict) or not isinstance(task_versions,dict):
        raise ValueError('Expected version mappings must be objects')
    views=data.get('views',[])
    if not expected: issues.append('No required review views declared')
    if len(expected)!=len(set(expected)): issues.append('Duplicate required view IDs')
    ids=[v.get('id') for v in views]
    if len(ids)!=len(set(ids)): issues.append('Duplicate captured view IDs')
    for wanted in expected:
        matches=[v for v in views if v.get('id')==wanted]
        if not matches:
            issues.append(f'Missing review view: {wanted}'); continue
        view=matches[0]
        if not versions.get(wanted) or view.get('artifact_version')!=versions[wanted]:
            issues.append(f'{wanted}: capture version does not match declared current version')
        for key in ('artifact_version','runtime','viewport','state','reviewer','observation'):
            if not isinstance(view.get(key),str) or not view[key].strip(): issues.append(f'{wanted}: missing {key}')
        capture=view.get('capture')
        target=(path.parent/capture).resolve() if isinstance(capture,str) and capture else None
        if target is None or not target.is_file() or target.stat().st_size==0:
            issues.append(f'{wanted}: capture file missing or empty')
        if view.get('visually_inspected') is not True:
            issues.append(f'{wanted}: visual inspection not declared')
    for item in data.get('findings',[]):
        if item.get('severity') in ('blocking','major') and item.get('status')!='resolved':
            issues.append('Unresolved material finding: '+str(item.get('description','unnamed')))
        if item.get('status')=='resolved' and not item.get('recheck_view') in ids:
            issues.append('Resolved finding has no captured recheck view')
        elif item.get('status')=='resolved':
            recheck=next(v for v in views if v.get('id')==item['recheck_view'])
            if item['recheck_view'] not in expected:
                issues.append('Resolved finding recheck must be included in required review views')
            if not item.get('fixed_in_version') or recheck.get('artifact_version')!=item['fixed_in_version']:
                issues.append('Resolved finding needs a recheck from its fixed version')
    for task in data.get('required_interactions',[]):
        records=[t for t in data.get('interactions',[]) if t.get('id')==task]
        if not records or not any(t.get('result')=='passed' and t.get('evidence') and
                task_versions.get(task) and t.get('artifact_version')==task_versions[task] for t in records):
            issues.append('Missing passing interaction evidence: '+str(task))
    return {'coverage_complete_as_declared':not issues,'issues':issues,'notice':'File presence and reviewer declarations only. This tool does not view pixels, verify claims, perform interaction tests, or certify visual quality.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('review_file',type=Path); a=p.parse_args()
    try: result=check(a.review_file)
    except (OSError,ValueError,TypeError,KeyError) as e:
        print(json.dumps({'coverage_complete_as_declared':False,'error':str(e)}));return 2
    print(json.dumps(result,indent=2));return 0 if result['coverage_complete_as_declared'] else 1
if __name__=='__main__':raise SystemExit(main())
