# Full Procedures — Generated Reference

**Generated artifact:** This file is assembled by [generate_full_procedures.py](../../../../capabilities/scripts/generate_full_procedures.py) from procedure01.md through procedure09.md in numeric order. Edit the individual inputs and run the generator; do not edit this composite manually.

**Role:** Historical integrated reference for review. Current task routing and operational sources are listed in [procedure-navigate.md](procedure-navigate.md).

---

<!--
Core-preserved procedure record 01.
Source draft: data/DP-C-v3 Edit.md
Current operational route: Nearest owning component and local instructions; root README task route 1.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 01 — Working Environment: feature creation and ordinary task work

**Intended destination:** Task-specific guidance belongs with its owning capability or component. Shared Working-mode instructions may be linked from the current repository entrypoint.

**Applies when:** The requested outcome is a new feature, tool, script, workflow, test, task-specific document, or ordinary local change that is not itself a maintenance task or protected core change.

## Objective
local autonomy with proportional responsibility:
A Working AI should have enough autonomy to make sensible decisions and complete bounded tasks without unnecessary procedural overhead, while remaining accountable to existing rules, shared contracts, and the actual scope of the work.
In short: Optimize for useful progress, not process uniformity.

##Task
A Working AI may make reasonable, locally scoped implementation decisions: place contributions in the nearest sensible existing area, follow useful local conventions, inspect only the target and directly relevant dependencies, and add only the supporting documentation, references, tests, and navigation needed to use and verify the work. It should implement the simplest coherent solution, respect existing instructions and shared contracts, defer non-blocking repository-wide normalization to Maintenance, verify the affected behavior proportionately, and report changes, verification, assumptions, and deferred issues accurately.

## Working stop conditions

Pause the affected operation and follow the applicable authority process when the task would change protected core, shared authority, repository entrypoints, or cross-repository contracts without the required authorization. Also stop or narrow the work when it would require an unapproved destructive action, violate a security boundary, or exceed the user's requested scope.

Do not interpret these stop conditions as a requirement to seek approval for ordinary local implementation choices that remain within the task and shared contracts.
---

<!--
Core-preserved procedure record 02.
Source draft: data/DP-C-v3 Edit.md
Current operational route: maintenance/minimal-maintenance/minimal.md; maintenance/alignment-maintenance/alignment.md; maintenance/improvement/improvement.md.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 02 — Maintenance Environment: organization and alignment

**Intended destination:** Bounded cleanup under **maintenance/minimal-maintenance/**; documentation and navigation alignment under **maintenance/improvement/** or the specific adopted alignment location; broader proven changes under the adopted improvement procedures.

**Applies when:** The requested outcome is to organize, clean, align, consolidate, or improve the workspace beyond the immediate needs of one local contribution.

## Objective and responsibility

Maintenance is the main organizing force of Sand-Box. It is responsible for gradually turning independently created local contributions into a coherent whole.

Maintenance owns the ongoing work of clarifying canonical ownership, consolidating genuine duplication, improving placement, aligning terminology where useful, repairing navigation, keeping shared documentation understandable, and reducing recurring organizational friction.

Maintenance is not a gatekeeper for feature creation. Working contributions do not need to be pre-approved or perfectly normalized by Maintenance before they can be useful. Maintenance should organize accumulated work over time without imposing its full process on every contribution.

## Maintenance responsibilities

Maintenance should:

- Establish or clarify the canonical home for shared requirements and guidance.
- Consolidate duplicated or overlapping material while preserving meaningful differences in authority, scope, and behavior.
- Improve document placement and clarify which component owns local instructions.
- Align terminology and naming when inconsistent wording creates real confusion.
- Maintain useful routes, indexes, maps, and navigation hubs.
- Identify broken, stale, circular, or unnecessarily expensive navigation paths.
- Improve cross-document consistency and remove unnecessary repetition.
- Review deferred issues and recurring friction from Working tasks.
- Integrate proven local patterns into more durable shared structure when actual use justifies it.
- Preserve local independence where it reduces complexity and does not break a shared contract.

Maintenance should not standardize for appearance alone. A difference is not a defect merely because two components use different formats. Normalize only when doing so improves reachability, usability, correctness, ownership, or long-term maintenance.

## Select the lowest sufficient maintenance scope

These scopes are alternatives, not mandatory sequential stages. A larger scope requires a reason grounded in the problem.

### Minimal Maintenance

**Purpose:** Correct a bounded local problem while preserving the existing organization.

Typical work:
- Repair a specific broken reference.
- Remove clearly unnecessary local clutter when removal is authorized and safe.
- Correct a small local inconsistency or defect.
- Check a bounded area for obvious health or consistency issues.

Avoid:
- Reorganizing unrelated documents.
- Redesigning navigation.
- Introducing speculative architecture or capability systems.
- Deleting uncertain or historical material.

### Alignment Maintenance

**Purpose:** Restore and improve coherence across related documents, components, and navigation without turning the task into broad capability development.

Typical work:
- Consolidate overlapping documents and duplicated guidance.
- Clarify mandatory requirements versus recommendations, examples, and proposals.
- Establish canonical ownership for shared rules and replace competing copies with references.
- Improve wording, terminology, placement, and component ownership.
- Repair, simplify, or restructure navigation hubs and maps.
- Connect related sources while avoiding unnecessary context loading.
- Identify and resolve recurring friction that can be addressed through bounded organizational changes.

Avoid:
- Major new capability or tool-building projects.
- Broad architectural redesign not required for alignment.
- Speculative registries, abstractions, telemetry, or subsystems.
- Unrequested changes to core policy, entrypoints, authority, or shared contracts.

When alignment reveals work requiring a broader implementation or architectural decision, separate it and route it to Improvement or the relevant sensitive-change procedure.

### Improvement Maintenance

**Purpose:** Evaluate and integrate broader changes supported by demonstrated use or a concrete need.

Typical work:
- Adopt proven tools, capabilities, and implementation improvements.
- Resolve cross-component design issues that cannot be handled through documentation alignment.
- Make justified architectural or shared-interface changes.
- Integrate useful patterns from local Working contributions into durable shared components.
- Verify affected consumers and prepare an authorized promotion path.

Improvement is not a license for speculative expansion. Prefer actual use, recurring demand, successful trials, or a clear reduction in workspace friction as evidence.

## Maintenance working method

1. **Name the friction.** Identify the concrete issue: duplication, unclear ownership, broken reachability, conflicting instructions, awkward placement, unnecessary context loading, or repeated repair.
2. **Bound the scope.** Select Minimal, Alignment, or Improvement. Do not expand the work just because related problems exist.
3. **Inspect the affected system.** Read the relevant sources, their routes, and the immediate dependencies needed to understand ownership and impact.
4. **Identify authority.** Determine which source is authoritative and whether any protected boundary requires separate authorization.
5. **Organize without erasing distinctions.** Consolidate true overlap, but preserve separate rules where scope, authority, or behavior differs.
6. **Improve reachability.** Make the next relevant source easy to find without creating navigation layers that add no value.
7. **Check Working usability.** Ensure ordinary feature work can still load only the small amount of context it needs.
8. **Verify and preserve.** Check changed references and affected contracts; retain source material and a recovery path where warranted.
9. **Record unresolved decisions.** Do not silently convert uncertain policy or architectural questions into authoritative rules.

This is a flexible method, not a mandatory checklist for every small maintenance correction.

## Consolidating many documents

Bulk consolidation is a distinct form of Alignment work. Optimize for total usefulness and maintenance cost, not simply for the smallest amount of repeated text.

1. Inventory affected documents, intended readers, operational sources, historical copies, generated outputs, and navigation routes.
2. Separate mandatory requirements from recommendations, examples, and explanatory material. Similar wording does not prove identical authority or scope.
3. Identify one canonical home for each shared mandatory rule and preserve local procedures where responsibilities differ.
4. Merge genuine overlap without erasing distinctions in authority, audience, purpose, or lifecycle.
5. Retain concise explanations when an independently loaded procedure needs the context to be understood and applied correctly. Keep the repetition within that procedure's scope.
6. Avoid copying the same long explanation into every entrypoint. Entrypoints should route; independently used procedures may contain the local explanation they need.
7. Distinguish operational sources, historical copies, generated composites, and navigation artifacts. Do not route current task work to an archive copy or generated composite.
8. Update relevant routes, source paths, section anchors, and local references after consolidation.
9. Verify that no requirement, meaningful distinction, source attribution, or recovery information was lost.

Necessary local repetition is useful when it makes a procedure independently usable or avoids loading a much larger document. It is not useful when it creates competing authority or boilerplate at every shared entrypoint.

## Record deterministic automation opportunities

When Maintenance encounters a recurring, mechanical action that may be suitable for automation, record the opportunity under observability/suggestions/ using the available suggestion format. Do not turn an alignment task into unsolicited tool development.

Include the current manual steps, repeat frequency, deterministic inputs and outputs, likely users, and estimated effects on context/tokens, model or tool calls, manual effort, execution, verification, errors, and rework. Note dependencies, required permissions, failure behavior, sensitive data, and expected ongoing maintenance cost where known. Label estimates and assumptions rather than inventing evidence.

A suggestion is a candidate for later evaluation, not an implementation commitment. Tool creation belongs to a separately scoped capability or improvement task.


## Maintenance priorities and limits

Prioritize observed friction over theoretical completeness. Useful signals include repeated confusion, recurring repairs, duplicated authority, hard-to-find guidance, broken routes, unclear ownership, and a growing context burden.

Maintenance does not:
- Automatically authorize changes to core, entrypoints, authority, or shared contracts.
- Own or silently invalidate recovery authority.
- Require every contribution to use an identical structure.
- Need to reorganize a component whose local organization remains clear and effective.
- Have to turn every deferred Working observation into a project.
---

<!--
Core-preserved procedure record 03.
Source draft: data/DP-C-v3 Edit.md
Current operational route: core/.../procedures/protected-change.md; core standards and authority documents.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 03 — Core, authority, and sensitive changes

**Intended destination:** **core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/**; authority references belong under **core/authority/**.

**Applies in either environment when:** A task would change repository identity, core policy, architecture, configuration, authority, entrypoints, shared routing, canonical discovery, or another contract with cross-repository effects.

### Procedure

1. **Confirm explicit authorization.** Verify that the task authorizes the sensitive change and that the applicable procedure permits it. Repository write access is not authorization.
2. **Load governing sources.** Read the current repository entrypoint, relevant core guidance, authority model, and required change procedure. Do not load unrelated core material.
3. **Map the impact.** Identify affected documents, routes, capabilities, workflows, catalog entries, tests, consumers, and branch or release processes.
4. **Make the smallest coherent change.** Preserve boundaries and compatibility where practical. Keep unrelated improvements separate.
5. **Verify affected consumers and controls.** Check references, interfaces, and required repository controls. Do not claim enforcement unless the relevant GitHub or execution system actually provides it.
6. **Stop if authority is unclear.** Do not modify the protected surface. Keep a proposal separate from authoritative instructions and identify the missing decision or authorization.

### Boundaries

- Working allowances do not bypass this procedure.
- Maintenance responsibility does not bypass this procedure.
- Policy, authorization, connector permissions, and technical enforcement are distinct.
- A proposed rule, directory, or control is not an implemented control.

### Main sources and protected historical copies

When a document is operationally owned outside core but also needs a protected core record, keep its main operational copy at its real owner and preserve a clearly identified historical copy in the appropriate core documents area.

The core historical copy must identify the main document's repository-relative source path and may link outward to it. Do not add a reverse link from the main operational document to the core historical copy. Route ordinary readers to the main source; use the core copy for protected history or core-specific work. Update historical copies deliberately rather than silently rewriting them whenever the main source changes.
---

<!--
Core-preserved procedure record 04.
Source draft: data/DP-C-v3 Edit.md
Current operational route: capabilities/capability-discovery.md and the relevant capability implementation.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 04 — Capability and tool work

**Intended destination:** **capabilities/** for implementations, scripts, tools, tests, workflows, and canonical discovery metadata as applicable.

**Applies when:** Adding, extending, integrating, testing, or documenting a reusable capability. This is normally Working work unless the requested outcome is broader capability alignment or integration, in which case use the appropriate Maintenance scope too.

### Working procedure

1. **Check for an obvious existing fit.** Inspect the nearest relevant capability and its interface. Do not perform an exhaustive architecture audit for a small feature.
2. **Choose extension or separation.** Extend when purpose and interface remain clear. Create a distinct capability when its purpose, interface, owner, or lifecycle genuinely differs.
3. **Define the usable contract.** State purpose, inputs, outputs, defaults, dependencies, limitations, and meaningful failure behavior at a level appropriate to the capability.
4. **Validate relevant boundaries.** Check paths, file types, sizes, user-supplied values, external dependencies, and privilege-sensitive assumptions as relevant.
5. **Keep implementation reusable.** Put shared logic in the capability implementation. Keep workflows and connector-facing surfaces thin; avoid duplicated implementations.
6. **Respect least privilege.** Use only permissions and dependencies required for the defined purpose. Keep credentials and sensitive data out of source, inputs, logs, and artifacts.
7. **Add proportionate verification.** Check normal behavior and relevant invalid or edge cases. Identify consumers before changing a shared interface.
8. **Leave broad alignment to Maintenance.** Make the requested capability usable and locally understandable. Do not create a repository-wide registry, navigation system, or cleanup project unless the task requires and authorizes it.

### Maintenance follow-through

Maintenance may later align capability naming, placement, catalogs, documentation, tests, and shared interfaces across multiple components. It should do this when the accumulated system demonstrates a real coherence problem, not as a reason to burden every feature task with repository-wide integration.

### Do not

- Build a general framework or registry for a one-off need without demonstrated recurring value.
- Treat a filename or search result as proof that a capability is registered or supported.
- Claim unavailable connector, runtime, network, or filesystem capabilities.
- Expand local capability work into broad cleanup without a separate maintenance scope.
---

<!--
Core-preserved procedure record 05.
Source draft: data/DP-C-v3 Edit.md
Current operational route: capabilities/documentation-Tree/document-look.md and document-creation.md.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 05 — Document creation and editing

**Intended destination:** Shared document-writing guidance under **capabilities/documentation-Tree/**; task-specific documents belong with their owning component.

**Applies when:** Creating, restructuring, or editing instructions, guides, references, or capability documentation. Local document creation is normally Working; broad consolidation and document-system alignment are Maintenance.

### Working document procedure

1. **Identify purpose and audience.** Make clear what the document is for and who needs it.
2. **Find the nearest sensible owner.** Check the target area and an obvious existing source. Do not audit the entire repository before writing a local guide.
3. **Use a locally suitable format.** Follow useful local conventions, but do not impose elaborate metadata, exhaustive cross-references, or a universal template.
4. **Write for immediate independent use.** Include enough context, requirements, steps, limitations, and next references for the intended reader.
5. **Separate authority from explanation.** Link to the canonical source for shared requirements rather than creating a competing copy.
6. **Keep it focused.** Split content only when parts have distinct tasks, audiences, or maintenance boundaries and benefit from independent loading.
7. **Add minimum useful navigation.** A direct local reference may be enough. Do not create a dedicated hub during ordinary Working tasks.
8. **Verify changed references.** Check links and routes added or modified by the task.

A Working document need not be perfectly indexed, globally normalized, or integrated into every related guide. It must still be accurate enough for its intended use and must not make unsupported claims about files, tools, permissions, or runtime behavior.

### Maintenance document procedure

When the task is to align documentation across an area or the repository:
- Identify duplicate authority and determine the canonical source.
- Consolidate genuinely overlapping material without erasing meaningful differences.
- Align terminology where inconsistency causes confusion.
- Clarify audience, applicability, ownership, and maintenance responsibility.
- Repair navigation and replace duplicated content with concise references where suitable.
- Preserve useful local variation; do not rewrite solely for stylistic uniformity.

### Document roles and authority

Classify each relevant document as one of the following:
- **Main operational source:** the maintained copy that current readers and tasks should use, stored with its owning responsibility.
- **Historical or protected copy:** a preserved record, not a competing current source. A main document outside core may have a protected copy in core when its status requires it.
- **Generated composite:** a mechanically assembled full reference. It is not manually edited and is not the default task destination.
- **Navigation document:** a route to sources and sections. It should not repeat the destination's full instructions.

### Core procedure documents area

The core procedures directory may contain core-specific procedures, tools, supporting data, and other operational instructions. Its documents subdirectory has a narrower purpose: preserve the individual procedure copies and store the generated full reference and procedure navigation.

Intended layout:

~~~text
core/
└── this-is-instruction-to-read-core-readme-before-proceeding/
    └── procedures/
        ├── [core-specific procedures, tools, data, and instructions]
        └── documents/
            ├── full-procedures.md
            ├── procedure-navigate.md
            ├── procedure01.md
            ├── procedure02.md
            ├── procedure03.md
            ├── procedure04.md
            ├── procedure05.md
            ├── procedure06.md
            ├── procedure07.md
            ├── procedure08.md
            └── procedure09.md
~~~

The procedure01.md through procedure09.md files in documents/ are preserved inputs for compilation. Their main operational copies live at their appropriate destinations in the repository architecture, such as maintenance/, capabilities/, recovery/, observability/, or the relevant owning component. Not every procedure is core-specific; an externally owned procedure can still have a protected historical copy in this core area.

### Compilation and navigation contract

- **full-procedures.md** is generated by collecting the individual procedure documents and appending them in numeric order. Preserve their authored text and section structure; do not summarize or reinterpret it.
- **procedure-navigate.md** lists each procedure number and title, its task trigger, a route to the corresponding section in full-procedures.md, the main operational source path, and the preserved-copy path.
- Keep the root README, this compilation, the individual procedure numbers, the navigation document, and the generated full document in the same order.
- Treat the historical procedure copies as deliberate publication inputs. The generation workflow assembles them; it does not decide which operational source is authoritative or silently synchronize newer content into the historical copies.
- Validate missing or duplicate numbers, ordering, section anchors, and main-source paths. Fail visibly on missing or inconsistent inputs rather than producing an incomplete composite.
- Never edit full-procedures.md manually. Update the correct individual input through its publication process, then regenerate the composite.
---

<!--
Core-preserved procedure record 06.
Source draft: data/DP-C-v3 Edit.md
Current operational route: core/authority/permission-model.md and core/authority/workspace.md.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 06 — Workspace access and operations

**Intended destination:** Shared authority and workspace operation guidance under **core/authority/**; task-specific operating references belong with their owning capability or workflow.

**Applies when:** Discovering or changing repository files, branches, commits, pull requests, workflows, or other GitHub-connected operations.

### Procedure

1. **Inspect the actual target.** Confirm repository, branch/ref, relevant state, and target paths before making changes.
2. **Use the available connector surface.** Work within the operations and permissions actually exposed by the connected GitHub environment.
3. **Keep capabilities distinct.** GitHub access, local or hosted execution, filesystem access, and external-service access are separate. Do not infer one from another.
4. **Use relevant existing routes.** Discover an obvious relevant tool or procedure without turning a small task into exhaustive discovery.
5. **Respect task authority.** Perform only the requested and authorized scope. Convenience, automation, and available write access do not grant broader authority.
6. **Verify before reporting.** Check the resulting file, commit, branch state, workflow result, or other relevant outcome. Report failures and limitations accurately.

Working operations should remain focused on the task. Maintenance operations may inspect a wider affected area when needed to restore coherence. Branch names and promotion routes must follow the current repository entrypoint and actual branch controls.
---

<!--
Core-preserved procedure record 07.
Source draft: data/DP-C-v3 Edit.md
Current operational route: recovery/policies/; recovery/procedures/; recovery/manifests/.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 07 — Recovery and preservation

**Intended destination:** **recovery/policies/** and **recovery/procedures/**; recovery records and manifests belong under **recovery/manifests/** when adopted.

**Applies when:** A change is destructive, structurally significant, difficult to reverse, or involves restoration, archival material, or known-good states.

### Before a potentially destructive or structural change

1. Identify the material and history affected.
2. Determine the applicable retention and recovery policy.
3. Identify a suitable known-good recovery point and verify that it is usable when the risk warrants it.
4. Define the exact scope of the proposed change and what must be preserved.
5. Avoid irreversible cleanup when recovery path or authority is unclear.

### Preservation rules

- Treat user material, source references, working branches, archives, snapshots, and version history as assets.
- Age or apparent inactivity alone does not make material disposable.
- Keep recovery authority and records independent from routine maintenance.
- Maintenance may request recovery but must not silently erase or invalidate available recovery options.
- Follow actual retention and restoration policy; do not invent one or claim a snapshot exists without verification.
---

<!--
Core-preserved procedure record 08.
Source draft: data/DP-C-v3 Edit.md
Current operational route: observability/collection/; observability/analytics/; observability/suggestions/.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 08 — Observability and improvement evidence

**Intended destination:** **observability/collection/**, **observability/analytics/**, and **observability/suggestions/**.

**Applies when:** Designing, operating, or reviewing mechanisms that record workspace activity or turn evidence into maintenance suggestions.

### Separate the information lifecycle

- **Collection:** Raw events or activity records captured by a real, authorized mechanism.
- **Analytics:** Derived patterns such as usage, dependencies, or navigation friction.
- **Suggestions:** Persistent, reviewable opportunities for maintenance or improvement.

### Guidance

1. Use automatic structured collection rather than manual self-reporting when a technically supported and authorized mechanism provides real value.
2. Define purpose, data scope, access, and retention boundaries before collecting information.
3. Collect only what is needed; protect credentials, sensitive content, and user material.
4. Keep raw events distinct from interpretation and proposed changes.
5. Make suggestions evidence-based and reviewable; telemetry does not itself authorize repository changes.
6. Verify that a collection or analytics mechanism exists before describing it as operational.

Do not add telemetry speculatively or impose reporting overhead that creates no durable information.

### Deterministic automation suggestions

When collection, analytics, or maintenance work reveals a repeated mechanical action, preserve the opportunity under observability/suggestions/ rather than requiring Maintenance to create a tool.

A suggestion should describe the current sequence, repeat frequency, deterministic inputs and outputs, users, likely savings in context/tokens and manual/tool steps, verification and error reduction, dependencies, permission needs, failure behavior, and ongoing cost. Distinguish measured evidence from estimates. A suggestion records an opportunity; it does not authorize implementation.
---

<!--
Core-preserved procedure record 09.
Source draft: data/DP-C-v3 Edit.md
Current operational route: README.md; core architecture routes; capabilities/capability-discovery.md.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 09 — Navigation and capability discovery

**Intended destination:** Core entrypoint/router under **core/this-is-instruction-to-read-core-readme-before-proceeding/**; capability discovery and catalog under **capabilities/**.

**Applies when:** Finding the right instruction, deciding what context to load, discovering a reusable capability, or maintaining task routes.

### Working use of navigation

1. Start from the current repository entrypoint and follow the route relevant to the task.
2. Load only the relevant section or linked source; do not read every guide by default.
3. Use the canonical capability-discovery mechanism when one is adopted.
4. Treat search as a locator, not proof of a complete repository inventory or capability registration.
5. For a small local contribution, add only the direct reference needed for immediate use.
6. Use existing hubs; do not create, expand, or redesign dedicated hubs as part of ordinary Working work.

### Maintenance of navigation

A navigation hub is a routing document, not a duplicate instruction source. Maintenance owns the creation, consolidation, hierarchy, and broad restructuring of hubs and repository maps when they materially improve reachability.

Keep hub entries concise: task trigger, destination, and a brief reason or scope. Layered hubs are acceptable in a large system when each layer has a clear purpose and the route remains understandable. Avoid hubs that merely add an unnecessary step.

A future DP C navigation hub may be useful if the document set grows enough to justify it. Do not create one merely because this document is modular.

### Source routing and procedure navigation

Route ordinary task work to the main operational copy in the owning component. Do not direct readers to historical procedure copies or the generated full compilation unless their task is specifically about preservation, the core procedure record, or integrated review.

The core procedure navigation document should route to both the relevant full-reference section and the current main operational source, clearly labeling their different roles. Core historical copies may link outward to their main source path; main operational copies must not link back to their core historical copies merely to establish provenance.

When a route changes, keep the root README, this procedure order, procedure-navigate.md, and affected component-local routes synchronized. The sequence and titles remain 01–09 as listed at the beginning of this document.
