#!/usr/bin/env python3
import os, json, urllib.request, urllib.error
PAGE_ID='38763525-80ed-81ae-a090-fa5b980aca89'
NOTION_VERSION='2025-09-03'
meetings_text='No calendar events scheduled.'
pending_priorities="""1. [P2 - High] Obtain documentation and justification for auditor salary raise request — relay to management — Atlas - Label (Today, due 2026-06-06)
2. [P2 - High] Verify May 1–15 pay cycle carry-over for annotators whose tasks completed after cutoff date — Atlas - Label (Today, due 2026-06-06)
3. [P2 - High] Check contract terms with Princess/HR — onsite vs remote auditor distinctions — Atlas - HR (Today, due 2026-06-11)
4. [P2 - High] Coordinate with engineering on dispute workflow automation — Atlas - General (Today, due 2026-06-16)
5. [P2 - High] Call Vimlesh Deo (Sparkme Electric NZ) — requested callback — BBX (Today, contact: Vimlesh Deo)
6. [P2 - High] Monthly payment reminder — KINGSWOOD FLORIST & CREATIVE BALLOONS ($80/month) — BBX (Today, contact: KINGSWOOD FLORIST & CREATIVE BALLOONS)
7. [P2 - High] Follow up on unreconciled excess payments with Julie — Atlas - General (In Progress, due 2026-06-10, contact: Roel / Julie)"""
suggested_plan="""6:50–7:00 AM → Review this briefing.
7:00–8:00 AM → BBX only: Call Vimlesh Deo (Sparkme Electric NZ) — requested callback; aim for 2 call attempts.
8:00–9:00 AM → BBX + Atlas overlap: handle urgent/high-priority task: Obtain documentation and justification for auditor salary raise request — relay to management.
9:00–11:00 AM → Deep work block: Obtain documentation and justification for auditor salary raise request — relay to management.
11:00 AM–12:00 PM → BBX member check-ins/email drafts: Monthly payment reminder — KINGSWOOD FLORIST & CREATIVE BALLOONS ($80/month).
12:00–1:00 PM → Lunch + async Slack/Discord check for Atlas.
1:00–2:00 PM → Atlas team coordination: Obtain documentation and justification for auditor salary raise request — relay to management.
2:00–3:00 PM → BBX wrap-up: remaining calls/logs to hit 5 calls + 10 logs.
3:00–5:00 PM → Atlas focused work / EOD prep: Verify May 1–15 pay cycle carry-over for annotators whose tasks completed after cutoff date.
Evening (if energy allows) → Story Writing with Claude."""
granola_note='Granola API unavailable — no meeting notes were pulled directly. Meeting action items are included only if they already exist in Notion or synced notes.'
full_body=f"""## 📅 Today: Tuesday, June 23

## ☎️ Yesterday's Meeting Action Items
{granola_note}

## 📆 Today's Schedule
{meetings_text}

## 🎯 Priority Tasks
{pending_priorities}

## 🗓️ Suggested Plan for the Day
{suggested_plan}

## 📊 BBX KPI Tracker
- Calls today: 0 / 5 target
- Logs today: 0 / 10 target
- (Update these as you complete them using Claude)
"""

def req(method,path,body):
    token=os.environ['NOTION_API_KEY']
    r=urllib.request.Request('https://api.notion.com/v1/'+path, data=json.dumps(body).encode(), method=method, headers={'Authorization':'Bearer '+token,'Notion-Version':NOTION_VERSION,'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(r,timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise SystemExit(f'HTTP {e.code}: '+e.read().decode(errors='replace'))

def chunks(s,n=1900):
    return [{'type':'text','text':{'content':s[i:i+n]}} for i in range(0,len(s),n)] or [{'type':'text','text':{'content':''}}]

page=req('PATCH','pages/'+PAGE_ID, {'properties': {'Meetings Today': {'rich_text': chunks(meetings_text)}}})
md=req('PATCH',f'pages/{PAGE_ID}/markdown', {'markdown': full_body})
print(json.dumps({'status':'updated','page_id':PAGE_ID,'url':page.get('url'), 'meetings_text': meetings_text}, indent=2))
