# JAM AI Workspace — Shared Agent Instructions

This is Jude's main JAM AI Workspace. Treat this repository as the shared operating context for Hermes, Claude, Codex, and future role agents.

## Operating model: WAT

Jude uses the WAT framework:

- **Workflows** = Markdown SOPs and repeatable processes.
- **Agents** = AI assistants that coordinate decisions and work.
- **Tools** = deterministic scripts and utilities.

## Coordination model: Option A + B

Jude chose the combined sync model:

1. **Option A — GitHub shared source of truth:** Claude, Codex, Hermes, and other assistants should read the same Markdown files before working.
2. **Option B — Hermes as coordinator:** Hermes keeps persistent user/project context and updates shared repo files when Jude approves durable changes.

Scheduled crons/routines should stay in Hermes. The repo may store supporting scripts, prompts, workflows, and documentation mirrors, but Hermes cron remains the canonical place for live schedules/jobs.

Do not assume another assistant has access to Hermes chat memory. If context should persist across assistants, write it into the correct repo file and commit/push when appropriate.

## Required reading order

Any assistant working in this repository should read these first:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `SOURCE_OF_TRUTH.md`
4. `JUDE_OS.md`
5. `PROJECTS.md`
6. `HANDOFF.md`
7. `DECISIONS.md`
8. Relevant project `AGENTS.md`, `CLAUDE.md`, workflows, and agent specs.

For BBX work, also read `/home/hermes/projects/bbx/AGENTS.md` and the relevant BBX workflow/agent files.

## Project folders

- `AI Agency/`
- `Atlas Capture/`
- `BBX/`
- `Hive/`
- `Scheduled/`
- `Story Writing/`

## Shared OS folders

- `workflows/` = SOPs and process documents.
- `agents/` = shared agent definitions and role-agent specs.
- `tools/` = deterministic scripts.
- `.tmp/` = disposable working files, not source of truth.

## Rules

- Do not treat chat history as the source of truth.
- Do not publish, email, upload, delete, or externally share anything without Jude's approval.
- Do not create or enable automation without Jude's approval.
- Do not commit secrets, credentials, tokens, private keys, OAuth stores, or `.env` files.
- If a path points to `C:\Users\Admin\Claude\Projects` or `D:\A - Work`, treat it as stale.
- The correct PC workspace root is `D:\JAM AI Workspace`.
- Prefer concise, practical outputs that Jude can paste into Notion, email, CRM notes, or a task.
