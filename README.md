# Sand-Box

Reusable scripts and GitHub Actions workspace.

> **Guiding principle: small core, expandable capabilities.** Keep durable cross-repository rules in `core/`; keep everyday tools in `scripts/`, workflows in `.github/workflows/`, and their index in `tools/catalog.json`.

## Start here

1. Inspect the current target ref, working state, open work branches, and relevant file tree.
2. For new work, branch from the latest `main` as `temp/<short-task>`. Continue on the existing task branch when extending that work.
3. Commit completed changes directly to the task branch; do not create a PR unless requested. Never commit or push directly to `main` unless specifically asked.
4. Load only the instructions needed for the task. Do not preload all of `core/`.

| Task | Read before proceeding |
| --- | --- |
| Change a core surface: repository architecture, instruction routing, catalog/discovery contracts, shared behavior, or repository-wide validation | Start with the [Core documentation router](core/read-core-readme-first/core-readme.md), then follow its task-specific routes. |
| Change the organization, structure, or routing of instructions and guides | Start with the [Core documentation router](core/read-core-readme-first/core-readme.md), then read [Instruction architecture](core/read-core-readme-first/instruction-architecture.md). |
| Find or select an existing tool; decide whether a new tool is needed | [Finding tools](core/finding-tools/README.md) |
| Build or substantially change a reusable tool | [Finding tools](core/finding-tools/README.md), then [Tool-building instructions](core/tool-building-instructions.md) |
| Remove files, workflows, artifacts, or branches | [Cleanup instructions](core/clean-up.md). When cleanup changes a core surface, start with the Core documentation router as well. |
| Use or modify one known capability | Find it in [the catalog](tools/catalog.json), then inspect only its listed entrypoint(s) and relevant tests. |
| Make an ordinary content change | Read the target file and its immediate dependencies. |

## Repository discovery

Search is a locator, not a complete file inventory. In this GitHub connection, code search covers the default branch and may not expose every file or the current working branch. For structural work, inspect the recursive tree of the **target ref** first (or run `git ls-tree -r --name-only HEAD` in a local clone), then fetch only the relevant files. Do not infer that a file or capability is absent from an empty search result.

## Directory map

- `AGENTS.md` — short entrypoint for compatible coding agents
- `core/read-core-readme-first/` — router and task-specific guidance for changes to core surfaces
- `core/` — durable rules and task-specific instructions; load only when routed here
- `scripts/` — reusable implementations
- `tools/catalog.json` — capability index
- `.github/workflows/` — GitHub Actions interfaces
- `tests/` — automated tests
- `data/`, `reports/` — retained input material and reports

This repository is public. Never commit credentials, secrets, private information, or confidential files.
