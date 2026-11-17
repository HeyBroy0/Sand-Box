# Tool-building instructions

Read [Finding tools](finding-tools/README.md) first. A new tool is justified only after checking whether an existing capability can be reused or extended.

## Default design

- Build for the repository's ChatGPT-oriented workflow: clear natural-language discoverability, small explicit interfaces, predictable outputs, and easy handoff to GitHub Actions or a local CLI.
- Prefer one capability with a few coherent operations (for example, `list`, `find`, and `extract`) over separate near-duplicate scripts for each operation.
- Keep the implementation in `scripts/`; put GitHub Actions entrypoints in `.github/workflows/`; register the capability once in `tools/catalog.json`.
- Keep workflow files as thin orchestration. Put reusable logic in the script so local and Actions behavior stay aligned.
- Avoid a new dependency when the standard library or an existing project dependency is adequate. Keep optional packages scoped to the feature that needs them.

## Interface and implementation

A useful command-line tool should:

- Have a clear purpose, explicit inputs, sensible defaults, and helpful usage/errors.
- Validate file paths, file types, sizes, and other assumptions at the boundary.
- Avoid destructive behavior by default. Make overwrite, deletion, external network access, or broad extraction explicit rather than implicit.
- Produce deterministic output where practical. Provide machine-readable JSON when another script or workflow needs to consume results; keep human-readable output useful too.
- Return non-zero exit codes for invalid inputs or failed operations.
- Keep unrelated concerns separate. Share helpers only when they represent a real common contract, not just to avoid a few repeated lines.

For GitHub Actions workflows:

- Prefer `workflow_dispatch` for manually requested repository processing.
- Grant only the permissions the workflow actually needs.
- Pin runtime assumptions such as the Python version and install only the required dependencies.
- Validate user-supplied paths/options and avoid constructing shell commands from untrusted input.
- Use short-lived artifacts for handoff and state their retention period.
- Do not put credentials or secrets in source files, workflow inputs, logs, or artifacts.

## Catalog and lifecycle

Add or update one grouped catalog record for the capability. Put related script and workflow paths under that record's `entrypoints`; do not create duplicate records for alternate ways of running the same capability. Keep summaries concise and aliases useful for how a person might ask for the capability.

Distinguish **stable**, **experimental**, and **deprecated** behavior in the documentation or pull request summary when that distinction helps users choose or avoid a capability. Do not invent a lifecycle field in the catalog or expand its schema only for decoration; make that a separate core change only when filtering or programmatic lifecycle handling becomes a real requirement.

## Verification and handoff

- Add tests for normal behavior, invalid inputs, and relevant boundary conditions.
- Update the catalog and validate it with `python scripts/find_tool.py --validate`.
- Run `python -m unittest discover -s tests -v` and any feature-specific checks.
- Update the README only when a user-facing workflow, capability, or task route changes; link to detailed docs instead of duplicating them.
- Summarize the tool's purpose, entrypoints, inputs, outputs, dependencies, safety boundaries, and test results in the pull request.
