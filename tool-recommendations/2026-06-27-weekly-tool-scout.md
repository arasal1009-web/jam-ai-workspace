# Weekly Tool Scout Report — 2026-06-27

## Focus this week

1. **BBX + JAM AI Workspace operations:** reduce manual Google Sheets / Notion / CRM-queue friction with agent-operable workflow glue.
2. **Story Writing visual/adaptation prep:** keep visual prompt and comic/movie planning local-first and scriptable before any paid media generation.

Selection rationale: recent handoffs show BBX daily plans, Notion task creation/deduping, and Google Sheets enrichment updates are active; Story Writing visual/canon prompts are also active and should remain review-only.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Google Apps Script** | Free with Google Workspace quotas; official Google tool | **5/5** — scripts, triggers, web apps, Workspace APIs, can be authored/reviewed by agents | **BBX, JAM AI Workspace, Atlas Capture** | Best near-term bridge for Sheets-based BBX workflows: can normalize/export tabs, create task payloads, and hand off to Notion/API scripts without browser scrolling. Official docs describe Apps Script as a way to “extend, automate & share” Google Workspace apps. | Needs Jude approval before deploying scripts/triggers, authorizing scopes, or writing Sheets/Notion. | Draft a **read-only** Apps Script or Python-equivalent spec that reads `Unified Members` headers and outputs a JSON/CSV task queue; no deployment/authorization yet. |
| **n8n self-host / cloud** | Self-host option; cloud starts paid after trial (pricing page showed Starter from €20/mo billed annually; free trial says no credit card). | **5/5** — webhooks, 400+ integrations per GitHub description, JS/Python code steps, HTTP/GraphQL requests, CLI/API on appropriate plans/self-host | **JAM AI Workspace, BBX, Hive** | Strong future workflow orchestrator for “when X file/report exists → create queue/task/draft” workflows. Official docs expose a REST API and OpenAPI spec; GitHub describes self-host/cloud and native AI capabilities. | Approval needed before installing/self-hosting, connecting credentials, or enabling workflows. Note: n8n docs say the public API is not available during the free trial; verify plan/self-host behavior before relying on API. | Create a paper workflow diagram only: `BBX daily plan Markdown → parser → Notion task payload → approval gate`. No account/install. |
| **Baserow** | Free cloud tier shown: $0, unlimited databases, 3,000 rows/workspace, 2GB storage/workspace; self-host option available | **4/5** — REST API, Docker/self-host, database views/forms; agent-friendly records | **BBX, Atlas Capture, JAM AI Workspace** | Good Airtable-like staging database for normalized member/contact/evidence queues when Google Sheets becomes slow or fragile. Official docs state backend/frontend communicate via REST API; pricing page lists free tier and self-host. | Approval needed before creating workspace/importing member data; privacy review needed for BBX/Atlas data. | Use a **synthetic sample CSV** only to evaluate schema fit: Market, Member ID, Account Manager, Next Action, Evidence. No real member data uploaded. |
| **Krita + Python scripting** | Free/open-source; GitHub describes Krita as free and open source; GPL-3.0 repo | **4/5** — Python scripting, file-based assets, templates, batchable exports | **Story Writing, Hive visual assets** | Better than manual-only design tools for character sheets, comic panels, and visual reference overlays because agents can produce prompt cards/templates and later scripts can batch-generate layouts. | Requires approval before installing on Jude’s PC or using private art/reference files. | Draft a Krita storyboard/contact-sheet template spec in Markdown; later Jude can approve installation or manual test. |
| **ComfyUI** | Open-source; GitHub API shows GPL-3.0 and describes it as a modular diffusion GUI, API, and backend | **4/5** — graph/node workflows, API/backend, reusable workflows | **Story Writing visual prompt pipeline, Hive product-video ideation** | Best future local-first image workflow if Jude wants repeatable character/scene generation without uploading private story assets to web services. Fits WAT because workflows can be versioned as graph files. | Approval needed before install, model download, GPU use, or generating media. Model licenses and private-reference handling must be reviewed. | Do **not** install yet. Save prompt/workflow requirements only: character anchors, negative prompts, output naming, approval gates. |

## Best pick this week

**Google Apps Script / Sheets-first queue tooling** is the safest immediate pick because BBX already depends on `Unified Members`, and recent friction is not “need another CRM” but “reduce low-value browser/Sheet scrolling.” Start with read-only queue export and task-payload generation, then decide whether Hermes/PC scripts or Apps Script should own each step.

Why it wins this week:

- no new SaaS account required if Jude already uses Google Sheets;
- directly supports BBX daily plan + Notion Command Center task flow;
- easy for agents to draft and review code before Jude authorizes anything;
- can remain read-only until a specific write path is approved.

## Free/open-source alternatives

- **Plain Python + Google Sheets API + Notion API** — already aligned with existing BBX helper scripts; highest control and easiest to keep in GitHub. Needs OAuth/API setup approval for live use.
- **Baserow self-host/free tier** — useful if Sheets becomes too fragile as the operational database, but do not migrate real data yet.
- **Krita / Blender / ComfyUI** — strong local-first Story visual stack. Prioritize Krita templates and prompt/contact sheets before heavier Blender/ComfyUI setup.
- **GitHub Actions** — useful for repo-only validation/report generation, but avoid connecting private integrations or schedules until Jude approves.

## Manual-only tools to avoid or defer

- Manual timeline/video editors with no API/batch/template path for Hive short-form videos; they may produce good videos but will consume Jude’s editing time.
- Closed AI video/image platforms that require uploading private Story references before visual canon is stable.
- CRM browser automation from the VPS; BBX handoffs say real CRM browser work should remain PC-local using the correct authenticated Chrome profile.

## Approval needed from Jude

Before any next step beyond documentation/dry-run, Jude approval is needed for:

- installing n8n, Baserow, Krita, ComfyUI, Blender, browser extensions, or plugins;
- authorizing Google Apps Script / Google Sheets / Notion scopes;
- uploading real BBX/Atlas member data or Story private references to any external service;
- creating triggers, webhooks, crons, Docker containers, or autonomous agents;
- writing live Notion/Sheets/CRM records.

## Next safe action

**Recommended zero-risk trial:** create a read-only BBX queue-export spec using fake/sanitized rows only.

Deliverable for the trial:

1. Markdown schema for `BBX Contact Task Queue`.
2. Sample JSON/CSV output with 3 fake members.
3. Pseudocode showing two implementation options:
   - existing Python helper path;
   - Google Apps Script path.
4. Explicit approval gates for live Sheets read, Notion write, and CRM/browser use.

No install, signup, account connection, cron, trigger, or private-data upload required.

## Sources checked

- Google Apps Script overview: https://developers.google.com/apps-script/overview
- n8n pricing: https://n8n.io/pricing/
- n8n API docs: https://docs.n8n.io/api/
- n8n GitHub API metadata checked 2026-06-27: `n8n-io/n8n`, described as fair-code workflow automation with native AI, self-host/cloud, 400+ integrations
- Baserow pricing: https://baserow.io/pricing
- Baserow REST API docs: https://baserow.io/docs/apis/rest-api
- Baserow GitHub API metadata checked 2026-06-27: `bram2w/baserow`, open-source platform available on cloud and self-hosted
- Krita Python scripting docs: https://docs.krita.org/en/user_manual/python_scripting.html
- Krita GitHub API metadata checked 2026-06-27: `KDE/krita`, GPL-3.0, free/open-source digital art application
- ComfyUI GitHub API metadata checked 2026-06-27: `comfyanonymous/ComfyUI`, GPL-3.0, modular diffusion GUI/API/backend
