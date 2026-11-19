# DP v2 — Repository Principles

Status: exploratory draft for review. This file is a new proposal in data; it does not replace the original DP, DP C, or any adopted core standard. The source documents remain unchanged.

## Purpose

Define the durable design principles for Sand-Box while preserving enough flexibility for ordinary task-driven work. The repository should be easy to use and extend; coherence should be maintained through focused maintenance rather than imposed as a large set of upfront creation requirements.

## How to read this document

The principles are separated into three scopes:

1. **Whole-repository principles** apply across all repository activity. They establish purpose, boundaries, authority, and the minimum conditions for a coherent workspace.
2. **Working and creation principles** apply to ordinary, non-maintenance tasks that add or change tools, documentation, or other local material. They deliberately allow lightweight, locally scoped decisions.
3. **Maintenance principles** apply when maintenance is the task. They define how the repository is cleaned up and aligned over time.

The scopes are not interchangeable. Working allowances do not override whole-repository protections. Maintenance does not grant authority to change protected core or entry surfaces.

## Part I — Whole-repository principles

### 1. Serve the real Sand-Box workspace

Sand-Box is an evolving toolbox and repository workspace for ChatGPT/Codex work through the connected GitHub environment. Prefer capabilities that improve real repository tasks in that environment. Do not expand into a general agent runtime or orchestration platform without an explicitly revised purpose.

Design for the connector and execution capabilities that actually exist. Repository instructions do not themselves change connector permissions, local execution rights, or external-service access.

### 2. Reachability over strictness

The right guidance, capability, or authority rule must be reachable when a task needs it. It does not follow that every task must read every guide, follow an elaborate universal template, or maintain the whole documentation system.

Keep essential entrypoints small. Use direct links, local references, catalog entries, and task-specific routes to make important material discoverable. Measure navigation by whether the next useful source can be found, not by the size or completeness of the index system.

### 3. Modular mash: local independence with central alignment

Prefer components that can be understood and used in their local context, connected through clear references and interfaces. A tool or document should not need the entire repository's history to be useful.

Keep shared principles, authority rules, and cross-component contracts in their appropriate canonical locations. Local components may have their own concise explanations and task-specific guidance, but should link to shared authority rather than reproduce it.

### 4. Protect authority boundaries

Distinguish repository policy, explicit authorization, connector permissions, and technical enforcement. They are related but are not substitutes for one another.

Core policy, repository identity, entrypoints, shared routing contracts, and other surfaces with repository-wide effects are sensitive change areas. Change them only with explicit task authorization and the applicable review or change procedure. Ordinary capability work and routine maintenance must not silently alter them.

A written rule is not technical enforcement. Do not claim that a permission, isolation boundary, branch restriction, or security control exists unless the relevant system actually enforces it.

### 5. Separate requirements from guidance

Keep mandatory constraints distinguishable from recommendations, examples, rationale, and preferred patterns. Mandatory rules should have one authoritative home. Other documents should link to that home instead of creating competing versions.

Use mandatory requirements when a boundary, safety property, shared contract, or necessary correctness condition depends on them. Use guidance when multiple reasonable approaches are acceptable.

### 6. Make capabilities and documents understandable at their point of use

A reusable capability should expose a sufficiently clear purpose, interface, inputs, outputs, dependencies, limitations, and failure behavior. A document should make its purpose and intended audience understandable without requiring unrelated context.

Keep shared capability discovery consistent. Where a canonical catalog or registry is adopted, treat it as the authoritative discovery record and keep its entries consistent with the actual implementation and supported interfaces.

### 7. Compose when useful; create when distinct

Prefer extending or composing an existing capability when it cleanly serves the need. Create a new tool or document when it has a distinct purpose, audience, interface, or ownership boundary, or when extension would make an existing component confusing.

Avoid duplicate authoritative rules and near-identical capabilities. Do not force unrelated concerns into one component merely to minimize file count.

### 8. Structure must earn its complexity

Prefer the smallest coherent structure that solves a demonstrated problem. Add directories, layers, schemas, abstractions, or routing machinery only when their practical benefit outweighs their ongoing navigation and maintenance cost.

A structure should not be created merely because a future use might exist. Conversely, useful local variation is acceptable when it keeps work simpler and does not break a shared contract.

Promote patterns because they have shown practical usefulness, not because a theoretically complete architecture can be drawn for them. The test for adding structure and the test for promoting a pattern are related but distinct: one controls complexity; the other controls adoption.

### 9. Preserve compatibility and verify important behavior

Treat shared interfaces and their consumers deliberately. Prefer compatible changes when practical. When a breaking change is justified, account for affected tools, workflows, catalog entries, tests, documents, and migration needs within the change.

Make important behavior verifiable. Use checks proportional to the risk and interface being changed; do not introduce a universal test burden for trivial local edits.

### 10. Preserve user material and recoverability

Treat user-provided material, source references, repository history, working branches, and recovery points as assets. Age or apparent inactivity alone is not a reason to delete something.

Scope destructive cleanup explicitly, preserve an appropriate recovery path, and keep recovery authority independent of routine maintenance. Preservation comes before irreversible cleanup.

### 11. Keep observability proportionate and truthful

Use structured, durable evidence when a supported and authorized mechanism provides real maintenance value. Collect only what has a defined purpose, with appropriate access and retention boundaries. Do not add telemetry infrastructure speculatively or imply that proposed collection exists before it is implemented and verified.

## Part II — Working and creation principles

These principles apply to ordinary task-driven work that is not itself a maintenance task and does not change a protected core or entry surface.

### 12. Keep the task primary

Load the minimum sufficient context for the actual task. Inspect the target and its immediate dependencies; consult broader guidance when the task reaches a broader boundary. Do not turn an ordinary tool or document task into a repository-wide audit.

Complete sufficiently specified work with minimal avoidable interaction, within the task's authority. If an approach fails, diagnose it and use a suitable alternative when safe.

### 13. Allow lightweight, locally scoped creation

Create useful local work without first designing its permanent place in the entire repository. Choose the nearest sensible owner or location, keep the scope clear, and make the result understandable to its intended user.

A first contribution does not need to be perfectly normalized, fully indexed, or integrated into every related guide. It should, however, avoid knowingly contradicting an authoritative rule, breaking an existing contract, or making its own use impossible to discover.

Leave repository-wide deduplication, broad wording cleanup, structural normalization, and navigation redesign to dedicated maintenance.

### 14. Keep document creation focused

Write a document for a real purpose and audience. Include the context, constraints, or next reference needed to use it correctly. Prefer concise, actionable material over exhaustive descriptions.

Do not require a universal document template or a full repository map for every new document. Split content when distinct purposes or audiences benefit from independent loading or maintenance; otherwise keep related material together.

A local direct reference may be added when it is necessary for immediate use. Do not create or redesign dedicated navigation hubs during ordinary task work.

### 15. Keep tool creation practical

Check for an obvious existing capability before creating a duplicate, but do not turn discovery into an exhaustive architecture exercise. Extend an existing capability when the fit is clean; otherwise create a distinct, appropriately scoped tool.

Give the tool a clear enough contract to use and verify it. Keep reusable logic in the capability rather than duplicating it in multiple workflows. Validate inputs and make destructive, network-dependent, or privilege-sensitive behavior explicit.

### 16. Do not make ordinary work perform maintenance

Ordinary tasks should not be required to deduplicate unrelated documents, normalize naming across the repository, repair every stale link, redesign navigation, or produce a comprehensive architecture map.

Fix an immediate issue that blocks the task. Record or leave broader organizational improvements for the appropriate maintenance scope.

## Part III — Maintenance principles

### 17. Maintenance owns gradual coherence

Dedicated maintenance should reduce friction accumulated through ordinary work. Its purpose is not to enforce visual uniformity; it is to make useful material easier to understand, reach, maintain, and safely extend.

Use maintenance to consolidate overlapping documentation, clarify wording, correct navigation, place material with its real owner, and improve small organizational features. Preserve meaningful differences in authority, scope, or behavior when consolidating.

### 18. Use three maintenance scopes

Choose the lowest scope that adequately addresses the task. These are scopes, not mandatory sequential stages.

- **Minimal Maintenance** performs narrow local cleanup and straightforward corrections without reorganizing the wider system.
- **Alignment Maintenance** consolidates documentation and navigation: deduplicating overlapping material, improving wording, connecting relevant sources, correcting placement, maintaining maps and hubs, and making small, directly related organizational improvements.
- **Improvement Maintenance** evaluates and integrates broader proven changes, including useful capability changes, architectural evolution, shared-contract changes, and porting working improvements into their appropriate long-term homes.

When an Alignment task uncovers work that requires substantial new capability or architectural change, separate or defer that portion to Improvement Maintenance rather than expanding Alignment without limit.

### 19. Let friction guide maintenance

Prioritize observed problems: orphaned or hard-to-find guidance, conflicting instructions, duplicated authority, broken routes, unclear ownership, unnecessary context loading, and repeated repair work.

Maintenance succeeds when future work becomes easier and more reliable. The number of rules, folders, links, or standardized documents is not a success measure by itself.

### 20. Navigation hubs are a maintenance responsibility

Dedicated navigation hubs are allowed when they materially improve reachability. In a sufficiently large system, a hub may point to other hubs when that hierarchy makes navigation more efficient.

Ordinary task work should use existing hubs and routes, not create, expand, or redesign dedicated hubs. Hub design, consolidation, hierarchy, and broad routing changes belong to Alignment Maintenance. A hub is a navigation artifact: it should route to authoritative material rather than duplicate that material's rules.

### 21. Maintenance does not bypass protected-change authority

No maintenance level grants automatic permission to change core policy, repository entrypoints, shared authority, or other sensitive cross-repository surfaces. Those changes still require explicit authorization and the applicable procedure. If the required authority or procedure is unclear, preserve the existing surface and separate the proposal from its implementation.

## Part IV — Compact decision tests

- **Does this serve Sand-Box?** It should improve the defined GitHub-connected workspace or one of its real capabilities.
- **Does this need to be in core or an entrypoint?** Only when it establishes a durable cross-repository identity, rule, route, or contract.
- **Does every task need to read it?** No. Make it reachable for the tasks that need it.
- **Should ordinary work create a hub?** No. Use existing routes; reserve hub development for Alignment Maintenance.
- **Should a new tool or document be created?** Yes, when it solves a distinct useful need and can be kept understandable locally.
- **Should structure be added?** Only when its practical benefit justifies its lasting complexity.
- **Should a pattern be promoted?** When actual use demonstrates value and the target owner is clear.
- **Should maintenance make everything uniform?** No. Consolidate friction and duplication while preserving useful local differences.
- **Can maintenance change core or entrypoints?** Only with the separate explicit authorization and applicable change procedure.
- **Should old material be deleted?** Not solely because it is old, quiet, or apparently unused.
- **Should telemetry or automation be assumed to exist?** No. Verify the actual implementation and permissions.

## Overall principle

Sand-Box should remain easy to use and extend, with reliable reachability and protected shared boundaries. Ordinary work should have enough freedom to create useful local tools and documentation without carrying the burden of repository-wide organization. Dedicated maintenance should turn that evolving work into a coherent, discoverable, and increasingly useful workspace over time.
