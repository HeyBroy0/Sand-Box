# Sand-Box

A small public workspace for reusable Python utilities and focused GitHub Actions. The catalog is the single source of truth for tool discovery.

## Start here

```bash
# List capabilities
python scripts/find_tool.py

# Search names, summaries, tags, aliases, and entrypoint paths
python scripts/find_tool.py "csv excel"
python scripts/find_tool.py "library docx" --kind script
python scripts/find_tool.py --tag data --tag statistics --format json

# Inspect catalog tags and validate every registered path
python scripts/find_tool.py --list-tags
python scripts/find_tool.py --validate

# Run the test suite
python -m unittest discover -s tests -v
```

Search uses relevance ranking and partial-word matching. Multiword queries can match any term; records matching more terms rank higher. Repeated `--tag` filters require every supplied tag. Use `--sort name` for alphabetical output, `--limit 20` to show more results, and `--format json` for compact machine-readable records. The default limit is five; the maximum is 50.

## Available workflows

| Workflow | Purpose |
| --- | --- |
| **Dataset analysis** | Analyze CSV, TSV, JSON, JSONL/NDJSON, XLSX, or XLS files. Add the input file under `data/`, then provide its repository-relative path when running the workflow. |
| **Library file handoff** | Stage one file from `data/` as a one-day artifact. Every copy is SHA-256 verified; DOCX files also receive Open XML package validation. The workflow does not upload directly to ChatGPT Library. |
| **Clean workflows** | Optionally delete completed workflow runs and their artifacts, or separately clean unused branches. Both operations require explicit confirmation. |

Install analysis dependencies before running the dataset script locally:

```bash
python -m pip install -r requirements-analysis.txt
python scripts/analyze_dataset.py --input data/file.csv --output-dir analysis-output
```

## Tool catalog

`tools/catalog.json` stores one record per capability. A capability can expose multiple entrypoints, such as a local `script` and a GitHub Actions `workflow`, without appearing as duplicate search results.

Each record contains:
- `id`, `name`, and a concise `summary`
- `tags` and optional `aliases` for discovery
- `entrypoints`: one or more `kind`, `path`, and `usage` objects

Keep summaries under 220 characters. Do not copy full source or documentation into the catalog. Add a catalog entry whenever a reusable tool or workflow is added, renamed, or removed.

## Repository layout

- `scripts/` — reusable command-line tools
- `tools/catalog.json` — discovery metadata
- `.github/workflows/` — focused, manually triggered Actions
- `tests/` — standard-library unit tests
- `data/` — files used as workflow inputs
- `reports/` — retained reports and review outputs

Prefer one workflow per capability, `workflow_dispatch`, minimal permissions, and shared scripts for reusable logic. Keep optional dependencies local to the command that needs them.

## Maintenance rules

1. Search the catalog before adding another tool.
2. Group related script and workflow entrypoints under one capability.
3. Keep experiments off `main`; use a working branch and reviewable pull request.
4. Preserve the default branch, `archive/*`, `protect/*`, GitHub-protected branches, and branches referenced by open pull requests during cleanup.
5. This is a public repository. Never commit credentials, secrets, private information, or confidential files.

Validate catalog changes and run tests before merging:

```bash
python scripts/find_tool.py --validate
python -m unittest discover -s tests -v
```
