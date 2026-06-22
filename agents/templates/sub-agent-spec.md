# [Agent Name]

**Status:** planned / draft / active  
**Project:** [Project name]  
**Parent role agent:** [Optional]  
**Owner:** Jude / Hermes / Claude / Codex / other  
**Last updated:** YYYY-MM-DD

## Mission

One paragraph describing what this sub-agent is responsible for and what outcome it exists to produce.

## Scope

### This agent may do

- [Allowed responsibility]
- [Allowed responsibility]

### This agent must not do without Jude approval

- Send external messages or emails.
- Publish content.
- Update CRM or other external systems.
- Delete or overwrite source-of-truth files.
- Enable automation, cron, or containers.
- Spend money or make legal/HR/payroll commitments.

## Inputs

| Input | Source | Required? |
|---|---|---|
| [Input name] | [Notion / Google Sheet / repo path / user message] | Yes/No |

## Outputs

| Output | Destination | Format |
|---|---|---|
| [Output name] | [Repo / Notion / Google Docs / Telegram draft] | Markdown / CSV / task list |

## Required reading

1. Project `AGENTS.md`.
2. Central JAM AI Workspace files:
   - `/home/hermes/projects/jam-ai-workspace/AGENTS.md`
   - `/home/hermes/projects/jam-ai-workspace/SOURCE_OF_TRUTH.md`
   - `/home/hermes/projects/jam-ai-workspace/JUDE_OS.md`
   - `/home/hermes/projects/jam-ai-workspace/agents/README.md`
3. Relevant project workflows.

## Workflows this agent follows

- `[workflow path]` — [purpose]

## Tools/scripts this agent may use

- `[tool path]` — [purpose]

## Sub-agents this agent may call

| Sub-agent | When to call | Expected output |
|---|---|---|
| [Name] | [Trigger] | [Output] |

## Handoff format

When finished, report:

1. Task completed.
2. Files/data read.
3. Files/data changed.
4. Decisions made.
5. Blockers or approval needed.
6. Recommended next action.

## Container profile — future only

Do not create this container until Jude approves.

| Field | Planned value |
|---|---|
| Container name | `[project-agent-name]` |
| Workdir | `[repo path]` |
| Toolsets | `[terminal,file,web,...]` |
| Env needed | `[names only, no secrets]` |
| Network access | `[none/read-only/web/etc.]` |
| Schedule | `[manual/cron TBD]` |
