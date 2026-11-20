# Architecture — Document Ownership and Lifecycle

**Status:** Proposed architecture reference, pending review and adoption.

**Use when:** Placing, connecting, consolidating, preserving, generating, or routing repository documents.

## Placement and ownership

Place an operational document, capability, or implementation with the responsibility that maintains it. Prefer the nearest sensible existing owner. Split or relocate only when purpose, audience, interface, authority, or lifecycle creates a real ownership boundary.

The directory closest to the responsibility normally owns the operational source. Core owns shared authority and protected procedures; it does not automatically own every guide that Core references.

## Document classes

| Class | Role | Routing behavior |
|---|---|---|
| Operational source | Current maintained guidance at its owning location | Route task work here |
| Core-native source | Canonical principles, architecture, authority, standards, or protected procedures owned by Core | Link directly; do not create redundant copies |
| Core-preserved copy | Historical record of an externally owned source at a particular point in time | Use for preservation, provenance, or review; not routine task work |
| Generated composite | Deterministic output assembled from declared inputs | Update inputs and regenerate; do not edit manually |
| Navigation document | Concise route to sources, sections, or artifacts | Route readers; do not reproduce destination content |
| Draft or proposal | Material under development, not adopted authority | Label status and keep separate from current requirements |

## Source direction

- An operational source is the canonical maintained version used for current work.
- A preserved copy records a source path, capture point, and source status. It is historical, not a synchronized mirror or competing authority.
- A preserved copy may link outward to its operational source. The operational source should not link back to a preserved copy merely to establish provenance.
- Generated composites identify their inputs and generation method. Edit inputs, then regenerate and verify the output.
- Navigation documents point to operational sources rather than historical or generated copies.
- Core-native sources remain at their canonical Core locations and are not duplicated under the preserved-copy directory.

## Reuse and separation

Keep related information together when it shares an owner, audience, purpose, and lifecycle. Split a document or process when independent ownership, audience, interface, authority, update cadence, or lifecycle makes that separation useful.

Do not split solely to achieve shorter files. A split is worthwhile when it lets a task load the relevant part without requiring unrelated sections or creating a burdensome chain of cross-references.

## Consolidation checks

Before moving or merging material, identify:
- The canonical source and its owner.
- The status and authority of each source.
- Intended audiences and distinct use cases.
- Inbound routes, direct consumers, and generated references.
- Lifecycle, retention, and preservation requirements.
- Recovery implications and the verification needed after the change.

Keep meaningful differences. Consolidate only genuine duplication, and update affected indexes and routes when ownership or paths change.

## Related architecture references

- [Responsibilities and Routing](responsibilities-and-routing.md) — how entrypoints reach owners and processes.
- [Maintenance and Change Boundaries](maintenance-and-change-boundaries.md) — how to scope cross-document changes.
