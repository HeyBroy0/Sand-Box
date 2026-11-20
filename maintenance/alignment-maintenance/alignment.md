# Alignment Maintenance

**Status:** Proposed operational guide; not adopted as authority.

**Use when:** Related documents, components, processes, owners, terminology, or routes have drifted enough to cause confusion, duplication, broken navigation, or avoidable context cost.

## Goal

Improve the whole work path—not document length alone. A reader should be able to reach the right task, operational owner, implementation, dependencies, and verification with minimal repeated reading.

Optimize four things:

1. **Reachability:** direct routes from entrypoint to current operational source.
2. **Ownership:** one clear owner and canonical home for each shared requirement.
3. **Separation:** distinct processes remain distinct when their triggers, owners, interfaces, authority, lifecycle, or verification differ.
4. **Context cost:** load only what the task needs; remove repeated explanations and unnecessary navigation layers.

## Choose scope

- **Scoped alignment:** one component or a connected set of sources. Inspect the source, direct consumers, and routes into it. Read only the relevant architecture reference, if needed.
- **Whole-repository alignment:** repository-wide coherence is the requested outcome. Inventory top-level owners, entrypoints, operational processes, shared capabilities, and cross-domain handoffs. Trace important routes, then deep-read only sources with unclear ownership, behavior, lifecycle, or authority.

For either scope, start at the root README and the Maintenance procedure in [DP-C](../../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/DP-C.md). Use this guide and the nearest operational owners. For whole-repository work, add the [Architecture Task Index](../../core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/architecture.md), [Repository Map](../../core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/repository-map.md), and [Document Ownership Registry](../../core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/document-ownership.md).

**Progressive loading still applies:** repository-wide scope expands relationship coverage, not the number of files that must be read. Do not load every architecture module, specialist guide, principle, or historical record by default.

## Alignment procedure

### 1. Trace the work path

For each affected process, identify only the relevant parts of this chain:

entrypoint → task route → operational owner → implementation → dependencies/consumers → verification → lifecycle

Check inbound links before moving a source and outbound links after editing it. Link directly to the operational source where practical. Avoid circular links, decorative cross-links, and extra hubs.

### 2. Confirm ownership and status

Before editing, identify the canonical source, owner, audience, authority, and lifecycle. Distinguish:

- **Operational source:** current instructions maintained by the responsible component.
- **Core-native source:** canonical shared authority or protected procedure.
- **Preserved copy:** historical record; not a competing current instruction.
- **Generated composite:** output assembled from inputs; edit the inputs.
- **Navigation page:** points to sources; does not replicate them.
- **Proposal:** not adopted authority.

Keep shared requirements in one canonical home. Retain local explanations needed to use a component independently. Consolidate only genuine duplication; preserve differences in purpose, audience, authority, behavior, or lifecycle.

### 3. Preserve process boundaries

Keep processes separate when a material difference exists in trigger, outcome, owner, decision authority, inputs/outputs, lifecycle, failure handling, or verification. Otherwise, prefer one coherent guide over multiple documents that add navigation cost.

Connect distinct processes through explicit handoffs: who provides what, to whom, and what happens next. Examples include authoring vs. export, routine Maintenance vs. Recovery, operational sources vs. preservation, and evidence collection vs. analysis vs. suggestions.

### 4. Reduce total context cost

- Put task-specific instructions beside the operational owner.
- State each shared mandatory rule once; link to it rather than copying it.
- Keep route documents to trigger, destination, owner, and next step.
- Make specialist instructions concise and independently usable: include only necessary assumptions, constraints, inputs, outputs, and verification.
- Mark conditional and background reading clearly.
- Prefer direct links to the exact source or section over broad hubs.
- Remove stale routes, duplicate explanations, and unused indexes.
- Keep concise context when it prevents ambiguity, unsafe assumptions, repeated searches, or rediscovery.

Measure success by total reading, search, reasoning, verification, and future maintenance effort—not word count in isolation.

### 5. Verify

Check every affected route and behavior:

- Entrypoints reach the current operational source.
- Relative links, anchors, paths, and filename casing resolve.
- No route points ordinary work to a preserved, generated, archived, or superseded copy.
- Owners, consumers, workflows, catalog entries, and tests reference the correct source or interface.
- Handoffs identify the expected input, output, owner, and next step.
- Consolidation has not erased a meaningful process or authority distinction.
- Preservation and recovery requirements remain intact.

Use targeted link checks and relevant tests where available. Report only checks actually performed; distinguish verified defects from unverified risks.

## Boundaries

- Use [Minimal Maintenance](../minimal-maintenance/minimal.md) for one local correction.
- Use [Improvement Maintenance](../improvement/improvement.md) when the solution requires a broader capability, integration, or design change supported by demonstrated need.
- Do not silently change Core principles, architecture, authority, root entrypoints, shared contracts, or protected records. Follow the applicable protected-change route and authorization.
- Recovery remains independent; do not invalidate recovery records or redefine its authority through routine Maintenance.
- Maintenance is not an approval gate for ordinary Working tasks.

## Complete when

The affected work path is direct, each source has a clear owner and status, distinct processes remain understandable, required routes and handoffs work, and future tasks need less repeated context without losing necessary guidance.
