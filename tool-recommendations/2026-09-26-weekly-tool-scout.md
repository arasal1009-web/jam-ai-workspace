# Weekly Tool Scout Report — 2026-09-26

## Focus this week

**Focus areas:**

1. **Atlas Capture + JAM AI Workspace — local document-to-Markdown/evidence ingestion.** Atlas needs clean evidence, docs, and meeting/action artifacts; JAM needs assistant-readable mirrors that stay in GitHub/Markdown instead of hidden chat context.
2. **Story Writing / BBX support — searchable OCR + document mirrors.** The same local-first tools can later help with scanned PDFs, Word docs, exported CRM/documentation files, and manuscript/reference mirrors without uploading private files by default.

**Why this focus:** recent reports covered JMD website factory, Music/Story style/audio tools, BBX/Atlas transcription, and cross-project browser/research automation. The remaining cross-project bottleneck is converting messy PDFs/DOCX/images/scans into Markdown/text/structured files that agents can cite, diff, and summarize.

**Boundary followed:** no software/packages/models were installed, no accounts/API keys were created, no private files were uploaded, no Google/Notion/GitHub/social/client integrations were connected, no workflows were changed as final, and no automation/cron/container was created.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Docling** | **Free / open-source; MIT.** GitHub API checked 2026-09-26: `docling-project/docling`, 67,960 stars, updated 2026-09-25. PyPI checked: `docling 2.130.0`, MIT. | **5/5** — Python SDK + CLI style workflow; converts PDF/DOCX/HTML and more into unified document representations suitable for GenAI workflows. | **Atlas Capture**, JAM docs, Story reference files, AI Agency client docs. | Best first candidate for local document-to-Markdown/JSON extraction where agents need reliable structure before summarizing. Strong fit for Atlas evidence packs and JAM documentation mirrors. | Installing/running on PC/VPS needs approval. OCR/table extraction quality must be checked on a few non-sensitive samples first. Do not upload private documents to hosted services. | **No-install next step:** draft an Atlas/JAM document-ingestion test list: 1 public PDF, 1 harmless DOCX, 1 scanned sample, with expected Markdown/JSON output fields. |
| **Microsoft MarkItDown** | **Free / open-source; MIT.** GitHub API checked 2026-09-26: `microsoft/markitdown`, 187,044 stars, updated 2026-09-26. PyPI checked: `markitdown 0.1.8`, MIT. | **5/5** — lightweight Python utility for converting files/Office docs to Markdown; output is directly agent-readable. | **JAM AI Workspace**, Story Writing, Atlas, AI Agency. | Strongest simple “convert this file to Markdown for LLM/repo use” option. Good for quick DOCX/PDF/PowerPoint/Excel-ish source mirrors before more complex extraction is needed. | README warns it performs I/O with current process privileges; inputs/paths must be sanitized. Installing/running needs approval. OCR/audio features may need extra dependencies or careful privacy handling. | **Safe trial after approval:** run only on a public/sample file and compare Markdown readability against manual copy/paste; do not use private files first. |
| **OCRmyPDF** | **Free / open-source; MPL-2.0.** GitHub API checked 2026-09-26: `ocrmypdf/OCRmyPDF`, 34,876 stars, updated 2026-09-25. PyPI checked: `ocrmypdf 17.12.1`, MPL-2.0. | **5/5** — scriptable command-line program; adds searchable/copyable OCR text layer to scanned PDFs. | **Atlas Capture**, BBX/CRM exports, JAM archive hygiene. | Best focused tool when the blocker is a scanned PDF that agents cannot search. It can make scanned evidence/searchable PDFs ready for Docling/MarkItDown or manual review. | Installing system dependencies/Tesseract/ghostscript may be needed; approval required. OCR can introduce errors, so outputs must be cited as OCR-derived and verified before legal/dispute use. | **No-install next step:** define a scanned-PDF handling rule: keep original PDF untouched, create OCR copy, then create Markdown extraction + human-verification notes. |
| **Unstructured** | **Free / open-source core; Apache-2.0.** GitHub API checked 2026-09-26: `Unstructured-IO/unstructured`, 15,493 stars, updated 2026-09-25. PyPI checked: `unstructured 0.27.8`, Apache-2.0. | **4/5** — Python document ETL; README also describes Transform MCP for agents, but account/auth may apply. | **JAM AI Workspace ops**, Atlas, AI Agency research/content pipelines. | Useful when documents need chunking/partitioning into structured elements for RAG/search/agent workflows. Good phase-2 candidate after Docling/MarkItDown prove the file-mirror need. | Production/platform/MCP paths may require account/auth and must not touch private files without approval. More complex dependency surface than MarkItDown. | **Defer/test later:** keep as phase-2 if Docling/MarkItDown output is not structured enough for Atlas evidence or JAM search. |
| **Paperless-ngx** | **Free / open-source; GPL-3.0.** GitHub API checked 2026-09-26: `paperless-ngx/paperless-ngx`, 46,018 stars, updated 2026-09-26. | **3/5** — searchable document management system; Docker-first deployment; supports archive/search workflows, but heavier than a converter. | **Atlas Capture**, personal/admin document archive, maybe BBX/AI Agency docs later. | Strong long-term option if Jude wants a searchable private document archive instead of scattered folders. Less ideal as a first step because it is a whole app/deployment, not just a WAT helper. | Requires Docker/server setup, document import decisions, storage/privacy/security planning, and explicit approval. Do **not** create containers or upload/import private documents from this cron. | **Defer:** only consider after a local converter/OCR pipeline is proven and Jude explicitly wants a document-management app. |

## Best pick this week

**Best pick: Docling + OCRmyPDF as the future Atlas/JAM document-ingestion spine, with MarkItDown as the lightweight fallback.**

Reason: this combination matches Jude’s WAT pattern and current bottleneck: agents need clean, searchable, citeable text/Markdown from real-world documents before they can safely summarize or create action queues. OCRmyPDF handles scanned PDFs; Docling handles richer parsing; MarkItDown is the quick Markdown mirror tool.

Practical future shape, pending approval before any install/run:

```text
Original document folder (read-only originals)
  → OCRmyPDF only if scanned/image PDF
  → Docling or MarkItDown extraction
  → Markdown + JSON/text mirror under documentation/markdown/ or .tmp/document-ingestion/
  → agent summary with source filename/page/section notes
  → Jude approval before Notion/AppSheet/Drive/client/legal updates
```

## Free/open-source alternatives

- **MarkItDown alone** — simplest first Markdown conversion route if Jude wants minimal setup and the docs are mostly Office/PDF files.
- **OCRmyPDF alone** — best first step for scanned PDFs where text selection/search does not work.
- **Unstructured** — stronger for production document ETL/chunking later, but heavier than needed for the first safe test.
- **Manual Pandoc DOCX → Markdown** — already known and useful for Word docs, but narrower than Docling/MarkItDown for mixed file types.
- **Existing repo mirror pattern** — keep originals in Drive/project originals, commit Markdown mirrors, and record mismatches in `HANDOFF.md`.

## Manual-only tools to avoid or defer

- Manual PDF copy/paste as the default Atlas evidence workflow; too error-prone and not repeatable.
- Cloud-only OCR/document AI services before a local-first baseline is tested.
- Whole document-management apps such as Paperless-ngx before the folder/mirror convention and security boundary are clear.
- Any tool that requires uploading Atlas/BBX/client/private documents before Jude approves the specific file and service.

## Approval needed from Jude

Jude approval is needed before:

- installing Docling, MarkItDown, OCRmyPDF, Unstructured, Paperless-ngx, Tesseract/Ghostscript, Python packages, Docker images, plugins, or desktop apps;
- processing private Atlas/BBX/Story/client/customer files with new tools;
- uploading documents to hosted OCR/document-processing services;
- connecting Google Drive, Notion, GitHub, AppSheet, CRM, or client accounts;
- writing extracted document data into Notion, Google Sheets, AppSheet, CRM, Drive, emails, or messages;
- creating cron jobs, Docker containers, webhooks, or autonomous document-processing agents.

## Next safe action

**Safest next action with no install and no external writes:** create a Markdown-only **Atlas/JAM Document Ingestion Test Plan**:

1. define input folders: `documentation/originals/`, `.tmp/document-ingestion/input-samples/`, `.tmp/document-ingestion/output/`;
2. define output types: OCR PDF copy, Markdown mirror, JSON/text extraction, source-citation notes;
3. choose only public/non-sensitive sample files for the first approval-based test;
4. require originals to remain untouched;
5. add verification fields: text searchable?, headings preserved?, tables readable?, OCR errors?, human review needed?, safe for repo?

## Sources checked

- Local JAM AI Workspace docs and handoffs: `AGENTS.md`, `agents/README.md`, `agents/tool-scout/AGENT.md`, `workflows/tool-scout-recommendations.md`, `PROJECTS.md`, central `HANDOFF.md`, plus recent Hive/Story/Atlas/BBX handoffs and recent durable Tool Scout reports to avoid repeating the same focus.
- GitHub API metadata checked 2026-09-26 for: `docling-project/docling`, `microsoft/markitdown`, `Unstructured-IO/unstructured`, `ocrmypdf/OCRmyPDF`, and `paperless-ngx/paperless-ngx`.
- PyPI JSON checked 2026-09-26 for: `docling`, `markitdown`, `unstructured`, and `ocrmypdf`.
- Official GitHub README/raw sources checked 2026-09-26 for the same projects to confirm positioning such as Markdown conversion, OCR/searchable PDFs, document ETL, and Docker-heavy document management.
