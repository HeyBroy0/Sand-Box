# Sand-Box

A small public workspace for reusable Python utilities and GitHub Actions. GitHub Actions is the remote execution path for repository workflows; the catalog is the single source of truth for tool discovery.

## Start here

Use GitHub Actions when you want repository processing to run on a GitHub-hosted runner rather than your local environment or ChatGPT's built-in data-analysis session:

- **Dataset analysis** — profile CSV, TSV, JSON, JSONL/NDJSON, XLSX, and XLS data.
- **ZIP archive access** — inspect archive contents, find candidate files, and extract one selected member.
- **Library file handoff** — validate and stage one file from data/ as a short-lived artifact.
- **Tool lookup** — search the catalog directly in Actions.

Open the repository's Actions tab, select the workflow, and choose Run workflow. Processing runs on GitHub's hosted runner and returns a downloadable artifact. This avoids using ChatGPT's data-analysis runtime for these supported repository tasks; it does not change GitHub Actions quotas, repository permissions, runner availability, or ChatGPT product limits.

## Local CLI

The scripts also run locally when Python and the relevant optional dependencies are available. Examples:

    # List and search capabilities
    python scripts/find_tool.py
    python scripts/find_tool.py "csv excel"
    python scripts/find_tool.py --tag data --tag statistics --format json

    # Inspect, search, and extract files in a ZIP under data/
    python scripts/zip_archive.py list --archive data/archive.zip
    python scripts/zip_archive.py find --archive data/archive.zip --query report --extension pdf
    python scripts/zip_archive.py extract --archive data/archive.zip --member documents/report.pdf

    # Validate discovery metadata and run tests
    python scripts/find_tool.py --validate
    python -m unittest discover -s tests -v

Search uses relevance ranking and partial-word matching. Multiword queries can match any term; records matching more terms rank higher. Repeated --tag filters require every supplied tag. Use --sort name for alphabetical output, --limit 20 to show more results, and --format json for machine-readable output.

## ZIP archive access

Place the ZIP file under data/, then choose an operation in Actions → ZIP archive access:

1. **List** shows member paths, extensions, file sizes, compression sizes, and extraction-safety notes without unpacking the archive.
2. **Find** searches partial paths/names, glob patterns, and extensions. Use this to identify a likely member when its exact name is unknown.
3. **Extract** retrieves one exact member path. A partial query is accepted only when it resolves to exactly one file; ambiguous results must be narrowed with Find first.

Extraction is selective: the workflow never unpacks the whole archive. It refuses parent-traversal paths, absolute paths, symbolic links, encrypted entries, and files above the configured size limit. The extracted file and a JSON integrity manifest are returned as a one-day artifact. Inventory/search operations also return a JSON report artifact.

The local CLI uses the same operations:

    python scripts/zip_archive.py list --archive data/archive.zip --limit 100
    python scripts/zip_archive.py find --archive data/archive.zip --query "annual report" --extension pdf
    python scripts/zip_archive.py extract --archive data/archive.zip --member "documents/Annual Report.pdf" --output-dir zip-output

## Dataset analysis

The Dataset analysis workflow uses requirements-analysis.txt and runs on GitHub Actions. Add the input file under data/, then provide its repository-relative path when launching the workflow. JSON Lines and NDJSON inputs are read in line-oriented mode. The local script is available with:

    python -m pip install -r requirements-analysis.txt
    python scripts/analyze_dataset.py --input data/file.csv --output-dir analysis-output

## File handoff

**Library file handoff** stages one file from data/ as a one-day artifact. Every copied file is verified by SHA-256; DOCX files also receive Open XML package validation. The workflow does not upload directly to ChatGPT Library. ZIP archive access is the appropriate workflow when the desired file is a member of an archive.

## Tool catalog

tools/catalog.json stores one record per capability. Related script and workflow entrypoints live together, so the same capability is not duplicated in search results.

Each record contains:
- id, name, and a concise summary
- tags and optional aliases for discovery
- entrypoints: one or more kind, path, and usage objects

Search examples:

    python scripts/find_tool.py "zip archive"
    python scripts/find_tool.py "spreadsheet" --kind workflow
    python scripts/find_tool.py --tag files --tag export
    python scripts/find_tool.py --list-tags
    python scripts/find_tool.py --validate

Keep summaries under 220 characters. Add or update one catalog entry whenever a reusable script or workflow is added, renamed, or removed. Do not duplicate source code or full documentation in the catalog.

## Repository layout

- scripts/ — reusable command-line tools
- tools/catalog.json — discovery metadata
- .github/workflows/ — focused, manually triggered Actions
- tests/ — unit tests
- data/ — workflow input files, including ZIP archives
- reports/ — retained reports and review outputs

Prefer one workflow per capability, workflow_dispatch, minimal permissions, and shared scripts for reusable logic. Keep optional dependencies scoped to commands that require them.

## Maintenance

1. Search the catalog before adding another tool.
2. Group related script and workflow entrypoints under one capability.
3. Keep experiments on working branches and merge through reviewable pull requests.
4. Preserve the default branch, archive/*, protect/*, GitHub-protected branches, and branches referenced by open pull requests during cleanup.
5. This is a public repository. Never commit credentials, secrets, private information, or confidential files.

Before merging changes:

    python scripts/find_tool.py --validate
    python -m unittest discover -s tests -v
