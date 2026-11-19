# DP C — Task Routes and Operating Messages

**Status:** Compact DP-C working draft for review. Route links should be checked against their current operational sources.

**Purpose:** Give each task a concise direction and a route to the right operational source. DP defines durable principles; DP C reminds the task owner what to do and where to continue. Detailed guidance belongs with its operational owner.

**Use:** Start with the root README, select the matching procedure below, then follow only the relevant source links.

**Order:** The nine procedures below retain the same order and titles as the root README and the core procedure-navigation index.

---

## Procedure 01 — Working Environment

**Task message**

Make the requested contribution in the nearest sensible location. Follow relevant local conventions, keep implementation and verification proportional, and defer non-blocking repository-wide cleanup to Maintenance. Respect applicable shared boundaries and leave the result usable.

**Primary route:** The nearest owning component and its local instructions. Begin at [root README](../README.md), route 1.

**Additional routes when relevant:** [Capability work](#procedure-04--capability-and-tool-work), [document work](#procedure-05--document-creation-and-editing), [protected changes](#procedure-03--core-and-sensitive-changes), or [recovery](#procedure-07--recovery-and-preservation).

---

## Procedure 02 — Maintenance Environment

**Task message**

Choose the lowest sufficient maintenance scope. Restore coherence where it materially improves ownership, usability, reachability, or recurring effort. Preserve meaningful differences and local independence; Maintenance organizes accumulated work but does not gate ordinary feature creation.

**Primary routes**
- [Minimal Maintenance](../maintenance/minimal-maintenance/minimal.md)
- [Alignment Maintenance draft](../maintenance/alignment-maintenance/alignment.md) — currently marked proposed and not adopted as authority.
- [Improvement Maintenance](../maintenance/improvement/improvement.md)

**Authority and preservation:** [Maintenance Authority](../core/authority/maintenance-authority.md), [Core Document Preservation](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/core-document-preservation.md), and the [core-preserved maintenance copies](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preservation-index.md).

---

## Procedure 03 — Core and Sensitive Changes

**Task message**

Treat changes to repository identity, core policy, authority, architecture, entrypoints, or shared contracts as protected. Read the relevant core sources and verify explicit authorization before changing them. Keep proposals separate from adopted rules.

**Primary route:** [Core README](../core/this-is-instruction-to-read-core-readme-before-proceeding/core-readme.md) and [Protected Change Procedure](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/protected-change.md).

**Additional sources:** [Change Gate](../core/this-is-instruction-to-read-core-readme-before-proceeding/standards/change-gate.md), [Permission Model](../core/authority/permission-model.md), [Principles](../core/this-is-instruction-to-read-core-readme-before-proceeding/standards/principles.md), and the applicable authority document.

---

## Procedure 04 — Capability and Tool Work

**Task message**

Discover before duplicating. Extend a suitable existing capability when its purpose and interface remain coherent; create a separate one when ownership, purpose, interface, or lifecycle genuinely differs. Verify the actual implementation, permissions, dependencies, and relevant behavior.

**Primary route:** [Capability Discovery](../capabilities/capability-discovery.md), then the owning capability under **capabilities/**.

**Core-preserved copy:** [Capability Discovery record](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preserved/capabilities/capability-discovery.md).

**Additional route:** [Document Creation and Editing](#procedure-05--document-creation-and-editing) when capability documentation is part of the task.

---

## Procedure 05 — Document Creation and Editing

**Task message**

Identify the document's purpose, audience, owner, authority, and lifecycle before writing. Keep shared requirements canonical, make the document usable at its point of use, and route readers to operational sources rather than historical or generated copies.

**Primary routes:** [Document Review](../capabilities/documentation-Tree/document-look.md), [Document Creation](../capabilities/documentation-Tree/document-creation.md), and [Document Lifecycle Standard](../core/this-is-instruction-to-read-core-readme-before-proceeding/standards/document-lifecycle.md).

**Core-preserved copies:** [Document Review](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preserved/capabilities/documentation-Tree/document-look.md) and [Document Creation](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preserved/capabilities/documentation-Tree/document-creation.md).

**Preservation route:** [Core Document Preservation](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/core-document-preservation.md) and the [Preservation Index](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preservation-index.md).

---

## Procedure 06 — Workspace Access and Operations

**Task message**

Confirm the repository, branch, target paths, available tool surface, and actual permissions before operating. Do not infer execution or write authority from a policy statement or from the presence of a tool. Verify the resulting state before reporting completion.

**Primary routes:** [Permission Model](../core/authority/permission-model.md) and [Workspace Authority](../core/authority/workspace.md).

---

## Procedure 07 — Recovery and Preservation

**Task message**

Before destructive or difficult-to-reverse work, identify what must be preserved and verify a suitable recovery path. Do not assume that a backup, snapshot, manifest, or restoration option exists. Keep recovery authority independent from routine maintenance.

**Primary routes:** [Recovery Authority](../core/authority/recovery-authority.md), recovery/policies/, recovery/procedures/, and recovery/manifests/.

**Document-specific preservation:** [Core Document Preservation](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/core-document-preservation.md).

---

## Procedure 08 — Observability and Improvement Evidence

**Task message**

Keep raw collection, analytics, and suggestions distinct. Use only authorized, technically available evidence. Record recurring deterministic work as a reviewable suggestion; do not turn an unrelated task into unsolicited tool development.

**Primary routes:** [Collection guide](../observability/collection/README.md), observability/analytics/, and observability/suggestions/.

---

## Procedure 09 — Navigation and Capability Discovery

**Task message**

Start at the root README and follow the nearest relevant owner route. Load only sources required by the task. Use existing navigation; broad route, hub, or repository-map changes belong to Maintenance.

**Primary routes:** [Root README](../README.md), [Repository Map](../core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/repository-map.md), [Document Ownership](../core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/document-ownership.md), and [Capability Discovery](../capabilities/capability-discovery.md).

**Procedure reference:** [Procedure Navigation](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/procedure-navigate.md) routes to the operational sources and preserved procedure records.

---

## Document and source roles

- **Operational source:** current instructions maintained by the owning component. Normal task work goes here.
- **Core-preserved copy:** a deliberate historical record of an externally owned source. It is not a competing current authority.
- **Core-native source:** canonical core policy, authority, architecture, standards, or procedure.
- **Generated composite:** assembled from declared inputs; edit the inputs and regenerate the output.
- **Navigation document:** points to sources and sections without duplicating their instructions.
- **Proposal or draft:** not adopted authority unless the responsible process explicitly adopts it.

The detailed procedure text retained from the working draft is available through [the generated full reference](../core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/full-procedures.md). It is a historical integrated reference, not the default destination for routine tasks.
