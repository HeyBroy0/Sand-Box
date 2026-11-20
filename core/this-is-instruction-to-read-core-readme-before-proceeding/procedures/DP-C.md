# DP-C — Implementation Procedure Register

**Status:** Proposed operational draft for review.

## Purpose

DP-C is the procedure-tracking and implementation-routing layer between adopted principles, the architecture design, and operational work. It translates what the workspace values and how it is designed into concise task messages, implementation destinations, and progress status.

DP-C is the single current source for procedure wording and task-level navigation. It is not another principles document, architecture specification, or detailed tutorial.

## Design-to-implementation chain

1. **Principles** — the durable desires, values, and constraints: [standards/principles.md](../standards/principles.md).
2. **Architecture** — the intended system structure and relationships: [architecture.md](../architecture/architecture.md).
3. **DP-C** — the procedures, task messages, implementation routes, and progress status that connect the design to work.
4. **Operational sources** — the current guides, capabilities, authority documents, and recovery or observability procedures at their owning locations.
5. **Verification and feedback** — check the affected behavior and route non-blocking coherence issues to Maintenance.

Do not make DP-C repeat the principles or reproduce the architecture. It should tell a task owner what posture to take and where to continue.

## Alignment scale

Keep ordinary work scoped, but increase alignment effort as a change approaches shared or protected surfaces.

| Scope | Expected alignment |
|---|---|
| **Local component work** | Use the nearest owner, follow useful local conventions, check direct dependencies, and keep additions and verification proportional. |
| **Shared or cross-component work** | Check component ownership, affected consumers, interfaces, naming, dependencies, and relevant architecture before changing shared behavior or routes. |
| **Core or protected work** | Read the relevant principles and architecture, identify authority and consumers, check compatibility and recovery, confirm explicit authorization, and verify all affected routes and controls. Stop when authorization or impact is unclear. |

This is a graduated alignment model, not a universal checklist. Do not apply protected-change overhead to ordinary local work. Do not treat a protected change as an ordinary local edit.

## Procedure register

The sequence and titles match the root README. Each procedure tracks the task message, operational destination, and current implementation state.

| No. | Procedure | Main implementation area | Current state |
|---|---|---|---|
| 01 | Working Environment | Nearest owning component and its local guidance | Local-work model established; specialist guidance remains component-owned |
| 02 | Maintenance Environment | Minimal, Alignment, and Improvement guides | Three operational drafts exist; Alignment remains explicitly proposed |
| 03 | Core and Sensitive Changes | Core standards, authority, and protected-change procedure | Initial guidance exists; authority and adoption review remain |
| 04 | Capability and Tool Work | Capability discovery, catalog, implementations, tests, and scripts | Discovery guide exists; catalog remains empty and capability entries are incomplete |
| 05 | Document Creation and Editing | Document review, creation, lifecycle, and preservation | Initial guidance and preservation structure exist; review and adoption remain |
| 06 | Workspace Access and Operations | Permission model and workspace authority | Initial drafts exist; actual technical enforcement must be verified separately |
| 07 | Recovery and Preservation | Recovery policies, procedures, and manifests | Authority draft exists; operational policies, procedures, and manifests remain incomplete |
| 08 | Observability and Improvement Evidence | Collection, analytics, and suggestions | Collection guide exists; analytics and suggestion formats remain incomplete |
| 09 | Navigation and Capability Discovery | Root entrypoint, architecture routes, and this register | Main routes exist; keep this register synchronized with implemented destinations |

## Procedure 01 — Working Environment

**Task message**

Place the contribution with its nearest sensible owner. Follow useful local conventions, keep the design and supporting material proportionate, and make the result usable. Leave unrelated organization to Maintenance.

**Primary route:** The nearest owning component and its local instructions. Start at the [root README](../../../README.md).

**Alignment:** Check direct dependencies and interfaces. Increase review only when the change affects shared consumers or protected surfaces.

## Procedure 02 — Maintenance Environment

**Task message**

Choose the lowest sufficient maintenance scope. Improve coherence where it reduces real friction; preserve useful local differences and avoid normalizing for appearance alone.

**Operational routes**

- [Minimal Maintenance](../../../maintenance/minimal-maintenance/minimal.md)
- [Alignment Maintenance](../../../maintenance/alignment-maintenance/alignment.md)
- [Improvement Maintenance](../../../maintenance/improvement/improvement.md)

**Core references:** [Maintenance Authority](../../authority/maintenance-authority.md), [Core Document Preservation](core-document-preservation.md), and the [Preservation Index](documents/preservation-index.md).

**Alignment:** Check ownership, authority, source status, and affected routes before consolidating or moving material. Escalate to protected-change review when a core standard, entrypoint, authority definition, or shared contract is affected.

## Procedure 03 — Core and Sensitive Changes

**Task message**

The closer a change gets to core, authority, architecture, entrypoints, or shared contracts, the stronger the alignment review must be. Compare it with the principles and architecture, identify authority and affected consumers, verify recovery and compatibility, and confirm explicit authorization before editing.

**Primary route:** [Core README](../core-readme.md), [Change Gate](../standards/change-gate.md), and [Protected Change Procedure](protected-change.md).

**Authority routes:** [Permission Model](../../authority/permission-model.md), [Maintenance Authority](../../authority/maintenance-authority.md), [Recovery Authority](../../authority/recovery-authority.md), and [Workspace Authority](../../authority/workspace.md).

**Stop condition:** Do not make the protected change when authorization, authority, or material impact remains unclear. Keep an unresolved proposal separate from adopted instructions.

## Procedure 04 — Capability and Tool Work

**Task message**

Prefer a suitable existing capability over a duplicate. Keep each capability's purpose, interface, permissions, dependencies, tests, and documentation clear at its point of use.

**Primary route:** [Capability Discovery](../../../capabilities/capability-discovery.md), then the owning capability under `capabilities/`.

**Alignment:** Check consumers and compatibility before changing a shared capability interface. Do not treat a catalog entry or filename as proof that an implementation is available.

## Procedure 05 — Document Creation and Editing

**Task message**

Put documents with the responsibility that maintains them. Make purpose, audience, status, and source ownership clear. Link to shared authority; distinguish operational sources from preserved copies, drafts, generated files, and navigation.

**Primary routes:** [Document Review](../../../capabilities/documentation-Tree/document-look.md), [Document Creation](../../../capabilities/documentation-Tree/document-creation.md), and [Document Lifecycle Standard](../standards/document-lifecycle.md).

**Preservation:** Use [Core Document Preservation](core-document-preservation.md) and the [Preservation Index](documents/preservation-index.md) when a core record is warranted.

**Alignment:** Before moving or consolidating documents, check ownership, lifecycle, inbound links, source authority, and recovery implications.

## Procedure 06 — Workspace Access and Operations

**Task message**

Use the actual repository, branch, tools, and permissions available. Confirm the target before writing and verify the resulting state. Do not infer technical enforcement from written policy.

**Primary routes:** [Permission Model](../../authority/permission-model.md) and [Workspace Authority](../../authority/workspace.md).

**Alignment:** Shared or protected operations require confirmation of authorization, target, and affected branch or consumers.

## Procedure 07 — Recovery and Preservation

**Task message**

Preserve before destructive work. Verify that the proposed recovery source actually exists and is usable; do not assume a backup, snapshot, or rollback path.

**Primary route:** [Recovery Authority](../../authority/recovery-authority.md), then the relevant files under `recovery/policies/`, `recovery/procedures/`, and `recovery/manifests/`.

**Alignment:** Structural, destructive, or core changes require an explicit preservation and recovery assessment before execution.

## Procedure 08 — Observability and Improvement Evidence

**Task message**

Keep collection, analysis, and suggestions separate. Use only authorized, supported evidence. Record worthwhile automation opportunities; do not expand an unrelated task into tool development.

**Primary routes:** [Collection guide](../../../observability/collection/README.md), `observability/analytics/`, and `observability/suggestions/`.

**Alignment:** Verify purpose, data scope, access, retention, and actual collection capability before introducing instrumentation.

## Procedure 09 — Navigation and Capability Discovery

**Task message**

Use this register and the root entrypoint to find the operational owner. Keep routes short and direct; broad navigation changes belong to Alignment Maintenance.

**Primary routes:** [Root README](../../../README.md), [Architecture](../architecture/architecture.md), [Repository Map](../architecture/repository-map.md), [Document Ownership](../architecture/document-ownership.md), and [Capability Discovery](../../../capabilities/capability-discovery.md).

## Procedure record archive

Detailed procedure text retained from earlier DP-C drafts is historical reference material, not a second current instruction set. Use [Procedure Navigation](documents/procedure-navigate.md) to locate the numbered records and generated full reference. Update this register when task wording, implementation destinations, or progress status changes.
