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
