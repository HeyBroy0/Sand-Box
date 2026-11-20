<!--
Core-preserved procedure record 02.
Source draft: data/DP-C-v3 Edit.md
Current operational route: maintenance/minimal-maintenance/minimal.md; maintenance/alignment-maintenance/alignment.md; maintenance/improvement/improvement.md.
Captured: 2026-11-19
Status: historical procedure reference; current task wording and routes are maintained in ../DP-C.md. This file is retained for provenance and review.
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
