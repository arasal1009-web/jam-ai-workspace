#!/usr/bin/env python3
import json, os, subprocess, urllib.request, urllib.error
from datetime import datetime
from zoneinfo import ZoneInfo

NOTION_VERSION='2025-09-03'
TASK_DS='daba8780-ec4c-4774-a839-6ca092a81e8c'
BRIEF_DS='f42e2c34-41a8-4253-abc3-be4110d97287'
BRIEF_PARENT_DB='9b323d41-36a6-4a69-8ac4-5ade3a5a9cb5'
GAPI=os.path.expanduser('${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/google_api.py')
# expand manually
GAPI=os.path.expandvars(GAPI).replace('${HERMES_HOME:-$HOME/.hermes}', os.path.expanduser(os.environ.get('HERMES_HOME','~/.hermes')))

# Load env
for p in [os.path.expanduser('~/.hermes/.env'), os.path.expanduser('~/.env')]:
    if os.path.exists(p):
        for line in open(p):
            line=line.strip()
            if not line or line.startswith('#') or '=' not in line: continue
            k,v=line.split('=',1)
            os.environ.setdefault(k, v.strip().strip('"').strip("'"))

api_key=os.environ.get('NOTION_API_KEY')
if not api_key:
    raise SystemExit('NOTION_API_KEY missing')

def notion(method, path, payload=None):
    data=None
    headers={'Authorization':f'Bearer {api_key}','Notion-Version':NOTION_VERSION,'Content-Type':'application/json'}
    if payload is not None:
        data=json.dumps(payload).encode()
    req=urllib.request.Request('https://api.notion.com/v1/'+path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body=r.read().decode()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        body=e.read().decode(errors='replace')
        raise RuntimeError(f'Notion {method} {path} failed: HTTP {e.code}: {body}')

def plain(prop):
    if not prop: return ''
    typ=prop.get('type')
    if typ in ('title','rich_text'):
        return ''.join(x.get('plain_text','') for x in prop.get(typ,[]))
    if typ=='select':
        return (prop.get('select') or {}).get('name','')
    if typ=='date':
        return (prop.get('date') or {}).get('start','')
    return ''

def rt(text):
    # Notion rich_text content chunks max 2000 chars
    if text is None: text=''
    return [{'type':'text','text':{'content':text[i:i+1900]}} for i in range(0, max(len(text),1), 1900)]

def title(text):
    return [{'type':'text','text':{'content':text[:1900]}}]

z=ZoneInfo('Asia/Manila')
now=datetime.now(z)
date_iso=now.date().isoformat()
date_title=now.strftime('%A, %B ') + str(now.day)
day_type='Weekday - BBX + Atlas' if now.weekday()<5 else ('Saturday - YT Shorts + Atlas Monitor' if now.weekday()==5 else 'Sunday - Rest / Emergency Only')
start=now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
end=now.replace(hour=0, minute=0, second=0, microsecond=0).replace(day=now.day).astimezone(z)
# safer add one day
from datetime import timedelta
end=(now.replace(hour=0, minute=0, second=0, microsecond=0)+timedelta(days=1)).isoformat()

# Calendar
cal_cmd=['python', GAPI, 'calendar', 'list', '--start', start, '--end', end]
cal_proc=subprocess.run(cal_cmd, capture_output=True, text=True, timeout=180)
if cal_proc.returncode!=0:
    calendar_error=cal_proc.stderr.strip() or cal_proc.stdout.strip()
    events=[]
else:
    calendar_error=''
    events=json.loads(cal_proc.stdout or '[]')

def fmt_event(ev):
    s=ev.get('start') or ''
    t='All day'
    if isinstance(s, dict): s=s.get('dateTime') or s.get('date') or ''
    if s:
        try:
            ds=s.replace('Z','+00:00')
            dt=datetime.fromisoformat(ds).astimezone(z)
            t=dt.strftime('%I:%M %p').lstrip('0')
        except Exception:
            t=s
    bits=[f"{t} — {ev.get('summary') or '(No title)'}"]
    loc=ev.get('location')
    if loc: bits.append(f"Location: {loc}")
    return ' | '.join(bits)

meetings_today='\n'.join(fmt_event(e) for e in events) if events else 'No calendar events scheduled.'
if calendar_error:
    meetings_today=f'Calendar pull failed: {calendar_error}'

# Tasks all pending
payload={"filter":{"and":[{"property":"Status","select":{"does_not_equal":"Done"}},{"property":"Status","select":{"does_not_equal":"Cancelled"}}]},"page_size":100}
tasks=[]
while True:
    res=notion('POST', f'data_sources/{TASK_DS}/query', payload)
    for row in res.get('results',[]):
        p=row.get('properties',{})
        tasks.append({
            'id': row.get('id'),
            'task': plain(p.get('Task')),
            'priority': plain(p.get('Priority')) or 'Unprioritized',
            'project': plain(p.get('Project')) or 'Other',
            'status': plain(p.get('Status')) or 'No status',
            'due': plain(p.get('Due Date')),
            'source': plain(p.get('Source')),
        })
    if not res.get('has_more'): break
    payload['start_cursor']=res.get('next_cursor')

def pri_rank(t):
    pri=t['priority']
    if pri.startswith('P1'): a=0
    elif pri.startswith('P2'): a=1
    elif t['project']=='BBX': a=2
    elif t['project'].startswith('Atlas'): a=3
    else: a=4
    overdue = 0 if t.get('due') and t['due'] <= date_iso else 1
    return (a, overdue, t.get('due') or '9999-99-99', t['task'])

tasks_sorted=sorted(tasks, key=pri_rank)
top=tasks_sorted[:7]
pending_priorities='\n'.join(f"{i+1}. [{t['priority']}] {t['task']} — {t['project']} ({t['status']}{', due '+t['due'] if t.get('due') else ''})" for i,t in enumerate(top)) or 'No pending tasks found.'

# Meeting action items note from available Notion tasks only: include any pending Granola/Meeting tasks in top-ish list
meeting_tasks=[t for t in tasks_sorted if t.get('source')=='Granola/Meeting'][:5]
granola_section='Granola API unavailable — no meeting notes were pulled directly. Meeting action items are included only if they already exist in Notion or synced notes.'
if meeting_tasks:
    granola_section += '\n\nExisting pending meeting-sourced tasks in Notion:\n' + '\n'.join(f"- [{t['priority']}] {t['task']} — {t['project']} ({t['status']})" for t in meeting_tasks)

# Suggested plan
p1p2=[t for t in tasks_sorted if t['priority'].startswith(('P1','P2'))]
bbx=[t for t in tasks_sorted if t['project']=='BBX']
atlas=[t for t in tasks_sorted if t['project'].startswith('Atlas')]
def task_text(lst, fallback):
    return lst[0]['task'] if lst else fallback
if day_type.startswith('Weekday'):
    suggested_plan='\n'.join([
        f"6:50–7:00 AM → Review this briefing; confirm zero scheduled calendar events." if not events else "6:50–7:00 AM → Review this briefing and today’s calendar.",
        f"7:00–8:00 AM → BBX only: {task_text(bbx, 'start call/log pipeline')} (aim for 2 call attempts).",
        f"8:00–9:00 AM → BBX + Atlas overlap: prioritize {task_text(p1p2, 'highest urgency open task')}.",
        f"9:00–11:00 AM → Deep work: {task_text(p1p2[1:] if len(p1p2)>1 else p1p2, 'top P1/P2 task')}.",
        "11:00 AM–12:00 PM → BBX member check-ins or email drafts; keep CRM/activity logs current.",
        "12:00–1:00 PM → Lunch + async check for Atlas Slack/Discord.",
        f"1:00–2:00 PM → Atlas team coordination: {task_text(atlas, 'QA/Label/CVA check-ins')}.",
        "2:00–3:00 PM → BBX wrap-up: complete remaining calls/logs toward 5 calls + 10 logs.",
        f"3:00–5:00 PM → Atlas focused work / EOD prep: {task_text(atlas[1:] if len(atlas)>1 else atlas, 'EOD reports and blockers')}.",
        "Evening (if energy allows) → Story Writing with Claude."
    ])
elif day_type.startswith('Saturday'):
    suggested_plan='\n'.join(['Morning → Atlas team monitoring.', 'Mid-morning → YouTube Shorts management (5–8 hr block).', 'If Atlas emergency → address as needed.'])
else:
    suggested_plan='Rest day / emergency only. Do a light check only if needed.'

body=f"""## 📅 Today: {date_title}

## ☎️ Yesterday's Meeting Action Items
{granola_section}

## 📆 Today's Schedule
{meetings_today}

## 🎯 Priority Tasks
{pending_priorities}

## 🗓️ Suggested Plan for the Day
{suggested_plan}

## 📊 BBX KPI Tracker
- Calls today: 0 / 5 target
- Logs today: 0 / 10 target
- (Update these as you complete them using Claude)
"""

properties={
    'Date': {'title': title(date_title)},
    'Day Type': {'select': {'name': day_type}},
    'Status': {'select': {'name': 'Planned'}},
    'Meetings Today': {'rich_text': rt(meetings_today)},
    'Pending Priorities': {'rich_text': rt(pending_priorities)},
    'Suggested Plan': {'rich_text': rt(suggested_plan)},
    'BBX Calls Today': {'number': 0},
    'BBX Logs Today': {'number': 0},
}
create_payload={'parent': {'database_id': BRIEF_PARENT_DB}, 'properties': properties, 'markdown': body}
result={'date_title': date_title, 'day_type': day_type, 'calendar_events': len(events), 'pending_tasks': len(tasks), 'pending_priorities': pending_priorities, 'suggested_plan': suggested_plan, 'meetings_today': meetings_today, 'body': body}
try:
    created=notion('POST', 'pages', create_payload)
    result.update({'write_succeeded': True, 'page_id': created.get('id'), 'url': created.get('url')})
except Exception as e:
    result.update({'write_succeeded': False, 'error': str(e)})

print(json.dumps(result, indent=2, ensure_ascii=False))
