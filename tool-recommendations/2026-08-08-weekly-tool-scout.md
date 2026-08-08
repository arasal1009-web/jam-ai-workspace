# Weekly Tool Scout Report — 2026-08-08

## Focus this week

1. **BBX + Atlas Capture call/meeting transcription pipeline** — BBX call outcomes and Atlas meetings/dispute notes are high-value inputs, but Jude’s safe pattern is still local/PC-first and approval-gated. This week prioritizes local/open-source speech-to-text tools that can produce files agents can review without uploading private audio.
2. **Job Market Digital / AI Agency website audit and QA pipeline** — JMD can benefit from repeatable site audits for prospective/local business clients: performance, SEO, accessibility, screenshots, broken states, and evidence-backed proposal notes. This week prioritizes CLI/scriptable browser tools rather than manual-only website graders.

Assumptions: no private audio, BBX exports, Atlas evidence, websites under login, Google/Notion/GitHub accounts, or client files were accessed. Research used public official/GitHub sources only. No software was installed; no accounts, APIs, browser extensions, webhooks, cron jobs, or workflows were created or changed.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **faster-whisper** — https://github.com/SYSTRAN/faster-whisper | **Open-source, MIT.** Free local Python library using CTranslate2. | **5/5** — Python API, local model loading, batch transcription patterns; can save Markdown/JSON/TXT artifacts for agents. | **BBX, Atlas Capture, JAM ops.** Best first candidate for local transcription of approved call/meeting recordings. | Faster local Whisper implementation; GitHub README describes CPU/GPU benchmarks, local model loading, PyAV audio decoding, Docker/CUDA notes, and related command-line clients. Strong fit for Jude’s current PC-local call recording → transcript → agent logging pattern. | Install/model download/GPU/CUDA setup needs approval. Do not process private calls/evidence until Jude approves exact folder, model, output path, and retention rule. Speaker labels are not built in by default. | **No-install trial:** draft a `call-transcript-artifact-schema.md` defining allowed input path, output Markdown fields, redaction notes, and how BBX/Atlas agents should consume transcripts. |
| **WhisperX** — https://github.com/m-bain/whisperX | **Open-source, BSD-2-Clause.** Free local Python package, with optional model/service dependencies. | **4/5** — command-line usage and Python examples; word-level timestamps and diarization workflow make structured notes easier for agents. | **Atlas meetings, BBX calls where speaker turns matter.** | Useful when raw transcript is not enough: word-level timestamps, forced alignment, and speaker diarization can make call summaries/evidence timelines easier to verify. | Heavier than faster-whisper. Diarization may require Pyannote/Hugging Face model access/token and acceptance of model terms; installation/model downloads require approval. Never upload private audio to sponsored/API services without approval. | **Safe trial:** compare as a *future tier* in the schema: use faster-whisper for basic transcript; use WhisperX only when Jude approves diarization/timestamps for a selected sample. |
| **Playwright** — https://github.com/microsoft/playwright | **Open-source, Apache-2.0.** Free framework for web testing/automation. | **5/5** — official README positions Playwright for web automation/testing, CLI, API, Python/.NET/Java support, traces/screenshots/videos, and MCP/agent use. | **Job Market Digital / AI Agency, BBX website checks, Atlas public-page evidence capture.** | Best browser automation base for evidence-backed website audits: screenshots, mobile/desktop checks, form-free page navigation, console/network errors, and reproducible client QA artifacts. Agents can operate it through scripts rather than manual browsing. | Installing browsers/packages or using logged-in/session pages requires approval. Must respect site terms, avoid private/account pages, and avoid submitting forms/messages. MCP/server mode is automation infrastructure and needs separate approval. | **No-install trial:** draft a fake-data audit checklist and JSON output shape for `website_audit_targets.csv → reports/*.md`; no browser run yet. |
| **Lighthouse CI** — https://github.com/GoogleChrome/lighthouse-ci | **Open-source, Apache-2.0.** Free CLI/CI tooling. | **5/5** — `@lhci/cli`, GitHub Actions examples, local/CI reports, assertions/budgets. | **JMD website audits, AI Agency proposals, JAM docs sites if created.** | Turns generic “your website is slow” into auditable metrics: performance, accessibility, SEO, offline/PWA support, best practices, budgets, and trend reports. Good proposal evidence for JMD if used on public client/prospect sites with care. | Installing Node packages/Chrome runners or setting CI requires approval. Metrics can vary by network/device; do not overpromise rankings or revenue impact. Avoid aggressive scanning. | **Safe trial:** create a proposal note template only: URL, Lighthouse categories, screenshot/evidence link, plain-English issue, low-risk fix, caveat. |
| **sitespeed.io** — https://github.com/sitespeedio/sitespeed.io | **Open-source, MIT.** README states it is free, open source, and data stays owned by the user; local browser-based tool. | **4/5** — CLI, Docker option, HTML reports, real-browser Core Web Vitals/visual metrics; outputs can be attached to agent reports. | **JMD website diagnostics and before/after evidence.** | Stronger than a single Lighthouse score when Jude needs richer performance evidence: repeated runs, Core Web Vitals, visual metrics, videos, browser matrix, HTML reports. Good “phase 2” after Playwright/Lighthouse basics. | Heavier setup: browser + Node/Docker + optional FFmpeg/Python for visual/video metrics. Install/Docker requires approval. Public/client site testing should be polite and scoped. | **Defer behind Lighthouse:** include it in the audit pipeline as an optional advanced report when a site needs deeper speed diagnostics. |

## Best pick this week

**Playwright + Lighthouse CI as a scriptable JMD website-audit starter pipeline** is the best pick.

Why: it helps Job Market Digital turn website-building opportunities into evidence-backed, repeatable reports without requiring Jude to manually inspect every site. It also supports BBX/JMD overlap safely: members with no website or weak public sites can be flagged internally for potential JMD opportunities, but no pitch or outreach should happen unless Jude explicitly approves that business-development context.

Best no-risk next move: create a Markdown-only spec for a future audit tool, not an install:

```text
.tmp/tool-scout/jmd-website-audit-pipeline-spec.md
```

Suggested contents: input CSV fields, allowed public-page scope, output Markdown template, screenshots/evidence filenames, Lighthouse score caveats, approval gates before running on real prospects, and “no form submission / no login / no messages” rules.

## Free/open-source alternatives

- **OpenAI Whisper** — MIT/open-source reference implementation and CLI/API shape; slower/heavier than faster-whisper for repeated local transcription, but still a useful baseline.
- **Plain Python + ffmpeg/PyAV + existing transcript scripts** — keep Jude’s current PC-local call workflow simple until a clear artifact schema exists.
- **Pagefind** — MIT/open-source static site search; useful later if JMD/JAM builds static documentation/client sites that need local search, but not the first audit need.
- **Cloudflare Wrangler / Workers SDK** — Apache-2.0 CLI for future low-cost deploy/API glue, but deployment/account connection belongs to a later approved JMD implementation phase.
- **Manual browser screenshots + a Markdown checklist** — acceptable for one-off review, but lower priority because it does not scale and is harder for agents to repeat.

## Manual-only tools to avoid or defer

- **Manual-only “AI website grader” SaaS with no export/API** — defer; it creates screenshots/scores Jude still has to copy by hand and may have unclear methodology.
- **Browser extensions that require logged-in browsing of CRM/member/client pages** — defer unless Jude approves PC-local use and exact data boundaries.
- **Hosted transcription services for private calls/evidence** — avoid until privacy, retention, pricing, and upload approval are reviewed.
- **Full website crawler/SEO suites before a target list exists** — avoid overwhelming Jude; start with a simple audit schema and 1–3 public test URLs after approval.

## Approval needed from Jude

Jude approval is needed before any of these actions:

- installing faster-whisper, WhisperX, OpenAI Whisper, Playwright, Lighthouse CI, sitespeed.io, browsers, Node/Python packages, ffmpeg, Docker images, CUDA/GPU dependencies, browser extensions, or models;
- downloading model weights or accepting Hugging Face/Pyannote model terms/tokens;
- processing private BBX calls, Atlas recordings/evidence, client files, or Story manuscripts with new tools;
- creating local servers, MCP servers, CI workflows, webhooks, cron jobs, containers, service accounts, or API keys;
- connecting Google/Notion/GitHub/CRM/Facebook/Shopee/YouTube/Suno/affiliate accounts;
- running website audits against non-public/logged-in pages, submitting forms, messaging prospects, or publishing reports externally.

## Next safe action

Create this report-only spec, with fake/example data only and no installation:

```text
.tmp/tool-scout/jmd-website-audit-pipeline-spec.md
```

If Jude approves later, the first live dry-run should use one public, non-login URL that Jude provides or approves, save outputs under `.tmp/website-audits/`, and make no external writes or contact.

## Sources checked

- faster-whisper GitHub metadata/README: `https://github.com/SYSTRAN/faster-whisper`, `https://raw.githubusercontent.com/SYSTRAN/faster-whisper/master/README.md`
- WhisperX GitHub metadata/README: `https://github.com/m-bain/whisperX`, `https://raw.githubusercontent.com/m-bain/whisperX/main/README.md`
- OpenAI Whisper GitHub metadata/README: `https://github.com/openai/whisper`, `https://raw.githubusercontent.com/openai/whisper/main/README.md`
- Playwright GitHub metadata/README: `https://github.com/microsoft/playwright`, `https://raw.githubusercontent.com/microsoft/playwright/main/README.md`
- Lighthouse CI GitHub metadata/README: `https://github.com/GoogleChrome/lighthouse-ci`, `https://raw.githubusercontent.com/GoogleChrome/lighthouse-ci/main/README.md`
- sitespeed.io GitHub metadata/README: `https://github.com/sitespeedio/sitespeed.io`, `https://raw.githubusercontent.com/sitespeedio/sitespeed.io/main/README.md`
- Additional OSS candidates checked but not top-ranked this week: Cloudflare Workers SDK/Wrangler, Astro, Pagefind.
