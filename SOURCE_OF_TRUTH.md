# Source of Truth

This file defines where information should live.

## Canonical Locations

| Information Type | Canonical Location |
|---|---|
| Agent instructions | GitHub repo root: AGENTS.md / CLAUDE.md |
| Workflows and SOPs | workflows/ |
| Deterministic scripts/tools | tools/ |
| Project materials | Project folders: Atlas Capture, BBX, etc. |
| Documentation originals | Google Drive/Docs/Sheets or project folder `documentation/originals/` |
| Documentation Markdown mirrors | Project folder `documentation/markdown/` or relevant `workflows/` file; committed to GitHub/VPS |
| Cross-assistant handoffs | HANDOFF.md |
| Durable decisions | DECISIONS.md |
| Project registry | PROJECTS.md |
| Human dashboard/task tracking | Notion Command Center |
| Project source of truth / knowledge | Notion JAM AI Source of Truth |
| Cloud documents/deliverables | Google Drive / Docs / Sheets; Markdown equivalent must exist in GitHub when agents need to work from it |
| VPS copy | /home/hermes/projects/jam-ai-workspace after GitHub clone |

## Documentation Rule

For Word documents, Google Docs, Google Sheets, Excel files, PDFs, and similar files:

1. Keep the original document in the appropriate cloud/project location.
2. Create an equivalent Markdown mirror for agent/VPS use.
3. Commit the Markdown mirror to GitHub so Hermes/VPS can read and diff it.
4. Do not treat `.docx`, `.xlsx`, `.pdf`, or Google-native files as the only source available to agents.
5. If the original file changes, update the Markdown mirror in the same commit or handoff.

Recommended project-level structure:

```text
<Project>/
  documentation/
    originals/   # optional local copies of .docx, .xlsx, .pdf, exports
    markdown/    # .md mirrors committed for GitHub/VPS/agents
```

Use `workflows/` instead of `documentation/markdown/` when the document is an SOP or repeatable process.

## Sync Path

The intended sync path is:

PC:
D:\JAM AI Workspace

to:

GitHub:
private repository, to be created/connected

to:

VPS/Hermes:
/home/hermes/projects/jam-ai-workspace

## Stale Paths

Do not use these old paths as active source of truth:

- D:\A - Work
- C:\Users\Admin\Claude\Projects

If they appear in old project settings, treat them as stale references.
