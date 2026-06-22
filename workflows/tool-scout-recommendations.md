# Tool Scout Recommendations Workflow

**Purpose:** Find and recommend helpful tools/apps/AI services for Jude's active projects without installing, buying, or changing workflows automatically.

## Default cadence

Manual first. Weekly automation can be enabled later only if Jude approves the exact cron job.

## Free-first rule

Prefer tools that are:

1. free;
2. open-source;
3. local-first;
4. freemium with a genuinely useful free tier;
5. cheap only if the free alternatives are weak and the time savings are high.

## AI-operable rule

Because Jude does not have time for manual edits, prioritize tools that can be operated by AI/agents or integrated into WAT workflows. Look for:

- public API or documented automation API;
- CLI or scriptable local workflow;
- browser-automation-friendly web interface;
- batch import/export;
- templates that agents can populate;
- plugin/extension system;
- local file-based workflows;
- GitHub/Notion/Google Drive/Zapier/Make/n8n-style integrations.

Manual-only timeline editors, manual-only design apps, and closed tools with no export/automation path should be ranked lower even if they are popular.

## Research rules

- Use current official pages, docs, GitHub repos, release notes, and reputable summaries.
- Do not rely on memory for current pricing or feature availability.
- Verify pricing/free-tier claims when possible.
- Label uncertainty clearly.
- Do not promote tools just because they are trendy; tie each recommendation to a concrete project workflow.

## Project matching

| Project | Good tool signals |
|---|---|
| BBX | reduces manual CRM/Sheets/call-log friction; works with exports; safe for PC-local workflow |
| Hive affiliate | improves product research, compliance, script/video production, or analytics without making unsupported claims |
| Story Writing | improves continuity, proofreading, character visuals, comic/storyboard planning, or AI video prep without changing canon |
| Job Market Digital | helps build websites, proposals, SEO, design assets, client onboarding |
| Atlas Capture | helps organize evidence, docs, meetings, timelines, tasks |
| JAM AI Workspace | improves sync, source-of-truth, backups, monitoring, assistant handoffs |

## Report scoring

Use a 1–5 score for:

- project fit;
- cost/value;
- AI-operability;
- ease of setup;
- privacy/safety;
- immediate usefulness.

## Approval gates

Always ask Jude before:

- installing apps/extensions/packages on his PC;
- signing up for accounts;
- connecting Google/Notion/GitHub/social accounts;
- entering API keys;
- subscribing to paid plans/trials;
- sending private project files into a third-party service;
- enabling a recurring cron/tool-monitor job.

## Suggested manual dry-run

When asked to dry-run Tool Scout:

1. Pick one focus area, e.g. `Story Writing visual/comic tools` or `Hive affiliate video tools`.
2. Research 5–10 candidates.
3. Return the top 3–7 only, ranked higher when AI/agent operation is realistic.
4. Save report under `.tmp/tool-scout/`.
5. Recommend one zero-cost trial action.
