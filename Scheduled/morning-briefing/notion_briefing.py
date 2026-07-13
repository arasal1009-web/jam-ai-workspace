#!/usr/bin/env python3
import json, os, sys, urllib.request, urllib.error
from datetime import date

TOKEN = os.environ.get('NOTION_API_KEY')
if not TOKEN:
    env_path = os.path.expanduser(os.environ.get('HERMES_HOME', '~/.hermes') + '/.env')
    try:
        with open(env_path) as f:
            for line in f:
                line=line.strip()
                if line.startswith('NOTION_API_KEY='):
                    TOKEN=line.split('=',1)[1].strip().strip('"').strip("'")
                    break
    except FileNotFoundError:
        pass
if not TOKEN:
    print(json.dumps({'error':'NOTION_API_KEY missing'})); sys.exit(2)
BASE='https://api.notion.com/v1'
HEADERS={'Authorization':f'Bearer {TOKEN}','Notion-Version':'2025-09-03','Content-Type':'application/json'}

def req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r=urllib.request.Request(BASE+path, data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            raw=resp.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw=e.read().decode(errors='replace')
        try: parsed=json.loads(raw)
        except Exception: parsed=raw
        raise RuntimeError(json.dumps({'status':e.code,'reason':e.reason,'body':parsed}, ensure_ascii=False))

def text_from_rich(arr):
    return ''.join((x.get('plain_text') or x.get('text',{}).get('content','')) for x in (arr or []))

def prop_value(p):
    if not p: return None
    typ=p.get('type')
    v=p.get(typ) if typ else None
    if typ=='title': return text_from_rich(v)
    if typ=='rich_text': return text_from_rich(v)
    if typ=='select': return (v or {}).get('name')
    if typ=='multi_select': return [x.get('name') for x in (v or [])]
    if typ=='date': return (v or {}).get('start')
    if typ=='checkbox': return v
    if typ=='number': return v
    if typ=='url': return v
    if typ=='email': return v
    if typ=='status': return (v or {}).get('name')
    if typ=='formula': return v
    if typ=='rollup': return v
    if typ=='relation': return [x.get('id') for x in (v or [])]
    if typ=='people': return [x.get('name') for x in (v or [])]
    return v

def simplify_page(pg):
    props=pg.get('properties',{})
    return {'id':pg.get('id'), 'url':pg.get('url'), 'properties':{k:prop_value(v) for k,v in props.items()}}

def main():
    cmd=sys.argv[1] if len(sys.argv)>1 else 'query'
    master='daba8780-ec4c-4774-a839-6ca092a81e8c'
    log='f42e2c34-41a8-4253-abc3-be4110d97287'
    if cmd=='schemas':
        print(json.dumps({'master':req('GET',f'/data_sources/{master}'), 'log':req('GET',f'/data_sources/{log}')}, ensure_ascii=False, indent=2))
    elif cmd=='tasks':
        body={'filter': {'and':[{'property':'Status','select':{'does_not_equal':'Done'}},{'property':'Status','select':{'does_not_equal':'Cancelled'}}]}, 'page_size':100}
        res=req('POST',f'/data_sources/{master}/query',body)
        print(json.dumps({'count':len(res.get('results',[])), 'has_more':res.get('has_more'), 'results':[simplify_page(x) for x in res.get('results',[])]}, ensure_ascii=False, indent=2))
    else:
        print('unknown', file=sys.stderr); sys.exit(1)
if __name__=='__main__': main()
