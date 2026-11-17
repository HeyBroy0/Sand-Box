# Core change gate — read this first

**Mandatory context step:** before planning, editing, or reviewing a change that may affect a core surface, read this entire file into the active context. Do not rely on its filename, a search excerpt, or a prior conversation as a substitute for reading it.

This file is intentionally separate from the root README. It should be loaded for core work and normally ignored for everyday tool use or isolated feature work.

## What counts as core

A surface is core when its rules, structure, or behavior are relied on across the repository or determine how future work is discovered, routed, validated, or maintained.

Current core surfaces include:

- The repository bootstrap and instruction-routing contract in `README.md` and `AGENTS.md`.
- The grouped capability schema in `tools/catalog.json` and the discovery contract implemented by `scripts/find_tool.py`.
- Shared conventions that multiple scripts or workflows depend on, including stable input/output contracts and common validation behavior.
- Test/CI infrastructure when a change alters the repository-wide validation contract.
- The instruction documents in `core/` and the directory-routing structure itself.

A change is **not** core merely because it is important, useful, or touches a shared folder. Examples that are normally not core:

- Adding or fixing one standalone analysis script.
- Improving a particular ZIP operation or one workflow's form.
- Updating a routine report or input document.
- Adding a one-off example or changing an isolated tool's implementation without changing shared contracts.

When uncertain, inspect dependencies and use the narrower scope unless the change alters a repository-wide contract.

## Design constraints

1. **Keep the always-read layer small.** The root README and root agent entrypoint are navigation surfaces, not encyclopedias.
2. **Load instructions progressively.** Read only the task document needed. Do not preload every file under `core/`.
3. **Keep everyday tools out of core.** Core stores durable maintenance rules and cross-capability contracts; implementation stays in `scripts/`, workflows in `.github/workflows/`, and capability metadata in `tools/catalog.json`.
4. **Prefer extension over duplication.** Reuse an existing capability or entrypoint when its interface can be extended cleanly.
5. **Preserve compatibility deliberately.** Before changing a core contract, find all consumers, callers, workflow inputs, catalog references, tests, and documentation that depend on it.
6. **Avoid speculative infrastructure.** Do not add a framework, registry, instruction layer, or schema field without a concrete recurring use case.
7. **Keep the core docs actionable and short.** Put task-specific procedures in their own files and link them from the root router. Do not copy full tool manuals into core instructions.

## Required process for core changes

1. **Read this gate first.** Then inspect the current target ref, the complete relevant directory tree, open pull requests, and the files that implement or consume the affected behavior.
2. **State the boundary.** Identify what is core, what is an ordinary capability, and what must remain unchanged. Do not widen the change simply because adjacent code is visible.
3. **Map dependencies.** For catalog or discovery changes, inspect the schema, validator, search CLI, workflows, and tests. For instruction-routing changes, inspect the README, AGENTS.md, and all linked instruction paths. For shared workflow/CI changes, inspect every affected workflow and test.
4. **Choose the right branch.** Start new work from the latest `main` on `temp/<short-task>`. When continuing an existing PR, use its head branch. Do not edit `main` directly.
5. **Make the smallest coherent change.** Preserve existing interfaces where possible. If a contract must change, document migration/compatibility behavior and update every known consumer in the same reviewable change.
6. **Update verification.** Add or revise tests for changed behavior. Update the catalog when a capability or entrypoint changes, and update README routing when instruction paths or core boundaries change.
7. **Review the resulting tree and links.** Check for duplicate instructions, stale paths, accidental everyday-tool material in `core/`, and unrelated changes. Run catalog validation, unit tests, and relevant workflow checks.
8. **Report precisely.** Summarize the contract changed, dependencies reviewed, tests run, and checks not run. Open a PR for review. Do not merge unless explicitly asked.

## Context-loading rule

- Core work: this file is required, followed by only the additional documents named by the affected area.
- Tool discovery/building: load `core/finding-tools/README.md` and, when appropriate, `core/tool-building-instructions.md`; this core gate is not needed unless the catalog/discovery contract itself is changing.
- Cleanup: load `core/clean-up.md`; this gate is not needed unless cleanup changes core architecture or repository-wide rules.
- Ordinary tool use: read the catalog entry and the selected tool's instructions/source only.

If this file's own rules or the README's routing rules change, read this file before modifying them and verify all references after the edit.
