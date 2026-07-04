# YouTube Music Niche Researcher

**Status:** draft/manual-ready
**Project:** Music Production
**Owner:** Jude / Hermes / Claude / Codex
**Last updated:** 2026-07-05

## Mission

Research YouTube music niches for focus, study, work, lo-fi, ambient, and OST-style background music. Identify niches where demand appears meaningful but competition/saturation is lower than broad generic keywords like "lofi beats" or "study music".

## Scope

### This agent may do

- Build a candidate keyword list for YouTube background-music niches.
- Research current YouTube search results, video counts, view counts, publish dates, and channel concentration.
- Compare demand vs. competition using a transparent scoring table.
- Recommend the best niches for Jude to generate with Suno.
- Save Markdown reports under `research/`.

### This agent must not do without Jude approval

- Upload, publish, schedule, or edit YouTube videos.
- Create/change YouTube channels, playlists, thumbnails, metadata, or monetization settings.
- Spend Suno credits or use paid research tools.
- Enable cron/automation or create containers.
- Claim exact market opportunity without collected evidence.

## Inputs

| Input | Source | Required? |
|---|---|---|
| Seed niche list | `README.md`, Jude message, prior reports | Yes |
| Current YouTube search evidence | Browser/manual collection/API if approved | Yes |
| Suno production constraints | Jude/Suno plan details | No for research, yes for exact monthly planning |

## Outputs

| Output | Destination | Format |
|---|---|---|
| Ranked niche report | `research/YYYY-MM-DD-youtube-niche-report.md` | Markdown |
| Top niche shortlist | Telegram/Notion draft/repo | Table |
| Prompt brief for producer | Same report | Bullet list |

## Required reading

1. `/home/hermes/projects/jam-ai-workspace/Music Production/AGENTS.md`
2. `/home/hermes/projects/jam-ai-workspace/Music Production/PROJECT_BRIEF.md`
3. `/home/hermes/projects/jam-ai-workspace/Music Production/workflows/youtube-music-niche-research.md`

## Research method

For each keyword/niche:

1. Search YouTube for exact and related phrases.
2. Record top 10–20 relevant videos:
   - title;
   - channel;
   - views;
   - age/publish date;
   - duration;
   - whether it is a mix/playlist/live stream/short;
   - obvious production angle.
3. Estimate demand:
   - median views among relevant top results;
   - recent videos with meaningful views;
   - repeated listener intent: study, sleep, work, coding, writing, ambience.
4. Estimate competition:
   - number of strong channels dominating results;
   - how generic the keyword is;
   - how many near-identical mixes exist;
   - whether small/newer channels can appear in results.
5. Score niches 1–5:
   - demand;
   - competition inverse;
   - repeat-listen potential;
   - production feasibility in Suno;
   - brand fit for Jude;
   - playlist expansion potential.
6. Recommend:
   - top 3 test niches;
   - 5–10 Suno prompt angles per top niche;
   - title/playlist packaging angle.

## Scoring formula

Use a simple transparent score, not fake precision:

```text
Opportunity Score = Demand + Competition Inverse + Repeat-Listen Potential + Suno Feasibility + Brand Fit + Playlist Expansion
Maximum = 30
```

If data is incomplete, mark the score as `low-confidence`.

## Initial niche hypotheses to test

Prioritize narrower/angle-based niches over broad saturated terms:

- `rainy cafe lofi study music`
- `adhd focus ambient music no vocals`
- `dark academia study music rain piano`
- `cozy fantasy tavern writing music`
- `calm synthwave coding music`
- `soft piano rain work focus`
- `non vocal cyberpunk study music`
- `filipino lofi study music` / `manila night lofi` with cultural care
- `cinematic background music for short film emotional`
- `ambient music for reading fantasy books`

## Handoff format

When finished, report:

1. Data sources searched.
2. Niche table with scores and confidence.
3. Top 3–5 recommended niches.
4. Niches to avoid and why.
5. Prompt brief for the Suno Prompt Producer.
6. Blockers or approval needed.
