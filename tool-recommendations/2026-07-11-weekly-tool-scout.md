# Weekly Tool Scout Report — 2026-07-11

## Focus this week

1. **Hive / CryptoCreep Facebook + Hive/Web3 revival** — recent handoff added a draft-only relaunch system and needs safe tools for content queues, source-backed Hive education posts, and eventual review/scheduling without posting yet.
2. **Music Production / Suno + YouTube workflow** — recent setup needs evidence-gathering and playlist/package planning without spending Suno credits, uploading, or connecting YouTube/Suno accounts.

Assumption: this week should prioritize tools that create repeatable, agent-operable pipelines and queue artifacts, not manual editors.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Baserow** | Free cloud tier; open-source/self-host option. Current pricing page says “Free forever” and lists a $0 free plan with rows/storage/automation credits. | **5/5** — REST API, database tokens, OpenAPI docs, import/export, self-host option. | Hive content queue, CryptoCreep post approvals, Music playlist/niche queue, JAM ops dashboards. | Better than scattered Markdown for sortable queues: post idea → draft → compliance check → approved → scheduled/exported. AI can operate rows through API later, while the first trial can use fake data only. | Live account connection/import of real content queues needs Jude approval. Self-host/install also needs approval. | Draft a Baserow schema in Markdown only: `CryptoCreep Content Queue` + `Suno Playlist Pipeline`, with fake rows and fields for approval gates. |
| **Hive Developers API / hive-js** | Hive developer docs are public; `openhive-network/hive-js` is MIT-licensed. | **4/5** — JSON-RPC APIs, JavaScript/Python docs, account/content/rewards/search APIs; agent scripts can read public chain data. | Hive/CryptoCreep education research and source-backed examples. | Lets agents pull public Hive concepts/examples/rewards/activity without logging into Facebook or making unsupported claims. Useful for beginner posts: “what ownership means,” “how comments/rewards work,” “what not to promise.” | Posting, wallet/auth, Hivesigner/Keychain use, or account operations need approval. Public read-only research is safest. | Create a read-only content-research spec listing 5 public Hive API queries and the exact caveat language for rewards; do not authenticate or post. |
| **Publer** | Freemium/social scheduling; pricing page advertises starting scheduling for free. | **3/5** — bulk scheduling via CSV is advertised; browser automation likely possible. API status/limits not confirmed from official docs in this run. | Hive/CryptoCreep social queue after Jude approves posting workflow. | Stronger than manual-only scheduling because agents can prepare CSV rows. Useful later for Facebook/Page queues if Jude chooses a scheduler. | Connecting Facebook/social accounts, scheduling, publishing, or using paid features requires approval. Need verify current free-plan limits before relying on it. | Defer live use. For now, generate a Publer-compatible CSV draft with 3 fake posts and approval/status columns only. |
| **yt-dlp** | Free/open-source; GitHub repo shows Unlicense and active maintenance. | **5/5** — CLI, scriptable metadata extraction/download features. | Music Production YouTube niche research and competitor evidence capture. | Can support a local/PC dry-run to collect public video metadata/title/duration/channel evidence for niche scoring without manual browsing. Should be used carefully and only within platform/legal boundaries. | Installing on Jude’s PC/VPS or downloading media needs approval; avoid private/account content and respect YouTube terms. | Draft a no-install evaluation plan: what public metadata fields a future script would collect, with 5 manually chosen example URLs supplied by Jude later. |
| **n8n** | Cloud has paid plans/free trial; standard self-hosted version available on GitHub. GitHub description says self-host or cloud, 400+ integrations. | **4/5** — workflows, custom code, integrations, REST API; docs note API is not available during free trial, but self-host has API playground. | JAM AI Workspace glue later: content queues → Notion tasks → GitHub reports → Telegram summaries. | Best future orchestrator once Jude has stable queue schemas. Not the first step because it introduces account connections/triggers and can become accidental automation. | Installing, self-hosting, connecting Notion/Google/GitHub/Facebook, or enabling triggers requires explicit approval. | Keep as future-only. First define queue schemas and approval gates; no install or account connection this week. |

## Best pick this week

**Baserow schema-first queue design** is the safest, highest-leverage pick.

Why: both recent focus areas need the same operating pattern: a structured queue with statuses, evidence/source fields, approval gates, and export paths. Baserow is API-friendly later, but the immediate safe action is only a Markdown schema + fake sample rows, so there is no signup, install, account connection, or private-data upload.

Recommended schema-first artifacts:

- `CryptoCreep Content Queue`
  - Post ID
  - Platform
  - Content pillar: Hive basics / Web3 safety / community / relaunch / myth-busting
  - Draft caption
  - Visual prompt
  - Source URL(s)
  - Compliance caveats: no financial advice / no income guarantee / realistic rewards
  - Review status: Idea / Draft / Compliance checked / Jude approved / Ready to schedule / Published manually
  - Approval notes
- `Suno Playlist Pipeline`
  - Niche/lane
  - Evidence URLs
  - Demand notes
  - Competition notes
  - Suno feasibility
  - Prompt pack status
  - Credit-use priority
  - YouTube package status
  - Approval notes

## Free/open-source alternatives

- **Google Sheets + Apps Script** — already fits Jude’s existing workflow and is AI-operable through scripts/API; best if Jude wants no new app. Downside: more fragile schema/permission management than a dedicated queue database.
- **Plain CSV/Markdown in GitHub** — zero signup and easiest for Hermes/Claude/Codex. Downside: less convenient for Jude to filter/review from mobile or dashboard.
- **SQLite/DuckDB local files** — very agent-operable and private; good for research evidence stores. Downside: less human-friendly unless paired with generated Markdown/CSV exports.
- **Hive API direct scripts** — free/public read-only for Hive education research; should stay unauthenticated unless Jude approves account operations.

## Manual-only tools to avoid or defer

- **Meta Business Suite as the primary workflow tool** — useful for final scheduling, but too manual/browser-bound for the current draft-first pipeline. Use only after Jude approves account access/scheduling.
- **Canva as the core queue/source of truth** — excellent for visuals, but not ideal as the agent-readable operating database. Better as an output target after captions/visual prompts are approved.
- **Manual video/audio editors for Music Production** — defer until the Suno lane and prompt-pack process is proven. Start with evidence and queue structure, not timeline editing.

## Approval needed from Jude

Approval is needed before any of the following:

- signing up for Baserow/Publer or any other service;
- installing/self-hosting Baserow, n8n, yt-dlp, or related tools;
- connecting Facebook, YouTube, Google, Notion, GitHub, Hive, Suno, or scheduler accounts;
- authenticating with Hive wallet tools or posting to Hive/Facebook;
- downloading YouTube media or scraping beyond safe public metadata;
- scheduling/publishing posts or uploading music/videos;
- enabling webhooks, triggers, Docker containers, cron jobs, or autonomous agents.

## Next safe action

Create a **Markdown-only queue schema and fake-data dry-run** for:

1. CryptoCreep/Hive 7-post relaunch queue; and
2. Suno/YouTube 5-lane playlist research queue.

No software installation, no account signup, no private uploads, and no publishing. If Jude likes the schema, the next approved step can be choosing where the live queue should live: GitHub Markdown/CSV, Google Sheets, Baserow cloud, or self-hosted Baserow.

## Sources checked

- Baserow pricing page and REST API docs — verified free plan wording, REST API, database token/OpenAPI docs.
- Baserow GitHub repo — public repo metadata checked 2026-07-11: active repo, ~5.3k stars, description includes open-source cloud/self-hosted platform.
- Hive Developers portal — verified public API docs, JSON-RPC/API categories, JavaScript/Python resources.
- openhive-network/hive-js GitHub repo — public repo metadata checked 2026-07-11: MIT-licensed JavaScript library for Hive API servers.
- Publer pricing/plans page — verified free-start wording and CSV/bulk scheduling claims from public page text; API availability not confirmed.
- yt-dlp GitHub repo — public repo metadata checked 2026-07-11: CLI audio/video downloader, Unlicense, active repo.
- n8n pricing/API docs and GitHub repo — verified cloud pricing/free-trial text, API docs note, self-host/cloud positioning, and active repo metadata.
- Suno pricing page — checked to ground Music Production constraints: free plan exists but no commercial use; Pro/Premier paid tiers list credits/commercial rights. No Suno account was accessed.
