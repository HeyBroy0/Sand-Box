# Tool-building instructions

Read [Finding tools](finding-tools/README.md) first. A new tool is justified only after checking whether an existing capability can be reused or extended.

## Default design

- Build for the repository's ChatGPT-oriented workflow: natural-language discoverability, small explicit interfaces, predictable outputs, and easy handoff to GitHub Actions or a local CLI.
- Prefer one capability with a few coherent operations over near-duplicate scripts.
- Keep implementations in `scripts/`, Actions entrypoints in `.github/workflows/`, and register each capability once in `tools/catalog.json`.
- Keep workflows thin: put reusable logic in scripts so local and Actions behavior stay aligned.
- Avoid unnecessary dependencies; keep optional packages scoped to the feature that needs them.

## Interface and implementation

A useful command-line tool should:

- Have a clear purpose, explicit inputs, sensible defaults, and helpful usage/errors.
- Validate file paths, file types, sizes, and other assumptions at the boundary.
- Avoid destructive behavior by default. Make overwrite, deletion, external network access, or broad extraction explicit.
- Produce deterministic output where practical. Provide machine-readable JSON when another script or workflow needs it.
- Return non-zero exit codes for invalid inputs or failed operations.
- Keep unrelated concerns separate. Share helpers only when they represent a real common contract.

For GitHub Actions workflows:

- Prefer `workflow_dispatch` for manually requested repository processing.
- Grant only the permissions actually needed.
- Pin runtime assumptions and install only required dependencies.
- Validate user-supplied paths/options; avoid constructing shell commands from untrusted input.
- Use short-lived artifacts for handoff and state their retention period.
- Never put credentials or secrets in source files, workflow inputs, logs, or artifacts.

## Catalog and lifecycle

Add or update one grouped catalog record for the capability. Put related script and workflow paths under its `entrypoints`; do not create duplicate records for alternate ways of running the same capability. Keep summaries concise and aliases useful.

Distinguish **stable**, **experimental**, and **deprecated** behavior in documentation or the task-branch commit summary when useful. Do not invent a lifecycle field in the catalog without a concrete programmatic need.

## Verification and handoff

- Add tests for normal behavior, invalid inputs, and relevant boundaries.
- Validate the catalog with `python scripts/find_tool.py --validate`.
- Run `python -m unittest discover -s tests -v` and feature-specific checks.
- Update the README only when a user-facing capability or task route changes; link to detailed instructions instead of duplicating them.
- Summarize purpose, entrypoints, inputs, outputs, dependencies, safety boundaries, and test results in the commit/task summary. Create a PR only when explicitly requested.
