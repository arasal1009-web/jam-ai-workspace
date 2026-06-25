# JAM AI Workspace

This is Jude's central AI operating workspace and the shared source of truth for Hermes, Claude, Codex, and future role agents.

## Required reading order for assistants

Before significant project work, read:

1. `AGENTS.md` — shared instructions for all assistants, especially Codex/OpenAI-style agents.
2. `CLAUDE.md` — Claude-specific operating instructions.
3. `SOURCE_OF_TRUTH.md` — where each type of information belongs.
4. `JUDE_OS.md` — Jude's operating context, preferences, and approval boundaries.
5. `PROJECTS.md` — project registry and repo/path map.
6. `HANDOFF.md` — current cross-assistant continuity.
7. `DECISIONS.md` — durable decisions.
8. Relevant project files, workflows, and agent specs.

## Sync model

```text
Hermes memory + coordination
        ↓
GitHub / Markdown shared source of truth
        ↓
Claude + Codex + other assistants read the same files before working
```

- **Option A:** GitHub/Markdown files are the shared brain.
- **Option B:** Hermes coordinates because it has Jude's persistent context and can keep repo files current.

## Structure

| Path | Purpose |
|---|---|
| `AGENTS.md` | Entry instructions for AI assistants and Codex-style agents |
| `CLAUDE.md` | Claude-specific project instructions |
| `SOURCE_OF_TRUTH.md` | Canonical homes for data, docs, tasks, and handoffs |
| `JUDE_OS.md` | Jude's operating context |
| `PROJECTS.md` | Project registry |
| `HANDOFF.md` | Cross-assistant handoffs |
| `DECISIONS.md` | Durable decision log |
| `workflows/` | SOPs and repeatable processes |
| `agents/` | Shared agent definitions and role-agent specs |
| `tools/` | Deterministic scripts/tools |
| `.tmp/` | Disposable scratch space, not source of truth |

## Projects

- AI Agency / Job Market Digital
- Atlas Capture
- BBX
- Hive
- Scheduled
- Story Writing

## Paths

| Environment | Root |
|---|---|
| PC | `D:\JAM AI Workspace` |
| VPS / Hermes | `/home/hermes/projects/jam-ai-workspace` |
| GitHub | `https://github.com/arasal1009-web/jam-ai-workspace.git` |

## Important rules

- Do not treat hidden chat history as source of truth.
- Do not publish, email, upload, delete, or externally share anything without Jude's approval.
- Do not create or enable automation without Jude's approval.
- Do not commit secrets, credentials, tokens, private keys, `.env` files, OAuth stores, or exported private data.
