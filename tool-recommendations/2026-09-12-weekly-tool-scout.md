# Weekly Tool Scout Report — 2026-09-12

## Focus this week

**Focus areas:**

1. **Music Production — YouTube/Suno research + audio QC/packaging.** The central handoff says the next Music Production step is YouTube niche research followed by Suno prompt packs. This week prioritizes tools that can inspect public video/channel metadata, analyze generated audio locally, and create repeatable YouTube-ready packaging artifacts without using Suno credits or logging into YouTube.
2. **Story Writing — privacy-first proofreading/style QA before Phase 2 automation.** Story handoffs say visual prompts are active and Python-assisted proofreading is planned later. This week looks at offline/scriptable prose checkers that can report issues without rewriting canon or uploading manuscripts.

**Boundary followed:** no software/packages/models were installed, no accounts/API keys were created, no private files were uploaded, no YouTube/Suno/Notion/Google/GitHub integrations were connected, no workflows were changed as final, and no automation/cron/container was created.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **yt-dlp** | **Free / open-source-style public-domain license (Unlicense).** GitHub API checked 2026-09-12; PyPI latest checked as `2026.8.19`. | **5/5** — CLI + Python package; can emit metadata, subtitles, and structured files in batch workflows. | **Music Production**, JAM research, Hive/CryptoCreep public video research. | Best fit for a future Music Production niche-research helper: collect public YouTube metadata/subtitles for *research only* so agents can compare titles, durations, upload cadence, descriptions, and content patterns before Jude spends Suno credits. | Installing/running it needs approval. Downloading copyrighted media or violating platform terms must be avoided. Use metadata/subtitles/public pages only unless Jude approves a specific compliant use. YouTube can rate-limit/block scraping. | **No-install next step:** draft a Music niche research CSV schema: URL, channel, title, duration, views if visible, upload date, keywords, format notes, “why repeat-listenable,” and Suno feasibility. |
| **librosa** | **Free / open-source ISC.** GitHub and PyPI checked 2026-09-12; PyPI latest checked as `1.0.0`. | **5/5** — Python library; batchable; outputs plots/JSON/CSV features. | **Music Production**, Story/audio reference if any. | Strong local audio-analysis layer after Jude manually generates Suno tracks: extract tempo-ish features, RMS/energy, spectral centroid/rolloff, onset strength, chroma, mel spectrograms, and flag distracting spikes or uneven dynamics for focus/study playlists. | Installing Python packages and processing private/generated audio requires Jude approval. Feature metrics are guidance, not a music-quality judge. | **No-install next step:** define an “audio QC report” template only: input filename, intended playlist lane, loudness/energy notes, loopability notes, distraction flags, and manual review decision. |
| **FFmpeg / ffprobe** | **Free / open-source project; license depends on build configuration.** GitHub mirror checked 2026-09-12. | **5/5** — mature CLI; scriptable filters; file-based batch processing. | **Music Production**, Hive videos, JAM media utilities. | Best default utility for future audio packaging: generate waveform/spectrum previews, convert formats, trim silence, normalize cautiously, create simple visualizer clips, and inspect audio/video metadata with `ffprobe`. Pairs well with Remotion later if Jude wants code-driven YouTube visuals. | Installing binaries or processing private media needs approval. Audio normalization/format conversion can alter final sound; keep originals untouched. Commercial distribution should use a known-good FFmpeg build/license posture. | **No-install next step:** write a paper-only folder convention: `raw-suno/`, `review-qc/`, `approved-masters/`, `youtube-packages/`, with original-preservation rule. |
| **Vale CLI** | **Free / open-source MIT.** GitHub API checked 2026-09-12; PyPI wrapper checked as `3.21.0.0`. | **5/5** — command-line prose linter; offline; configurable style rules; CI/editor friendly. | **Story Writing**, JAM docs, AI Agency client docs. | Best fit for *custom Jude/story rules* rather than generic grammar: catch banned AI-isms, inconsistent terms, stale chapter footers, style-sheet terms, or “do not use exact price/best/must-buy” affiliate-copy warnings. Agents can generate/maintain `.vale` rules and output a review report without editing chapters. | Installing/running needs approval. Rules must be tuned carefully or they create noise. It should flag issues only; no automatic prose rewrites without Jude approval. | **No-install next step:** draft 10 candidate Story/JAM style rules in Markdown only, e.g. canon names, AI-isms, overused phrases, and affiliate compliance terms. |
| **Harper** | **Free / open-source Apache-2.0.** GitHub API checked 2026-09-12; README describes it as offline/privacy-first grammar checking. | **4/5** — Rust-powered grammar checker; useful through editor/LSP-style workflows and potentially CLI/editor integrations. | **Story Writing**, JAM docs, draft social posts. | Good privacy-first grammar checker candidate for manuscripts/drafts because it is offline and less account/SaaS dependent than Grammarly-style tools. Useful as a second pass after deterministic story scanners. | Need approval before installing. English grammar suggestions can fight Jude’s fiction voice, Chavacano/Filipino/Maranao terms, dialogue style, and invented names; must be report-only and allowlisted. | **Defer one step:** evaluate after Vale-style project-specific checks, because custom canon/style rules matter more than generic grammar for Story. |

## Best pick this week

**Best pick: Vale CLI for Story/JAM style-rule reports, paired with a future librosa/FFmpeg audio QC spec for Music Production.**

Reason: Vale is highly AI-operable and can start as a Markdown-only rule design before any install. It also fits Jude’s current “review-only first” boundary: it can produce flagged line reports while leaving manuscript canon untouched. For Music Production, the safest immediate move is not a tool install; it is defining the file/schema conventions that a future `librosa + ffprobe` script would use after Jude approves local processing of Suno outputs.

Practical future shape, pending approval before any install/run:

```text
Story chapter/reference Markdown
  → deterministic scanners already in repo
  → Vale custom style/canon/compliance checks
  → report under .tmp/story-proofing/
  → Jude approval before any chapter edits

Suno-generated audio files on Jude PC
  → ffprobe/librosa read-only analysis
  → audio QC Markdown + optional waveform/spectrogram image
  → playlist package draft
  → Jude approval before upload/publish
```

## Free/open-source alternatives

- **LanguageTool** — free/open-source core and strong grammar/style coverage for 25+ languages; more complex Java/server setup and generic suggestions make it a phase-2 candidate after Vale/Harper.
- **Essentia** — open-source AGPL audio-analysis library with Python bindings and command-line extractors; powerful for music information retrieval, but heavier/licensing-sensitive compared with librosa for Jude’s first audio QC pass.
- **Existing Story scanners** — keep using `scripts/story_continuity_scan.py` first where available, then add prose/style tools only as report layers.
- **Plain Markdown/CSV schemas** — still the safest immediate layer for Music Production niche research and Suno prompt packs before any YouTube/audio tool is approved.

## Manual-only tools to avoid or defer

- Manual YouTube niche research spreadsheets where Jude must copy every title/view/duration by hand; use an agent-readable CSV schema first, then consider scriptable metadata capture after approval.
- Grammarly-style cloud editors for Story manuscripts by default; avoid uploading private canon/manuscript text before offline options are tested.
- Manual audio/video editors as the main Music Production packaging workflow; prefer FFmpeg/librosa/Remotion-style file/code pipelines, with manual editing only for final polish.
- Any “AI music growth” service that requires YouTube/Suno login, paid credits, or account connection before a local research/QC workflow exists.

## Approval needed from Jude

Jude approval is needed before:

- installing yt-dlp, librosa, FFmpeg, Vale, Harper, LanguageTool, Essentia, Node/Python/Rust/Java packages, plugins, models, or desktop apps;
- running YouTube scraping/downloading tools beyond documented public research boundaries;
- downloading or processing copyrighted media except where clearly allowed;
- processing private Story manuscripts, reference images, Suno outputs, or client/customer files with new tools;
- connecting YouTube/Suno/Google/Notion/GitHub/Facebook/Shopee/Hive/affiliate accounts or creating API keys;
- uploading files to hosted grammar/audio/video services;
- changing canonical Story chapter prose, publishing/scheduling music/videos/posts, spending credits, or enabling new automations/cron/containers.

## Next safe action

**Safest next action with no install and no external writes:** create two Markdown-only templates:

1. `Music Production/templates/audio-qc-report-template.md` — filename, playlist lane, intended use, loopability notes, distraction flags, loudness/energy notes, suggested edit, approval status.
2. `Story Writing/templates/style-check-report-template.md` or `.tmp/story-proofing/vale-rule-ideas.md` — custom Story/JAM rules to test later: canon names, stale chapter markers, AI-isms, repeated filler, affiliate compliance words, and “report-only/no rewrite” instructions.

## Sources checked

- Local JAM AI Workspace docs and handoffs: `AGENTS.md`, `agents/README.md`, `agents/tool-scout/AGENT.md`, `workflows/tool-scout-recommendations.md`, `PROJECTS.md`, central `HANDOFF.md`, and recent BBX/Hive/Story/Atlas handoffs.
- GitHub API snapshots checked 2026-09-12 for: `yt-dlp/yt-dlp`, `librosa/librosa`, `MTG/essentia`, `errata-ai/vale` / redirected `vale-cli/vale`, `Automattic/harper`, `languagetool-org/languagetool`, and `FFmpeg/FFmpeg`.
- Official GitHub README/raw sources checked 2026-09-12 for the same projects.
- PyPI JSON checked 2026-09-12 for `yt-dlp`, `librosa`, `essentia`, `ffmpeg-python`, `language-tool-python`, and `vale`.
