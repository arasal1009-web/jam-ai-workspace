#!/usr/bin/env python3
import json, os, sys, urllib.request, urllib.error

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
    print(json.dumps({'ok': False, 'error':'NOTION_API_KEY missing'})); sys.exit(2)

BASE='https://api.notion.com/v1'
HEADERS={'Authorization':f'Bearer {TOKEN}','Notion-Version':'2025-09-03','Content-Type':'application/json'}

def rich_text(s):
    # Notion text content objects max at 2000 chars; preserve all content by chunking.
    return [{'type':'text','text':{'content':s[i:i+1900]}} for i in range(0, len(s), 1900)] or [{'type':'text','text':{'content':''}}]

def req(method, path, body=None):
    data=json.dumps(body).encode('utf-8') if body is not None else None
    request=urllib.request.Request(BASE+path, data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(request, timeout=60) as resp:
            raw=resp.read().decode('utf-8')
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw=e.read().decode(errors='replace')
        try: parsed=json.loads(raw)
        except Exception: parsed=raw
        print(json.dumps({'ok': False, 'status': e.code, 'reason': e.reason, 'body': parsed}, ensure_ascii=False, indent=2))
        sys.exit(1)

DATE_TITLE='Thursday, June 25'
DAY_TYPE='Weekday - BBX + Atlas'
MEETINGS='No calendar events scheduled for today.'
PENDING_PRIORITIES='''1. [P2 - High / BBX] Follow up after left message — SIMCORP NZ LIMITED
2. [P2 - High / BBX] Send follow-up email — SUNSHINE RESTAURANT/FOUR SEASONS
3. [P2 - High / BBX] CRM queue — record closed account — AIRCON NZ TRUST ACCOUNT
4. [P2 - High / Atlas - General] Coordinate with engineering on dispute workflow automation
5. [P2 - High / Atlas - QA] Validate new QC tickets and double-check entries by EOD
6. [P2 - High / Atlas - General] Draft rate-structure & workload-adjustment proposal
7. [P2 - High / BBX] Monthly payment reminder — KINGSWOOD FLORIST & CREATIVE BALLOONS'''
SUGGESTED_PLAN='''6:50–7:00 AM → Review this briefing.
7:00–8:00 AM → BBX only: start KPI push; prioritize SIMCORP follow-up and Sunshine Restaurant/Four Seasons follow-up email; aim for 2 call attempts/logs.
8:00–9:00 AM → BBX + Atlas overlap: clear AIRCON NZ CRM queue item and check for any urgent Atlas issues.
9:00–11:00 AM → Deep work: Atlas P2 block — dispute workflow automation coordination, QC ticket validation, and rate/workload proposal progress.
11:00 AM–12:00 PM → BBX member check-ins: KINGSWOOD payment reminder and remaining NZ trade-preference calls.
12:00–1:00 PM → Lunch + async Slack/Discord check for Atlas.
1:00–2:00 PM → Atlas team coordination: HR/Label follow-ups and EOD report expectations.
2:00–3:00 PM → BBX wrap-up: remaining calls/logs to hit 5 calls and 10 activity logs.
3:00–5:00 PM → Atlas focused work / EOD prep: verify QA, Label, CVA EOD reports and capture blockers.
Evening (if energy allows) → Story Writing with Claude.'''
GRANOLA_NOTE='Granola API unavailable — no meeting notes were pulled directly. Meeting action items are included only if they already exist in Notion or synced notes.'
BODY=f'''## 📅 Today: Thursday, June 25

## ☎️ Yesterday's Meeting Action Items
{GRANOLA_NOTE}

## 📆 Today's Schedule
{MEETINGS}

## 🎯 Priority Tasks
{PENDING_PRIORITIES}

## 🗓️ Suggested Plan for the Day
{SUGGESTED_PLAN}

## 📊 BBX KPI Tracker
- Calls today: 0 / 5 target
- Logs today: 0 / 10 target
- (Update these as you complete them using Claude)
'''

payload={
  'parent': {'database_id':'9b323d41-36a6-4a69-8ac4-5ade3a5a9cb5'},
  'properties': {
    'Date': {'title': rich_text(DATE_TITLE)},
    'Day Type': {'select': {'name': DAY_TYPE}},
    'Status': {'select': {'name': 'Planned'}},
    'Meetings Today': {'rich_text': rich_text(MEETINGS)},
    'Pending Priorities': {'rich_text': rich_text(PENDING_PRIORITIES)},
    'Suggested Plan': {'rich_text': rich_text(SUGGESTED_PLAN)},
    'BBX Calls Today': {'number': 0},
    'BBX Logs Today': {'number': 0}
  },
  'markdown': BODY
}
res=req('POST','/pages',payload)
print(json.dumps({'ok': True, 'id': res.get('id'), 'url': res.get('url'), 'created_time': res.get('created_time'), 'title': DATE_TITLE}, ensure_ascii=False, indent=2))
