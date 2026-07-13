# YouTube Music Niche Report — 2026-07-05

## Executive recommendation

Dry-run result: the best first Suno test lanes are:

1. **Calm synthwave coding / programming music** — strongest balance of visible demand, smaller-channel visibility, and easy Suno production.
2. **Cozy fantasy tavern / writing music** — good repeat-listen intent, strong writing/creative fit, and a clear playlist/visual identity lane.
3. **Ambient music for reading fantasy books** — good demand and strong repeat-listen use case; slightly more channel concentration than #1–2.

Secondary tests:

- **Dark academia study music with rain/piano** — viable, but use more specific packaging to avoid generic saturation.
- **Manila night / Filipino-inspired lo-fi** — low competition and unique brand angle, but current visible YouTube demand is much weaker; treat as an experimental cultural lane, not the first volume driver.

Avoid spending the first major Suno batch on broad **rainy café lo-fi** or **soft piano rain focus**. They show huge demand but look saturated and dominated by large, established ambience/music channels.

## Method and limits

- Run time: **2026-07-05 13:11 PHT**.
- Tooling: free/manual-style YouTube search collection using `yt-dlp` search results; no YouTube login, no paid tool, no account action.
- Scope: 11 seed niches, top 8 visible search results each = 88 result slots.
- Raw dry-run data: `.tmp/youtube_niche_dryrun_raw.json`.
- Important limitation: flat YouTube search results returned titles/channels/views/durations but **not publish dates**. A follow-up browser/manual pass is needed before treating “recent breakout” as confirmed.
- Confidence: **medium-low** overall because this is a first dry-run and lacks publish age/date data.

## Recommendation-ranked niches

The table is ranked by **first-batch usefulness**, not pure total score. I weighted visible demand + competition balance + confidence higher than novelty, because Jude’s first Suno batch should prioritize niches with a realistic chance of plays.

| Rec. rank | Niche | Demand | Competition inverse | Repeat-listen | Suno feasibility | Brand fit | Expansion | Total | Confidence | Notes |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Calm synthwave coding music | 4 | 4 | 5 | 5 | 5 | 5 | **28** | Medium | Median top-result views ~230k; 5/8 results under 500k suggests smaller-channel visibility; strong work/coding fit. |
| 2 | Cozy fantasy tavern writing music | 4 | 4 | 5 | 5 | 5 | 5 | **28** | Medium | Median ~672k; several smaller results plus strong high-end demand; excellent writing/creative lane. |
| 3 | Ambient music for reading fantasy books | 4 | 3 | 5 | 5 | 5 | 5 | **27** | Medium | Median ~690k; strong reader/writer intent; some concentration around fantasy ambience channels. |
| 4 | Dark academia study music rain piano | 4 | 4 | 5 | 4 | 5 | 4 | **26** | Medium | Median ~458k with 4/8 under 500k; viable if packaged narrowly, e.g. gothic library/rain/piano. |
| 5 | ADHD focus ambient music no vocals | 5 | 2 | 5 | 4 | 4 | 4 | **24** | Low-medium | Demand is strong, median ~1.19M, but channel concentration is high and health/ADHD claims need careful wording. |
| 6 | Manila night lo-fi | 2 | 5 | 4 | 5 | 5 | 4 | **25** | Low | Low median ~78k, but low competition and unique local angle; some irrelevant/non-Manila results. Experimental lane. |
| 7 | Non-vocal cyberpunk study music | 3 | 4 | 5 | 4 | 4 | 4 | **24** | Low | Exact query median very low (~6k) but has high-view related results. Avoid “Cyberpunk 2077”/trademark framing. |
| 8 | Cinematic emotional background music for short film | 5 | 2 | 3 | 4 | 4 | 3 | **21** | Medium | Strong demand, median ~926k, but this is more licensing/cue-pack oriented than repeat playlist listening. |
| 9 | Filipino lo-fi study music | 2 | 5 | 4 | 5 | 5 | 4 | **25** | Low | Very low median ~2.9k except a few outliers; potentially distinctive, but not first if goal is plays. |
| 10 | Rainy café lo-fi study music | 5 | 1 | 5 | 5 | 4 | 4 | **24** | Medium | Huge median ~7.0M, but saturated and partly dominated by established channels/near-identical coffee/rain mixes. |
| 11 | Soft piano rain work focus | 5 | 1 | 5 | 5 | 4 | 4 | **24** | Low-medium | Huge views, but very broad/saturated; one search result had missing view data. Better as ingredient, not standalone niche. |

> Note: Total score is not the only decision factor. “Rainy café” and “soft piano rain” score high because demand and feasibility are huge, but their competition inverse is poor, so they should not lead the first batch.

## Top 3 to test first

### 1. Calm synthwave coding / programming flow

**Why:** visible demand without total saturation; easy to produce many Suno variants; clean fit for students, remote workers, coders, and deep work playlists.

**Packaging angles:**

- `Flow State Coding — Calm Synthwave for Deep Work`
- `Terminal at Midnight — No-Vocal Synthwave Coding Mix`
- `Neon Rain Desk Setup — Focus Music for Programming`
- `Retro Future Study Session — Minimal Synthwave Beats`

**Suno prompt direction:** instrumental, no vocals, calm synthwave, soft analog pads, gentle arpeggios, restrained kick, warm bass, 80–95 BPM, seamless loop feel, no aggressive leads.

### 2. Cozy fantasy tavern / writing music

**Why:** strong creative/writing repeat-listen intent; good balance of small and larger results; highly expandable into series.

**Packaging angles:**

- `Cozy Tavern Writing Music — Medieval Inn Ambience for Fantasy Authors`
- `Quiet Corner of the Inn — Warm Fantasy Study Music`
- `Rain Outside the Tavern — Music for Writing and Reading`
- `Wandering Scholar’s Rest — Gentle Medieval Focus Music`

**Suno prompt direction:** warm acoustic plucks, soft hand drums, gentle strings, woodwinds, fireplace ambience feel, no vocals, loopable, non-intrusive melody.

### 3. Ambient fantasy reading music

**Why:** strong fit for reading/writing/fantasy audiences; high repeat-listen potential; can share assets with the fantasy tavern lane while staying broader.

**Packaging angles:**

- `Fantasy Reading Music — Deep Focus for Books and Writing`
- `Rainy Castle Library — Ambient Fantasy Study Music`
- `Forest Mage Study Room — Calm Reading Ambience`
- `Ancient Library at Night — Soft Fantasy Background Music`

**Suno prompt direction:** ambient pads, soft strings, subtle choir-like texture without lyrics, low percussion, calm fantasy atmosphere, avoid copyrighted/franchise references.

## Niches to avoid for now

| Niche | Why avoid as first batch | Possible later use |
|---|---|---|
| Rainy café lo-fi study music | Massive demand but saturated; top results include very large channels and recurring near-identical coffee/rain packaging. | Use as a modifier inside more specific lanes, e.g. “Manila rainy study desk” or “fantasy café writing.” |
| Soft piano rain work focus | Very broad and dominated by huge study/sleep/work ambience videos. | Use piano/rain as sonic texture in dark academia or fantasy reading. |
| Cinematic emotional background music for short film | Demand exists, but listener intent is less playlist/repeat-listen and more licensing/download/cue use. | Build later as a separate OST/cue-pack branch. |
| Generic “ADHD relief” claims | Strong demand, but potential medical/health-claim risk and heavy competition. | Reframe as “distraction-free focus,” “no-vocal deep work,” “steady pulse focus.” |
| Cyberpunk-branded results | Some high-view results rely on Cyberpunk 2077/OST framing. | Use generic “neon future city,” “rainy future desk,” “no-vocal sci-fi focus.” |

## Prompt brief for Suno Prompt Producer

Generate prompt packs for the top 3 lanes first:

1. **Calm synthwave coding music**
   - 10–15 variants.
   - Prioritize no vocals, steady tempo, clean loops, no aggressive hooks.
   - Include title/thumbnail mood words: neon, terminal, midnight, rain, flow state, deep work.

2. **Cozy fantasy tavern writing music**
   - 10–15 variants.
   - Prioritize warm acoustic/fantasy instrumentation, gentle ambience, writing/reading focus.
   - Avoid named fantasy franchises, copyrighted taverns, or artist references.

3. **Ambient fantasy reading music**
   - 10–15 variants.
   - Prioritize long ambient beds, subtle melodic motifs, fantasy library/forest/castle packaging.
   - Keep melodies non-distracting for reading.

Optional small experimental pack:

- **Manila night lo-fi / Filipino-inspired ambience** — 5 variants only, with careful cultural framing and no unsupported claims. Use “Manila night commute,” “tropical rain study desk,” “quiet city balcony,” etc.

## Evidence notes

| Keyword | Median views among visible results | Max views | Small-result signal | Channel concentration note |
|---|---:|---:|---|---|
| rainy cafe lofi study music | ~7.0M | 48.2M | 2/8 under 500k | `Lofi Coffee` appeared 3x. |
| adhd focus ambient music no vocals | ~1.19M | 18.4M | 2/8 under 500k | `Greenred Productions` appeared 3x; `SOUND ISLAND` 2x. |
| dark academia study music rain piano | ~458k | 1.89M | 4/8 under 500k | `Nostalgic Dark Academia` appeared 3x. |
| cozy fantasy tavern writing music | ~672k | 10.65M | 4/8 under 500k | `The Resting Bard` appeared 3x. |
| calm synthwave coding music | ~230k | 6.65M | 5/8 under 500k | Top channels more varied; `Cosmic Hippo` appeared 2x. |
| soft piano rain work focus | ~12.28M | 22.66M | 1/7 counted under 500k | Broad/high-view ambience lane. |
| non vocal cyberpunk study music | ~6k | 2.74M | 5/8 under 500k | Results include copyrighted/trademarked game framing risk. |
| filipino lofi study music | ~2.9k | 1.93M | 7/8 under 500k | Low competition, weak visible demand. |
| manila night lofi | ~78k | 1.1M | 7/8 under 500k | Low competition, some off-target results. |
| cinematic background music for short film emotional | ~926k | 18.0M | 3/8 under 500k | Strong demand but different intent. |
| ambient music for reading fantasy books | ~690k | 1.71M | 3/8 under 500k | `FanTaisia Ambience` appeared 3x. |

## Recommended next step

Run the **Suno Prompt Producer** on the top 3 lanes and create a first manual generation pack. Before large-scale production, do one follow-up YouTube pass using browser/manual checks for:

- publish dates/age;
- whether recent small channels are breaking out;
- thumbnail/title patterns;
- duration norms;
- comment/listener intent clues.
