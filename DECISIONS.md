# Decision Log

Use this file for durable decisions.

## Format

### YYYY-MM-DD — Decision Title

**Decision:**

**Reason:**

**Applies to:**

**Links / paths:**

### 2026-06-25 — Claude/Codex/Hermes sync model

**Decision:** Use Option A + B for assistant sync: GitHub/Markdown files are the shared source of truth, and Hermes acts as coordinator because it has Jude's persistent context.

**Reason:** Claude, Codex, and Hermes do not automatically share hidden chat memory. Shared repo files let all assistants read the same instructions, workflows, agent specs, and templates before working.

**Applies to:** JAM AI Workspace, BBX SpeedBiz checks, future multi-assistant workflows.

**Links / paths:**

- `/home/hermes/projects/jam-ai-workspace/AGENTS.md`
- `/home/hermes/projects/jam-ai-workspace/CLAUDE.md`
- `/home/hermes/projects/bbx/workflows/speedbiz-member-fit-check.md`
- `/home/hermes/projects/bbx/agents/speedbiz-fit-checker/AGENT.md`

### 2026-06-25 — Scheduled crons stay in Hermes

**Decision:** Scheduled crons/routines should stay in Hermes. The JAM AI Workspace repo can store supporting scripts, prompts, workflow docs, and mirrors, but Hermes cron is the canonical place for live schedules/jobs.

**Reason:** Hermes is the coordinator and is designed to run durable routines, deliver scheduled outputs, and manage cron job state. Claude/Codex should share instructions through GitHub but should not become the scheduler.

**Applies to:** Scheduled routines, daily briefings, BBX lead-agent cron/pilot runs, Tool Scout recommendations, future recurring assistant work.

**Links / paths:**

- Hermes cron via `hermes cron` / cronjob tool
- `/home/hermes/projects/jam-ai-workspace/SOURCE_OF_TRUTH.md`
- `/home/hermes/projects/jam-ai-workspace/AGENTS.md`
- `/home/hermes/projects/jam-ai-workspace/CLAUDE.md`
