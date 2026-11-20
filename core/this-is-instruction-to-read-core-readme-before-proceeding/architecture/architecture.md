# Architecture — Task Index

**Status:** Proposed architecture reference, pending review and adoption.

**Purpose:** Route readers to the smallest architecture context needed to understand the structure beneath a task. This index replaces the former all-in-one architecture reading path; it does not introduce a new always-read requirement.

Architecture describes responsibility domains, information flow, ownership, lifecycles, and shared boundaries. The root README remains the ordinary task entrypoint. DP-C remains the task procedure register. Architecture references explain underlying design only when that design matters to the work.

## Choose by task

| Task or question | Read this reference |
|---|---|
| Which responsibility owns this work? How do task routes and handoffs connect? | [Responsibilities and Routing](responsibilities-and-routing.md) |
| Where should a document live? Which copy is operational, preserved, or generated? | [Document Ownership and Lifecycle](document-ownership-and-lifecycle.md) |
| How much alignment is needed? What is the boundary between Maintenance, Core, and Recovery? | [Maintenance and Change Boundaries](maintenance-and-change-boundaries.md) |
| How should a reusable tool, script, workflow, or shared interface fit together? | [Capability Architecture](capability-architecture.md) |
| How should preservation, rollback, and restoration be handled? | [Recovery Architecture](recovery-architecture.md) |
| How do collection, analytics, and suggestions connect? | [Observability Architecture](observability-architecture.md) |

## Maintenance reading paths

### Scoped maintenance

Start with the root README and the relevant DP-C maintenance procedure. Read the local maintenance guide, then inspect the affected owner, its direct consumers, and the routes that reach it. Add only the architecture reference for the design boundary actually involved.

Do not load the full architecture suite, `principles.md`, or unrelated authority documents by default.

### Whole-repository maintenance

Use this index with the [Repository Map](repository-map.md) and [Document Ownership Registry](document-ownership.md) to inventory owners, entrypoints, process flows, and shared dependencies. Review relevant architecture references by domain; do not repeatedly load one large architecture document or deep-read every source simply because the scope is repository-wide.

Whole-repository scope broadens the relationships to inspect. It does not remove progressive loading or require every historical record and specialist implementation to be read.

## Reading boundaries

- `principles.md` is not a routine task prerequisite. Read the relevant principle only when a change concerns a principle, an architectural conflict needs resolution, or the protected-change procedure requires it.
- The Core README is a route for core-specific work, not a universal task checklist.
- Read source-level ownership from the registry and operational guidance from its owning component.
- Preserved copies and generated composites are not current operational sources.
- When a task crosses several domains, read each relevant reference once and reuse that understanding throughout the pass.

## Architecture suite

- [Responsibilities and Routing](responsibilities-and-routing.md)
- [Document Ownership and Lifecycle](document-ownership-and-lifecycle.md)
- [Maintenance and Change Boundaries](maintenance-and-change-boundaries.md)
- [Capability Architecture](capability-architecture.md)
- [Recovery Architecture](recovery-architecture.md)
- [Observability Architecture](observability-architecture.md)

## Design decision checks

| Question | Direction |
|---|---|
| Is the task local to one owner? | Use the owner and direct dependencies; avoid repository-wide context. |
| Does it span related sources or routes? | Trace the relationship using the relevant architecture reference. |
| Does a document have a different owner, audience, or lifecycle? | Keep its source and route distinct. |
| Is a separate process or module justified? | Require a real difference in trigger, owner, input/output, authority, lifecycle, or verification. |
| Would another index, hub, or abstraction reduce repeated effort? | Add it only when it reduces total discovery and maintenance cost. |
| Does the task alter a protected boundary? | Use the protected-change procedure and applicable authority; this index grants no permission. |
