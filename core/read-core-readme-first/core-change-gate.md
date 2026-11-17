# Core change gate

**Required for core-surface changes:** read [the Core documentation router](core-readme.md) first, then read this entire file before planning, editing, or reviewing the change. Add only the specialist documents identified by the router. This gate is not required for ordinary work that does not affect a core surface.

## What counts as core

A surface is core when its rules, structure, or behavior are relied on across the repository or determine how future work is discovered, routed, validated, or maintained. A file being important or located under `core/` does not, by itself, make every change to it a repository-wide change. Classify the effect of the proposed change, not just the path being edited.

The following scope identifiers are concise labels for architectural discussion. They are not a machine-readable schema, a registry, or a requirement to label ordinary tasks.

### Core scope identifiers

- `core.bootstrap_routing` — repository bootstrap and agent entrypoints, including the routing contract in `README.md` and `AGENTS.md`.
- `core.instruction_routing` — rules determining which instructions or guides apply, how they are organized, and how they are loaded.
- `core.capability_discovery` — the grouped capability schema in `tools/catalog.json`, discovery behavior in `scripts/find_tool.py`, and their shared workflow/documentation contracts.
- `core.shared_contracts` — stable inputs, outputs, validation, or conventions consumed by multiple capabilities.
- `core.repository_validation` — test/CI infrastructure or validation behavior relied on repository-wide.
- `core.instruction_system` — durable cross-cutting rules and the structure/authority of the core instruction system.

### Non-core scope identifiers

These are normally local changes unless dependency inspection shows that they alter a core identifier above:

- `local.standalone_capability` — adding or fixing one isolated script or capability without changing a shared contract.
- `local.workflow` — changing one workflow's form or implementation without changing shared workflow behavior or repository-wide validation.
- `local.routine_content` — updating a routine report, input document, or retained content.
- `local.isolated_example` — adding or changing a one-off example that does not establish a shared convention.

When uncertain, inspect dependencies and use the narrower scope unless the change demonstrably alters a repository-wide contract. The examples clarify the labels; they do not override the effect-based test.

## Required process for core changes

1. **Inspect the target.** Identify the active target ref, current repository state, relevant file tree, open work branches/PRs, and the files that implement or consume the affected behavior.
2. **State the boundary.** Identify the core scope identifier(s), any local areas involved, and what must remain unchanged. Do not widen the change simply because adjacent code is visible.
3. **Map dependencies.** Follow the router's specialist reading path. Inspect all relevant callers, consumers, workflow inputs, catalog references, tests, and documentation. For instruction-routing changes, inspect `README.md`, `AGENTS.md`, and every affected instruction link.
4. **Choose the appropriate work branch.** Follow the repository's current branch policy in the root README and the user's explicit task instructions. Do not infer permission to change `main` from this gate.
5. **Make the smallest coherent change.** Preserve existing interfaces where possible. If a contract must change, document compatibility or migration behavior and update every known consumer in the same change.
6. **Update verification.** Add or revise tests for changed behavior. Update the catalog when a capability or entrypoint changes, and update README routing when instruction paths or core boundaries change.
7. **Review the resulting tree and links.** Check for duplicate instructions, stale paths, accidental everyday-tool material in `core/`, and unrelated changes. Run catalog validation, unit tests, and relevant workflow checks when applicable.
8. **Report precisely.** Summarize the contract changed, dependencies reviewed, tests run, and checks not run. Commit completed changes only as authorized by the task and current branch policy. Create a PR or merge a branch only when explicitly requested.

## Context-loading rule

- Any core-surface change: this router, this gate, and only the matching specialist document(s).
- Tool discovery/building without a change to the discovery contract: [Finding tools](../finding-tools/README.md) and, when appropriate, [Tool-building instructions](../tool-building-instructions.md); this gate is not needed.
- Cleanup without a core-surface change: [Cleanup instructions](../clean-up.md); this gate is not needed.
- Ordinary capability use: read the relevant catalog entry and selected capability instructions/source only.

If this gate's scope definition or the router's task routes change, verify the README, `AGENTS.md`, cleanup links, and all affected instruction paths.
