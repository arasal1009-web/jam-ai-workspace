# JAM AI Workspace — Agent Instructions

This is Jude's main JAM AI Workspace.

## Operating Model: WAT

Jude uses the WAT framework:

- Workflows = Markdown SOPs and repeatable processes
- Agents = AI assistants that coordinate decisions and work
- Tools = deterministic scripts and utilities

## Required Reading Order

Any assistant working in this repository should read these first:

1. AGENTS.md
2. CLAUDE.md
3. SOURCE_OF_TRUTH.md
4. JUDE_OS.md
5. PROJECTS.md
6. HANDOFF.md
7. DECISIONS.md

## Project Folders

- AI Agency/
- Atlas Capture/
- BBX/
- Hive/
- Scheduled/
- Story Writing/

## Shared OS Folders

- workflows/ = SOPs and process documents
- tools/ = deterministic scripts
- .tmp/ = disposable working files, not source of truth

## Rules

- Do not treat chat history as the source of truth.
- Do not publish, email, upload, delete, or externally share anything without Jude's approval.
- Do not create or enable automation without Jude's approval.
- Do not commit secrets, credentials, tokens, private keys, or .env files.
- If a path points to C:\Users\Admin\Claude\Projects or D:\A - Work, treat it as stale.
- The correct PC workspace root is D:\JAM AI Workspace.
