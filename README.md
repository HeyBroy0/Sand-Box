# Sand-Box
Reusable scripts and GitHub Actions workspace.

## Start here
1. For new work, branch from the latest `main` as `temp/<task-name>`.
2. Work on the same task-branch when extending that work. Commit completed changes directly to the task-branch; without PR unless asked.
3. Never commit or push directly to `main` unless specifically asked
4. Guidance/Instructions found below, read only what is necessary to preserve context window.

| Task | **Required:** Read before proceeding |
| --- | --- |
| Changing repository architecture, core behavior (core/ files) | [Core change gate](core/check-core-readme-first/core-readme.md) |
| Instruction routing |
| Find or select an existing tool; decide whether a new tool is needed | [Finding tools](core/finding-tools/README.md) |
| Build or substantially change a reusable tool | [Finding tools](core/finding-tools/README.md), then [Tool-building instructions](core/tool-building-instructions.md) |
| Remove files, workflows, artifacts, branches, or clean up | [Cleanup instructions](core/clean-up.md) |
| Use or modify one known capability | Find it in [the catalog](tools/catalog.json), then inspect only its listed entrypoint(s) and relevant tests |
| Make an ordinary content change | Read the target file and its immediate dependencies |

## Repository discovery
Search is a locator, not a complete file inventory. In this GitHub connection, code search covers the default branch and may not expose every file or the current working branch. For structural work, inspect the recursive tree of the **target ref** first (or run `git ls-tree -r --name-only HEAD` in a local clone), then fetch only the relevant files. Do not infer that a file or capability is absent from an empty search result.

## Directory map

- `AGENTS.md` — short entrypoint for compatible coding agents
- `core/` — durable rules and task-specific instructions; load only when routed here
- `core/Instruction-decision-tree/` — Place to store Instructions
- `scripts/` — reusable implementations
- `tools/catalog.json` — capability index
- `.github/workflows/` — GitHub Actions interfaces
- `tests/` — automated tests
- `data/`, `reports/` — retained input material and output reports

This repository is public. Never commit credentials, secrets, private information, or confidential files.
