# DP C — Task Guidance and Operating Instructions

**Purpose:** Translate DP into practical guidance for repository work. This document is modular: each part is intended to be independently loadable for the task that needs it. Do not read every part by default.

**Relationship:** DP defines durable design principles. DP C explains how to apply them. Repository-specific authority procedures and technical controls remain authoritative for their own domains; this document does not grant permissions or claim that proposed infrastructure exists.

**Status:** Consolidated task-guidance document integrating the original DP C and DP-C-v2. Directory destinations below are intended homes derived from the source architecture tree. They are placement guidance, not a claim that every path currently exists.

## How to select a part

| Task trigger | Load this part | Intended destination |
| --- | --- | --- |
| Changing identity, core rules, architecture, or shared contracts | Part 1 — Core and sensitive changes | `core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/` and `core/authority/` |
| Creating or changing a tool, script, workflow, or capability | Part 2 — Capability work | `capabilities/` |
| Writing or editing task documentation | Part 3 — Document creation | `capabilities/documentation-Tree/` |
| Using repository access, branches, commits, or verification | Part 4 — Workspace operations | `core/authority/` and the applicable repository operation guidance |
| Cleaning, aligning, or improving repository organization | Part 5 — Maintenance | `maintenance/minimal-maintenance/` or `maintenance/improvement/` |
| Preserving, restoring, or planning destructive changes | Part 6 — Recovery and preservation | `recovery/policies/` and `recovery/procedures/` |
| Collecting or interpreting usage evidence | Part 7 — Observability | `observability/collection/`, `observability/analytics/`, or `observability/suggestions/` |
| Finding the next relevant instruction or capability | Part 8 — Navigation and discovery | `core/this-is-instruction-to-read-core-readme-before-proceeding/` and `capabilities/` |

A task may need more than one part when its actual effects cross responsibilities. Load only those parts. If a task encounters a protected surface, apply Part 1 regardless of its original task category.

---

# Part 1 — Core, authority, and sensitive changes

**Intended destination:** `core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/`; authority references belong under `core/authority/`.

**Applies when:** A task would change or evaluate repository identity, core policy, architecture, configuration, authority, entrypoints, shared routing, canonical discovery, or another contract with cross-repository effects.

### Procedure

1. **Confirm authorization.** Verify that the task explicitly authorizes the sensitive change and that the applicable core-change or improvement procedure permits it. Repository write access is not authorization.
2. **Load the governing sources.** Read the current repository entrypoint, relevant core guidance, authority model, and change procedure. Do not load unrelated core material.
3. **Map the impact.** Identify affected documents, routes, capabilities, workflows, catalog entries, tests, and other consumers.
4. **Make the smallest coherent change.** Preserve existing boundaries and compatibility where practical. Keep unrelated improvements separate.
5. **Verify the result.** Check affected consumers, references, contracts, and required controls. Do not claim enforcement unless the relevant GitHub or execution system actually provides it.
6. **Stop when authority is unclear.** Do not modify the protected surface. Keep the proposal separate from authoritative instructions and identify the missing decision or authorization.

### Non-negotiable boundaries

- Ordinary task allowances and maintenance levels do not override the sensitive-change gate.
- Policy, authorization, connector permissions, and technical enforcement are distinct.
- Do not assume repository instructions or a container restrict an already-authorized GitHub connector.
- A proposed rule, directory, or control is not an implemented control.

---

# Part 2 — Capability and tool work

**Intended destination:** `capabilities/` (implementation, scripts, tools, tests, workflows, and canonical catalog as applicable).

**Applies when:** Adding, extending, integrating, testing, or documenting a reusable capability.

### Procedure

1. **Check for an existing fit.** Inspect the obvious existing capability and its interface. Keep discovery proportionate; a small task does not require an exhaustive architecture audit.
2. **Choose extension or separation.** Extend when the existing purpose and interface remain clear. Create a separate capability when its purpose, interface, owner, or lifecycle is genuinely distinct.
3. **Define the usable contract.** State purpose, inputs, outputs, defaults, dependencies, limitations, and meaningful failure behavior.
4. **Validate boundaries.** Check paths, file types, sizes, user-supplied values, external dependencies, and privilege-sensitive assumptions as relevant.
5. **Keep implementation reusable.** Put shared logic in the capability implementation. Keep workflows and connector-facing surfaces thin; do not duplicate implementation across entrypoints.
6. **Respect least privilege.** Use only permissions and dependencies required for the capability. Keep credentials and sensitive data out of source, inputs, logs, and artifacts.
7. **Keep discovery consistent.** Where a canonical catalog applies, align its entry with the actual implementation, supported entrypoints, documentation, and tests.
8. **Verify proportionately.** Check normal behavior and relevant invalid or edge cases. Identify consumers before changing a shared interface.

### Do not

- Build a general framework or registry for a one-off need without demonstrated recurring value.
- Treat a filename or search result as proof that a capability is registered or supported.
- Claim unavailable connector, runtime, network, or filesystem capabilities.
- Expand a local capability task into repository-wide cleanup without authorization and a separate maintenance scope.

---

# Part 3 — Document creation and editing

**Intended destination:** `capabilities/documentation-Tree/` for shared document-writing guidance; task-specific documents belong with their owning component.

**Applies when:** Creating, restructuring, or editing instructions, guides, references, or capability documentation.

### Procedure

1. **Identify audience and use.** State what the document is for, who needs it, and when it applies.
2. **Find its owner and authority.** Check for an existing canonical rule or document. Link to shared authority rather than creating a competing copy.
3. **Choose the nearest sensible home.** Place the document with the responsibility it serves. Do not design a new directory hierarchy merely to make the document appear complete.
4. **Write for independent use.** Include enough purpose, constraints, steps, and next references for the intended reader to use the document without unrelated context.
5. **Separate requirement from guidance.** Mark mandatory requirements clearly. Keep recommendations, examples, and rationale from sounding mandatory.
6. **Keep it focused.** Split only when parts have distinct tasks, audiences, or maintenance boundaries and can be useful independently. Otherwise keep related material together.
7. **Add minimum useful navigation.** Link directly to the next relevant source when needed. Do not create a dedicated hub during ordinary task work.
8. **Verify changed references.** Check links and routes added or modified by the task.

### Document quality tests

- Can the intended reader tell when this document applies?
- Can the reader identify what is required versus recommended?
- Is the authoritative source for shared rules clear?
- Can the relevant section be used without loading unrelated sections?
- Does the document avoid unsupported claims about files, tools, permissions, or runtime behavior?

Do not require universal templates, elaborate metadata, exhaustive cross-references, or a full repository map for every local document.

---

# Part 4 — Workspace access and operations

**Intended destination:** Shared authority and workspace operation guidance under `core/authority/`; task-specific operating references belong with their owning capability or workflow.

**Applies when:** Discovering or changing repository files, branches, commits, pull requests, workflows, or other GitHub-connected operations.

### Procedure

1. **Inspect the actual target.** Confirm the repository, branch/ref, relevant state, and target paths before making changes.
2. **Use the available connector surface.** Work within the operations and permissions actually exposed by the connected GitHub environment.
3. **Keep boundaries distinct.** GitHub access, local or hosted execution, filesystem access, and external-service access are separate capabilities. Do not infer one from another.
4. **Use existing routes and capabilities.** Discover an obvious relevant tool or procedure before repeating a manual process; do not turn a small task into exhaustive discovery.
5. **Respect task authority.** Perform only the requested and authorized scope. Convenience, automation, and available write access do not grant broader authority.
6. **Verify before reporting.** Check the resulting file, commit, branch state, workflow result, or other relevant outcome. Report failures and limitations accurately.

### Operational defaults

- Prefer explicit inputs, predictable outputs, sensible defaults, and clear failure signals.
- When an approach fails, diagnose the cause and use a safe supported alternative where appropriate.
- Preserve user material and existing repository history.
- Do not claim a test, permission, workflow, or technical restriction exists unless verified.

Branch names and promotion routes must follow the current repository entrypoint and actual branch controls. Do not rely on examples in older documents when the current repository says otherwise.

---

# Part 5 — Maintenance and alignment

**Intended destination:** `maintenance/minimal-maintenance/` for bounded cleanup; `maintenance/improvement/` for alignment and broader improvement procedures. If separate maintenance guides are adopted, this part is their routing and shared boundary.

**Applies when:** The task is explicitly to clean, align, consolidate, or improve repository organization. Maintenance is not automatically part of ordinary capability work.

## Select the lowest sufficient scope

### Minimal Maintenance
**Purpose:** Correct a narrow local problem while preserving the existing organization.

Use for a bounded defect, a specific broken reference, or straightforward local cleanup. Avoid unrelated reorganization, navigation redesign, speculative architecture, and deletion of uncertain material.

### Alignment Maintenance
**Purpose:** Improve documentation coherence, wording, ownership, placement, and navigation without turning the task into broad capability or architectural development.

Use for overlapping guidance, duplicate authority, unclear wording, broken routes, orphaned material, inconsistent placement, or unnecessary context loading. Alignment may consolidate documents, establish canonical ownership, repair navigation, and create or restructure hubs when doing so materially improves reachability.

Do not expand Alignment into major architecture, broad tool-building, speculative infrastructure, or unrequested changes to core, entrypoints, authority, or shared contracts. Separate such work and route it to Improvement or the sensitive-change process.

### Improvement Maintenance
**Purpose:** Evaluate and integrate broader changes whose value is supported by actual use or a demonstrated need.

Use for proven capability adoption, justified architecture or shared-interface changes, cross-component problems, and preparing coherent changes for their appropriate long-term homes. Improvement does not itself grant authority to alter protected surfaces or promote changes without the applicable authorization.

## Alignment working method

1. Identify the concrete friction and keep the scope bounded.
2. Inspect the affected documents, paths, and immediate navigation routes.
3. Identify the authoritative source and the component that owns local guidance.
4. Consolidate genuine overlap while preserving differences in authority, scope, and behavior.
5. Clarify requirements, recommendations, examples, and proposals.
6. Repair the smallest effective navigation route; create a hub only when it reduces navigation cost.
7. Check that tasks can load the relevant source without unrelated documentation.
8. Verify changed links, references, ownership, and affected contracts.
9. Record unresolved policy or architecture decisions rather than silently deciding them.

This is a guide, not a mandatory nine-step checklist for every small correction. Choose the lowest scope that solves the observed problem; the scopes are not sequential stages.

## Maintenance-wide boundaries

- Maintenance does not substitute for authorization.
- No maintenance level automatically permits core, entrypoint, authority, or shared-contract changes.
- Do not delete material merely because it is old, quiet, or not found in a quick search.
- Do not invalidate recovery points or assume maintenance owns recovery authority.
- Do not claim telemetry or automated observability exists without checking its implementation.
- Keep work proportional; do not force uniformity where local differences are useful.

---

# Part 6 — Recovery and preservation

**Intended destination:** `recovery/policies/` and `recovery/procedures/`; recovery records and manifests belong under `recovery/manifests/` when that structure is adopted.

**Applies when:** A change is destructive, structurally significant, difficult to reverse, or involves restoration, archival material, or known-good states.

### Before a potentially destructive or structural change

1. Identify the material and history affected.
2. Determine the applicable retention and recovery policy.
3. Identify a suitable known-good recovery point and verify that it is usable when the risk warrants it.
4. Define the exact scope of the proposed change and what must be preserved.
5. Avoid irreversible cleanup when the recovery path or authority is unclear.

### Preservation rules

- Treat user material, source references, working branches, archives, snapshots, and version history as assets.
- Age or apparent inactivity alone does not make material disposable.
- Keep recovery authority and records independent of routine maintenance.
- Maintenance may request a recovery action but must not silently erase or invalidate the available recovery options.
- Follow the repository's actual retention and restoration policy; do not invent one or claim a snapshot exists without verification.

---

# Part 7 — Observability and improvement evidence

**Intended destination:** `observability/collection/`, `observability/analytics/`, and `observability/suggestions/`.

**Applies when:** Designing, operating, or reviewing mechanisms that record workspace activity or turn evidence into maintenance suggestions.

### Separate the information lifecycle

- **Collection:** Raw events or activity records captured by a real, authorized mechanism.
- **Analytics:** Derived patterns such as usage, dependencies, or navigation friction.
- **Suggestions:** Persistent, reviewable opportunities for maintenance or improvement.

### Guidance

1. Use automatic structured collection rather than manual self-reporting when a technically supported and authorized mechanism provides real value.
2. Define the purpose, data scope, access, and retention boundaries before collecting information.
3. Collect only what is needed; protect credentials, sensitive content, and user material.
4. Keep raw events distinct from interpretation and proposed changes.
5. Make suggestions evidence-based and reviewable; telemetry does not itself authorize repository changes.
6. Verify that a collection or analytics mechanism exists before describing it as operational.

Do not add telemetry infrastructure speculatively or impose progress-reporting overhead that creates no durable information.

---

# Part 8 — Navigation and capability discovery

**Intended destination:** Core entrypoint/router under `core/this-is-instruction-to-read-core-readme-before-proceeding/`; capability discovery and catalog under `capabilities/`.

**Applies when:** Finding the right instruction, deciding what context to load, discovering a reusable capability, or maintaining task routes.

### For ordinary task work

1. Start from the current repository entrypoint and follow the route relevant to the task.
2. Load only the relevant section or linked source; do not read every guide by default.
3. Use the canonical capability-discovery mechanism when one is adopted.
4. Treat search as a locator, not proof of a complete repository inventory or capability registration.
5. For a small local contribution, add only the direct reference needed for immediate reachability.
6. Use existing hubs; do not create, expand, or redesign dedicated hubs as part of ordinary work.

### For Alignment Maintenance

A navigation hub is a routing document, not a duplicate instruction source. Create or restructure one only when it materially reduces the effort of selecting the next useful source. Keep entries concise: task trigger, destination, and a brief reason or scope. Layered hubs are acceptable in a large system when each layer has a clear purpose and the route remains understandable.

A future DP-C navigation hub may be useful if the document set grows enough to justify it; do not create one merely because DP C is modular.

---

## Cross-part decision tests

| Question | Default |
| --- | --- |
| Does every task need to read all of DP C? | No. Select only the applicable part and its necessary dependencies. |
| Can ordinary work create a useful local tool or document? | Yes, within shared principles, authority, and existing contracts. |
| Must every contribution be perfectly indexed immediately? | No. Give it a sensible owner and minimum useful reachability. |
| Should ordinary work create a navigation hub? | No. Use existing routes; hub design belongs to Alignment Maintenance. |
| When is Alignment Maintenance appropriate? | When the problem is documentation coherence, deduplication, wording, ownership, placement, or reachability. |
| When is Improvement Maintenance appropriate? | When proven capability, architecture, or shared-contract changes are required beyond alignment. |
| Can maintenance change core automatically? | No. Explicit authorization and the applicable sensitive-change procedure still apply. |
| Can a consolidated document justify deleting its source? | No. Follow explicit retention and recovery policy. |
| What if similar documents have different authority or behavior? | Preserve the distinction; do not consolidate away meaningful differences. |
| What if a broader issue appears during a small task? | Complete the authorized local work and route or record the broader issue. |

## Overall operating rule

Do the task that is authorized, load only the guidance it needs, and preserve the workspace's shared boundaries. Ordinary work should remain lightweight; maintenance should make accumulated work coherent; sensitive changes should pass their separate authority gate; and recovery should remain independently protected.
