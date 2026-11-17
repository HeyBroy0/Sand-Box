# Sand-Box

A small, modular workspace for reusable scripts, ChatGPT-friendly workflows, and GitHub Actions.

> **Operating principle: small core, expandable capabilities.** Keep the always-read entrypoint short. Load detailed instructions and tool implementations only when the current task needs them. Prefer extending a reusable capability over accumulating one-off tools.

## Start here

At the beginning of a repository task, read this file first. Coding agents that support repository instructions can also read [AGENTS.md](AGENTS.md) automatically; other ChatGPT/GitHub-connected workflows may retrieve repository content on demand, so explicitly ask the agent to read this README rather than assuming it has loaded the repository.

### 1. Start from the correct repository state

Inspect the current branch/ref, working tree, relevant open pull requests, and repository tree before editing. Do not assume that `main`, a previous conversation, or a search result represents the current working state.

For a **new task**, create a separate branch from the latest `main` and use the `temp/` prefix:

```bash
git fetch origin
git status --short
git switch main
git pull --ff-only origin main
git switch -c temp/<short-task-name>
```

Choose a different suffix if that branch already exists. Do not discard existing local changes. When continuing work on an existing pull request, continue on that PR's head branch instead of creating another branch. Keep changes reviewable and do not commit directly to `main`.

When working through GitHub APIs rather than a local clone, apply the same rule: create the `temp/<short-task-name>` branch from the current `main` ref, or continue the explicitly relevant open PR branch.

### 2. Load only the instructions needed for this task

| Task | Read |
| --- | --- |
| Change repository architecture, core behavior, instruction routing, catalog schema/discovery contract, or shared infrastructure | **Required first:** [Core change gate](core/check-core-readme-first/core-readme.md) |
| Find an existing capability or decide whether a new tool is needed | [Finding tools](core/finding-tools/README.md) |
| Build or substantially change a reusable tool | Read [Finding tools](core/finding-tools/README.md) first, then [Tool-building instructions](core/tool-building-instructions.md) |
| Clean up files, workflows, artifacts, or branches | [Cleanup instructions](core/clean-up.md) |
| Use or modify one known capability | Read its entry in [tools/catalog.json](tools/catalog.json), then open only the relevant script, workflow, and tests |
| Make an ordinary content change that does not affect core rules | Read the relevant file and its immediate dependencies; no extra core documents are needed |

The core documents are a task-specific reference library, **not** a bundle to load at startup. Do not read every file in `core/` for an ordinary tool run or isolated change. If no existing tool fits, use the tool-building instructions to decide whether a new composable capability is justified.

### 3. Search is not a complete repository inventory

Use search to find likely files, symbols, and examples. Do not treat search results as proof that a file or capability does not exist.

GitHub Code Search currently indexes only default branches and does not index every file. ChatGPT's GitHub connection retrieves permitted content on demand; it does not automatically sync the entire repository into the conversation. For structural work, list the repository tree on the **target ref** or inspect a local clone, then fetch the specific files needed. Useful references: [GitHub Code Search limitations](https://docs.github.com/en/search-github/github-code-search/using-github-code-search) and [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt-deep-research).

Examples for a local clone:

```bash
# Complete tracked-file inventory on the current ref
git ls-tree -r --name-only HEAD

# Search source and documentation after inspecting the tree
git grep -n "search term"
```

When using GitHub APIs, request a recursive tree for the target branch/commit and fetch files by their exact paths. A code-search query is a locator, not a substitute for tree inspection.

## What belongs in core

`core/` contains durable repository-wide operating rules and task-specific instructions. It does **not** contain everyday tools, individual tool source code, user data, or routine reports. Tool implementations stay in their natural locations such as `scripts/`, workflows in `.github/workflows/`, and discovery metadata in `tools/catalog.json`.

Core is limited to contracts that affect how the repository is maintained or how multiple capabilities work together: the agent entrypoint and task routing, tool-discovery/catalog behavior, shared input/output conventions, and genuinely shared validation or automation infrastructure. An isolated feature or a normal new script is not automatically a core change.

A change to any of those core surfaces must pass through [the core change gate](core/check-core-readme-first/core-readme.md) **before editing**. The gate defines scope, compatibility review, required tests, and documentation updates.

## Available capabilities

The catalog is the single source of truth for reusable capabilities and their script/workflow entrypoints.

| Capability | Purpose |
| --- | --- |
| Dataset analysis | Profile CSV, TSV, JSON, JSONL/NDJSON, XLSX, and XLS data |
| ZIP archive access | Inventory archive members, find candidates, and selectively extract one member |
| File export and handoff | Copy a file from `data/`, verify SHA-256, and validate DOCX packages |
| Tool discovery | Search grouped capabilities by name, purpose, tags, aliases, and entrypoint |
| Workflow cleanup | Review and prune completed Actions runs and eligible unprotected branches |

Search the catalog locally:

```bash
python scripts/find_tool.py
python scripts/find_tool.py "csv excel"
python scripts/find_tool.py "zip archive" --kind script
python scripts/find_tool.py --tag files --tag export
python scripts/find_tool.py --list-tags
python scripts/find_tool.py --format json
python scripts/find_tool.py --validate
```

Search ranks partial and multi-term matches. Repeated `--tag` filters require every supplied tag. Use `--sort name` for alphabetical output and `--limit 20` to show more results.

## Run capabilities

GitHub Actions is the remote execution path for supported repository workflows. It runs on a GitHub-hosted runner rather than ChatGPT's built-in data-analysis session or your local environment. This does not change GitHub Actions quotas, repository permissions, runner availability, or ChatGPT product limits.

Open **Actions**, choose the matching workflow, select **Run workflow**, provide the repository-relative input path or options, and download the resulting artifact.

### Dataset analysis

Add an input file under `data/`, then supply its repository-relative path when launching **Dataset analysis**. JSON Lines and NDJSON are read in line-oriented mode.

Local use:

```bash
python -m pip install -r requirements-analysis.txt
python scripts/analyze_dataset.py --input data/file.csv --output-dir analysis-output
```

### ZIP archive access

Place the ZIP file under `data/`, then run **ZIP archive access**:

1. **List** inventories member paths, extensions, file sizes, compressed sizes, and safety notes without extracting files.
2. **Find** searches partial names/paths, glob patterns, and extensions.
3. **Extract** retrieves one exact member path. A partial query is accepted only when it resolves to exactly one member; ambiguous results must be narrowed with **Find** first.

The workflow does not unpack the whole archive. It rejects traversal/absolute paths, symbolic links, encrypted entries, and members over the configured size limit. Outputs are returned as one-day artifacts, with integrity metadata for extracted files.

Local use:

```bash
python scripts/zip_archive.py list --archive data/archive.zip
python scripts/zip_archive.py find --archive data/archive.zip --query report --extension pdf
python scripts/zip_archive.py extract --archive data/archive.zip --member documents/report.pdf
```

### File export and handoff

**Library file handoff** stages one file from `data/` as a one-day artifact. Copies are verified by SHA-256; DOCX files also receive Open XML package validation. This workflow does not upload directly to ChatGPT Library. Use ZIP archive access when the desired file is inside an archive.

## Repository map

- `AGENTS.md` — small entrypoint for compatible coding agents
- `core/` — durable repository rules and task-specific instruction files, loaded only when relevant
- `scripts/` — reusable command-line implementations
- `tools/catalog.json` — grouped capability discovery metadata
- `.github/workflows/` — focused GitHub Actions entrypoints
- `tests/` — unit tests
- `data/` — workflow input files and retained source documents
- `reports/` — retained reports and review outputs

## Maintenance baseline

- Search the catalog and inspect nearby implementations before adding a capability.
- Prefer one composable capability with a small number of useful operations over multiple near-duplicate tools.
- Keep shared logic in scripts; workflows should orchestrate rather than duplicate implementation.
- Keep optional dependencies scoped to the capabilities that need them.
- Prefer focused workflows, explicit inputs, minimal permissions, short-lived artifacts, and non-destructive defaults.
- Keep experimental work on isolated branches. Mark a capability experimental or deprecated only when that distinction affects how it should be used; do not add metadata fields without a concrete need.
- Preserve `data/` and `reports/` by default. See [cleanup instructions](core/clean-up.md) before deleting or pruning anything.
- Never commit credentials, secrets, private information, or confidential files. This is a public repository.

Before merging a pull request, run:

```bash
python scripts/find_tool.py --validate
python -m unittest discover -s tests -v
```

The Tests workflow also runs Python compilation, catalog validation, and the unit-test suite for pull requests and pushes to `main`. Keep changes in a reviewable pull request; do not merge unless the repository owner explicitly asks.
