# Weekly Tool Scout Report — 2026-07-04

## Focus this week

1. **Atlas Capture + JAM AI Workspace document operations** — recent Atlas work added local Claude/Codex → GitHub → VPS/Hermes sync, so the highest-leverage tool category is local/document-to-Markdown and evidence organization that can feed agents without manual copy-paste.
2. **Hive affiliate + Story visual/video prep** — Jude needs AI-operable content production paths, not manual-only video editors. This week prioritizes scriptable video/storyboard pipelines that can turn agent-generated scripts/prompts into repeatable assets.

Assumptions: no new private files were uploaded and no accounts were connected. Research used public/official sources and GitHub metadata only.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Docling** | **Open-source / MIT**. GitHub repo `docling-project/docling`; PyPI currently reports version `2.109.0`. | **5/5** — Python SDK + CLI; converts PDFs, DOCX, PPTX, XLSX, HTML and more into structured representations/Markdown/JSON for downstream GenAI workflows. | **Atlas Capture, JAM AI Workspace, Story Writing references** | Best fit for converting documents into agent-readable Markdown without sending files to a cloud service. Useful for Atlas evidence docs, Drive exports, old Word docs, and source-of-truth mirrors. | Installation on PC/VPS requires Jude approval. OCR/complex layout accuracy still needs spot checks. Do not process sensitive documents through any non-local hosted path. | Draft a fake-data conversion test plan: one public/sample PDF → Markdown → agent summary, with no private Atlas files. |
| **paperless-ngx** | **Free/open-source / GPL-3.0**. GitHub repo `paperless-ngx/paperless-ngx`; active document-management/OCR project. | **4/5** — Docker-first deployment; official docs include a fully documented REST API and browsable schema at `/api/schema/view/`. | **Atlas Capture, JAM ops, BBX paperwork** | Strong candidate for evidence/document intake: scan, OCR, tag, archive, and retrieve documents. API makes it more agent-operable than a manual folder pile. | Requires installation/server storage planning and approval. Do not upload private documents to third-party hosting. Docker/container setup is approval-gated. | Create a folder/tag schema only, e.g. `Atlas > case > evidence type > date`, using synthetic filenames. |
| **Remotion** | **Free for individuals/small companies under its own license; not standard OSI open-source.** NPM `remotion` currently reports `4.0.484`; GitHub repo `remotion-dev/remotion`. | **5/5** — React/Node video generation; Node APIs, captions, templates, server-side rendering options. | **Hive affiliate videos, Story Writing trailers/storyboards, Job Market Digital promo clips** | Better than manual editors for Jude because agents can write scripts, scene JSON, captions, and templates, then render repeatable 20-second product videos or story mood reels. | License must be checked before commercial/for-profit scale. Installing Node packages/rendering videos needs approval. Product claims still need source verification. | Create a no-install storyboard JSON/template spec for one Hive 5-shot, 20-second video using placeholder assets only. |
| **Activepieces** | **Open-source core / MIT-style for non-EE parts**; GitHub repo `activepieces/activepieces`; docs describe it as an open-source Zapier replacement. | **4/5** — workflow automation, pieces/connectors, AI-agent/MCP positioning, self-host option. | **JAM AI Workspace ops, BBX/Notion/Sheets glue, Atlas handoffs** | Potential future glue layer when Jude wants workflows between GitHub, Notion, Google Sheets, Telegram, Drive, etc. More AI-operable than manual dashboard editing. | Account connections, self-hosting, webhooks, and automations are approval-gated. Cloud pricing/limits should be checked before any live setup. | Design one fake-data workflow on paper: `GitHub handoff file changed → create draft Notion task`, with every live connector marked “approval required.” |
| **FFmpeg + template files** | **Free/open-source multimedia toolchain**; GitHub mirror active. | **5/5** — CLI, batch processing, scriptable from Python/Node. | **Hive, Story Writing, BBX call/media utilities** | Not flashy, but extremely useful as the deterministic backend behind video resizing, caption burn-in, audio extraction, GIFs, and batch renders. Pairs well with Remotion or Python scripts. | Installation/use on Jude's PC still needs approval. It does not provide creative UI; agents must generate exact commands/templates. | Draft a command-template library only: `extract audio`, `resize vertical video`, `burn captions`, `make preview GIF` using placeholder paths. |

## Best pick this week

**Docling** is the best pick this week.

Why: Atlas Capture just gained a local assistant sync workflow, and JAM AI Workspace already depends on Markdown mirrors for agent-readable truth. Docling directly reduces manual document conversion friction while staying local-first and scriptable. It can also support Story Writing reference cleanup and Job Market Digital proposal/document intake later.

Best zero-risk next step: create a small `docling-evaluation-plan.md` using public sample files only. The plan should define expected outputs, quality checks, and where Markdown mirrors would live if Jude later approves installation.

## Free/open-source alternatives

- **Pandoc** — still the simplest DOCX/Markdown converter for clean documents. Less layout/OCR intelligence than Docling but very stable.
- **Marker / marker-pdf** — local PDF-to-Markdown option worth comparing if Docling struggles with a specific PDF type.
- **Tesseract OCR** — proven local OCR engine; more technical setup and less all-in-one than paperless-ngx.
- **n8n** — already noted in the previous Tool Scout run as a possible future workflow orchestrator; Activepieces is this week's alternate to compare because it markets itself around open-source automation and AI/MCP workflows.

## Manual-only tools to avoid or defer

- **Manual timeline/video editors as the default Hive pipeline** — defer unless they have script/template/export paths. Jude does not have time for manual edits.
- **Cloud-only document upload/OCR services for Atlas evidence** — avoid until Jude explicitly approves data handling, account connection, and privacy terms.
- **Browser-extension-heavy automation** — defer for BBX/Atlas unless it can run on Jude's PC-local authenticated profile with clear stop conditions.

## Approval needed from Jude

Before any live trial:

1. Install Docling, paperless-ngx, Remotion, Activepieces, FFmpeg, or dependencies.
2. Create Docker containers or self-host services.
3. Connect Google, Notion, GitHub, Telegram, affiliate, CRM, or Drive accounts.
4. Upload private Atlas/BBX/Story/Hive files to external services.
5. Render/publish/schedule affiliate videos or public content.
6. Enable webhooks, automations, or new cron jobs.

## Next safe action

**Recommended next safe action:** draft a local-first Docling evaluation plan using only public sample documents and fake Atlas metadata. No installation, account connection, private files, or workflow change required.

Suggested artifact:

```text
.tmp/tool-scout/2026-07-04-docling-evaluation-plan.md
```

If Jude approves later, the first real test should be one non-sensitive public/sample PDF converted to Markdown and checked for headings, tables, dates, and citation-friendly line references.

## Sources checked

- GitHub API: `docling-project/docling` — description, MIT license, active updates, topics.
- PyPI JSON: `docling` — current package summary/version and project URLs.
- GitHub raw README: `docling-project/docling` — confirms document parsing focus for GenAI workflows.
- GitHub API + raw docs: `paperless-ngx/paperless-ngx` — GPL-3.0, OCR/document-management topics, Docker guidance, REST API docs.
- GitHub API + NPM registry + raw license/README: `remotion-dev/remotion` / `remotion` — programmatic React video, Node APIs, license terms.
- GitHub API + raw README/license: `activepieces/activepieces` — open-source Zapier replacement positioning, automation/MCP/AI-agent topics, MIT/non-EE license wording.
- GitHub API: `FFmpeg/FFmpeg` — active multimedia CLI/toolchain repository.
