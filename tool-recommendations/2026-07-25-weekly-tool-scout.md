# Weekly Tool Scout Report — 2026-07-25

## Focus this week

1. **Story Writing revision/proofreading support** — recent Story work is still review-only/canon-safe, and the next planned automation phase is Python-assisted proofreading after visual prompts stabilize. This week prioritizes local/offline writing QA tools that agents can run against Markdown without rewriting canon.
2. **BBX / JAM AI Workspace structured-data glue** — BBX still depends on exported/normalized tables, call/task queues, and safe approval-gated updates. This week looks at spreadsheet-database tools with APIs/local/self-host options that could eventually reduce Google Sheets friction without creating live automation now.

Assumptions: no private accounts or project files were accessed. This report is research-only: no installs, signups, account connections, uploads, webhooks, cron changes, or workflow changes were made.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Harper** — https://github.com/Automattic/harper | **Open-source, Apache-2.0. Free local/offline grammar checker.** | **5/5** — local/offline Rust grammar engine; available via binaries/packages/editor integrations; agent-friendly because it can be run on text/Markdown without uploading manuscripts. | **Story Writing** proofreading Phase 2; also JAM docs cleanup. | Strong fit for Jude’s privacy/canon constraints: local grammar/style catches before an LLM pass, so the agent only reviews flagged evidence and does not need to ingest entire chapters by default. | Installing binaries/editor plugins requires approval. Treat suggestions as advisory only; do not auto-apply to fiction prose or Chavacano/culture-specific language. | **Zero-install trial:** choose one chapter/report later and define a Harper review checklist in Markdown: what to flag, what to ignore, and how to route suggestions to `.tmp/overnight/` only. |
| **Vale** — https://github.com/vale-cli/vale / https://vale.sh | **Open-source, MIT. Free CLI prose linter.** | **5/5** — command-line, markup-aware, configurable rules/styles, CI/script friendly. | **Story Writing**, JAM AI Workspace docs, AI Agency proposals/templates. | Best for custom Jude-specific style rules: avoid AI-ish phrases, enforce approval-gate wording, flag inconsistent terms in docs, and run repeatable checks over Markdown. More deterministic than asking an LLM to “proofread everything.” | Installing CLI or adding project config requires approval. Bad rules can create noise; start with advisory/report-only mode. | **Safe trial:** draft a `.vale.ini` + `styles/Jude/` rule plan in a report only; no config committed until Jude approves. |
| **LanguageTool** — https://github.com/languagetool-org/languagetool | **Open-source core, LGPL-2.1-or-later; public/hosted services also exist.** | **4/5** — HTTP API docs and local server option; scriptable checks, multi-language support. | **Story Writing** line proofreading; possible Chavacano/Filipino-adjacent caution notes; docs/proposals. | Useful second opinion when Harper/Vale miss ordinary grammar issues. API/local server shape makes batch checking possible later. | Local server/Docker setup needs approval; public API use may send text externally and should not receive private manuscript/project text without explicit approval. | **Safe trial:** compare only using a tiny non-private sample paragraph created for testing, not canon manuscript text. |
| **Grist** — https://github.com/gristlabs/grist-core / https://support.getgrist.com/api/ | **Open-source community core, Apache-2.0; self-host/desktop options; hosted cloud has free/paid plans.** | **5/5** — REST API, Zapier-style integrations, service accounts noted in docs, desktop/local options, and emerging MCP support in current repo docs. | **BBX**, Atlas Capture, JAM AI Workspace operations. | Promising bridge between spreadsheet UX and database-like reliability for queues: BBX call queue, CRM update queue, Tool Scout source registry, Atlas evidence/task tables. More agent-operable than manual spreadsheets because records can be addressed via API. | Do not migrate live BBX/Atlas data or connect accounts without approval. Self-host/Docker/cloud signup/API tokens all need Jude approval. | **Safe trial:** design a Markdown-only schema for one table: `BBX Contact Queue` with stable keys, status, evidence, and approval fields; no Grist instance yet. |
| **Baserow** — https://github.com/baserow/baserow / https://api.baserow.io/api/redoc/ | **Open-core; README says non-premium/non-enterprise features under MIT and self-hosting available.** | **4/5** — API-first, OpenAPI schema, self-host/cloud, database/app/automation orientation. | **BBX/JAM/Atlas** queue databases and internal mini-apps. | Worth watching as an Airtable-style alternative if Jude wants forms/apps/dashboards in addition to a database. Good AI-operability through API and structured tables. | License is open-core, not purely OSS for all features; account/cloud/self-host/API-key decisions require approval. Avoid moving private data until privacy/access model is reviewed. | **Defer behind Grist:** compare after a schema exists; use public docs only. |

## Best pick this week

**Harper + Vale as a two-layer Story Writing review stack** is the best immediate pick.

Reason: it directly supports Jude’s next planned Story phase while respecting the rule that overnight/story work should be review-only and should not rewrite canon. Harper can catch local/offline grammar issues; Vale can enforce Jude-specific terminology/style/approval-gate rules. Together they produce compact flagged evidence for an LLM reviewer instead of requiring the model to read whole chapters every time.

Best no-risk next action: create a **Markdown-only “Story Writing proofreading lint plan”** that defines:

- files to scan later;
- canon-safe output path under `.tmp/overnight/`;
- allowed issue categories;
- terms/rules to ignore;
- how an LLM should review flagged lines without applying edits.

## Free/open-source alternatives

- **Plain Python scanners already in Story Writing** — keep using deterministic scanners first where available, especially `scripts/story_continuity_scan.py`, before adding new tools.
- **LanguageTool local server** — good later for a grammar second pass, but heavier than Harper and needs setup approval.
- **Grist Desktop/Core** — best structured-data candidate if Jude wants a local/self-hosted queue database later; start with schema design before any installation.
- **NocoDB** — very popular self-hostable Airtable alternative with REST APIs, but current license is Sustainable Use License, so it is less cleanly free/open-source than Grist for Jude’s preference.

## Manual-only tools to avoid or defer

- **Grammarly-only manuscript workflow** — avoid as primary because it is account/cloud-centric and sends writing to an external service unless a specific privacy-reviewed plan is approved.
- **Manual spreadsheet/database redesigns** — avoid asking Jude to manually rebuild BBX/Atlas trackers. Any future move should be schema-first, import/export-first, and agent/script-assisted.
- **Manual writing editors with no CLI/export path** — defer unless they produce Markdown/CSV/JSON artifacts that agents can inspect.

## Approval needed from Jude

Jude approval is needed before any of these actions:

- installing Harper, Vale, LanguageTool, Grist, Baserow, NocoDB, browser/editor plugins, Docker images, or packages;
- creating local servers, containers, webhooks, MCP servers, API credentials, or service accounts;
- connecting Google Sheets, Notion, GitHub, CRM, Facebook, Shopee, YouTube, Suno, or affiliate accounts;
- uploading private manuscripts, BBX member data, Atlas evidence, call transcripts, or project files to external services;
- changing active Story/BBX/Atlas/JAM workflows as final;
- auto-applying proofreading changes to canon chapter files.

## Next safe action

Create a report-only plan file, no install:

```text
.tmp/tool-scout/story-writing-proofreading-lint-plan.md
```

Suggested contents: Harper/Vale/LanguageTool evaluation matrix, proposed issue categories, ignore list for fictional names/cultural terms, output format for `.tmp/overnight/`, and verification steps. After Jude approves, the first implementation can be a dry-run on a small non-canonical sample or a single approved chapter excerpt.

## Sources checked

- Harper GitHub metadata and README: `https://github.com/Automattic/harper`, `https://raw.githubusercontent.com/Automattic/harper/master/README.md`
- Vale GitHub metadata and README/docs links: `https://github.com/vale-cli/vale`, `https://raw.githubusercontent.com/errata-ai/vale/master/README.md`, `https://vale.sh`
- LanguageTool GitHub metadata and README: `https://github.com/languagetool-org/languagetool`, `https://raw.githubusercontent.com/languagetool-org/languagetool/master/README.md`
- Grist GitHub metadata and README/API references: `https://github.com/gristlabs/grist-core`, `https://raw.githubusercontent.com/gristlabs/grist-core/main/README.md`, `https://support.getgrist.com/api/`
- Baserow GitHub metadata and README/API references: `https://github.com/baserow/baserow`, `https://raw.githubusercontent.com/bram2w/baserow/develop/README.md`, `https://api.baserow.io/api/redoc/`
- NocoDB GitHub metadata and README/license note: `https://github.com/nocodb/nocodb`, `https://raw.githubusercontent.com/nocodb/nocodb/develop/README.md`
