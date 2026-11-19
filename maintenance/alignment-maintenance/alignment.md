# Alignment Maintenance

Status: proposed maintenance-level guide created alongside DP-C v2. It is a draft for review and is not yet an adopted authority document.

## Purpose

Alignment Maintenance is the middle maintenance scope between Minimal Maintenance and Improvement Maintenance. It keeps documentation and navigation coherent as ordinary task work adds useful local material, without imposing extensive organization requirements on every contribution.

Its primary output is a clearer, more reachable, less duplicated repository—not a broad new capability or an architectural redesign.

## When to use it

Use Alignment Maintenance when the main problem is one or more of the following:

- Documentation overlaps, repeats itself, or has unclear ownership.
- Instructions are difficult to understand, unnecessarily expansive, or inconsistent.
- Important documents exist but are difficult to reach from the relevant task path.
- Navigation routes or repository maps are stale, redundant, or unnecessarily deep.
- A recurring organizational issue can be corrected with a small documentation or navigation improvement.
- A useful local document needs consolidation or a better long-term home.

Use Minimal Maintenance for narrow local cleanup. Use Improvement Maintenance when the work primarily requires broader capability development, integration of proven changes, shared-interface changes, or architectural evolution.

## Principles

1. **Reduce friction, not merely variation.** A difference in style or layout is not automatically a defect. Correct differences that cause confusion, duplicated authority, broken reachability, or unnecessary work.
2. **Consolidate without losing meaning.** Merge overlapping material only after identifying differences in authority, purpose, audience, scope, and behavior.
3. **Keep requirements and guidance distinct.** Do not turn recommendations into mandatory rules during a wording cleanup.
4. **Give shared rules one canonical home.** Link local documents to the authority source instead of maintaining competing copies.
5. **Preserve local independence.** A component should retain enough local explanation to be understood and used without loading the whole repository.
6. **Use the smallest effective navigation structure.** Direct links are often enough. Dedicated hubs are allowed when they improve reachability; layered hubs are allowed when scale justifies them.
7. **Keep hub development in maintenance.** Ordinary task-driven work should use existing hubs rather than create, expand, or redesign them.
8. **Prefer demonstrated usefulness.** Keep or promote a pattern when actual use shows it helps. Do not standardize a theoretical design merely for completeness.
9. **Preserve source material and history.** Do not silently delete original documents or user material because a consolidated version exists.
10. **Respect protected surfaces.** This guide does not grant permission to change core, entrypoints, authority rules, or shared contracts. Their separate authorization and change procedures still apply.

## Bounded working method

1. Identify the concrete friction and the area it affects.
2. Inspect only the relevant documents, owners, routes, and immediate dependencies.
3. Decide which source should be canonical and which content is genuinely duplicative.
4. Consolidate, clarify, or relocate only where the benefit is clear.
5. Update the minimum useful set of local references and navigation routes.
6. Create or restructure a hub only when it reduces navigation effort; permit hub-to-hub routing when useful at repository scale.
7. Verify links, task paths, preserved meaning, and affected consumers.
8. Note unresolved policy or architectural questions instead of silently deciding them.

This is a guide, not a universal checklist. A small wording or link correction does not require a full repository review.

## Boundaries and handoff

Alignment Maintenance should not become a substitute for Improvement Maintenance. Defer or separately scope work that requires substantial new functionality, a major architecture change, or a broad shared-contract redesign.

It must not bypass sensitive-change authorization. If a core or entrypoint change is needed, identify the proposal and required authorization before making that change.

## Expected result

A successful Alignment Maintenance task makes the affected area easier to understand and navigate, removes unnecessary duplication, preserves meaningful distinctions, and leaves ordinary future work no more burdensome than before.
