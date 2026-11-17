# Instruction and guide architecture

Read this document when creating, restructuring, splitting, or routing Sand-Box instructions and guides. For any change that affects a core surface, first read the [Core documentation router](core-readme.md) and [core-change gate](core-change-gate.md).

## Document types

- **Instructions are normative.** They state when they apply and the requirements, constraints, and decisions that must be followed. Use direct, testable language for mandatory behavior.
- **Guides are explanatory and procedural.** They help an agent find, understand, or use a capability through workflows, examples, references, and recommendations. They should not silently introduce repository-wide policy.
- A document can contain both kinds of material only when separating them would make the task harder to follow. Make the normative requirements visibly distinct from optional explanation.

The filename does not determine the document type. A `README.md` may be a guide, and a file named “instructions” should not be treated as globally mandatory unless a router makes its scope explicit.

## Loading hierarchy

1. **Repository entrypoint:** `README.md` gives the task router and repository-wide workflow.
2. **Agent entrypoint:** `AGENTS.md` points compatible agents to the repository entrypoint and reinforces minimal context loading.
3. **Core router:** `core/read-core-readme-first/core-readme.md` is loaded when a task may change a core surface. It routes to the mandatory core-change gate and relevant specialist documents.
4. **Core-change gate:** `core-change-gate.md` defines the core boundary and the process for changing it.
5. **Specialist core documents:** design principles, instruction architecture, and capability-discovery guidance are loaded only for matching tasks.
6. **Task guides:** capability-specific guides such as `core/finding-tools/README.md`, `core/tool-building-instructions.md`, and `core/clean-up.md` are loaded when the task calls for them.

Do not load every level automatically. Follow the route required by the task and stop when the relevant requirements and dependencies are understood.

## When to split a document

Create a separate document when it has a distinct task trigger or audience, can be understood and used independently, and separating it materially reduces unnecessary context loading or improves maintenance. Keep related material together when the same tasks need it together. Document length alone is not sufficient reason to split.

Use a decision tree when there are multiple stable routes and choosing the wrong route would cause meaningful over-reading or missed requirements. For a small number of clear routes, a short table is easier to maintain. Do not create a directory for a single speculative future document; establish a real grouping need first.

## Authoring and maintenance rules

- Give each document a clear title, purpose, and statement of when it applies.
- Put mandatory requirements in one authoritative location. Link to that location rather than copying the same rule into several files.
- Keep each document focused on one coherent task or concern; avoid broad catch-all instruction files.
- Use descriptive, consistent, lowercase kebab-case filenames.
- Prefer relative links within the repository, and verify every changed link against the target branch's file tree.
- Update the router whenever a document is added, removed, renamed, or changes scope. Remove stale routes in the same change.
- Keep examples subordinate to the rule they illustrate; examples should not accidentally become additional policy.
- Do not require an agent to leave narrative progress notes merely to satisfy a workflow. Record durable, machine-observable events through appropriate tooling when such a system exists and is authorized.
