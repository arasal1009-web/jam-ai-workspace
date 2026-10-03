# Weekly Tool Scout Report — 2026-10-03

## Focus this week

**Focus areas:**

1. **JAM AI Workspace + all project repos — secret/leak prevention before commits and pushes.** Jude’s workspace now spans multiple GitHub-backed projects with repo mirrors, handoffs, exports, docs, and future scripts. The highest-risk recurring failure is accidentally committing `.env`, OAuth stores, API keys, CRM/affiliate exports, or private tokens while agents are syncing files.
2. **BBX / Atlas / AI Agency support — safe preflight checks before handling client/member/evidence files.** These projects increasingly depend on exported tables, screenshots, document mirrors, and scripts. A local secret-scan preflight is a low-friction safety layer before any agent suggests `git add`, `git commit`, or project sync.

**Why this focus:** recent Tool Scout reports covered document ingestion, static docs/search, website QA, AI-operable research crawlers, video tools, and local writing QA. This week focuses on repo hygiene/security because it protects every active project and aligns with the central rule: never commit secrets, credentials, tokens, private keys, OAuth stores, or `.env` files.

**Boundary followed:** no software/packages/extensions were installed, no accounts/API keys were created, no private files were uploaded, no services were connected, no workflows were changed as final, and no automation/cron/container was created.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **Gitleaks** | **Free / open-source; MIT.** GitHub API checked 2026-10-03: `gitleaks/gitleaks`, 29,620 stars, updated 2026-10-02. README says Gitleaks is feature-complete and future releases are security patches only. | **5/5** — CLI, Docker image, GitHub Action, config files, scripted scans. | **JAM AI Workspace**, BBX, Atlas, Hive, Story Writing, AI Agency, Music Production. | Best first local scanner before commits/pushes. Agents can run a read-only scan and report findings without exposing data to hosted services. Good match for WAT “tools do deterministic checks.” | Installing binary/package or enabling hooks/CI needs approval. Findings can include false positives; never paste real secret values into Telegram/reports. | **No-install next step:** approve a Markdown-only “secret-scan preflight checklist” first. Later, if approved, test Gitleaks on a harmless sample repo or public fixture before scanning private repos. |
| **detect-secrets** | **Free / open-source; Apache-2.0.** GitHub API checked 2026-10-03: `Yelp/detect-secrets`, 4,648 stars, updated 2026-10-02. PyPI checked: `detect-secrets 1.5.0`. | **5/5** — Python CLI, baseline workflow, pre-commit-friendly, scriptable. | **JAM repo hygiene**, Story/Atlas docs mirrors, BBX exports/scripts. | Strong fit for maintaining an allowlisted baseline: once known false positives are reviewed, future scans can focus on newly introduced leaks. Useful for multi-project agent work where the scanner should not block every historical false positive forever. | Installing/running needs approval. Baseline review is human-sensitive: if it detects possible secrets, Jude should rotate/remove anything real rather than simply allowlisting it. | **Safe planning step:** define a policy: baseline file may be committed only after manual review and must not include secret values in reports. |
| **TruffleHog** | **Free / open-source; AGPL-3.0.** GitHub API checked 2026-10-03: `trufflesecurity/trufflehog`, 28,245 stars, updated 2026-10-03. README says it finds leaked credentials and highlights verification/analysis. | **4/5** — CLI-oriented; can scan Git and other sources; verification features are powerful but need careful handling. | **Deeper audits** for JAM/BBX/Atlas/AI Agency repos after Gitleaks/detect-secrets. | Best phase-2 scanner when Jude wants higher confidence or verification-oriented checks, especially before making a repo public or sharing with another assistant/client. | More powerful and potentially noisier. AGPL license and verification/network behavior should be reviewed before business/client use. Do not scan external/cloud sources or verify credentials without explicit approval. | **Defer until needed:** use only after a local Gitleaks/detect-secrets workflow is agreed, and run on non-sensitive samples first. |
| **pre-commit** | **Free / open-source; MIT.** GitHub API checked 2026-10-03: `pre-commit/pre-commit`, 15,608 stars, updated 2026-10-02. PyPI checked: `pre-commit 4.6.2`. | **5/5** — hook framework, local CLI, config-as-code, works with many languages/tools. | **All GitHub-backed project repos.** | Not a scanner by itself, but the best way to make the scanner repeatable before commits: format checks, secret checks, Markdown hygiene, large-file prevention. Agents can inspect `.pre-commit-config.yaml` and run hooks deterministically. | Installing hooks changes local developer behavior and needs approval. Bad hook configs can slow Jude down, so start with a manual command/checklist before enforcing hooks. | **Safe trial later:** draft a disabled/not-installed sample `.pre-commit-config.yaml` in `.tmp/` showing how Gitleaks/detect-secrets could run, then Jude can approve or reject. |
| **git-secrets** | **Free / open-source; Apache-2.0.** GitHub API checked 2026-10-03: `awslabs/git-secrets`, 13,410 stars, updated 2026-10-02. README says it prevents committing passwords and sensitive info and supports `--scan`, `--scan-history`, and AWS patterns. | **4/5** — Git hooks + CLI; AWS-focused patterns; scriptable. | **AI Agency / JAM ops** if AWS-style credentials ever appear; general repo guardrail. | Useful lightweight guard when AWS keys are the main risk. Less broad than Gitleaks/TruffleHog but simple and mature. | Installing hooks or registering global patterns needs approval. Do not rely on it as the only scanner for non-AWS secrets. | **Defer:** keep as a specialized add-on if Jude later handles AWS/cloud credentials. |

## Best pick this week

**Best pick: Gitleaks as the first scanner, with detect-secrets as the baseline/history companion.**

Why: Gitleaks is the simplest high-value “scan before push” candidate across every repo, while detect-secrets adds a reviewed baseline pattern that suits Jude’s multi-project workspace. Together they support a safe, repeatable workflow without uploading private files:

```text
Agent prepares repo changes
  → agent checks git status/diff
  → secret-scan preflight runs locally (future approval needed before installing/running scanner)
  → report only filenames + redacted finding types, never secret values
  → human/agent removes or ignores false positives with review notes
  → commit/push only after clean or approved-redacted result
```

This week’s practical recommendation is **not** to install anything yet. The safest immediate step is to document the preflight checklist first, then later approve one local scanner test on a harmless sample.

## Free/open-source alternatives

- **detect-secrets alone** — best if Jude wants a baseline-first Python workflow and fewer “new vs old finding” headaches.
- **TruffleHog** — stronger deeper audit/verification option, but better after the basic scan workflow is stable.
- **pre-commit** — best enforcement layer after Jude is comfortable with scanner behavior.
- **git-secrets** — good AWS/key-pattern-focused hook, but narrower than Gitleaks.
- **Existing `.gitignore` + careful `git add --dry-run`** — still mandatory, but not enough by itself because secrets can appear in ordinary tracked files.

## Manual-only tools to avoid or defer

- Manual eyeballing of diffs as the only secret check; agents can miss credentials hidden in long JSON, CSV, notebook, or OAuth files.
- Browser-only “repo security dashboards” as the first layer; local checks should catch issues before they reach GitHub.
- Enforcing pre-commit hooks across every repo before one sample scan is reviewed; that could slow Jude/agents down with false positives.
- Any scanner workflow that pastes detected secret values into Telegram, Notion, GitHub issues, or reports.

## Approval needed from Jude

Jude approval is needed before:

- installing Gitleaks, detect-secrets, TruffleHog, pre-commit, git-secrets, binaries, packages, hooks, Docker images, or GitHub Actions;
- scanning private repos/files if scan results might reveal sensitive filenames or tokens outside the local machine;
- committing scanner baselines/configs to project repos;
- enabling pre-commit hooks, CI checks, GitHub Actions, scheduled scans, webhooks, or notifications;
- rotating/removing credentials if a real leak is found;
- connecting GitHub security tools, third-party dashboards, or hosted monitoring services.

## Next safe action

**Safest next action with no install and no external writes:** create a Markdown-only **Repo Secret-Scan Preflight SOP** under `workflows/` or `.tmp/` after Jude approves the doc change. It should define:

1. run `git status` and inspect staged/untracked files before every commit;
2. never commit `.env`, OAuth stores, browser profiles, credential exports, API keys, private keys, or client/member/affiliate credentials;
3. if a scanner later runs, report only redacted finding type + file path + line number, never the secret value;
4. if a real secret is found, stop commit/push and rotate/remove it before continuing;
5. start with one repo/manual run before adding hooks or CI.

## Sources checked

- Local JAM AI Workspace docs and handoffs: `AGENTS.md`, `agents/README.md`, `agents/tool-scout/AGENT.md`, `workflows/tool-scout-recommendations.md`, `PROJECTS.md`, central `HANDOFF.md`, and recent durable Tool Scout reports to avoid repeating the previous focus.
- GitHub API metadata checked 2026-10-03 for: `gitleaks/gitleaks`, `trufflesecurity/trufflehog`, `Yelp/detect-secrets`, `pre-commit/pre-commit`, and `awslabs/git-secrets`.
- PyPI JSON checked 2026-10-03 for: `pre-commit` and `detect-secrets`.
- Official GitHub README/raw sources checked 2026-10-03 for Gitleaks, TruffleHog, detect-secrets, pre-commit, and git-secrets to confirm CLI/hook/baseline positioning and licensing notes.
