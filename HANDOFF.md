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

