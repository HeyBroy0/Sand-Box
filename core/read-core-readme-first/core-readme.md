# Core documentation router

This is the entrypoint for work that may change a core surface: a repository-wide rule, structure, or contract that other capabilities rely on. Read this file first, then load only the routes that apply. Do not preload every file in `core/`.

## Required reading order

1. Identify the surface and likely scope of the proposed change.
2. Read [the core-change gate](core-change-gate.md) for any change to a core surface.
3. Read only the additional document(s) matching the task below. If the task does not match a specialist route, use the core-change gate and inspect the affected dependencies without inventing another instruction layer.
4. Re-check the routes and links after changing repository structure or documentation.

## Task routes

| Task | Additional reading |
| --- | --- |
| Define, evaluate, or change the repository's architectural principles | [Design principles](design-principles.md) |
| Change instruction organization, document types, instruction routing, or the core documentation layout | [Instruction architecture](instruction-architecture.md) |
| Change the capability catalog schema, tool-discovery contract, or catalog validator | [Capability discovery](capability-discovery.md) |
| Change a shared script/workflow contract or repository-wide CI/validation behavior | Use the dependency-mapping requirements in [the core-change gate](core-change-gate.md); inspect each affected implementation, workflow, consumer, and test. |
| Perform cleanup that changes a core surface | [Cleanup instructions](../clean-up.md), in addition to the core-change gate. |
| Find or build an ordinary capability without changing the catalog/discovery contract | [Finding tools](../finding-tools/README.md), then [Tool-building instructions](../tool-building-instructions.md) when building. The core-change gate is not required for ordinary capability work. |

## Scope boundary

A file's location alone does not decide whether a task is core. A change is core when its effects alter a repository-wide rule, a cross-capability contract, or how work is discovered, routed, validated, or maintained. The core-change gate defines the scope labels and decision process.

This router is intentionally small. Add a specialist document only when a distinct recurring task needs independently loaded instructions or reference material. Keep one-off procedures in the relevant capability guide instead.
