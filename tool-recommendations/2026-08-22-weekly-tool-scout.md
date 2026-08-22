# Weekly Tool Scout Report — 2026-08-22

## Focus this week

**Focus areas:**

1. **AI-operable web/product/lead research for Hive affiliate, CryptoCreep/Hive education, BBX/JMD lead checks, and JAM AI Workspace research.** Recent handoffs point to Shopee/product research friction, CryptoCreep content revival, BBX member website checks, and JMD website-lead opportunities.
2. **Programmatic short-form content production foundations for Hive/CryptoCreep.** Jude does not have time for manual editors, so code/template-driven video beats manual-only timelines.

**Assumption:** no live accounts/API keys should be connected by this cron. Recommendations below are for review and safe dry-run planning only.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Crawl4AI** — https://docs.crawl4ai.com/ / https://github.com/unclecode/crawl4ai | **Open-source**; GitHub reports Apache-2.0 license. | **5/5** — Python/scriptable, CLI/docs for crawling, Markdown generation, page interaction, extraction strategies, local files/raw HTML, multi-URL crawling. | Hive product research, CryptoCreep education-source capture, JMD prospect website audits, BBX public website checks. | Best free-first fit for turning public pages into agent-readable Markdown/structured context without sending private files to a SaaS. Strong WAT fit: deterministic script first, LLM summary second. | Installing packages on VPS/PC still needs approval. Crawling must respect site terms/robots and avoid logged-in/private pages. | **No-install planning trial:** pick 5 public URLs from Hive/JMD/BBX and draft the desired CSV/Markdown schema. After approval, run only on public pages in a venv. |
| **Firecrawl** — https://www.firecrawl.dev/pricing / https://github.com/mendableai/firecrawl | **Freemium + open-source.** Pricing page showed Free Plan at **$0/month**, **1,000 pages**, 2 concurrent requests; GitHub reports AGPL-3.0. | **5/5** — API-oriented web scrape/search/extract; built for agent context. | Same as Crawl4AI, especially when a hosted API is easier than maintaining a crawler. | Fast path for converting messy pages into clean Markdown/JSON for agents. Useful for Hive product-page capture when pages are publicly accessible; also JMD lead audits. | Cloud use requires signup/API key and may send page data to Firecrawl; approval needed before account/API use. Self-hosting is heavier and also approval-gated. | Use docs/pricing only for now. If Jude approves later, test free plan on 3 non-private public URLs and compare output vs Crawl4AI. |
| **n8n Community Edition / n8n Cloud** — https://n8n.io/pricing/ / https://github.com/n8n-io/n8n | **Self-host Community Edition available on GitHub; Cloud is paid.** Pricing page showed Starter at 20€/mo annually and notes a standard self-hosted Community Edition. | **5/5** — API/CLI, webhooks/queues, JS/Python code steps, cURL import, HTTP/GraphQL, 400+ integrations per GitHub description. | JAM AI Workspace ops, BBX Notion/Sheets/GitHub glue, recurring research queues, controlled handoffs. | Best workflow glue candidate once Jude wants agent-readable automation beyond cron prompts. Could connect GitHub → Notion/Sheets → Telegram/Drive with explicit gates. | Do **not** install, self-host, connect accounts, or create webhooks without approval. Self-host introduces credentials/secrets management. | Safe trial now: design one paper workflow only — “Tool Scout candidate URL list → Markdown report → Notion draft task,” with all credentials marked as placeholders. |
| **Remotion** — https://www.remotion.dev/docs/ / https://github.com/remotion-dev/remotion | **Free for local evaluation; commercial licensing should be checked before business use.** | **4/5** — videos are code/templates; docs explicitly provide coding-agent prompts and local render workflow. | Hive affiliate videos, CryptoCreep reels, Music/visualizer experiments, Story adaptation pitch animatics. | Better than manual timeline editors for Jude: agents can generate reusable React templates for 5-shot affiliate videos, caption cards, Hive explainers, or audio visualizers. | Requires Node install and local rendering setup; publishing/uploading remains separate approval. Commercial/license fit needs review before client/monetized use. | Safe trial: draft a **template spec only** for a 20-second Hive affiliate reel: 5 shots × 4 sec, variables from CSV, no install/render yet. |
| **Playwright** — https://playwright.dev / https://github.com/microsoft/playwright | **Open-source**; GitHub reports Apache-2.0 license. | **4/5** — scriptable browser automation across Chromium/Firefox/WebKit. | BBX/Atlas PC-local browser simulations, JMD public website QA, screenshots, non-login page checks. | Useful when simple scraping fails or screenshots/browser QA are needed. Safer than SaaS browser agents for private workflows because it can run PC-local under Jude’s control. | Installation and any logged-in browser automation need approval. Real CRM/Facebook/Shopee account actions remain approval-gated and should usually be PC-local. | Safe trial: write a dry-run checklist for 3 public JMD prospect websites: load page, capture title/meta, screenshot, broken-link count. No login, no forms. |

## Best pick this week

**Crawl4AI** is the best first pick because it is free/open-source, local-first, and directly addresses multiple current pain points:

- Hive/Shopee-style product research needs agent-readable page facts without inventing blocked details.
- CryptoCreep/Hive education content needs source capture and summarization from public docs/articles.
- JMD can use public website checks to identify missing/no-website leads from BBX-style data.
- It fits WAT: a deterministic crawler produces Markdown/JSON; agents then summarize, score, and draft.

Suggested first real experiment after Jude approval: create a tiny `tools/public_page_context_probe.py` in a venv that accepts a CSV of public URLs and writes `.tmp/tool-scout/page-context/*.md` — no private pages, no logins, no external account connection.

## Free/open-source alternatives

- **Crawl4AI** — strongest free/local-first crawler for LLM-ready Markdown and extraction.
- **Playwright** — best free browser automation foundation for public-page QA and PC-local browser dry-runs.
- **n8n Community Edition** — free/self-host workflow glue, but setup/secrets burden is higher.
- **Firecrawl self-host** — open-source AGPL option if hosted API is not acceptable, but operationally heavier than Crawl4AI.
- **Remotion** — code-first video generation; verify commercial terms before monetized/client use.

## Manual-only tools to avoid or defer

- **CapCut / Canva manual editing as the main workflow:** useful for human polish, but lower priority because Jude lacks time for manual edits. Consider only if agents prepare templates/scripts/assets first.
- **Closed “AI video generator” subscriptions without API/batch export:** defer unless they provide reliable API/templates and do not require paid credits for basic tests.
- **Browser cloud agents for logged-in CRM/Facebook/Shopee work:** defer. BBX and social account operations should stay approval-gated and usually PC-local to avoid session/logout/account risks.

## Approval needed from Jude

Approval is needed before any of these:

- installing Crawl4AI, Playwright, Remotion, n8n, browser extensions, packages, or models;
- signing up for Firecrawl/n8n/browser services or entering API keys;
- connecting Notion, Google, GitHub, Facebook, Shopee, affiliate, CRM, or Drive accounts;
- crawling logged-in/private pages or uploading private project files to third-party services;
- generating/publishing/scheduling videos or posts;
- creating webhooks, new cron jobs, Docker containers, or autonomous agents.

## Next safe action

**Safest next action:** Jude can approve a read-only, no-account, no-install planning task: create a candidate URL list and schema for a future Crawl4AI/Playwright public-page probe.

Proposed micro-scope for that future task:

1. 2 public Hive/Web3 education URLs.
2. 2 public JMD/BBX prospect websites or no-website examples from already available data.
3. 1 public affiliate/product information page that is not login-blocked.
4. Output only Markdown/CSV under `.tmp/tool-scout/`; no external writes.

## Sources checked

- Local JAM AI Workspace docs: `AGENTS.md`, `agents/README.md`, `agents/tool-scout/AGENT.md`, `workflows/tool-scout-recommendations.md`, `PROJECTS.md`, and recent project handoffs for Hive, Story Writing, BBX, Atlas.
- GitHub API snapshots on 2026-08-22 for `n8n-io/n8n`, `mendableai/firecrawl`, `unclecode/crawl4ai`, `microsoft/playwright`, `remotion-dev/remotion`, `browserless/browserless`, and `browserbase/mcp-server-browserbase`.
- Official pages/docs checked in browser: n8n pricing, Firecrawl pricing, Crawl4AI docs, Remotion docs/license pages.
