# Handoff Log

Use this file to record cross-assistant continuity.

## Format

### YYYY-MM-DD — Assistant / Tool

**What changed:**

**Files touched:**

**Current status:**

**Blockers:**

**Suggested next action:**

## 2026-06-22 — Hermes — Sub-agent setup foundation

### What changed

- Added central sub-agent registry at `agents/README.md`.
- Added reusable sub-agent specification template at `agents/templates/sub-agent-spec.md`.
- Added future Docker role-agent blueprint at `agents/runtime/docker-role-agent-blueprint.md`.
- Cleaned `PROJECTS.md` so it points to current PC/VPS/GitHub project locations.
- Updated project `AGENTS.md` / `CLAUDE.md` files to point at `/home/hermes/projects/jam-ai-workspace` instead of stale `/home/hermes/wat-backup`.

### Boundary

No containers, daemons, role agents, or new automations were created. This is documentation/setup only.

### Next recommended action

Create individual BBX `AGENT.md` files first, then test one manual BBX workflow before considering any containerization.

## 2026-06-22 — Hermes — BBX role-agent specs completed

### What changed

The BBX repo now has individual manual-dry-run-ready `AGENT.md` specs for eight BBX agents:

- Account Manager Lead
- Member Follow-up Agent
- Call & Activity Logging Agent
- Directory Listings Agent
- Member Intelligence & Trade Match Agent
- Email & Message Drafting Agent
- CRM Browser Operator Agent
- Weekly Performance Review Agent

BBX commit: `3b594e5 docs: add BBX role agent specs`.

### Boundary

No Docker containers, role-agent processes, cron jobs, CRM updates, or messages were created/sent.

### Next recommended action

Manual dry-run of `/home/hermes/projects/bbx/agents/account-manager-lead/AGENT.md` to produce a sample BBX daily action plan from read-only approved inputs.

## 2026-06-22 — Hermes — BBX windows recorded and Hive setup started

### What changed

- BBX calling windows recorded in the BBX repo: NZ until 1:00 PM PHT, AU until 3:00 PM PHT. After those windows, agents should prepare queues/drafts/research for the next day rather than suggesting immediate calls.
- Hive role-agent setup created in `/home/hermes/projects/hive` for low-attention content/affiliate work.
- Central agent registry updated to make Hive the next setup focus, then Story Writing.

### Boundary

No automations, containers, publishing, CRM updates, or external messages were created/sent.

### Suggested next action

Dry-run Hive Content Strategist, then Affiliate Video Producer. After Hive is validated, continue to Story Writing setup.

## 2026-06-22 — Hermes — Story Writing setup added after Hive

### What changed

Story Writing role-agent specs were created in `/home/hermes/projects/story-writing` after Hive setup, focused on part-time Book 1 progress:

- Story Director / Bookrunner
- Continuity & Canon Keeper
- Plot Architect
- Character Psychologist
- Worldbuilding & Cultural Researcher
- Prose Stylist / Line Editor
- Visual Prompt Designer

Central registry updated to mark Story Writing specs ready.

### Boundary

No chapter files were rewritten and no publishing/automation/container action was taken.

### Suggested next action

Dry-run Hive Content Strategist first if continuing Hive, or Story Director / Bookrunner if switching to Story Writing.

## 2026-06-22 — Hermes — Hive affiliate-first focus recorded

### What changed

Hive sub-agent setup was refined to focus on affiliate marketing first, especially Shopee/TikTok AI short-form product videos.

The Hive repo now has affiliate-first sub-agent specs for product research, hook/script writing, AI video prompts, compliance review, queue management, and performance review.

### Boundary

No content was published, no posts were scheduled, no affiliate dashboard/account was accessed, no paid action was taken, and no automation or containers were created.

### Suggested next action

Dry-run `Hive Affiliate Market Lead` using one product/link, likely the PetMarra cat food link already in Hive files unless Jude provides another product.

## 2026-06-22 — Hermes — Cross-project Tool Scout agent added

### What changed

Added a cross-project agent to recommend helpful tools/apps/AI services for Jude's projects:

```text
agents/tool-scout/AGENT.md
workflows/tool-scout-recommendations.md
```

Purpose: suggest useful tools, with free/open-source/freemium options preferred, for BBX, Hive affiliate marketing, Story Writing, Job Market Digital, Atlas Capture, and JAM AI Workspace operations.

### Boundary

Manual-dry-run-ready only. No apps/extensions/packages were installed, no accounts created, no paid trials/subscriptions started, no external services connected, and no cron was enabled.

### Suggested next action

Run a manual Tool Scout dry-run for one focus area, e.g. `Story Writing visual/comic tools` or `Hive affiliate video tools`. If useful, ask Jude to approve a weekly read-only recommendation cron.

