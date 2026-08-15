# Weekly Tool Scout Report — 2026-08-15

## Focus this week

1. **Hive affiliate marketing — AI-operable short-form product-video pipeline.** Jude’s Hive work needs repeatable draft/queue-first product videos, not manual timeline editing. This week prioritizes tools where agents can generate video structure from templates, JSON, code, or APIs.
2. **Story Writing — visual/comic/adaptation prep without touching canon.** Story work is moving toward visual prompts, comic planning, and later adaptation workflows. This week prioritizes controllable local/open tools for images/storyboards, while ranking manual-only editors lower.

Assumptions: no Shopee/Facebook/TikTok/Hive affiliate dashboards, Story manuscripts, private images, Google/Notion/GitHub account connections, API keys, models, or paid credits were used. Research used public official/GitHub/docs/pricing pages only. No software was installed and no workflow was changed as final.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Remotion** — https://github.com/remotion-dev/remotion | **Free for individuals/small companies per Remotion license; source-available with custom/commercial license terms.** GitHub README: “Video tools for the agent era,” React/code as source of truth, programmatic/batch rendering. | **5/5** — code-first React components, templates, data-driven/batch rendering, agent-editable source files. | **Hive affiliate video, AI Agency client video templates, JAM reusable asset systems.** | Best fit for Jude’s “AI can operate it” preference: an agent can create a reusable 20-second affiliate template, populate product facts from a vetted Markdown/CSV/JSON file, and render drafts later after approval. Much better than manual-only video editors for repeatable product videos. | Install/build/render setup needs approval. License is not plain MIT; check terms before commercial/agency-scale use. Video claims still need source-backed product facts and affiliate disclaimers. No publishing/scheduling. | **No-install trial:** draft one `hive-affiliate-video-template-schema.md` with 5 shots × 4 seconds, fields for product facts, caveats, overlay text, voiceover, CTA, and compliance notes. |
| **ComfyUI** — https://github.com/Comfy-Org/ComfyUI | **Open-source GPL-3.0; local/free if Jude supplies hardware/models.** GitHub describes it as a modular AI engine/GUI/API/backend with graph/nodes. | **5/5** — workflows can be exported as API JSON; official `script_examples/basic_api_example.py` shows queueing a prompt to local server. | **Story visual prompts, Hive product-background/scene images, future comic/adaptation look-dev.** | Strongest open/local candidate for repeatable visual generation once Jude approves setup: agents can preserve a workflow graph, vary prompt/seed/reference fields, and save `.tmp/` outputs for review. Useful for Story visual consistency and Hive ad scene drafts. | Installing ComfyUI, models, custom nodes, GPU dependencies, or running a local server/API requires approval. Generated images must not override Story canon; private references/manuscripts should not be uploaded externally. | **Safe trial:** define a paper-only “ComfyUI workflow card” template: goal, inputs, prompt slots, negative prompt, seed policy, output path, reviewer checklist, and canon/compliance gates. |
| **Creatomate** — https://creatomate.com/docs/api/introduction / pricing page | **Freemium/trial.** Pricing page states full-featured trial with **50 credits**, no credit card required; paid tiers after that. | **4/5** — API, templates, feed rows, JS Preview SDK, no-code + API access. | **Hive affiliate video drafts, JMD/AI Agency client social assets.** | Good hosted alternative if Jude wants template-based video generation without maintaining a render stack. Agents can prepare JSON/template inputs and batch variants; useful for product-video drafts and client social packages. | Signup/API key/external upload required; paid after trial. Do not upload private product/account data or Story assets without approval. Hosted render privacy/retention must be checked first. | **Safe trial:** no signup; compare a future Creatomate template field map against the Remotion schema to see if Jude needs hosted rendering at all. |
| **JSON2Video** — https://json2video.com/docs/api/ / pricing page | **Freemium.** Pricing metadata states free entry plans; pricing page says **600 credits**, no credit card needed. | **4/5** — JSON/API video creation fits agent-generated specs. | **Hive affiliate video, AI Agency social-video production.** | A simpler hosted “JSON in → video out” path. Good if Jude wants agents to produce strict JSON video specs and avoid manual editing. More directly API-shaped than timeline editors. | Signup/API key/external rendering required; verify current credit/minute math before use. Paid plans start after free credits. No product claims unless source-backed; no auto-publishing. | **Safe trial:** create a fake-data JSON video spec only, using no real products and no API call. Compare complexity vs Remotion/Creatomate. |
| **Krita AI Diffusion plugin** — https://github.com/Acly/krita-ai-diffusion | **Open-source GPL-3.0 plugin; local/open/free positioning in README.** | **3/5** — useful in artist workflow; less batch/agent-native than ComfyUI, though it integrates with Krita and local generation. | **Story character/scene paintovers, visual correction, comic/look-dev.** | Best when Jude needs human-in-the-loop image refinement: inpaint/outpaint, reference images, sketches, line art/depth guidance inside Krita. Good after Story visual anchors are locked. | Requires Krita/plugin/model setup and likely manual review/editing. Lower rank for weekly Tool Scout because it is more GUI/manual than code/API-first. | **Defer:** keep as a later visual-refinement option after ComfyUI workflow cards and Story visual prompts are stable. |

## Best pick this week

**Remotion for Hive affiliate video templates** is the best pick.

Why: it matches Jude’s exact constraint — he does not have time for manual edits, and agents should be able to operate the workflow. A Remotion-style template keeps the video as code + structured data: product facts, overlay text, voiceover, timing, CTA, affiliate disclosure, and compliance caveats can all live in a Markdown/JSON file before any render happens.

Best no-risk next move: create a schema/spec only, not an install:

```text
.tmp/tool-scout/hive-affiliate-video-template-schema.md
```

Suggested fields: product/source URL, verified facts, stale marketplace facts to avoid, compatibility caveats, 5 shots × 4 seconds, overlay text, voiceover, CTA, affiliate disclosure, negative claims list, render status, and approval state.

## Free/open-source alternatives

- **Plain Markdown/JSON + existing Hive agents** — still the safest first layer. Have Affiliate Market Lead / Scriptwriter / Compliance Reviewer produce structured inputs before any video tool.
- **ComfyUI** — best local/open visual-generation backend if Jude approves installation/model setup later.
- **OpenShot** — free/open-source video editor with broad format support, but mostly GUI/manual; useful only if Jude needs occasional final manual edits.
- **Storyboarder** — useful for fast storyboards/Fountain-script-adjacent planning, but manual drawing/workflow-heavy and less automation-friendly.
- **Krita + Python scripting** — Krita docs expose Python scripting/plugin API, but this is better for custom art tools than first-pass automated affiliate videos.

## Manual-only tools to avoid or defer

- **CapCut/Canva-style manual timeline editing as the primary workflow** — okay for final human polish, but not ideal as Jude’s core repeatable system unless templates/export/automation are clearly defined.
- **Hosted AI video generators with no API, no batch export, or vague credit pricing** — defer; they risk creating another manual dashboard Jude must babysit.
- **Product-video tools that encourage unverified “best/must-buy” or price/discount claims** — avoid unless live source verification and compliance review are built in.
- **Story visual tools that overwrite canon through image output** — defer; visuals must remain draft/reference until Jude approves canon changes.

## Approval needed from Jude

Jude approval is needed before any of these actions:

- installing Remotion, ComfyUI, Krita plugins, OpenShot, Storyboarder, Node/Python packages, models, custom nodes, GPU/CUDA dependencies, or browser extensions;
- running local render/API servers, Docker containers, webhooks, CI render jobs, or scheduled video/image generation;
- signing up for Creatomate, JSON2Video, Shotstack, or any hosted video/image service, or creating API keys;
- uploading Shopee/Facebook/TikTok/Hive affiliate data, private product screenshots, Story manuscripts/reference images, client files, or account exports to external services;
- spending credits, starting paid trials/subscriptions, publishing/scheduling videos, posting/commenting/DMing, or connecting affiliate/social accounts.

## Next safe action

Create a **Markdown-only Hive affiliate video template schema** with fake/example data only:

```text
.tmp/tool-scout/hive-affiliate-video-template-schema.md
```

No install, no API call, no real product upload, no account connection. If Jude approves later, the first live test should use one product screenshot/title/details Jude provides, produce draft-only video specs, and stop before rendering/publishing unless separately approved.

## Sources checked

- Remotion GitHub metadata/README/license: `https://github.com/remotion-dev/remotion`, `https://raw.githubusercontent.com/remotion-dev/remotion/main/README.md`, `https://raw.githubusercontent.com/remotion-dev/remotion/main/LICENSE.md`
- ComfyUI GitHub metadata/README/API example: `https://github.com/Comfy-Org/ComfyUI`, `https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md`, `https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/script_examples/basic_api_example.py`
- Creatomate docs/pricing page: `https://creatomate.com/docs/api/introduction`, `https://creatomate.com/pricing`
- JSON2Video docs/pricing page: `https://json2video.com/docs/api/`, `https://json2video.com/pricing/`
- Krita AI Diffusion GitHub metadata/README: `https://github.com/Acly/krita-ai-diffusion`, `https://raw.githubusercontent.com/Acly/krita-ai-diffusion/main/README.md`
- OpenShot GitHub metadata/README/site: `https://github.com/OpenShot/openshot-qt`, `https://raw.githubusercontent.com/OpenShot/openshot-qt/develop/README.md`, `https://www.openshot.org/`
- Storyboarder GitHub metadata/README: `https://github.com/wonderunit/storyboarder`, `https://raw.githubusercontent.com/wonderunit/storyboarder/master/README.md`
- Krita scripting docs: `https://docs.krita.org/en/user_manual/python_scripting/introduction_to_python_scripting.html`
