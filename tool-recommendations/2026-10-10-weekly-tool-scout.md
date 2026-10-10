# Weekly Tool Scout Report — 2026-10-10

## Focus this week

**Focus areas:**

1. **BBX + Atlas + JAM AI Workspace — agent-operable internal dashboards and lightweight data apps.** Jude already has Google Sheets, Notion, repo handoffs, and scripts; the next bottleneck is turning queues, evidence lists, CRM/export mirrors, and task states into simple review dashboards without requiring manual spreadsheet editing.
2. **AI Agency / Job Market Digital — reusable client/admin app patterns.** The same tools can become future low-cost deliverables or internal admin panels for small-business websites, but only after Jude approves a pilot.

**Why this focus:** recent reports covered repo secret scanning, document ingestion/OCR, website QA, research crawlers, video tooling, and transcription. This week rotates toward **low-code/internal-tool layers** that are still AI-operable: APIs, CLIs, self-hosting, database connectors, scripted imports/exports, and app/dashboard builders.

**Boundary followed:** no software/packages/extensions were installed, no accounts/API keys were created, no private files were uploaded, no services were connected, no workflows were changed as final, and no automation/cron/container was created.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **NocoDB** | **Free / self-hostable Airtable alternative.** GitHub API checked 2026-10-10: `nocodb/nocodb`, 65,229 stars, updated 2026-10-09. NPM checked: `nocodb 0.301.3`; license listed as Sustainable Use License. | **5/5** — database/spreadsheet UI, REST/API-oriented use cases, import/export friendly, self-hostable, can sit on top of SQL. | **BBX**, Atlas, JAM ops, AI Agency. | Best first candidate if Jude wants a simple Airtable-like layer over tables/queues without forcing everything through Google Sheets. Could mirror BBX call queues, Atlas evidence indexes, or AI Agency lead/client trackers for review. | Installing/self-hosting or connecting real Sheets/DBs needs approval. License should be reviewed before using for paid client deliverables. Do not import private CRM/member/evidence data without approval. | **No-install next step:** draft a sample schema only: `BBX Contact Queue`, `Atlas Evidence Index`, and `JAM Project Registry` fields in Markdown/CSV under `.tmp/`, then decide if a real NocoDB pilot is worth approving. |
| **Baserow** | **Open-source/self-hostable platform per README.** GitHub API checked 2026-10-10: `baserow/baserow`, 6,107 stars, updated 2026-10-09; repo description says open-source, cloud and self-hosted. | **5/5** — README says API-first; supports databases, automations, apps, dashboards, and AI-facing workflows. | **JAM workspace**, BBX, Atlas, Hive queue management. | Stronger than a plain spreadsheet when agents need structured tables plus simple apps/dashboards. Good candidate for queue review dashboards and cross-project registries. | Approval needed before install, self-hosting, cloud signup, or connecting Google/Notion/GitHub. Review license/plan limits before client use. | **Safe trial:** create a paper design for one `Tool Recommendations` database and one `Hive Affiliate Content Queue` with fields, statuses, and approval gates; no account/install yet. |
| **Appsmith** | **Free / open-source core; Apache-2.0.** GitHub API checked 2026-10-10: `appsmithorg/appsmith`, 41,043 stars, updated 2026-10-09. README positions it for dashboards, admin panels, internal tools, and 25+ database/API integrations. | **4/5** — API/database connectors and UI builder are agent-friendly; less ideal than pure file/CLI tools but good for dashboards. | **BBX**, Atlas, AI Agency/JMD. | Best fit when Jude needs an actual internal web app: e.g. a BBX call review panel, Atlas case dashboard, or client website intake/admin tool. More polished for app screens than Baserow/NocoDB. | Requires deployment/signup and connection to databases/APIs. Any real BBX/Atlas/client data connection needs approval. | **Defer to design-only:** sketch one BBX “daily calls dashboard” page: candidate list, call status, next action, evidence/source links, and CRM-update queue. |
| **Windmill** | **Open-source/community edition; self-hostable developer platform.** GitHub API checked 2026-10-10: `windmill-labs/windmill`, 18,149 stars, updated 2026-10-09. NPM checked: `windmill-cli 1.830.0`, Apache 2.0. README describes scripts, APIs, background jobs, workflows, and UIs. | **5/5** — CLI, scripts in Python/TypeScript/Go/Bash, GitHub sync concepts, workflows, generated UIs. | **JAM ops**, BBX scripts, Atlas document/evidence pipelines, AI Agency automations. | Best for turning Jude’s deterministic scripts into approved manual-run tools with forms/UIs later. Strong match for WAT because scripts stay central and the UI/workflow layer wraps them. | Powerful automation platform: do not deploy, create webhooks, connect secrets, or schedule workflows without approval. | **Safe trial:** identify 2–3 existing scripts that could become manual-only forms later, e.g. BBX daily plan generator, document ingestion test, repo secret-scan preflight. |
| **Budibase** | **Open-source operations platform per README; CLI package exists.** GitHub API checked 2026-10-10: `Budibase/budibase`, 28,329 stars, updated 2026-10-10. NPM checked: `@budibase/cli 3.48.0`, GPL-3.0. README mentions apps, automations, agents, self-hosting, and public API. | **4/5** — public API, CLI, apps/automations; good for internal tools, but broader platform surface than needed for first pilot. | **AI Agency/JMD**, Atlas, JAM ops. | Useful if Jude wants to build operational apps quickly and possibly adapt the same pattern for client admin dashboards. | More platform complexity; automations/agents could overreach if enabled too early. Approval needed before install/cloud/self-host/client use. | **Defer:** keep as an alternative to Appsmith if Appsmith/Baserow do not fit the UI + data needs. |

## Best pick this week

**Best pick: NocoDB or Baserow for the first “agent-readable queue dashboard” design, with Windmill as the later script-execution layer.**

Recommended future shape, pending approval before any installation or real data connection:

```text
Existing source files / exports / scripts
  → agent prepares normalized CSV/Markdown schema in .tmp/
  → Jude reviews fields and approval gates
  → optional pilot in NocoDB or Baserow with harmless sample data only
  → later: Windmill wraps approved scripts as manual-run forms
  → only after review: connect real BBX/Atlas/JAM data sources
```

This keeps Jude’s source-of-truth discipline intact: GitHub/Markdown/scripts remain canonical for agents, while a low-code tool can become a human-friendly review surface.

## Free/open-source alternatives

- **Direct Markdown/CSV + GitHub only** — still the safest zero-install baseline; enough for schemas and dry-runs.
- **Google Sheets + existing Python scripts** — already fits BBX; best when Jude wants no new platform. Downside: dashboards and approval queues can become manual/fragile.
- **NocoDB** — strongest Airtable-like self-hostable table candidate.
- **Baserow** — strongest table + app/dashboard candidate if the built-in app/automation direction is useful.
- **Appsmith** — better for true internal app screens than table-first tools.
- **Windmill** — better for script/workflow execution than data-table management.
- **Budibase** — potentially strong all-in-one ops apps, but defer until a smaller pilot proves the need.

## Manual-only tools to avoid or defer

- Manual spreadsheet redesigns that agents cannot reproduce from scripts or schemas.
- Closed no-export dashboard tools where data cannot be backed up to CSV/Markdown/GitHub.
- Building a full internal app before the queue schema and approval gates are stable.
- Turning on automations/webhooks/agents in any low-code platform before Jude approves the exact workflow.
- Connecting real CRM/member/evidence/client data during the first tool trial.

## Approval needed from Jude

Jude approval is needed before:

- installing or self-hosting NocoDB, Baserow, Appsmith, Windmill, Budibase, Docker images, packages, CLIs, or plugins;
- creating cloud accounts/workspaces or starting trials;
- connecting Google Sheets, Notion, GitHub, CRM, Drive, AppSheet, affiliate/social accounts, or databases;
- importing BBX member data, Atlas evidence, client data, private docs, or affiliate/account exports;
- creating webhooks, scheduled workflows, automations, agents, containers, or public endpoints;
- using any of these tools for paid client deliverables before license/plan review.

## Next safe action

**Safest next action with no install and no external writes:** create a **Markdown/CSV schema mockup** under `.tmp/tool-scout/internal-dashboard-pilot/` for one of these:

1. **BBX Contact Queue Dashboard** — member, market, last contact, trade acceptance status, suggested call spiel, next action, CRM queue status, source link.
2. **Atlas Evidence / Task Index** — case/doc name, source location, evidence type, status, action needed, Notion/AppSheet update needed, approval gate.
3. **JAM Tool Recommendation Tracker** — tool, project fit, cost, AI-operability, approval status, safe trial, report link.

If Jude likes the schema, then he can approve a tiny sample-data pilot in NocoDB or Baserow later.

## Sources checked

- Local JAM AI Workspace docs and handoffs: `AGENTS.md`, `agents/README.md`, `agents/tool-scout/AGENT.md`, `workflows/tool-scout-recommendations.md`, `PROJECTS.md`, central `HANDOFF.md`, recent Hive/Story/Atlas/BBX handoffs, and the latest durable Tool Scout reports to avoid repeating the same focus.
- GitHub API metadata checked 2026-10-10 for: `nocodb/nocodb`, `baserow/baserow`, `appsmithorg/appsmith`, `windmill-labs/windmill`, and `Budibase/budibase`.
- NPM registry checked 2026-10-10 for: `nocodb`, `windmill-cli`, `@budibase/cli`, `n8n`, and `@n8n/n8n-nodes-langchain` to confirm active package/CLI surfaces where relevant.
- Official GitHub README/raw sources checked 2026-10-10 for NocoDB, Baserow, Appsmith, Windmill, and Budibase to confirm positioning around self-hosting, APIs, dashboards/internal tools, scripts/workflows, and public API/CLI notes.
