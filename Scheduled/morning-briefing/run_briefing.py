#!/usr/bin/env python3
import os, json, subprocess, urllib.request, urllib.error, textwrap
from datetime import datetime, date
from zoneinfo import ZoneInfo

NOTION_VERSION = "2025-09-03"
MASTER_DS = "daba8780-ec4c-4774-a839-6ca092a81e8c"
BRIEFING_DB = "9b323d41-36a6-4a69-8ac4-5ade3a5a9cb5"  # parent.database_id for Daily Briefing Log data source

PHT = ZoneInfo("Asia/Manila")
today_dt = datetime.now(PHT)
today = today_dt.date()
day_name = today_dt.strftime("%A")
month_name = today_dt.strftime("%B")
date_title = f"{day_name}, {month_name} {today.day}"
if day_name == "Saturday":
    day_type = "Saturday - YT Shorts + Atlas Monitor"
elif day_name == "Sunday":
    day_type = "Sunday - Rest / Emergency Only"
else:
    day_type = "Weekday - BBX + Atlas"


def notion_request(method, path, body=None):
    token = os.environ.get("NOTION_API_KEY")
    if not token:
        raise RuntimeError("NOTION_API_KEY is not set")
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        f"https://api.notion.com/v1/{path}", data=data, method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Notion {method} {path} failed: HTTP {e.code}: {detail}")


def rich_text_plain(prop):
    arr = prop.get(prop.get("type", ""), []) if isinstance(prop, dict) else []
    if isinstance(arr, list):
        return "".join(x.get("plain_text", "") for x in arr)
    return ""

def title_plain(prop):
    return "".join(x.get("plain_text", "") for x in prop.get("title", []))

def select_name(prop):
    s = prop.get("select") if isinstance(prop, dict) else None
    return (s or {}).get("name") or ""

def date_start(prop):
    d = prop.get("date") if isinstance(prop, dict) else None
    return (d or {}).get("start") or ""


def get_calendar_events():
    hermes_home = os.environ.get("HERMES_HOME") or os.path.join(os.path.expanduser("~"), ".hermes")
    gapi = os.path.join(hermes_home, "skills/productivity/google-workspace/scripts/google_api.py")
    start = f"{today.isoformat()}T00:00:00+08:00"
    # compute tomorrow local date without arithmetic assumptions
    from datetime import timedelta
    end_date = today + timedelta(days=1)
    end = f"{end_date.isoformat()}T00:00:00+08:00"
    cp = subprocess.run(["python", gapi, "calendar", "list", "--start", start, "--end", end], text=True, capture_output=True, timeout=120)
    if cp.returncode != 0:
        raise RuntimeError(f"Google Calendar failed: {cp.stderr or cp.stdout}")
    return json.loads(cp.stdout or "[]")


def fmt_time(ev):
    st = ev.get("start", {})
    if isinstance(st, dict):
        val = st.get("dateTime") or st.get("date") or ""
    else:
        val = str(st or "")
    if not val:
        return "Time TBD"
    if len(val) == 10:
        return "All day"
    try:
        return datetime.fromisoformat(val.replace("Z", "+00:00")).astimezone(PHT).strftime("%-I:%M %p")
    except Exception:
        return val


def task_brief(page):
    p = page["properties"]
    return {
        "task": title_plain(p.get("Task", {})),
        "priority": select_name(p.get("Priority", {})) or "No priority",
        "project": select_name(p.get("Project", {})) or "No project",
        "status": select_name(p.get("Status", {})) or "No status",
        "due": date_start(p.get("Due Date", {})),
        "source": select_name(p.get("Source", {})),
        "type": select_name(p.get("Task Type", {})),
        "contact": rich_text_plain(p.get("Member / Contact", {})),
        "id": page.get("id"),
    }

priority_rank = {"P1 - Urgent": 0, "P2 - High": 1, "P3 - Normal": 2, "P4 - Low": 3, "No priority": 4}
status_rank = {"Today": 0, "In Progress": 1, "Blocked": 2, "Waiting": 3, "Backlog": 4, "No status": 5}

def sort_key(t):
    due = t["due"] or "9999-12-31"
    return (priority_rank.get(t["priority"], 9), status_rank.get(t["status"], 9), due, t["project"], t["task"])


def chunks(s, n=1900):
    out=[]
    while s:
        out.append({"type":"text", "text":{"content":s[:n]}})
        s=s[n:]
    return out or [{"type":"text", "text":{"content":""}}]

try:
    events = get_calendar_events()
except Exception as e:
    events = []
    calendar_error = str(e)
else:
    calendar_error = None

body = {"filter":{"and":[{"property":"Status","select":{"does_not_equal":"Done"}},{"property":"Status","select":{"does_not_equal":"Cancelled"}}]},"page_size":100}
resp = notion_request("POST", f"data_sources/{MASTER_DS}/query", body)
tasks = [task_brief(x) for x in resp.get("results", [])]
tasks.sort(key=sort_key)

top = tasks[:7]
meetings_lines = []
for ev in events:
    title = ev.get("summary") or ev.get("title") or "Untitled event"
    line = f"{fmt_time(ev)} — {title}"
    loc = ev.get("location")
    if loc:
        line += f" @ {loc}"
    meetings_lines.append(line)
meetings_text = "\n".join(meetings_lines) if meetings_lines else "No calendar events scheduled."
if calendar_error:
    meetings_text += f"\n(Calendar pull error: {calendar_error})"

priority_lines = []
for i,t in enumerate(top,1):
    due = f", due {t['due']}" if t['due'] else ""
    contact = f", contact: {t['contact']}" if t['contact'] else ""
    priority_lines.append(f"{i}. [{t['priority']}] {t['task']} — {t['project']} ({t['status']}{due}{contact})")
pending_priorities = "\n".join(priority_lines) if priority_lines else "No pending tasks found."

def find_task(project_contains=None, priority=None, contains=None, skip=None):
    skip = skip or set()
    for idx,t in enumerate(tasks):
        if idx in skip: continue
        if project_contains and project_contains not in t['project']: continue
        if priority and t['priority'] != priority: continue
        if contains and contains.lower() not in t['task'].lower(): continue
        return idx,t
    return None,None
used=set()
_, p1 = find_task(priority="P1 - Urgent", skip=used)
if not p1: _, p1 = find_task(priority="P2 - High", skip=used)
# choose key tasks for slots
bbx_tasks = [t for t in tasks if t['project']=='BBX']
atlas_tasks = [t for t in tasks if t['project'].startswith('Atlas')]
bbx1 = bbx_tasks[0]['task'] if bbx_tasks else "BBX calls/logs toward daily KPI"
bbx2 = bbx_tasks[1]['task'] if len(bbx_tasks)>1 else "BBX member check-ins / email drafts"
atlas1 = atlas_tasks[0]['task'] if atlas_tasks else "Atlas team coordination"
atlas2 = atlas_tasks[1]['task'] if len(atlas_tasks)>1 else "Atlas focused work / EOD prep"
focus = (p1 or top[0] if top else {"task":"highest-priority pending task"})['task']

if day_type.startswith("Weekday"):
    suggested_plan = "\n".join([
        "6:50–7:00 AM → Review this briefing.",
        f"7:00–8:00 AM → BBX only: {bbx1}; aim for 2 call attempts.",
        f"8:00–9:00 AM → BBX + Atlas overlap: handle urgent/high-priority task: {focus}.",
        f"9:00–11:00 AM → Deep work block: {focus}.",
        f"11:00 AM–12:00 PM → BBX member check-ins/email drafts: {bbx2}.",
        "12:00–1:00 PM → Lunch + async Slack/Discord check for Atlas.",
        f"1:00–2:00 PM → Atlas team coordination: {atlas1}.",
        "2:00–3:00 PM → BBX wrap-up: remaining calls/logs to hit 5 calls + 10 logs.",
        f"3:00–5:00 PM → Atlas focused work / EOD prep: {atlas2}.",
        "Evening (if energy allows) → Story Writing with Claude.",
    ])
elif day_type.startswith("Saturday"):
    suggested_plan = "\n".join([
        f"Morning → Atlas monitoring: {atlas1}.",
        "Mid-morning → YouTube Shorts management (5–8 hr block).",
        "If Atlas emergency → address as needed.",
    ])
else:
    suggested_plan = "Rest day / emergency only. Review only urgent or blocked items if needed."

granola_note = "Granola API unavailable — no meeting notes were pulled directly. Meeting action items are included only if they already exist in Notion or synced notes."
full_body = f"""## 📅 Today: {date_title}

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

create_body = {
    "parent": {"database_id": BRIEFING_DB},
    "properties": {
        "Date": {"title": [{"text": {"content": date_title}}]},
        "Day Type": {"select": {"name": day_type}},
        "Status": {"select": {"name": "Planned"}},
        "Meetings Today": {"rich_text": chunks(meetings_text)},
        "Pending Priorities": {"rich_text": chunks(pending_priorities)},
        "Suggested Plan": {"rich_text": chunks(suggested_plan)},
        "BBX Calls Today": {"number": 0},
        "BBX Logs Today": {"number": 0},
    },
    "markdown": full_body,
}

result = {"date_title": date_title, "day_type": day_type, "events_count": len(events), "tasks_count": len(tasks), "top_priorities": pending_priorities, "meetings_text": meetings_text, "suggested_plan": suggested_plan, "full_body": full_body}
try:
    created = notion_request("POST", "pages", create_body)
    result.update({"notion_write": "succeeded", "page_id": created.get("id"), "url": created.get("url")})
except Exception as e:
    result.update({"notion_write": "failed", "error": str(e)})
print(json.dumps(result, ensure_ascii=False, indent=2))
