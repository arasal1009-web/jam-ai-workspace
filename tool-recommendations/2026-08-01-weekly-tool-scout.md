# Weekly Tool Scout Report — 2026-08-01

## Focus this week

1. **Atlas Capture + JAM AI Workspace document-to-Markdown pipeline** — recent Atlas sync work depends on keeping documents, evidence, handoffs, and assistant-readable context aligned. The highest leverage this week is a safe local-first conversion/search pipeline before any Notion/Drive/AppSheet writes.
2. **Music Production + Tool Scout public research capture** — the Music Production project needs evidence-backed YouTube niche research, while Tool Scout itself needs repeatable source monitoring. Prioritize official APIs, public RSS/feed workflows, and file-based artifacts agents can review.

Assumptions: no private files, accounts, Google/Notion/YouTube data, Atlas evidence, or project documents were accessed. Research used public official pages/GitHub/docs only. No software was installed and no workflow was changed as final.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **MarkItDown** — https://github.com/microsoft/markitdown | **Open-source, MIT; free Python CLI/library.** | **5/5** — direct CLI (`markitdown file.pdf -o file.md`) and Python API; converts local files into Markdown for LLM/search pipelines. | **Atlas Capture, JAM AI Workspace, Story Writing, BBX, AI Agency.** | Lightweight first-pass converter for PDFs, DOCX, PPTX, XLSX, HTML, CSV/JSON/XML, ZIPs, images with OCR metadata, audio metadata/transcription, YouTube URLs, EPUBs, and more. Best for turning human-facing docs into assistant-readable Markdown mirrors. | Installation/package use needs Jude approval. Its README warns it performs I/O with current process privileges, so inputs must be trusted/sanitized and scoped. Do not send private documents to optional cloud analyzers without approval. | **No-install trial:** draft a Markdown-only `document-mirror-pipeline.md` spec listing source folders, output folders, naming rules, and approval gates for Atlas/JAM docs. |
| **Docling** — https://github.com/docling-project/docling / https://docling-project.github.io/docling/ | **Open-source, MIT; free local execution possible.** | **5/5** — CLI, Python, Markdown/JSON exports, local execution, OCR, agent integrations, MCP/API-server options documented. | **Atlas Capture evidence/docs, JAM documentation mirrors, Story scanned/reference material.** | Stronger than MarkItDown for complex PDFs/scans: advanced PDF understanding, reading order, tables, formulas, images, OCR, Markdown/HTML/WebVTT/JSON export, and local/air-gapped use. Good future backend for Atlas evidence packs. | Heavier install/model/OCR setup needs approval. API server/MCP/server modes are automation infrastructure and need separate approval. Keep private Atlas evidence local-only unless Jude approves otherwise. | **Safe trial:** create a comparison checklist only: when to use MarkItDown vs Docling, expected output fields, and `.tmp/doc-mirrors/` review path. |
| **Datasette** — https://datasette.io / https://github.com/simonw/datasette | **Open-source, Apache-2.0; free local CLI/server.** | **5/5** — SQLite-first, stable JSON API in Datasette 1.x docs, plugins, CLI/server; turns CSV/SQLite exports into queryable local APIs. | **BBX exports, Atlas case tables, JAM source registries, Tool Scout source database.** | Gives agents a clean read-only way to query messy CSV/SQLite data instead of reopening large Sheets/CSVs. Could expose synthetic or exported tables as local browsable/API data for queue planning and source tracking. | Installing/running local server needs approval. Publishing/public hosting should be avoided unless explicitly approved. Private BBX/Atlas data must stay local/VPS-private. | **Zero-risk trial:** design a fake-data SQLite schema for `tool_sources`, `project_handoffs`, and `bbx_contact_queue`; no Datasette install. |
| **YouTube Data API v3** — https://developers.google.com/youtube/v3 | **Google API with default quota; docs state projects get 100 `search.list` calls/day, 100 `videos.insert` calls/day, and 10,000 units/day for other endpoints by default.** | **4/5** — official API, client libraries, quota monitoring, API keys/OAuth depending on access type. | **Music Production niche research, Hive/CryptoCreep public channel/video research, AI Agency SEO/content evidence.** | Best official path for evidence-backed YouTube niche research without manual browsing: search videos/channels/playlists, collect titles/descriptions/stats where permitted, and build repeatable research tables. Avoids relying on scraped/blocked pages. | Requires Google Cloud project/API key or OAuth; Jude approval required before creating credentials or connecting accounts. Quotas and API terms apply. Do not upload/post/update anything. | **Safe trial:** create a research table template only: keyword, query intent, video count sample, channel age, view/engagement notes, Suno feasibility, evidence URL, quota cost estimate. |
| **RSSHub** — https://github.com/DIYgod/RSSHub / https://docs.rsshub.app | **Open-source AGPL-3.0; self-hostable, Docker/npm options; public instances may have limits.** | **4/5** — route-based feeds are machine-readable; agents can poll RSS/Atom outputs later; strong fit with file-based monitoring. | **Tool Scout monitoring, JAM ops, Hive/CryptoCreep trend/source watch, AI tool release notes.** | Useful for turning public pages/platforms without native feeds into RSS so Tool Scout can monitor official docs/releases with less manual searching. Could pair with GitHub release feeds and saved Markdown source cards. | Self-host/Docker/npm install, scheduled polling, or account-required routes need approval. Respect site terms; avoid logged-in/private/account pages. AGPL matters if hosting/modifying. | **Safe trial:** define a public-source watchlist in Markdown: official docs, GitHub releases, pricing pages, and project-fit tags. No feed polling yet. |

## Best pick this week

**MarkItDown + Docling as a two-tier document mirror pipeline** is the best pick.

Why: Jude’s workspace relies on Markdown as the agent-readable source of truth, but Atlas/JAM/BBX/Story inputs often start as PDFs, Docs, Sheets, screenshots, audio/video notes, or exports. MarkItDown is the lightweight default; Docling is the heavier fallback for complex/scanned documents. Together they directly support the WAT rule: keep originals in human-facing systems, mirror important content into Markdown/JSON for agents, and never rely on hidden chat history.

Best no-risk next move: write a **pipeline spec only**, not an install:

```text
.tmp/tool-scout/document-mirror-pipeline-spec.md
```

Suggested sections: allowed source types, output folders, naming/date convention, private-data handling, when to use MarkItDown vs Docling, review checklist, and approval gates before any package install or private document conversion.

## Free/open-source alternatives

- **Pandoc** — excellent for DOCX/Markdown conversions and already noted in JAM docs; less broad than MarkItDown/Docling for OCR/scans/media.
- **Plain Python + PyMuPDF / python-docx / openpyxl** — best when Jude needs exact deterministic extraction from known formats; more custom work than MarkItDown.
- **SQLite + Python scripts without Datasette** — enough for small queue/report generation; Datasette becomes useful when agents need browsable/queryable JSON APIs.
- **Native GitHub release feeds / vendor RSS feeds** — use before RSSHub when official feeds already exist.
- **Manual YouTube browsing/export** — acceptable for one-off niche checks, but lower priority than an API/template workflow because it is hard for agents to repeat safely.

## Manual-only tools to avoid or defer

- **Manual document organizers with no Markdown/JSON export** — they may look tidy for humans but do not improve assistant handoffs.
- **YouTube trend dashboards that require account login/payment before export** — defer until the official YouTube Data API table design is clear.
- **OCR/scanner apps that upload private Atlas evidence by default** — avoid unless Jude explicitly approves the privacy model.
- **Public RSSHub routes for logged-in/private pages** — avoid; keep Tool Scout monitoring to public sources.

## Approval needed from Jude

Jude approval is needed before any of these actions:

- installing MarkItDown, Docling, Datasette, RSSHub, Pandoc extensions, Docker images, npm/Python packages, OCR/model dependencies, or browser extensions;
- running local servers, API servers, MCP servers, webhooks, scheduled pollers, or containers;
- creating Google Cloud projects, YouTube API keys/OAuth credentials, service accounts, or quota requests;
- connecting Google/Notion/GitHub/YouTube/Suno/Shopee/Facebook/CRM accounts;
- converting private Atlas evidence, BBX member data, call recordings/transcripts, Story manuscript files, or client documents with new tools;
- uploading private files to external services or publishing any generated data.

## Next safe action

Create a **Markdown-only document mirror pipeline spec** for Atlas + JAM AI Workspace:

```text
.tmp/tool-scout/document-mirror-pipeline-spec.md
```

No installs. No private-file conversion. The spec should decide how an agent would mirror future approved documents into Markdown/JSON, where outputs would live, and exactly what Jude must approve before live conversion.

## Sources checked

- MarkItDown GitHub metadata/README/package README: `https://github.com/microsoft/markitdown`, `https://raw.githubusercontent.com/microsoft/markitdown/main/README.md`, `https://raw.githubusercontent.com/microsoft/markitdown/main/packages/markitdown/README.md`
- Docling GitHub metadata/README/docs: `https://github.com/docling-project/docling`, `https://raw.githubusercontent.com/docling-project/docling/main/README.md`, `https://docling-project.github.io/docling/`
- Datasette GitHub metadata/README/JSON API docs: `https://github.com/simonw/datasette`, `https://datasette.io/`, `https://raw.githubusercontent.com/simonw/datasette/main/docs/json_api.rst`
- YouTube Data API official docs: `https://developers.google.com/youtube/v3/getting-started`, `https://developers.google.com/youtube/v3/determine_quota_cost`, `https://developers.google.com/youtube/registering_an_application`
- RSSHub GitHub metadata/README/docs: `https://github.com/DIYgod/RSSHub`, `https://raw.githubusercontent.com/DIYgod/RSSHub/master/README.md`, `https://docs.rsshub.app`
