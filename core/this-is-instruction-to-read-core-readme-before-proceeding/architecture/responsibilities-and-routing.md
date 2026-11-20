# Architecture — Responsibilities and Routing

**Status:** Proposed architecture reference, pending review and adoption.

**Use when:** Understanding task ownership, responsibility boundaries, or how work moves through Sand-Box. This is a task-level architecture reference, not a universal prerequisite.

## Responsibility domains

These are logical responsibilities. They do not imply separate agent runtimes, permission systems, or one-to-one directory structures.

| Domain | Responsibility | Boundary |
|---|---|---|
| Workspace Core | Identity, principles, architecture, configuration, authority, shared contracts | Protected from ordinary feature work and routine maintenance |
| Working | Features, local tools, task-scoped documents, implementation, proportionate checks | Optimizes local progress; does not own repository-wide organization |
| Maintenance | Canonical ownership, alignment, consolidation, placement, navigation, long-term coherence | Organizes accumulated work; does not inherit core or recovery authority |
| Capability System | Reusable tools, scripts, workflows, integrations, tests, discovery metadata | Implements reusable capability; does not redefine core policy |
| Workspace Operations | Repository work through supported GitHub and execution surfaces | Limited to the capabilities and permissions actually provided |
| Recovery | Preservation, known-good states, history, rollback, restoration | Independent from routine cleanup and maintenance |
| Observability | Authorized evidence, analytics, reviewable suggestions | Proportionate; does not itself authorize changes |

## Entry and routing

- The root README is the always-read workspace entrypoint.
- DP-C is the current procedure register and owns task messages, detailed task routes, implementation destinations, and progress status.
- The Core README routes core-specific work; it is not the ordinary task entrypoint.
- Component-local guidance is the normal destination for local implementation details.
- This architecture suite explains underlying relationships. It is not required context for every ordinary task.

## Work information flow

```text
Root README
    |
    v
Relevant DP-C procedure
    |
    v
Owning component or specialist source
    |
    v
Implementation and proportionate verification
    |
    +---- bounded result ----------------> report completion
    |
    +---- non-blocking coherence issue --> Maintenance
    |
    +---- protected boundary ------------> authority and protected-change review
    |
    +---- destructive / hard to reverse -> Recovery
```

A task may cross multiple responsibilities. Add specialist context only when the actual work crosses that boundary. Do not load all domain guidance as a universal checklist.

## Routing principles

1. Route to the smallest useful set of instructions and the operational owner.
2. Prefer direct links from entrypoints to task procedures and from procedures to their implementation.
3. Keep shared requirements at one canonical source; let local instructions explain only what is needed at the point of use.
4. A handoff changes task ownership, not permissions or authority.
5. Treat filenames, catalog entries, and search results as locators; verify the destination and its operational status.

## Related architecture references

- [Document Ownership and Lifecycle](document-ownership-and-lifecycle.md) — source ownership, placement, preservation, generated outputs, and document lifecycle.
- [Maintenance and Change Boundaries](maintenance-and-change-boundaries.md) — alignment scope, shared consumers, protected changes, and maintenance levels.
- [Capability Architecture](capability-architecture.md) — reusable tools, interfaces, entrypoints, and discovery.
- [Recovery Architecture](recovery-architecture.md) — preservation and restoration responsibilities.
- [Observability Architecture](observability-architecture.md) — collection, analytics, suggestions, and feedback.
