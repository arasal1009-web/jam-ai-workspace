# Weekly Tool Scout Report — 2026-07-18

## Focus this week

1. **Hive / CryptoCreep / Music Production short-form content systems** — Jude has draft-only Hive/CryptoCreep content work and a new Music Production project. The best leverage is not another manual video editor; it is a batch/scriptable video workflow that agents can help prepare.
2. **JAM AI Workspace + BBX/Atlas workflow glue** — recent handoffs keep pointing to GitHub/Markdown/Notion/Sheets coordination. Tools should help connect existing files and services safely, with approval gates before external writes.

Assumption: focus rotated toward recent July momentum: CryptoCreep revival, Atlas assistant sync, Music Production setup, and weekly Tool Scout itself. No private accounts or project files were accessed.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Remotion** — https://github.com/remotion-dev/remotion / https://www.remotion.dev | **Free license for individuals, non-profits, and small for-profit orgs up to 3 employees; company license needed above that. Source-available.** | **5/5** — React/code source of truth, CLI/project files, batch rendering, documented “agentic” video creation. | Hive affiliate videos, CryptoCreep reels, Music Production visualizers, future Story trailers. | Turns repeated short-form formats into templates agents can edit: captions, overlays, product fact cards, waveform/visualizer scenes, 5-shot affiliate scripts. Better fit than manual-only editors because videos become code + reusable templates. | Installing Node/packages or rendering videos on Jude’s machine/VPS needs approval. Need care around copyright/trademarks, affiliate claims, and no unverified product facts. | **Zero-write trial:** draft one `Remotion template spec` in Markdown for a 20-second Hive affiliate video: 5 shots × 4 seconds, inputs as JSON, no install/render yet. |
| **n8n** — https://github.com/n8n-io/n8n / https://n8n.io | **Self-hostable fair-code; cloud plans available. Not OSI-open-source because n8n uses Sustainable Use License for main code.** | **5/5** — API/integrations, webhooks, JavaScript/Python, AI workflow support, human-approval steps, 1500+ integrations claimed in README. | JAM AI Workspace ops, BBX task creation, Atlas meeting-to-task routing, Tool Scout feeds, Notion/GitHub/Google Sheets glue. | Good candidate for *future* approval-gated workflows where Hermes/agents draft decisions and n8n performs deterministic integration steps. Human approval nodes fit Jude’s external-write gates. | Do **not** connect Google/Notion/GitHub, create webhooks, or enable automations without explicit approval. Self-hosting/container setup also needs approval. | **Safe trial:** design one read-only workflow diagram in Markdown: “GitHub handoff changed → summarize → draft Notion task queue,” with all write nodes disabled/pending approval. |
| **Crawlee** — https://github.com/apify/crawlee | **Open-source Apache-2.0. Free local library; Apify cloud is optional/paid-freemium.** | **4/5** — Node/Python libraries, CLI starter, Playwright/Puppeteer/Cheerio support, stores datasets to disk/cloud. | BBX/JMD website checks, Tool Scout source monitoring, Hive public product/page research when allowed, Atlas public evidence organization. | Useful for repeatable public-web checks: member websites missing/unreachable, directory QA, official tool-page monitoring, public page metadata. Can save JSON/CSV/Markdown for agents to review. | Scraping must respect site terms/robots, avoid logged-in/private pages, and avoid affiliate/account data. Installing packages requires approval. | **Safe trial:** create a target/source list only: 10 public URLs to monitor for Tool Scout or BBX website-health checks; no crawler run yet. |
| **Obsidian Web Clipper** — https://github.com/obsidianmd/obsidian-clipper / https://help.obsidian.md/web-clipper | **Free browser extension; GitHub repo is MIT.** | **3/5** — manual browser capture, but outputs durable Markdown and supports templates/variables/filters per docs. | Story Writing research, Tool Scout evidence capture, Atlas documentation, JAM OS knowledge base. | Good for turning official pages/research into Markdown that assistants can diff/search. Less automatable than CLI/API tools, but output format matches WAT. | Browser extension installation and any browser/account usage needs Jude approval. Capturing private/account pages should be avoided unless explicitly approved. | **Safe trial:** no install; define a clipping template in Markdown for “Tool Scout source card” with fields: source URL, pricing evidence, automation notes, risk, project fit. |
| **Creatomate / Shotstack API video platforms** — https://creatomate.com/docs/api/introduction and https://shotstack.io/docs/api/ | **Likely paid/freemium/API SaaS; pricing pages exist but exact free limits were not reliably extracted in this run, so treat as approval-gated paid candidates.** | **5/5** — API-first video generation, templates, SDK/API docs. | Hive affiliate videos, CryptoCreep reels, music visual snippets. | Strong if Jude wants hosted API rendering instead of maintaining local video rendering. More “agent-operable” than CapCut-style manual editing. | Needs account/API key/payment review before use. Uploading assets/product media to third-party SaaS needs approval. Verify pricing/free limits first. | **Defer:** compare only after a Remotion template spec exists; then decide whether hosted API rendering is worth the account/cost/privacy tradeoff. |

## Best pick this week

**Remotion** is the best immediate pick because it matches Jude’s “no time for manual edits” preference while staying draft-first. It can turn Hive affiliate scripts, CryptoCreep education reels, and Music Production playlist visuals into reusable code templates that agents can populate from Markdown/JSON. The safest next move is not installation: create one detailed template spec first, then Jude can approve whether to install/render later.

## Free/open-source alternatives

- **Crawlee** — best open-source option for public-web research and monitoring workflows; useful before considering Apify cloud.
- **Obsidian Web Clipper** — best Markdown capture path if Jude wants human-friendly source cards, but it is more manual and requires extension approval.
- **Plain Python + ffmpeg/MoviePy/Manim** — likely useful for later local video automation, but not researched deeply this week because Remotion is currently more aligned with agentic short-form templates.
- **n8n self-host** — useful low-cost/fair-code workflow glue, but not fully open-source and should wait for explicit automation approval.

## Manual-only tools to avoid or defer

- **CapCut-only workflows**: useful editor, but defer as the primary system unless there is an export/template/API path Jude actually wants. Manual timeline editing does not fit the weekly Tool Scout preference.
- **Canva-only workflows**: useful for assets, but lower priority unless paired with templates/export/import and a clear agent handoff.
- **Hosted API video tools before pricing/account review**: Creatomate/Shotstack are promising, but should not be used until pricing, free limits, privacy, asset upload rules, and API-key handling are reviewed.

## Approval needed from Jude

Before taking the next implementation step, Jude would need to approve any of the following:

- installing Node/npm packages, Remotion, Crawlee, browser extensions, or video tooling;
- creating n8n containers, webhooks, credentials, or workflows;
- connecting Google, Notion, GitHub, Facebook, Shopee, affiliate, YouTube, or Suno accounts;
- entering API keys or payment details;
- uploading private project files, product screenshots, media assets, or account data to external SaaS;
- rendering/publishing/scheduling any content.

## Next safe action

Create a **Markdown-only Remotion template spec** for one Hive/CryptoCreep short-form video format:

```text
.tmp/tool-scout/remotion-template-spec-hive-20s.md
```

It should define the input JSON fields, 5 shots × 4 seconds, overlay rules, affiliate/compliance caveats, and export targets. No software install or rendering needed until Jude approves.

## Sources checked

- Remotion README and license: `https://github.com/remotion-dev/remotion`, `https://raw.githubusercontent.com/remotion-dev/remotion/main/LICENSE.md`
- n8n README and license: `https://github.com/n8n-io/n8n`, `https://raw.githubusercontent.com/n8n-io/n8n/master/LICENSE.md`
- Crawlee README/GitHub metadata: `https://github.com/apify/crawlee`
- Obsidian Web Clipper README/help: `https://github.com/obsidianmd/obsidian-clipper`, `https://help.obsidian.md/web-clipper`
- Creatomate API docs/pricing page shell: `https://creatomate.com/docs/api/introduction`, `https://creatomate.com/pricing`
- Shotstack API docs/pricing page shell: `https://shotstack.io/docs/api/`, `https://shotstack.io/pricing/`
