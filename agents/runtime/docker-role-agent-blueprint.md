# Docker Role-Agent Blueprint

This is a future runtime blueprint for Jude's role agents. It is documentation only; it does not create or start containers.

## Purpose

Jude wants major role agents to eventually run in separate Docker containers on the VPS, with each role agent able to call smaller sub-agents for bounded tasks.

## Why containers

- Isolate credentials and filesystem access by role/project.
- Keep long-running agents separate from Hermes chat sessions.
- Make failure/restart behavior clearer.
- Allow role-specific toolsets and schedules.

## Proposed container layers

```text
Base image: Python + Hermes/agent runtime dependencies
Project mount: one GitHub repo clone per project
Config mount: role-specific non-secret config
Secret source: environment variables / credential vault, never git
Logs: per-agent logs outside the repo
```

## Minimum per-agent config

| Field | Meaning |
|---|---|
| `agent_name` | Human-readable role agent name |
| `project` | Project this agent belongs to |
| `repo_path` | VPS clone path |
| `allowed_toolsets` | Toolsets available to that role |
| `read_paths` | Files/folders it may read |
| `write_paths` | Files/folders it may edit |
| `approval_gates` | Actions requiring Jude confirmation |
| `delivery_target` | Telegram/Discord/Notion/etc. if approved |
| `schedule` | Manual or cron schedule if approved |

## Default approval gates

Containers must not independently:

- send emails/messages;
- update CRM;
- publish content;
- change money/legal/HR/payroll decisions;
- delete source files;
- create new automation;
- modify credentials;
- approve their own escalation.

## Recommended first Docker candidates

| Priority | Candidate role agent | Reason |
|---|---|---|
| 1 | BBX Account Manager Lead | Most concrete daily/weekly routines and member-intelligence workflows |
| 2 | Story Writing Bookrunner | Can coordinate continuity, canon, plot, and visual prompt sub-agents |
| 3 | Atlas Operations Lead | Good fit for document/action tracking, but process approvals matter |
| 4 | Job Market Digital Website Builder | Wait until the website-building scope is chosen |
| 5 | Hive Content Strategist | Wait until naming/split decision is made |

## Setup phase separation

1. **Documentation setup** — create `AGENT.md`, workflows, tool list, approval gates.
2. **Dry-run setup** — manually invoke agents/sub-agents inside Hermes without background automation.
3. **Container setup** — create Dockerfiles/compose files after Jude approves the exact role agent.
4. **Automation setup** — enable cron/daemon only after dry-run success and Jude approval.
