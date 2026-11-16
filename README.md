# Sand-Box

Public workspace for stable tools, scripts, and focused GitHub Actions. Keep `main` small, dependable, and easy to navigate.

## Start here

- **Find a tool:** `python scripts/find_tool.py "csv excel"`; add `--format json` for compact agent output. Leave the query blank to list the first five; use `--limit 20` for the full catalog.
- **Dataset analysis:** Actions → **Dataset analysis** → **Run workflow**. Select a file under `data/`; download the results artifact.
- **Repository cleanup:** Actions → **Clean workflows** → **Run workflow**. Run-history cleanup and branch cleanup have separate confirmations. Set `keep_recent_runs` to the number of newest completed runs to retain.
- **Tool lookup in Actions:** Actions → **Tool lookup** → **Run workflow**. Search by name, purpose, tag, alias, or path.

## Tool maintenance

`tools/catalog.json` is the compact source of truth for discovery. Add one short entry whenever a reusable script or workflow is added, renamed, or removed. Keep summaries under 180 characters; use tags and aliases for common search terms. Do not copy full documentation or source into the catalog. Validate with `python scripts/find_tool.py --validate` and test with `python -m unittest discover -s tests -v`.

Put reusable scripts in `scripts/`, inputs in `data/`, and durable reports in `reports/` (or workflow artifacts for temporary outputs). Add one focused workflow per capability under `.github/workflows/`; prefer manual `workflow_dispatch` and grant only required permissions. Reuse existing tools and native AI/client capabilities rather than duplicating them unless a concrete constraint requires it.

## Branch and repository rules

- Update `main` only with stable, working tools and concise instructions. Keep experiments off `main`.
- Never overwrite or modify `archive/` branches. Before risky work, create a new snapshot such as `archive/main-YYYY-MM-DD-topic`; use `protect/` for branches that cleanup must retain.
- Cleanup always preserves the default branch, `archive/*`, `protect/*`, GitHub-protected branches, and branches referenced by open pull requests. Other branches are deletion candidates only after the separate branch-cleanup confirmation.
- This is a public repository: never commit credentials, secrets, private information, or confidential files.

## One-time history reset

To make `main` a single initial commit, open Actions → **One-time history reset** → **Run workflow** on `main`, set `confirm_reset` to `true`, and enter `RESET MAIN HISTORY` exactly. The `archive/main-2026-11-16-pre-maintenance` snapshot preserves the previous history. The workflow uses a force-with-lease update and removes itself from the new root commit; do not recreate or rerun it.

## Adding or changing a tool

1. Check the catalog before building something new.
2. Implement the reusable tool under `scripts/` or as a focused workflow.
3. Add or update its short catalog entry and README instructions only when needed.
4. Run catalog validation and tests before updating `main`.
