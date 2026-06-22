# JAM AI Sub-Agent Registry

This folder is the agent-readable registry for Jude's planned role agents and sub-agents.

**Status:** setup/planning only. These files do **not** create Docker containers, enable cron jobs, send messages, or start autonomous work.

## Current operating boundary

Jude's target architecture is:

```text
Jude / Notion Command Center
        ↓
Central JAM AI Workspace source of truth
        ↓
Project role agents, eventually one Docker container per major role agent
        ↓
Sub-agents for research, drafting, QA, logging, and tool execution
```

For now, we are setting up **instructions and registries** only. Running containers or enabling automations requires a separate explicit approval from Jude.

## Repository map

| Project | Project repo/path | Existing sub-agent plan | Immediate setup status |
|---|---|---|---|
| BBX | `/home/hermes/projects/bbx` | `/home/hermes/projects/bbx/agents/README.md` | **Role-agent specs created**; manual Account Manager Lead dry-run is next |
| Atlas Capture | `/home/hermes/projects/atlas-capture` | `/home/hermes/projects/atlas-capture/agents/README.md` | Ops/documentation agents planned |
| AI Agency / Job Market Digital | `/home/hermes/projects/ai-agency` | `/home/hermes/projects/ai-agency/agents/README.md` | Website-building business agents planned |
| Story Writing | `/home/hermes/projects/story-writing` | `/home/hermes/projects/story-writing/agents/README.md` | Book 1 creative/revision agents planned |
| Hive | `/home/hermes/projects/hive` | `/home/hermes/projects/hive/agents/README.md` | **Role-agent specs created**; manual content strategist dry-run is next |
| Scheduled routines | `/home/hermes/projects/jam-ai-workspace/Scheduled` | `/home/hermes/projects/jam-ai-workspace/Scheduled/morning-briefing/SKILL.md` | Morning briefing cron exists |

## Shared rules for all role agents and sub-agents

1. Follow WAT:
   - **Workflows** define repeatable SOPs.
   - **Agents** decide, coordinate, and escalate.
   - **Tools** execute deterministic scripts.
2. Read the project `AGENTS.md` first, then this central registry when doing cross-project work.
3. Use Notion Command Center for human-facing tasks and priorities.
4. Use GitHub/VPS Markdown files for agent-readable operating context.
5. Prefer Python/scripts for bulk table/file operations.
6. Use LLM sub-agents for judgment-heavy, bounded work: research synthesis, copy drafting, QA review, continuity checking, and prioritization.
7. Never treat hidden chat history as source of truth.
8. Never commit secrets, tokens, OAuth files, `.env`, private keys, browser profiles, or credential exports.
9. Ask Jude before:
   - creating/running Docker containers;
   - enabling cron jobs or automations;
   - sending messages/emails;
   - updating CRM or other external systems;
   - deleting files/records;
   - spending money or making legal/HR/payroll commitments.

## Agent specification standard

Each role agent should eventually have an `AGENT.md` file using `templates/sub-agent-spec.md`.

Minimum fields:

- agent name;
- project;
- mission;
- allowed inputs;
- outputs;
- workflows it may use;
- tools/scripts it may run;
- approval gates;
- sub-agents it may call;
- container profile, if/when Docker is approved.

## Recommended next implementation sequence

1. **BBX first** — role-agent specs and manual dry-runs completed; real calls/CRM depend on market windows and PC-local workflows.
2. **Hive next** — role-agent specs are now created; dry-run low-attention content/affiliate workflows while Jude is between higher-focus work.
3. **Story Writing next after Hive** — create or refine Book 1-focused agents for canon, continuity, character, proofing, and visual prompts.
4. **Atlas Capture later** — create agents around dispute process, documentation mirrors, and meeting-to-actions.
5. **AI Agency / Job Market Digital later** — create website/funnel/content agents after first website scope is chosen.

## Docker/container note

The Docker-ready shape is documented in `runtime/docker-role-agent-blueprint.md`, but no container should be created until Jude approves the specific agent.
