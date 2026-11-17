# Core change gate — read this first

**Mandatory context step:** before planning, editing, or reviewing a change that may affect a core surface, read this entire file into the active context. Do not rely on its filename, a search excerpt, or a prior conversation as a substitute.

This file is intentionally separate from the root README. Load it for core work; normally ignore it for everyday tool use or isolated feature work.

## What counts as core

A surface is core when its rules, structure, or behavior are relied on across the repository or determine how future work is discovered, routed, validated, or maintained.

Current core surfaces include:

- The repository bootstrap and instruction-routing contract in `README.md` and `AGENTS.md`.
- The grouped capability schema in `tools/catalog.json` and the discovery contract in `scripts/find_tool.py`.
- Shared conventions used by multiple scripts or workflows, including stable input/output contracts and common validation behavior.
- Test/CI infrastructure when a change alters repository-wide validation.
- The instruction documents in `core/` and the directory-routing structure itself.

A change is **not** core merely because it is important, useful, or touches a shared folder. Examples that are normally not core:

- Adding or fixing one standalone analysis script.
- Improving a particular ZIP operation or one workflow's form.
- Updating a routine report or input document.
- Adding a one-off example or changing an isolated tool without changing shared contracts.
W.I.P. note: Write identifiers instead of examples?

When uncertain, inspect dependencies and use the narrower scope unless the change alters a repository-wide contract.

W.I.P. note: deciding whether to separate core-readme.md design constraints and core changes into their own documents under core/check-core-readme-first/

## Design constraints and principles
1.**Keep the always-read layer small.** The root README and root agent entrypoint are navigation surfaces, not encyclopedias
2. **Load instructions progressively.** Only relevant documents should be read for a task; separate Instruction and Guide documents with decision tree navigation
3. **Keep Instructions concise and specific.** Instructions should not be expansive or broad, if needed construct a decision tree to separate documents.
3. **Keep everyday tools out of core.** Core stores durable maintenance rules and cross-capability contracts; implementations stay in `scripts/`, workflows in `.github/workflows/`, and capability metadata in `tools/catalog.json`.
4. **Prefer extension over duplication.** Reuse an existing capability or entrypoint when its interface can be extended cleanly.
5. **Preserve compatibility deliberately.** Before changing a core contract, find all consumers, callers, workflow inputs, catalog references, tests, and documentation that depend on it.
6. **Avoid speculative infrastructure.** Do not add a framework, registry, instruction layer, or schema field without a concrete recurring use case.
7. **Keep core docs actionable and short.** Put task-specific procedures in their own files and link them from the root router. Do not copy full tool manuals into core instructions.

## Required process for core changes
1. **Read this gate first.** Then inspect the current target ref, the complete relevant directory tree, open work branches, and the files that implement or consume the affected behavior.
2. **State the boundary.** Identify what is core, what is an ordinary capability, and what must remain unchanged. Do not widen the change simply because adjacent code is visible.
3. **Map dependencies.** For catalog or discovery changes, inspect the schema, validator, search CLI, workflows, and tests. For instruction-routing changes, inspect the README, AGENTS.md, and all linked instruction paths. For shared workflow/CI changes, inspect every affected workflow and test.
4. **Choose the right branch.** Start new work from the latest `main` on `temp/<short-task>`. Continue on the existing task branch when continuing that work. Do not edit or commit directly to `main`.
5. **Make the smallest coherent change.** Preserve existing interfaces where possible. If a contract must change, document migration/compatibility behavior and update every known consumer in the same change.
6. **Update verification.** Add or revise tests for changed behavior. Update the catalog when a capability or entrypoint changes, and update README routing when instruction paths or core boundaries change.
7. **Review the resulting tree and links.** Check for duplicate instructions, stale paths, accidental everyday-tool material in `core/`, and unrelated changes. Run catalog validation, unit tests, and relevant workflow checks.
8. **Report precisely.** Summarize the contract changed, dependencies reviewed, tests run, and checks not run. Commit completed changes directly to the task branch. Create a PR or merge a branch only when explicitly requested.

## Context-loading rule

- Core work: this file is required, followed by only the additional documents named by the affected area.
- Tool discovery/building: load `core/finding-tools/README.md` and, when appropriate, `core/tool-building-instructions.md`; this gate is not needed unless the catalog/discovery contract itself is changing.
- Cleanup: load `core/clean-up.md`; this gate is not needed unless cleanup changes core architecture or repository-wide rules.
- Ordinary tool use: read the catalog entry and the selected tool's instructions/source only.

If this file's own rules or the README's routing rules change, read this file before modifying them and verify all references after the edit.
