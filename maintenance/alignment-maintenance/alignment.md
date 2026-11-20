# Alignment Maintenance

**Status:** Proposed operational guide; not adopted as authority.

**Use when:** Related documents, components, processes, ownership, terminology, or routes have drifted enough to create confusion, duplication, broken reachability, inconsistent behavior, or avoidable context and maintenance cost.

## Purpose

Alignment Maintenance keeps the workspace connected, navigable, and understandable while preserving distinct processes and reducing the amount of context required for future work.

Prioritize three outcomes:

1. **Connectivity:** A reader can move from entrypoint to the correct task, owner, implementation, dependencies, and verification without dead ends or misleading routes.
2. **Process separation:** Different responsibilities remain independently understandable when their purpose, inputs, outputs, authority, owner, or lifecycle differs.
3. **Context efficiency:** Shared requirements have one canonical home; task instructions are concise and independently usable; irrelevant context is not loaded or repeated.

Do not optimize document length in isolation. Optimize total repeated reading, navigation, reasoning, maintenance, and verification effort.

## Select the alignment scope

### Scoped alignment

Use when the problem is confined to one component or a connected set of documents and processes.

1. Start from the root README and the Maintenance procedure in DP-C.
2. Read this guide and the nearest operational owner.
3. Identify the source, its direct consumers, and the entrypoints that route to it.
4. Load only the architecture reference that explains the affected relationship, if needed.
5. Make the smallest coherent changes and verify every affected route and behavior.

Do not read the full repository map, all architecture references, `principles.md`, or unrelated component guides unless the affected boundary requires them.

### Whole-repository alignment

Use when the requested outcome is coherence across the repository rather than a local repair.

1. Start with the root README, the Maintenance procedure in DP-C, this guide, the [Architecture Task Index](../../core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/architecture.md), the [Repository Map](../../core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/repository-map.md), and the [Document Ownership Registry](../../core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/document-ownership.md).
2. Build an inventory of top-level owners, entrypoints, operational processes, shared capabilities, and cross-domain handoffs.
3. Trace the important routes and dependencies. Group findings by process or owner instead of repeatedly rereading the same documents.
4. Deep-read only the sources where ownership, behavior, lifecycle, or authority is unclear or inconsistent.
5. Load architecture references by task area. A repository-wide scope does not require reading every architecture module or historical record.
6. Prioritize broken or misleading routes, competing sources, tangled processes, and repeated context before cosmetic consistency.

Do not turn a whole-repository pass into an unconditional read of every file. Broad scope changes the inventory and relationship coverage, not the progressive-loading rule.

## Alignment work

### 1. Trace connectivity

For each affected process, identify:

- **Entry:** Where does the reader or task discover that this process exists?
- **Route:** Which task procedure and local instructions should be followed?
- **Owner:** Which component maintains the operational source?
- **Execution:** Which implementation, workflow, or service performs the work?
- **Dependencies:** Which inputs, consumers, shared interfaces, or adjacent processes matter?
- **Verification:** Where is success, failure behavior, or output integrity checked?
- **Lifecycle:** Where do archival, retention, recovery, or supersession decisions belong?

Repair the links that make these connections usable. Check inbound routes before moving a source and outbound references after changing it. Prefer direct links to the operational owner over chains of hubs or links to preserved copies.

Connectivity does not mean every document must link to every other document. Create purposeful routes along the actual work path; avoid circular or decorative cross-linking.

### 2. Separate distinct processes

Do not combine processes merely because they use similar files or tools. Consider a separate guide, workflow, or capability when one or more material boundaries differ:

- Trigger and intended outcome.
- Responsible owner or decision authority.
- Inputs, outputs, or interface.
- Lifecycle, retention, or preservation requirements.
- Failure modes, safety requirements, or verification method.
- Consumers and update cadence.

Keep processes together when they share the same owner, use, lifecycle, and execution path and separation would create more navigation than clarity.

Examples of distinctions to preserve include:
- Document authoring versus file export and handoff.
- Operational sources versus historical preservation.
- Routine Maintenance versus Recovery.
- Raw evidence collection versus analytics versus suggestions.
- Capability implementation versus its thin workflow or connector entrypoint.

Connect these processes through clear inputs, outputs, handoffs, and ownership routes. Separation should not create isolated silos.

### 3. Establish canonical ownership

- Identify the operational source and owner before editing, moving, or merging material.
- Keep one canonical home for shared requirements.
- Preserve local explanations that make an independently used component usable.
- Distinguish adopted requirements, proposals, historical copies, generated composites, and navigation pages.
- Keep externally owned sources at their operational location. Use Core preservation only when its preservation purpose and procedure warrant it.
- Edit generation inputs, not generated outputs.
- Do not delete or invalidate historical or recovery material merely because a newer source exists.

Consolidate genuine duplication while preserving differences in authority, purpose, audience, scope, behavior, and lifecycle.

### 4. Reduce context and token cost

Optimize the total context needed to complete recurring tasks, not just the size of individual files.

- Give each shared mandatory rule one canonical home; link to it instead of repeating the full rule.
- Put task-specific instructions beside the owning process.
- Keep navigation documents short: trigger, destination, owner, and next step.
- Make local procedures independently usable with the minimum necessary assumptions, constraints, inputs, outputs, and verification.
- Mark what is always needed, conditionally needed, and background-only.
- Replace broad links with links to the exact relevant document or section where possible.
- Remove stale routes, duplicate explanations, unused indexes, and unnecessary intermediate hubs.
- Add concise information when it prevents repeated searches, ambiguity, unsafe assumptions, or expensive rediscovery.
- Do not remove useful local context merely to minimize word count.

`principles.md` and the full architecture suite are not routine prerequisites. Consult only the relevant architecture reference when the underlying design affects the task. Read the relevant principle only when a principle is being changed, a real conflict needs resolution, or the protected-change route requires it.

### 5. Verify the resulting system

Verify more than whether edited files look consistent:

- Every changed entrypoint reaches the current operational source.
- Relative links, anchors, filenames, and case-sensitive paths resolve.
- No route sends ordinary task work to an archived, preserved, generated, or superseded copy by mistake.
- Shared consumers, workflows, catalog entries, and tests still reference the correct owner and interface.
- Process handoffs identify the expected input, output, owner, and next step.
- New or consolidated guidance does not duplicate authority or hide an unresolved decision.
- Recovery and preservation requirements remain intact.

Use targeted link checks and relevant tests where available. Do not claim a check or technical control that was not actually verified.

## Boundaries

- Use Minimal Maintenance for one bounded local correction.
- Use Improvement Maintenance when the problem requires a broader capability, integration, or design change supported by demonstrated need.
- Do not silently change Core principles, architecture, authority, root entrypoints, shared contracts, or protected records. Follow the protected-change procedure and applicable authorization.
- Recovery remains independent. Maintenance must not silently redefine recovery authority or invalidate recovery records.
- Maintenance is not an approval gate for ordinary Working tasks.

## Complete when

The affected workspace is easier to enter, navigate, and maintain; each process has a clear owner and boundary; important routes and handoffs work; repeated context has been reduced without losing necessary local explanation; and protected, preservation, or unresolved decisions remain explicit.
