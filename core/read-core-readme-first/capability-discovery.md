# Capability catalog and discovery contracts

Read this document when changing the grouped capability schema, catalog validation, tool-discovery behavior, or a workflow that exposes the discovery contract. For ordinary tool selection or capability building, use the task guides linked below instead; this document and the core-change gate are not required unless the shared discovery contract itself changes.

For a core discovery change, first read the [Core documentation router](core-readme.md) and [core-change gate](core-change-gate.md).

## Contract surfaces

Treat these components as a connected discovery contract:

- `tools/catalog.json` — the canonical index of capabilities, aliases, tags, summaries, and script/workflow entrypoints.
- `scripts/find_tool.py` — catalog loading, search behavior, output formats, and validation.
- `.github/workflows/tool-lookup.yml` — the workflow interface that exposes tool lookup.
- `README.md` and task guides — instructions for discovering and selecting capabilities.
- `tests/` — expected catalog structure, search behavior, and validation guarantees.

Inspect the active target ref and all consumers before changing any part of this contract. Do not assume that changing one file is isolated merely because the edit is small.

## Required checks

1. Read the catalog structure and relevant records before changing the schema.
2. Inspect the catalog loader, search/filter behavior, command-line interface, and validator in `scripts/find_tool.py`.
3. Inspect `.github/workflows/tool-lookup.yml` and any other workflow or script that reads the catalog or calls the discovery CLI.
4. Inspect relevant tests and documentation, including all paths named by catalog entrypoints.
5. Preserve existing capability identities and entrypoint compatibility where practical. When a contract change is necessary, update all known consumers and tests in the same change.
6. Avoid duplicate catalog records for alternate entrypoints of one capability. Group related script and workflow entrypoints under one capability record.
7. Run `python scripts/find_tool.py --validate` and the relevant unit tests. Report any checks that could not be run.

## Ordinary capability work

- To find or select an existing tool, read [Finding tools](../finding-tools/README.md).
- To build or substantially change a reusable tool, read [Finding tools](../finding-tools/README.md), then [Tool-building instructions](../tool-building-instructions.md).
- Do not load this document or the core-change gate for ordinary capability work that does not change the catalog/discovery contract.
