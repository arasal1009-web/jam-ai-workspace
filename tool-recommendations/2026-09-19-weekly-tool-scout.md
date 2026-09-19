# Weekly Tool Scout Report — 2026-09-19

## Focus this week

**Focus areas:**

1. **Job Market Digital / AI Agency — agent-operable website factory + QA.** The project registry says Job Market Digital is Jude’s website-building business. This week prioritizes a repeatable static-site/docs stack where agents can prepare Markdown/content, generate pages, and run QA reports before Jude or a human publishes anything.
2. **JAM AI Workspace operations — searchable source-of-truth/docs.** The same tools can also turn WAT workflows, agent specs, and client-facing documentation into fast searchable sites later, while keeping GitHub Markdown as the source of truth.

**Boundary followed:** no software/packages/models were installed, no accounts/API keys were created, no private files were uploaded, no Google/Notion/GitHub/social/client integrations were connected, no workflows were changed as final, and no automation/cron/container was created.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Astro** | **Free / open-source package; npm latest checked as `7.3.3`, MIT license shown in npm metadata.** GitHub API checked 2026-09-19. | **5/5** — file-based static/site framework; Markdown/MDX content; agent-editable templates/components; CLI/build workflows. | **Job Market Digital / AI Agency**, JAM docs, lightweight client sites. | Strong base for a repeatable “website starter” that agents can populate from Markdown: service pages, local business pages, landing pages, blogs, and documentation without manual page-builder work. | Installing Node packages or creating a live client site requires Jude approval. Commercial/client use should keep dependencies/licensing reviewed per project. | **No-install next step:** draft one Markdown-only JMD starter site map: Home, Services, Portfolio, Contact, FAQ, Local SEO page, and `content/pages/*.md` schema. |
| **Astro Starlight** | **Free / open-source; npm latest checked as `0.42.2`, MIT license.** GitHub API checked 2026-09-19. | **5/5** — docs-as-files; Markdown/MDX; sidebar/nav config; easy for agents to maintain. | **JAM AI Workspace docs**, AI Agency client onboarding docs, Atlas/BBX internal SOP mirrors. | Best fit for turning WAT workflows and role-agent docs into a searchable assistant/human handbook later. Keeps durable Markdown in GitHub instead of hidden chat memory. | Installation/build/publishing needs approval. Avoid exposing private/internal docs publicly unless Jude explicitly approves. | **No-install next step:** choose one private doc-site outline only: `JAM Handbook`, `Client Website SOP`, or `BBX Internal SOP`; no build yet. |
| **Pagefind** | **Free / open-source; GitHub license MIT; npm latest checked as `1.5.2`.** | **5/5** — static search index generated from built files; CLI; no hosted search account required. | **JAM docs**, client static sites, Story/Atlas doc mirrors if ever exported privately. | Adds fast search to static docs/sites without Algolia-style account setup. Good for “Jude cannot scroll forever” use cases: searchable SOPs, workflows, agent specs, client docs, and project handoffs. | Installing/running indexing requires approval. Do not publish private indexed content unless explicitly approved. | **No-install next step:** add a paper-only search requirement to future site specs: search indexes must exclude secrets, `.tmp/`, archives, and private client data. |
| **Lighthouse CI** | **Free / open-source; GitHub license Apache-2.0; npm `@lhci/cli` latest checked as `0.15.1`.** | **5/5** — CLI/CI friendly; emits reports; can gate performance/accessibility/SEO regressions. | **Job Market Digital / AI Agency**, public website QA, client delivery checklists. | Lets agents generate a pre-delivery website QA report: performance, accessibility, best practices, SEO, and regression tracking before Jude sends a site to a client. | Running against private/client staging URLs needs approval and access boundaries. Do not connect CI/GitHub checks without approval. | **No-install next step:** create a Markdown-only JMD “website QA report” template with Lighthouse categories, manual checks, screenshots needed, and pass/fix/follow-up fields. |
| **Decap CMS** | **Free / open-source; GitHub license MIT; npm `decap-cms` latest checked as `3.16.2`.** | **4/5** — Git-based CMS for static sites; content stored in repo; agents can still edit files directly. | **AI Agency client sites**, low-maintenance client content editing. | Useful later if a client needs simple browser-based content editing while the actual site remains Git-backed. Keeps content as files rather than locking it inside a page builder. | Requires setup, auth/provider configuration, and likely GitHub/Netlify/Git backend decisions. Approval needed before client use or connecting accounts. | **Defer until client need:** first build the Markdown schema manually; add Decap only when a real client needs non-technical editing. |

## Best pick this week

**Best pick: Astro + Lighthouse CI as the first JMD website-factory spine.**

Reason: this pair fits Jude’s “AI-operable, not manual-edit-heavy” preference. Agents can draft content as Markdown and templates, while Lighthouse CI provides a repeatable QA report before any client handoff. Pagefind and Starlight are strong add-ons when the priority is searchable docs/knowledge bases rather than marketing sites.

Practical future shape, pending approval before any install/run:

```text
Client/project brief
  → agent drafts Markdown pages + metadata schema
  → Astro template builds static site locally
  → Lighthouse CI generates QA report
  → Pagefind adds private/public search where appropriate
  → Jude approves before publishing, connecting domains, or sending to clients
```

## Free/open-source alternatives

- **Sitespeed.io** — free/open-source MIT; GitHub API checked 2026-09-19 and npm latest checked as `42.7.0`. More comprehensive real-browser performance monitoring than Lighthouse CI, but heavier for Jude’s first website QA pass.
- **Plain HTML/CSS templates in the JAM repo** — safest first step if Jude wants zero package installs; agents can still produce a reusable client-site structure.
- **Existing GitHub Markdown + README navigation** — keep this as default for internal source-of-truth until a doc site is approved.
- **Playwright** — already recommended in earlier Tool Scout reports; still useful for screenshots and public site smoke tests, but not repeated as a top pick this week because the immediate gap is website factory + QA structure.

## Manual-only tools to avoid or defer

- Manual page builders as the default JMD workflow if they require Jude to drag/drop every section and cannot export clean source files.
- Hosted search products that require account setup/API keys before Pagefind-style static search is tested.
- Heavy performance-monitoring dashboards before a simple Lighthouse CI report template exists.
- Client CMS setup before a real client editing need exists; Decap is useful later, not step one.

## Approval needed from Jude

Jude approval is needed before:

- installing Astro, Starlight, Pagefind, Lighthouse CI, Decap CMS, Sitespeed.io, Node/npm packages, browser binaries, plugins, or templates;
- creating or changing real websites, client repos, GitHub Actions, CI checks, hosting, domains, DNS, forms, analytics, or search indexes;
- connecting GitHub/Netlify/Vercel/Cloudflare/Google/Notion/client accounts or entering API keys;
- publishing sites/docs, sharing client deliverables, uploading private files, or exposing internal JAM/BBX/Atlas/Story docs;
- creating cron jobs, Docker containers, webhooks, or autonomous website-builder agents.

## Next safe action

**Safest next action with no install and no external writes:** create a Markdown-only **Job Market Digital Website Starter Spec**:

1. target folder structure for a future Astro site;
2. page/content schema (`title`, `description`, `service`, `location`, `CTA`, `proof`, `FAQ`);
3. reusable sections agents can populate;
4. QA report checklist based on Lighthouse categories;
5. publishing/hosting steps marked as approval-gated.

## Sources checked

- Local JAM AI Workspace docs and handoffs: `AGENTS.md`, `agents/README.md`, `agents/tool-scout/AGENT.md`, `workflows/tool-scout-recommendations.md`, `PROJECTS.md`, central `HANDOFF.md`, and recent BBX/Hive/Story/Atlas handoffs.
- Prior durable Tool Scout report checked: `tool-recommendations/2026-09-12-weekly-tool-scout.md` to avoid repeating the same Music/Story focus.
- GitHub API snapshots checked 2026-09-19 for: `withastro/astro`, `withastro/starlight`, `cloudcannon/pagefind`, `GoogleChrome/lighthouse-ci`, `decaporg/decap-cms`, `sitespeedio/sitespeed.io`, plus repeat-reference checks for `microsoft/playwright` and `remotion-dev/remotion`.
- npm registry metadata checked 2026-09-19 for: `astro`, `@astrojs/starlight`, `pagefind`, `@lhci/cli`, `decap-cms`, `decap-cms-app`, and `sitespeed.io`.
