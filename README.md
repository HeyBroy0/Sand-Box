# Sand-Box — workspace entrypoint

This is the always-read layer for Sand-Box. It establishes the workspace purpose, essential shared boundaries, and routes to the next relevant owner. It is a router, not a replacement for specialist instructions.

## How to route work

For the procedure-specific task message, implementation destination, and progress state, continue to the [DP-C procedure register](core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/DP-C.md). DP-C is the single current source for detailed task wording and procedure tracking.

1. Identify the requested outcome and the files, systems, or repository boundaries it affects.
2. Follow the matching route below. The route order matches DP C's numbered procedure order.
3. Load only the instructions needed for the task and the boundaries it actually touches.
4. Check available tools and permissions before choosing an execution path.
5. Keep ordinary task work focused. Use Maintenance when organization, alignment, consolidation, or broader improvement is itself the requested outcome.

## Task routes

1. **Working Environment — create or edit a feature**  
   For ordinary feature creation, local implementation, task-scoped documents, tests, and focused changes, start with the nearest owning component and its local usage guidance. Keep context task-scoped and make the contribution usable at its point of use.

2. **Maintenance Environment — organize and align**  
   For cleanup, consolidation, document placement, deduplication, terminology, navigation, or repository-wide coherence, choose the lowest sufficient maintenance scope: [Minimal Maintenance](maintenance/minimal-maintenance/minimal.md), [Alignment Maintenance draft](maintenance/alignment-maintenance/alignment.md), or [Improvement Maintenance](maintenance/improvement/improvement.md). The Alignment guide is currently marked as proposed and not adopted authority. Maintenance is the main organizing force, not an approval gate for ordinary feature work. See [Maintenance Authority](core/authority/maintenance-authority.md).

3. **Core and sensitive changes**  
   When a task changes repository identity, protected policy, authority, entrypoints, shared routes, or cross-repository contracts, read the [Core README](core/this-is-instruction-to-read-core-readme-before-proceeding/core-readme.md), [Change Gate](core/this-is-instruction-to-read-core-readme-before-proceeding/standards/change-gate.md), and [Protected Change Procedure](core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/protected-change.md). Verify explicit authorization; do not infer authority from repository write access.

4. **Capability and tool work**  
   For capability lookup, tool creation, scripts, workflows, integrations, or tests, start with [Capability Discovery](capabilities/capability-discovery.md) and the relevant component under [capabilities](capabilities/).

5. **Document creation and lifecycle**  
   For instructions, guides, reference documents, or large document consolidations, use [Document Review](capabilities/documentation-Tree/document-look.md), [Document Creation](capabilities/documentation-Tree/document-creation.md), and the document's actual owning component. Distinguish operational sources from historical copies, generated composites, and navigation documents.

6. **Workspace access and operations**  
   For repository access, branches, commits, workflows, connectors, or execution environments, read the [Permission Model](core/authority/permission-model.md) and [Workspace Authority](core/authority/workspace.md). Confirm the actual repository/ref, tools, and permissions. Use supported GitHub actions when sufficient; use an execution environment only when the task needs capabilities it actually provides.

7. **Recovery and preservation**  
   Before destructive, structural, or difficult-to-reverse changes, read [Recovery Authority](core/authority/recovery-authority.md) and follow the applicable [recovery policies](recovery/policies/), [recovery procedures](recovery/procedures/), and [recovery manifests](recovery/manifests/).

8. **Observability and improvement evidence**  
   For usage evidence, analytics, recurring friction, and improvement suggestions, use the [Collection guide](observability/collection/README.md), [analytics](observability/analytics/), and [suggestions](observability/suggestions/). When a deterministic repeated action may be worth automating, record a suggestion rather than expanding the task into tool development.

9. **Navigation and capability discovery**  
   Start here, follow the owning component's local routes, and use the canonical capability-discovery mechanism where available. Broad routing and hub changes belong to Alignment Maintenance. Core source ownership and preserved-copy routes are described in the [Repository Map](core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/repository-map.md) and [Document Ownership](core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/document-ownership.md).

## Progressive loading

- **Always read:** this README only.
- **Feature creation and ordinary task work:** nearest component instructions and only the relevant specialist guidance.
- **Maintenance:** the relevant maintenance scope and only the affected specialist areas.
- **Protected changes:** the applicable explicit authorization and protected-change procedure.
- **Documentation:** the shared document guidance when relevant, plus the owning component's instructions.
- **Recovery:** the applicable preservation and restoration guidance.
- **Observability:** the relevant collection, analytics, or suggestions guidance.
- **Capability discovery:** the capability-discovery route and the relevant capability documentation.

Do not load every procedure by default. A task route selects context; it does not require a universal mode checklist or repository-wide audit.

## Shared boundaries

All work remains subject to applicable task scope, security, authority, compatibility, user-material preservation, and recovery requirements. Working and Maintenance are operating approaches selected through task routing, not separate technical permission systems. Actual access and enforcement come from the connected services and execution environment.

Written policy does not itself restrict an already-authorized GitHub connector. Do not claim that a permission, isolation boundary, workflow, test, or control exists unless the relevant system actually enforces or provides it.

## Full reference material

Design drafts and integrated historical procedure references are not routine task routes. Use the operational instructions reached through the routes above. The core procedure index links operational sources and preserved reference records.
