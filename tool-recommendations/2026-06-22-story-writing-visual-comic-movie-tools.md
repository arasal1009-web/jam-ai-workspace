# Tool Scout Report — Story Writing Visual / Comic / Movie Tools

**Run time:** 2026-06-22 22:08 PHT  
**Mode:** manual dry-run / recommendation only  
**Focus:** Story Writing tools for visual prompts, comic adaptation planning, storyboard/animatic work, and realistic AI movie/series planning.

## Boundary

| Action | Status |
|---|---|
| Researched public tool pages / GitHub pages | Yes |
| Installed apps/extensions/packages | No |
| Created accounts / signed into services | No |
| Started trials/subscriptions | No |
| Connected project files to external tools | No |
| Generated images/videos | No |
| Changed Story Writing canon/workflows | No |
| Created cron/container/automation | No |

## Current Story Writing needs matched

1. **Visual prompt packages** for characters.
2. **Comic adaptation planning** from Book 1 chapters.
3. **Realistic AI movie/series planning** later.
4. **Free-first / local-first** tooling where possible.
5. Keep private manuscript/canon files out of third-party tools unless Jude explicitly approves.

## Best shortlist

| Rank | Tool | Free? | Project fit | Why useful | Risk / approval needed | Suggested zero-cost trial |
|---:|---|---|---|---|---|---|
| 1 | **Storyboarder** | Free download | Comic/storyboard planning | Fast panels, shot order, animatics; ideal bridge from chapter → comic/series board | Install approval needed on PC | Try Chapter 1: create 8–12 rough panels from existing comic outline |
| 2 | **Krita** | Free/open-source | Character sheets + comic panels | Drawing, paint-overs, model sheets, expression sheets; good base app for visual prompt refinement | Install approval only | Create a `Jul` character reference board or expression sheet |
| 3 | **Blender** | Free/open-source | Realistic/movie planning | 3D blocking, camera/lens tests, set layout, previsualization, animation | Steeper learning curve; install approval | Block one scene: Jul on Cawa-Cawa Boulevard / passage shadow |
| 4 | **ComfyUI** | Free/open-source, local if GPU available | AI image/video workflow control | Node-based reproducible character generation; can preserve prompts/workflows for repeatable character looks | Setup/GPU/model downloads; install approval; model license checks | Later: test one local character image workflow using non-private prompt only |
| 5 | **Krita AI Diffusion plugin** | Free/open-source plugin | AI-assisted paint-over/inpaint/outpaint inside Krita | Useful after character prompts stabilize: refine outfits, faces, expressions, backgrounds | Requires Krita + AI model backend; setup approval | Later: use on a non-canon sample image first |
| 6 | **OpenToonz** | Free/open-source | 2D animation / comic-to-animation path | Open-source animation production software; useful if you want stylized/animated adaptation | More complex than Storyboarder/Krita | Watch/tutorial first; no install needed yet |
| 7 | **DaVinci Resolve** | Free version available | Movie/series editing + trailer tests | Professional free editor for assembling AI clips, voice/music, animatics | Heavy install; not needed until clips exist | Later: use only after visual clips are being generated |

## Best pick this week

### 1. Storyboarder

**Why first:** It supports the immediate next phase: turning chapters into a comic/series plan without needing AI generation yet.

Source-backed notes from official page:

- Official page describes it as “The best way to visualize your story.”
- Page says “Download for Free.”
- It supports quickly drawing/testing story ideas and creating animatics.

**Recommended use for Jude:**

```text
Chapter → panel list → rough storyboard → comic/series shot plan
```

Best first trial:

```text
Use Chapter 1 or existing Ch1 comic outline to create a 12-panel storyboard sample.
```

Why Chapter 1:

- It already has a comic outline archived for reference.
- It has strong visual beats: Cawa-Cawa Boulevard, phone battery, debt envelope, wrong shadow, passage.
- It does not require touching canon prose.

## Best free-first workflow stack

### Stage 1 — Planning / no AI generation

| Step | Tool | Output |
|---|---|---|
| Character visual packets | Hermes overnight Visual Prompt Designer | Markdown prompt packages |
| Panel planning | Storyboarder | rough comic/series boards |
| Character/reference boards | Krita | model sheets / mood boards |

### Stage 2 — AI image/video tests, later

| Step | Tool | Output |
|---|---|---|
| Repeatable character image workflow | ComfyUI | saved node workflows + seed/style notes |
| Paint-over/refinement | Krita + Krita AI Diffusion | improved stills / inpainted details |
| Scene/blocking tests | Blender | camera blocking / rough 3D sets |

### Stage 3 — Editing / assembly, later

| Step | Tool | Output |
|---|---|---|
| Animatic assembly | Storyboarder or DaVinci Resolve | rough episode/video timing |
| Final short trailer/scene edit | DaVinci Resolve or Kdenlive | edited clip |

## Free-first alternatives / supporting tools

| Tool | Free? | Use |
|---|---|---|
| **Kdenlive** | Free/open-source | Lighter open-source video editor alternative to DaVinci Resolve |
| **Freesound** | Free with Creative Commons licenses | Sound effects for animatics; must check each license |
| **Mixamo** | Free Adobe tool, account likely needed | Quick 3D character animation references for Blender |
| **Cascadeur** | Has Free plan | AI-assisted 3D keyframe animation; maybe useful later, not urgent |

## Not recommended as first step

| Tool/type | Reason to wait |
|---|---|
| Paid AI video generators | Cost can grow quickly; visual identity is not stable yet |
| Full ComfyUI character workflow immediately | Powerful but setup-heavy; better after 3–5 character prompts are reviewed |
| DaVinci Resolve immediately | Great editor, but unnecessary until you have boards/clips |
| Uploading full chapters to online comic/storyboard tools | Privacy/canon risk; use local/manual summaries first |

## Approval needed from Jude

Before doing any of these, ask Jude:

- install Storyboarder on PC;
- install Krita on PC;
- install Blender / ComfyUI / DaVinci Resolve;
- download AI models or use GPU-heavy local generation;
- upload manuscript text, character profiles, or story bibles into third-party services;
- create a recurring Tool Scout cron.

## Recommended next zero-cost trial

Do **not** install anything yet if Jude is not ready. First create a planning artifact in Markdown:

```text
Chapter 1 Visual Adaptation Trial
```

Suggested output:

1. 12 panel beats for comic version;
2. 12 shot beats for realistic series version;
3. character appearances needed: Jul, implied Nanay memory, Kuya Mike/Dodoy references if shown;
4. location references needed: Cawa-Cawa Boulevard, RT Lim Boulevard, sea wall, old lamppost, shadow/passage;
5. questions for Jude before opening Storyboarder.

This uses the repo only and costs no software setup.

## If Jude approves a PC app trial

First app to install/test:

```text
Storyboarder
```

Second:

```text
Krita
```

Hold until later:

```text
ComfyUI / Blender / DaVinci Resolve
```

## Sources checked

| Tool | Source checked | Evidence captured |
|---|---|---|
| Storyboarder | `https://wonderunit.com/storyboarder/` | official title + “Download for Free”; storyboard/animatic description |
| Krita | `https://krita.org/en/` | official page reachable; digital painting / creative freedom |
| Blender | `https://www.blender.org/about/` | official page says Free and Open Source software |
| ComfyUI | `https://github.com/Comfy-Org/ComfyUI` | GitHub description: modular diffusion model GUI/API/backend with graph/nodes interface |
| Krita AI Diffusion | `https://github.com/Acly/krita-ai-diffusion` | GitHub description: AI generation in Krita, inpaint/outpaint |
| OpenToonz | `https://opentoonz.github.io/e/` | official page: free for commercial/non-commercial; open-source |
| DaVinci Resolve | `https://www.blackmagicdesign.com/products/davinciresolve` | official page: free and paid versions for Mac/Windows/Linux |
| Kdenlive | `https://kdenlive.org/en/` | official site reachable |
| Freesound | `https://freesound.org/` | Creative Commons sound database |
| Cascadeur | `https://cascadeur.com/` + `/plans` | AI-assisted animation; plans include Free |

## Tool Scout scores

Scoring: 1 low / 5 high.

| Tool | Project fit | Cost/value | Setup ease | Privacy/safety | Immediate usefulness | Total /25 |
|---|---:|---:|---:|---:|---:|---:|
| Storyboarder | 5 | 5 | 4 | 5 | 5 | 24 |
| Krita | 5 | 5 | 4 | 5 | 4 | 23 |
| Blender | 4 | 5 | 2 | 5 | 3 | 19 |
| ComfyUI | 5 | 5 | 2 | 4 | 3 | 19 |
| Krita AI Diffusion | 4 | 5 | 2 | 4 | 3 | 18 |
| OpenToonz | 3 | 5 | 2 | 5 | 2 | 17 |
| DaVinci Resolve | 4 | 4 | 3 | 5 | 2 | 18 |

## Final recommendation

For the next Story Writing visual/comic/movie phase, use this order:

1. **Markdown adaptation plan first** — no install, no risk.
2. **Storyboarder** — first PC app trial for comic/series boards.
3. **Krita** — character sheets and reference boards.
4. **ComfyUI/Krita AI Diffusion** — only after visual prompts are stable.
5. **Blender/DaVinci Resolve** — later for realistic series staging/editing.
