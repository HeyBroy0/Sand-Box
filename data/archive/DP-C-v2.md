# DP-C v2 — Task Guidance, Creation Allowances, and Maintenance

Status: exploratory draft for review. This is a new companion document in data; it does not replace the original DP C or establish adopted repository policy. Use it as a proposed task-guidance model, not as an instruction that every task must load in full.

## 1. Purpose and relationship to DP

DP defines the whole-repository principles. This document translates them into task-scoped guidance while keeping ordinary work lightweight.

The separation is deliberate:

- **Whole-repository principles** define the workspace's durable identity, authority boundaries, preservation requirements, and shared design expectations. See DP v2.
- **Working and creation guidance** applies to ordinary, non-maintenance tasks. It allows local, practical choices within the global boundaries.
- **Maintenance guidance** applies when the task is explicitly to maintain, align, or improve the repository.
- **Sensitive-change controls** apply whenever a task would change core, an entrypoint, shared authority, or a cross-repository contract. They are not waived by ordinary working allowances or a maintenance level.

DP-C is selectively loaded. A task should consult only the relevant section or linked source. This document is not an instruction to read the entire repository before working.

## 2. Classify the task by its actual effect

Use the task's intended outcome and affected paths to identify the applicable mode.

| Mode | Typical work | Main guidance |
| --- | --- | --- |
| Ordinary task-driven work | Add or change a local tool, document, test, or capability | Sections 3–6 |
| Dedicated maintenance | Local cleanup, documentation alignment, broader improvement | Sections 7–10 and the matching maintenance guide |
| Sensitive change | Core policy, repository entrypoint, authority, or shared routing/contract change | Section 11 and the applicable authorized change procedure |

A task can cross modes. For example, a tool change may discover a documentation problem that is worth recording for Alignment Maintenance. Do the task-scoped work that is authorized; do not silently expand it into a repository-wide maintenance or core-change project.

## Part A — Working and creation guidance

## 3. Ordinary task-driven work

### 3.1 Load only what the task needs

1. Inspect the actual target branch/ref, relevant working state, and the target paths before editing.
2. Read the repository's current task entrypoint and only the guidance relevant to the requested work.
3. Inspect the target file and its immediate dependencies. Search or inspect broader structure only when the task requires it.
4. Discover an existing capability or document when there is an obvious candidate; do not perform an exhaustive repository audit for a small task.
5. Keep unrelated documentation and maintenance concerns out of the task's working context.

Search is a locator, not proof of a complete repository inventory. For structural decisions, inspect the target ref's tree rather than inferring absence from an empty search result.

### 3.2 Small allowances for useful creation

Ordinary work may make locally scoped choices to keep creation practical:

- Add a focused document or tool in the nearest sensible owning area.
- Use a locally appropriate format rather than forcing a repository-wide template.
- Keep a small amount of local explanation with the capability when that makes it usable.
- Add only the immediately necessary dependencies, tests, or references for the requested result.
- Leave non-blocking style normalization, broader deduplication, and placement refinement to maintenance.
- Record an unresolved organizational choice rather than building a new subsystem to settle it prematurely.

These allowances do not permit a contribution to contradict an authoritative rule, bypass a permission boundary, break a shared interface without accounting for its consumers, or modify protected core/entry surfaces without authorization.

### 3.3 Creating documentation

For a new or changed document:

1. Be clear about what the document is for and who is expected to use it.
2. Put it near the component or responsibility it belongs to, using the nearest sensible existing location.
3. Include only enough context, constraints, and next-step references for the document to be understood and used.
4. Link to an authoritative rule when necessary; do not copy the rule and create a second authority.
5. Keep the content focused. Split only when the parts have distinct purposes, audiences, or useful independent loading.
6. Verify any links that the change directly adds or changes.

Do not require every document to include an elaborate metadata block, full navigation tree, exhaustive cross-references, or a universal set of sections. A focused local document is preferable to delaying useful work for repository-wide normalization.

### 3.4 Creating or changing tools

1. Check whether an existing capability is an obvious fit.
2. Extend it when the purpose and interface remain clear; create a separate tool when its responsibility or interface is genuinely distinct.
3. State the useful contract: purpose, inputs, outputs, defaults, dependencies, limitations, and meaningful failure behavior.
4. Validate assumptions at the boundary, especially paths, file types, user-supplied values, and privilege-sensitive operations.
5. Keep reusable logic in the capability implementation. Keep workflows or other entry surfaces thin.
6. Add verification proportional to the behavior and risk, including invalid or edge cases where relevant.
7. Keep the capability's registration and documentation consistent with the actual implementation when a canonical catalog applies.

Do not design a general framework, registry, or abstraction for a one-off need without a demonstrated reason.

### 3.5 What ordinary work should leave to maintenance

An ordinary task is not expected to:

- Audit or rewrite unrelated documents.
- Deduplicate the whole repository.
- Standardize every filename or document style.
- Create or reorganize navigation hubs.
- Build a complete repository map.
- Design future directory structures for hypothetical capabilities.
- Resolve every non-blocking architectural inconsistency it encounters.

Fix an immediate problem that blocks the requested task. For broader issues, preserve the relevant context and leave them for the matching maintenance scope.

## 4. Navigation and reachability during ordinary work

The goal is minimum reliable reachability, not maximum indexing.

- Use the repository entrypoint and existing task routes where they apply.
- Follow an existing hub to its destination; do not load unrelated branches of the hub.
- For a new local document, choose a natural owning location and add only a direct local reference when it is necessary for immediate use.
- Do not create a dedicated navigation hub, expand a hub hierarchy, or redesign repository navigation during ordinary task work.
- Do not duplicate the content of a destination in a navigation file.
- If an existing route is broken and blocks the task, repair only what is necessary when authorized; otherwise record it for Alignment Maintenance.

Dedicated hubs and hub-to-hub navigation are permitted when they reduce navigation cost in a large system. Their design and broad maintenance belong to Alignment Maintenance, not ordinary contribution.

## 5. Distinguish requirements from recommendations

When writing or editing guidance:

- Mark genuine requirements as requirements and keep their canonical source identifiable.
- Present recommendations, examples, and preferred patterns as guidance rather than implied restrictions.
- Do not strengthen a preference into a mandatory rule merely to make a document appear complete.
- Avoid duplicating rules from DP, authority documents, or other canonical sources.
- When a local document needs to repeat a constraint for immediate clarity, point to the authority source and make clear that the source remains authoritative.

If the status of a statement is uncertain and the distinction matters, do not silently elevate it to a repository-wide requirement. Flag it for review.

## 6. Preservation and verification for ordinary changes

- Preserve existing user material and source information unless the task explicitly authorizes its removal.
- Do not delete a file just because it is old, unreferenced in a quick search, or apparently inactive.
- Identify shared consumers when changing an interface or catalog contract.
- Verify the requested behavior and the directly affected references.
- Do not claim that a test, permission, workflow, telemetry mechanism, or enforcement control exists unless it has been checked.

Ordinary verification should be proportionate. It is not a mandate to run a full repository-wide review for every small edit.

## Part B — Maintenance guidance

## 7. Maintenance model

Maintenance is a dedicated task mode. It is the repository's mechanism for reducing organizational friction accumulated through ordinary work.

Choose the lowest maintenance scope that can solve the actual problem. The scopes are not mandatory sequential stages, and selecting a higher scope does not automatically authorize protected changes.

### 7.1 Minimal Maintenance

**Purpose:** Clean or correct a narrowly specified area while preserving its existing organization.

Typical work:
- Remove clearly unnecessary local clutter when authorized.
- Repair a specific broken reference or small defect.
- Check a bounded area for obvious consistency or health issues.
- Perform straightforward cleanup without broad consolidation.

Avoid:
- Reorganizing unrelated documentation.
- Redesigning navigation.
- Introducing new architecture or capability systems.
- Treating local cleanup as permission to delete uncertain material.

### 7.2 Alignment Maintenance

**Purpose:** Improve documentation coherence, wording, placement, and navigation without turning the task into broad architectural development.

Typical work:
- Consolidate overlapping documents and duplicated guidance.
- Reword unclear, inconsistent, or unnecessarily expansive instructions.
- Clarify the distinction between requirements, recommendations, examples, and future proposals.
- Establish or clarify a canonical home for a shared rule, then replace duplicates with references.
- Improve local placement and ownership of documents.
- Repair and simplify navigation paths.
- Create, consolidate, or restructure navigation hubs when useful.
- Build a deduplicated repository map or task router when it solves a real reachability problem.
- Add small improvements that directly support documentation, navigation, discoverability, or maintenance.
- Identify recurring friction and make a bounded correction to prevent its recurrence.

Alignment should preserve useful local independence. Do not force all components into identical layouts or rewrite working material solely for stylistic uniformity.

Do not let Alignment expand into:
- A broad new capability or tool-building project.
- Major architectural redesign.
- Speculative registries, abstractions, telemetry, or new subsystems.
- Unrequested changes to core policy, entrypoints, authority, or shared contracts.

When a needed change crosses those boundaries, record or separate the work and route it to Improvement or the relevant sensitive-change process.

### 7.3 Improvement Maintenance

**Purpose:** Evaluate and integrate broader changes that have demonstrated value.

Typical work:
- Merge or port useful, working changes from development work.
- Adopt proven tools, capabilities, and implementation improvements.
- Make justified architectural or shared-interface changes.
- Resolve cross-component design issues that cannot be handled as documentation alignment.
- Verify affected consumers and prepare a safe promotion path.

Improvement is not a license for speculative expansion. Prefer changes supported by a real use case, successful trial, recurring need, or clear improvement to the workspace.

## 8. Alignment Maintenance working method

Use a bounded method rather than an exhaustive universal checklist.

1. **Identify the friction.** Name the concrete problem: duplication, unclear wording, broken reachability, orphaned material, conflicting instructions, unclear ownership, or excessive context load.
2. **Inspect the affected area.** Read the relevant documents and their immediate routes. Expand the inspection only if a dependency or conflict requires it.
3. **Identify authority and ownership.** Determine which source should own each requirement and which local component owns its task-specific guidance.
4. **Consolidate carefully.** Merge genuinely overlapping material, but preserve distinctions in scope, authority, security, and behavior. Do not collapse merely similar concepts.
5. **Clarify the language.** Separate mandatory requirements from recommendations and explanatory material. Use direct wording and remove unnecessary repetition.
6. **Repair reachability.** Add or improve the smallest effective route. Create or revise a hub only when that structure makes navigation materially easier.
7. **Check task loading.** Ensure a typical task can reach the relevant source without being forced to load unrelated documentation.
8. **Verify.** Check changed links, references, routes, ownership, and any directly affected contracts. Confirm that source material has not been silently lost.
9. **Record unresolved boundaries.** Keep uncertain policy or architectural decisions explicit rather than silently deciding them during a cleanup task.

The method is a guide, not a requirement to perform all nine steps for every small alignment correction.

## 9. Navigation hubs and repository maps

A navigation hub is a document whose primary purpose is to route readers to other authoritative documents, capabilities, or task paths. It is not a second copy of the underlying instructions.

Use a hub when it reduces the effort of finding the next relevant source. In a large system, layered hubs are acceptable when each layer has a clear scope and the route remains understandable. A hub may point to another hub.

Rules:
- Ordinary task-driven work should use hubs, not develop them.
- Alignment Maintenance owns the creation, consolidation, and restructuring of dedicated hubs and maps.
- Keep hub entries concise: task trigger, destination, and brief reason or scope are usually enough.
- Link to the canonical source; do not paraphrase its entire contents.
- Avoid hubs that merely add a navigation step without improving selection or orientation.
- Update affected routes when Alignment Maintenance moves or consolidates a destination.

A future DP-C-nav may serve as a task router if the document set becomes large enough to justify it. It should not be created merely because DP-C exists.

## 10. Maintenance-wide boundaries

- Maintenance is not a substitute for authorization.
- No maintenance level inherently permits core, entrypoint, authority, or shared-contract changes.
- Keep recovery and preservation authority distinct from routine cleanup.
- Do not delete original source material merely because a consolidated version exists; follow the applicable retention and recovery policy.
- Do not add telemetry or claim automated observability unless a real, authorized mechanism is implemented.
- Keep the work proportional to the identified friction.
- Prefer an incomplete but honest alignment proposal over silently making a disputed policy decision.

## Part C — Sensitive and cross-repository changes

## 11. Core, entrypoint, and shared-contract changes

Treat changes to repository identity, core principles, authority rules, root task entrypoints, core routers, canonical discovery contracts, and other widely consumed interfaces as sensitive because their effects extend beyond one local task.

Before changing such a surface:

1. Confirm that the task explicitly authorizes the sensitive change. Repository write access alone is not authorization.
2. Read the current repository entrypoint and the applicable core or authority procedure.
3. Identify affected routes, documents, tools, workflows, catalog entries, and consumers.
4. Make the smallest coherent change and preserve compatibility where practical.
5. Verify the changed route or contract and its affected consumers.
6. Do not claim a technical restriction or protection unless it is actually enforced by GitHub or the relevant execution layer.

If authorization or the required procedure is missing or unclear, do not modify the protected surface. Keep the proposal in a non-authoritative review location and identify what decision is needed.

The working allowances in Part A and the maintenance scopes in Part B do not override this gate.

## 12. Recovery, telemetry, and promotion

### Recovery
Preserve known-good states, user material, and repository history. Structural or potentially destructive changes should have an appropriate recovery path. Routine maintenance must not silently invalidate recovery options.

### Telemetry and observability
Use automatic, structured records only where technically supported, authorized, useful, and proportionate. Distinguish raw collection from analysis and improvement suggestions. Do not invent or assume an existing telemetry facility.

### Branches and promotion
Follow the current repository entrypoint and actual branch controls for branch workflow. Keep stable branches distinct from ordinary task work. Promotion of broad or shared changes requires the applicable authorization and verification. Do not rely on outdated branch naming examples copied from older source material.

## 13. Compact task decision tests

| Question | Default |
| --- | --- |
| Does ordinary work need the whole DP-C? | No. Load only the relevant part. |
| May ordinary work create a useful local document or tool? | Yes, within the global boundaries and with a clear local purpose. |
| Must a new document be perfectly indexed immediately? | No. Give it a sensible owner and minimum useful local reachability; leave broad navigation alignment to maintenance. |
| Should ordinary work create a hub? | No. Use existing routes and defer hub development to Alignment Maintenance. |
| When is Alignment Maintenance appropriate? | When the problem is coherence, deduplication, wording, ownership, reachability, maps, or hubs. |
| When is Improvement Maintenance appropriate? | When the task requires proven capability, interface, or architectural changes beyond alignment. |
| Can any maintenance level change core or entrypoints automatically? | No. Explicit authorization and the applicable sensitive-change procedure still apply. |
| What if similar documents contain different authority or behavior? | Preserve the distinction; do not deduplicate away meaningful differences. |
| What if a broader issue appears during a small task? | Complete the authorized local work and record or route the broader issue. |

## Overall operating principle

Ordinary work should be able to create useful local results with minimal overhead. The repository-wide principles and sensitive boundaries remain stable; dedicated maintenance supplies the missing consolidation, wording, navigation, and architectural stewardship over time. Reachability is required, but universal loading and perfect upfront organization are not.
