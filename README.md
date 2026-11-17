# Sand-Box

Reusable scripts and GitHub Actions for repository tasks.

> **Guiding principle: small core, expandable capabilities.** Keep durable cross-repository rules in `core/`; keep everyday tools in `scripts/`, workflows in `.github/workflows/`, and their index in `tools/catalog.json`.

## Start here

1. Inspect the current target ref, working state, open work branches, and relevant file tree.
2. For new work, branch from the latest `main` as `temp/<short-task>`. Continue on the existing task branch when extending that work. Commit completed changes directly to the task branch; do not create a PR unless requested. Never commit or push directly to `main`.
3. Load only the task instructions below. **Do not preload all of `core/`.**

| Task | Read before proceeding |
| --- | --- |
| Change repository architecture, core behavior, instruction routing, catalog/discovery contracts, or shared infrastructure | **Required:** [Core change gate](core/check-core-readme-first/core-readme.md) |
| Find or select an existing tool; decide whether a new tool is needed | [Finding tools](core/finding-tools/README.md) |
| Build or substantially change a reusable tool | [Finding tools](core/finding-tools/README.md), then [Tool-building instructions](core/tool-building-instructions.md) |
| Remove files, workflows, artifacts, or branches | [Cleanup instructions](core/clean-up.md) |
| Use or modify one known capability | Find it in [the catalog](tools/catalog.json), then inspect only its listed entrypoint(s) and relevant tests |
| Make an ordinary content change | Read the target file and its immediate dependencies |

The `core/check-core-readme-first/` directory is deliberately an on-demand instruction gate for core changes. Its `core-readme.md` must be added to context before planning, editing, or reviewing such work; ordinary tool tasks should normally ignore it.

## Repository discovery

Search is a locator, not a complete file inventory. In this GitHub connection, code search covers the default branch and may not expose every file or the current working branch. For structural work, inspect the recursive tree of the **target ref** first (or run `git ls-tree -r --name-only HEAD` in a local clone), then fetch only the relevant files. Do not infer that a file or capability is absent from an empty search result.

## Tool catalog

[`tools/catalog.json`](tools/catalog.json) is the single index of reusable capabilities and their script/workflow entrypoints. Search it with:

```bash
python scripts/find_tool.py "search terms"
python scripts/find_tool.py --format json
python scripts/find_tool.py --validate
```

For local verification, run:

```bash
python scripts/find_tool.py --validate
python -m unittest discover -s tests -v
```

## Directory map

- `AGENTS.md` — short entrypoint for compatible coding agents
- `core/` — durable rules and task-specific instructions; load only when routed here
- `scripts/` — reusable implementations
- `tools/catalog.json` — capability index
- `.github/workflows/` — GitHub Actions interfaces
- `tests/` — automated tests
- `data/`, `reports/` — retained input material and reports

This repository is public. Never commit credentials, secrets, private information, or confidential files.
