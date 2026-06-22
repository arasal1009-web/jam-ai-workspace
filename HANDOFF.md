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

