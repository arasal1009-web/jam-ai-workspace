# Music Production

**Status:** setup/manual-first
**Owner:** Jude
**Primary tool:** Suno AI subscription
**Goal:** Use Jude's monthly Suno credits intentionally to produce focus/study/work background music, plus optional OST/cinematic/music-inspiration tracks.

## Mission

Create a repeatable AI-assisted music production system that helps Jude:

1. identify low-competition YouTube music niches with meaningful listener demand;
2. generate Suno-ready prompts for those niches;
3. organize monthly batches so the 2,500 monthly Suno credits are used productively;
4. prepare playlist/channel packaging drafts for YouTube without publishing anything automatically.

## Current project boundaries

This setup is **documentation and manual-agent instructions only**.

No automation was enabled. No Suno credits are spent automatically. No YouTube uploads, publishing, scheduling, account changes, or paid actions should happen without Jude's explicit approval.

## Core use cases

| Use case | Output |
|---|---|
| Focus/study/work playlists | Long-form background tracks/playlists for YouTube |
| Lo-fi / ambient experiments | Suno prompt sets and generated track review notes |
| OST/cinematic ideas | Scene-specific prompts, mood boards, cue sheets |
| Monthly credit usage | Batch plan that maps available credits to experiments, variations, and keepers |

## Folder map

```text
Music Production/
├── AGENTS.md
├── CLAUDE.md
├── PROJECT_BRIEF.md
├── README.md
├── agents/
│   ├── README.md
│   ├── suno-prompt-producer/AGENT.md
│   └── youtube-niche-researcher/AGENT.md
├── prompts/
│   └── suno-focus-music-prompt-bank.md
├── research/
│   └── README.md
├── templates/
│   ├── suno-prompt-template.md
│   └── youtube-playlist-package-template.md
└── workflows/
    ├── suno-monthly-credit-production.md
    └── youtube-music-niche-research.md
```

## Recommended first manual dry-run

1. Run `agents/youtube-niche-researcher/AGENT.md` against 10–20 candidate music niches.
2. Save a ranked niche report under `research/YYYY-MM-DD-youtube-niche-report.md`.
3. Pick the top 3 niches.
4. Run `agents/suno-prompt-producer/AGENT.md` to generate 10–20 Suno prompt variations per chosen niche.
5. Jude manually generates music in Suno and records keep/reject notes.

## Candidate niche seed list

These are starting hypotheses only; the niche researcher must verify demand and competition with current YouTube data before Jude invests credits.

- lofi study music, but with narrower themes: rainy provincial café, library at midnight, Manila night commute, tropical rain desk setup
- ambient study music for ADHD/deep focus
- non-vocal cyberpunk study ambience
- cozy fantasy tavern writing music
- soft piano + rain for coding/work
- dark academia library ambience without vocals
- calm synthwave for programming
- cinematic emotional background cues for short films
- Filipino-inspired ambient/lo-fi study music, handled respectfully and without unsupported cultural claims
- OST-style scene cues: reunion, betrayal, discovery, grief, victory, magical awakening
