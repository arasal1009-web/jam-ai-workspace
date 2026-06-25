# Claude Instructions — JAM AI Workspace

This is Jude's JAM AI Workspace. Use it as shared context instead of relying only on the current Claude chat.

## Correct paths

| Environment | Root |
|---|---|
| PC | `D:\JAM AI Workspace` |
| VPS / Hermes | `/home/hermes/projects/jam-ai-workspace` |

Do not use old paths:

- `D:\A - Work`
- `C:\Users\Admin\Claude\Projects`
- `/home/hermes/wat-backup`

## Operating framework

Follow WAT:

- **Workflows** = Markdown SOPs.
- **Agents** = AI assistants that coordinate decisions.
- **Tools** = deterministic scripts.

## Required behavior

Before significant work:

1. Read `AGENTS.md`.
2. Read `SOURCE_OF_TRUTH.md`.
3. Read `JUDE_OS.md`.
4. Read `PROJECTS.md`.
5. Check `HANDOFF.md` and `DECISIONS.md`.
6. Read the relevant project `AGENTS.md`, workflow, and agent spec.

For BBX/SpeedBiz/member-check work, also read:

1. `/home/hermes/projects/bbx/AGENTS.md`
2. `/home/hermes/projects/bbx/workflows/speedbiz-member-fit-check.md`
3. `/home/hermes/projects/bbx/templates/speedbiz-outreach.md`
4. The relevant BBX agent spec, usually `member-intelligence-trade-match` or `email-message-drafting`.

On Jude's PC, use the equivalent path under `D:\JAM AI Workspace\BBX`.

## Coordination with Hermes and Codex

- Hermes is Jude's coordinator and has persistent context, but Claude does not automatically share that memory.
- Durable context must be read from and written to the shared repo files.
- If Hermes gives a task handoff, preserve its boundaries and source-of-truth references.
- If you produce a durable decision, workflow change, or handoff, update the appropriate Markdown file if Jude approved the change.

## File organization

- Put SOPs and repeatable processes in `workflows/`.
- Put scripts in `tools/`.
- Put project-specific materials inside the relevant project folder.
- Use `.tmp/` only for disposable scratch work.

## Safety rules

- Do not invent policy, legal, financial, HR, CRM, member, or website details.
- If information is missing, label it as missing or add it under Open Questions.
- Do not publish, email, delete, share, or externally upload anything without Jude's approval.
- Do not create or enable automation without Jude's approval.
- Do not commit secrets, credentials, tokens, private keys, OAuth stores, or `.env` files.
