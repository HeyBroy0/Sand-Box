# DP C — Operating Guidance and Procedures

**Purpose:** Translate DP into task routes and practical guidance for repository work. The principles should be implemented through routing, ownership, and task-specific procedures rather than repeated as universal instructions.

**Relationship:** DP defines durable principles and boundaries. DP C explains how to apply them. Repository-specific authority procedures and technical controls remain authoritative for their own domains. This document does not grant permissions or claim that proposed infrastructure exists.

**Status:** DP C-v3 working draft for review. It is intentionally unsplit: its nine numbered procedures are independently selectable sections and establish the stable order for future separation. Directory destinations are intended homes derived from the repository architecture; they are placement guidance, not proof that every path or control is implemented.

## Procedure order and task routing

The root README and this document use the same canonical order. A task should follow the route that matches its requested outcome, then load only the additional procedure required by an affected boundary.

| Order | Procedure | Primary trigger | Main route or owner |
| --- | --- | --- | --- |
| 01 | Working Environment | Create or edit a feature, tool, task-scoped document, test, or ordinary local contribution | Nearest owning component and its local guidance |
| 02 | Maintenance Environment | Clean, align, consolidate, relocate, or improve existing workspace material | maintenance/minimal-maintenance/, maintenance/alignment-maintenance/, maintenance/improvement/ |
| 03 | Core and Sensitive Changes | Change protected identity, policy, authority, entrypoints, shared routing, or cross-repository contracts | Applicable protected core instructions and authority procedure |
| 04 | Capability and Tool Work | Find, create, extend, test, or integrate a reusable capability | capabilities/ |
| 05 | Document Creation and Editing | Create, edit, consolidate, publish, preserve, or route documents | Owning component; shared document guidance under capabilities/documentation-Tree/ |
| 06 | Workspace Access and Operations | Use repository access, branches, commits, workflows, connectors, or execution environments | Actual repository and tool surfaces |
| 07 | Recovery and Preservation | Plan destructive changes, preserve material, archive, or restore a known-good state | recovery/policies/, recovery/procedures/, recovery/manifests/ |
| 08 | Observability and Improvement Evidence | Assess evidence, recurring friction, suggestions, or deterministic automation opportunities | observability/collection/, observability/analytics/, observability/suggestions/ |
| 09 | Navigation and Capability Discovery | Find instructions or capabilities, or maintain routing and discovery | Root README, component-local routes, and capability discovery |

The sequence is shared by the root README, this compilation, future procedure files, procedure-navigate.md, and full-procedures.md. Keep the numbers and titles synchronized.

Working and Maintenance describe work responsibilities, not separate technical permission systems. Routing should make the relevant approach implicit: ordinary creation reaches local owner guidance; organization and consolidation reach Maintenance. Do not require every task to load a general environment preamble. Protected-change, preservation, or other specialist procedures are added when their actual triggers are present.

# Procedure 01 — Working Environment: feature creation and ordinary task work

**Intended destination:** Task-specific guidance belongs with its owning capability or component. Shared Working-mode instructions may be linked from the current repository entrypoint.

**Applies when:** The requested outcome is a new feature, tool, script, workflow, test, task-specific document, or ordinary local change that is not itself a maintenance task or protected core change.

## Objective

Produce a useful, correct, locally understandable result with minimal unnecessary organizational overhead. Working is deliberately lighter than Maintenance: it creates and extends the workspace; it is not responsible for keeping the entire repository uniformly organized.

## Working allowances

A Working AI may:

1. **Make local placement decisions.** Put a contribution in the nearest sensible existing area. Do not design a repository-wide directory scheme before a small feature can be built.
2. **Use a locally appropriate format.** Follow an existing local convention when it is helpful, but do not force a universal template, elaborate metadata, or uniform document layout on every contribution.
3. **Keep context task-scoped.** Inspect the target, its immediate dependencies, and an obvious existing implementation. Do not perform an exhaustive repository or architecture audit for a bounded task.
4. **Add only immediate supporting material.** Include the explanation, references, tests, dependencies, and navigation needed to use and verify this contribution. Do not build a full catalog, map, or hub unless the requested feature actually requires it and the relevant authority permits it.
5. **Make reasonable local design choices.** Choose a practical implementation and local structure when multiple approaches satisfy the task and do not violate a shared interface or rule.
6. **Defer non-blocking normalization.** Leave broad deduplication, naming alignment, style normalization, relocation, and navigation redesign to Maintenance.
7. **Verify proportionately.** Check the requested behavior and directly affected boundaries. Do not run a repository-wide review merely because a local feature was added.

These are allowances about process, structure, and overhead. They are not permission to produce unusable work, ignore directly relevant instructions, bypass security, break shared contracts carelessly, discard user material, or exceed the task's scope.

## Working procedure

1. **Confirm the task and target.** Identify the requested outcome, repository, branch/ref, target paths, and any stated constraints.
2. **Load minimum sufficient context.** Read the current entrypoint, this part, and specialist guidance that directly applies. Follow authority or security references when the task touches those boundaries.
3. **Check for an obvious existing fit.** Inspect the nearest relevant capability or document before duplicating it. Keep the search proportionate; expand only when an actual dependency or shared contract requires it.
4. **Choose the simplest locally coherent approach.** Extend an existing component when the fit is clean. Create a separate component when its purpose, interface, owner, or lifecycle is genuinely distinct.
5. **Implement the requested result.** Keep changes focused, make assumptions visible, and avoid unrelated cleanup.
6. **Add minimum useful documentation and verification.** Explain how to use the result, state relevant limitations, and check behavior at the level warranted by its risk.
7. **Handle discovered maintenance separately.** Fix a local issue if it blocks the requested result and is within scope. For non-blocking repository-wide friction, note the issue in an existing maintenance channel when one exists; otherwise report it clearly at completion. Do not invent a tracker or expand the task just to record it.
8. **Report the outcome accurately.** State what changed, what was checked, and any known limitation or deferred alignment item.

## What Working is not expected to do

Unless explicitly requested as a separate, authorized maintenance task, Working is not expected to:

- Audit or rewrite unrelated documents.
- Deduplicate the whole repository or establish canonical ownership across unrelated areas.
- Standardize every filename, heading, document style, or metadata block.
- Create or redesign navigation hubs, repository maps, or global task routers.
- Reorganize directories for hypothetical future capabilities.
- Resolve every non-blocking architectural inconsistency it encounters.
- Integrate every local contribution into every related guide or index.

## Working stop conditions

Pause the affected operation and follow the applicable authority process when the task would change protected core, shared authority, repository entrypoints, or cross-repository contracts without the required authorization. Also stop or narrow the work when it would require an unapproved destructive action, violate a security boundary, or exceed the user's requested scope.

Do not interpret these stop conditions as a requirement to seek approval for ordinary local implementation choices that remain within the task and shared contracts.

---

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

---

## Working-to-Maintenance handoff

Working should not silently absorb repository-wide organizational work. When a non-blocking maintenance issue is found:

1. Complete the authorized Working task unless the issue blocks correctness, safety, or usability.
2. Preserve enough context for Maintenance to understand the issue: affected location, observed friction, and why it matters.
3. Use an existing issue, backlog, maintenance note, or handoff mechanism when one exists.
4. If no such mechanism exists, mention the deferred issue in the task completion report. Do not invent a new tracking system for a single observation.
5. Let Maintenance prioritize the item against other observed friction. A note is not an automatic commitment to perform the work.

Maintenance may return a focused request to Working when a local implementation is needed, but it should state the required outcome and boundaries rather than impose unrelated organizational work.

## Cross-procedure decision tests

| Question | Default |
| --- | --- |
| Is the task to create a feature or complete an ordinary local change? | Use Working, Procedure 01, and only the necessary specialist parts. |
| Is the task's main outcome improved repository coherence? | Use Maintenance, Procedure 02, and the relevant specialist parts. |
| Does every new feature require repository-wide organization first? | No. Working may make reasonable local choices and defer non-blocking normalization. |
| Is Maintenance the main organizing force? | Yes. It owns accumulated coherence, canonical ownership, broad alignment, and navigation. |
| Is Maintenance an approval gate for ordinary Working tasks? | No. It organizes the workspace over time; it does not pre-approve each contribution. |
| May Working ignore a directly relevant rule or shared contract? | No. Local allowances do not override applicable requirements or protected boundaries. |
| Should Working create a navigation hub? | Normally no. Use existing routes and hand broad hub work to Maintenance. |
| What if a broader issue appears during a feature task? | Complete the authorized work and route the non-blocking issue to Maintenance. |
| Can either environment change core or authority automatically? | No. Explicit authorization and the sensitive-change procedure still apply. |
| Can maintenance delete original source material because a consolidated copy exists? | No. Follow explicit retention and recovery policy. |
| Should all local documents and tools be forced into one format? | No. Align only where it improves usability, ownership, reachability, or maintenance. |
| Are the environments technical permission boundaries? | No. Actual permissions and enforcement come from GitHub and the relevant execution systems. |

## Overall operating rule

Route each task to the smallest useful set of instructions and the correct operational owner. Local creation should remain practical and self-contained; Maintenance should make accumulated work coherent; protected changes should follow their separate authority process; historical records should preserve rather than compete with operational sources; and deterministic automation opportunities should be recorded for evaluation so that future work can spend less effort on mechanical repetition.