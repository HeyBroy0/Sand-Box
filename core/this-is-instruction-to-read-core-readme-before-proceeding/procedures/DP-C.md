# DP-C — Implementation Procedure Register

**Status:** Proposed operational draft for review.

**Purpose:** Translate [Principles](../standards/principles.md) and [Architecture](../architecture/architecture.md) into task messages, implementation routes, and progress tracking. DP-C is the single current source for procedure wording and task navigation. It should guide the work, not repeat the principles or reproduce the architecture.

**Use:** Select the procedure matching the requested outcome. Each numbered part is independently usable and contains its own trigger, task direction, essential boundaries, destination, and completion expectation. Read only that part and the operational sources it names.

## Implementation status

| No. | Procedure | Current implementation state |
|---|---|---|
| 01 | Working Environment | Local-work model established; detailed guidance remains with each component |
| 02 | Maintenance Environment | Three operational guides exist; Alignment remains proposed |
| 03 | Core and Sensitive Changes | Initial gate, procedure, and authority drafts exist; adoption review remains |
| 04 | Capability and Tool Work | Discovery guide exists; catalog is empty and capability registration remains incomplete |
| 05 | Document Creation and Editing | Review, creation, lifecycle, and preservation guidance exists as initial drafts |
| 06 | Workspace Access and Operations | Permission and workspace guidance exists as proposed drafts; technical controls require independent verification |
| 07 | Recovery and Preservation | Authority draft exists; operational policies, procedures, and manifests remain incomplete |
| 08 | Observability and Improvement Evidence | Collection guide exists; analytics and suggestion formats remain incomplete |
| 09 | Navigation and Capability Discovery | Main routes exist; this register is the current procedure source |

Update status when an implementation destination or its readiness materially changes. Do not mark a proposed document adopted merely because it exists.

---

## Procedure 01 — Working Environment

**Use when:** Creating or changing a feature, tool, test, workflow, task-specific document, or other bounded contribution within one owning component.

**Task message:** Put the contribution with its nearest sensible owner. Follow useful local conventions, make reasonable local design choices, and add only what makes the result usable.

**Working bounds:** Inspect the target and direct dependencies rather than auditing the repository. Extend an existing component when the fit is coherent; separate it only when purpose, interface, owner, or lifecycle differs. Verify the affected behavior and report important assumptions or limitations. Leave unrelated organization to Maintenance.

**Alignment:** Check direct interfaces and consumers. When the change crosses component boundaries or touches shared contracts, expand review to the affected owners and dependencies. If it reaches core or another protected surface, use Procedure 03 before editing.

**Destination:** Start at the [root README](../../../README.md), then use the nearest component's local guidance. The component owner maintains the operational implementation and its detailed instructions.

**Complete when:** The requested contribution is usable, proportionately verified, placed with its owner, and its result and known limitations are clear.

---

## Procedure 02 — Maintenance Environment

**Use when:** The requested outcome is improved coherence across existing documents, components, terminology, placement, ownership, or navigation—not merely the completion of one local contribution.

**Task message:** Choose the lowest sufficient maintenance scope. Correct genuine friction, preserve useful differences, and avoid normalization for appearance alone.

**Select the scope:**
- **Minimal:** one bounded local defect or inconsistency; preserve the existing organization.
- **Alignment:** related documents, components, ownership, terminology, or routes have drifted and need coherent treatment.
- **Improvement:** the problem requires a broader capability, integration, shared interface, or architectural change supported by demonstrated need.

**Working bounds:** Establish source ownership and status before moving or consolidating material. Keep one canonical home for shared requirements, retain local explanations that make a component independently usable, and verify affected routes. Maintenance organizes accumulated work; it is not an approval gate for ordinary Working tasks.

**Alignment:** Before changing core standards, architecture, authority, root routes, or shared contracts, stop ordinary maintenance and use Procedure 03. Preserve source material and check recovery implications before destructive changes.

**Destinations:** [Minimal Maintenance](../../../maintenance/minimal-maintenance/minimal.md), [Alignment Maintenance](../../../maintenance/alignment-maintenance/alignment.md), [Improvement Maintenance](../../../maintenance/improvement/improvement.md), and [Maintenance Authority](../../authority/maintenance-authority.md). Use [Core Document Preservation](core-document-preservation.md) when an externally owned source needs a protected core record.

**Complete when:** The affected area is easier to understand, maintain, and navigate without losing meaningful distinctions or adding unnecessary process.

---

## Procedure 03 — Core and Sensitive Changes

**Use when:** A change may alter repository identity, principles, architecture, authority, permissions, root entrypoints, shared routes, cross-component contracts, or the meaning or status of a protected record.

**Task message:** Increase alignment checks with proximity to protected surfaces. Understand the design and authority before editing; do not infer permission from general write access.

**Before editing:** Identify affected files, owners, consumers, and downstream behavior. Read the relevant [Principles](../standards/principles.md), [Architecture](../architecture/architecture.md), [Change Gate](../standards/change-gate.md), and authority sources. Check compatibility, migration, preservation, and recovery implications. Confirm explicit authorization through the actual applicable process.

**Boundaries:** Keep proposals separate from adopted requirements. Verify the actual GitHub or execution controls rather than assuming written instructions enforce permissions. Stop when authorization, source authority, impact, or required recovery is unclear.

**Destinations:** [Core README](../core-readme.md), [Protected Change Procedure](protected-change.md), [Change Gate](../standards/change-gate.md), [Permission Model](../../authority/permission-model.md), and the relevant core authority owner.

**Complete when:** The authorized change is bounded, affected consumers and routes are checked, required recovery is accounted for, verification is recorded, and unresolved decisions remain explicit.

---

## Procedure 04 — Capability and Tool Work

**Use when:** Finding, creating, extending, testing, or integrating a reusable tool, script, workflow, integration, or other capability.

**Task message:** Discover before duplicating. Prefer a suitable existing capability; create a separate one only when its purpose, interface, owner, or lifecycle is meaningfully different.

**Working bounds:** Verify that the implementation actually exists and is usable. Make the purpose, inputs, outputs, defaults, dependencies, limitations, failure behavior, and permissions clear at the point of use when relevant. Keep shared logic reusable and integration surfaces thin. Use only the permissions needed for the capability.

**Alignment:** Before changing a shared capability or interface, identify its consumers and compatibility requirements. A catalog entry, filename, or search result is a locator, not proof of operational support.

**Destination:** [Capability Discovery](../../../capabilities/capability-discovery.md), then the owning capability under `capabilities/`. Update implementation, tests, documentation, and catalog metadata only where the task and actual catalog contract require it.

**Complete when:** The capability's owner and contract are clear, relevant behavior and failures are checked, and support or registration status is reported accurately.

---

## Procedure 05 — Document Creation and Editing

**Use when:** Creating, editing, reviewing, relocating, consolidating, preserving, or routing repository documents.

**Task message:** Place each document with the responsibility that maintains it. Make its purpose, audience, status, and lifecycle clear. Keep shared authority canonical and local instructions usable at their point of need.

**Before writing:** Identify the operational owner and check for an existing source. Distinguish an operational source, core-native source, core-preserved historical copy, generated composite, navigation document, and proposal. Use a format that fits the reader; do not impose unnecessary templates or hubs.

**Working bounds:** State necessary context, requirements, assumptions, and limitations. Link to shared authority rather than reproducing it. Preserve enough local explanation for independent use. Verify factual claims and links.

**Alignment:** Before moving or consolidating documents, check ownership, authority, status, lifecycle, inbound links, and recovery implications. Preserve externally owned documents in core only through the preservation procedure. Edit generation inputs, not generated composites.

**Destinations:** [Document Review](../../../capabilities/documentation-Tree/document-look.md), [Document Creation](../../../capabilities/documentation-Tree/document-creation.md), [Document Lifecycle](../standards/document-lifecycle.md), and [Core Document Preservation](core-document-preservation.md).

**Complete when:** The document has a clear owner and status, is usable for its intended task, does not create competing authority, and affected routes resolve.

---

## Procedure 06 — Workspace Access and Operations

**Use when:** Reading or changing repository files, branches, commits, pull requests, workflows, connector settings, or execution environments.

**Task message:** Confirm the repository, branch or reference, target paths, available tool surface, and actual permissions before acting. Verify the resulting state before reporting.

**Working bounds:** Use only the capabilities actually provided by the connected service or runtime. GitHub access, local filesystem access, hosted execution, workflow execution, and external-service access are distinct. Do not infer one from another, or treat successful write access as proof of task authorization.

**Alignment:** Shared and protected operations require confirmation of scope, authorization, affected branch or consumers, and the relevant protection controls. Do not force-update or overwrite user-authored material without explicit authorization.

**Destinations:** [Permission Model](../../authority/permission-model.md) and [Workspace Operations](../../authority/workspace.md).

**Complete when:** The intended operation is confirmed, the resulting state has been checked, and limitations or failures are accurately reported.

---

## Procedure 07 — Recovery and Preservation

**Use when:** A change is destructive, difficult to reverse, structurally significant, or involves archival material, preservation, rollback, or restoration.

**Task message:** Preserve before destructive work. Verify that the recovery source exists and is usable; never assume a backup, snapshot, manifest, or rollback path.

**Before acting:** Identify affected material and history, applicable retention requirements, the proposed change scope, and the known-good recovery point. Check who has authority to approve exceptional recovery or policy changes. Avoid irreversible cleanup when the recovery path or authority is unclear.

**Boundaries:** Recovery remains independent from routine Maintenance. Age or apparent inactivity alone is not a reason to delete material. Maintenance may request recovery but must not silently invalidate recovery records.

**Destinations:** [Recovery Authority](../../authority/recovery-authority.md), `recovery/policies/`, `recovery/procedures/`, and `recovery/manifests/`.

**Complete when:** Required source material and recovery state are identified and verified, the authorized operation is bounded, and preservation or restoration results are recorded accurately.

---

## Procedure 08 — Observability and Improvement Evidence

**Use when:** Designing or reviewing activity collection, analytics, recurring-friction evidence, or improvement suggestions.

**Task message:** Keep raw collection, analysis, and suggestions distinct. Use only authorized and technically supported evidence. Record worthwhile automation opportunities without expanding unrelated work into tool development.

**Working bounds:** Define the purpose and necessary data before collecting. Minimize data, establish access and retention boundaries, and protect sensitive information. Verify that the collection mechanism exists before describing it as active.

**Information flow:** Collection stores raw records; Analytics derives patterns; Suggestions records reviewable opportunities. Evidence may inform decisions but does not itself authorize repository changes or capability development.

**Destinations:** [Collection guide](../../../observability/collection/README.md), `observability/analytics/`, and `observability/suggestions/`.

**Complete when:** The evidence's origin and limitations are clear, access and data boundaries are respected, and suggestions distinguish observation from estimate and implementation decision.

---

## Procedure 09 — Navigation and Capability Discovery

**Use when:** Finding the correct instructions or capability, improving routes, or changing shared navigation and discovery.

**Task message:** Start at the root entrypoint and follow the route to the operational owner. Keep navigation direct and task-oriented; avoid creating another layer unless it materially improves reachability.

**Working bounds:** For ordinary work, use existing routes and add only a direct local reference needed to use the contribution. Treat filenames, search results, and catalog records as locators; verify the actual destination and capability status.

**Alignment:** Broad route, hub, repository-map, ownership, or capability-discovery changes belong to Alignment Maintenance. Check all affected entrypoints, local routes, source owners, and consumers before changing shared navigation. If the change affects core or protected routes, use Procedure 03.

**Destinations:** [Root README](../../../README.md), [Architecture](../architecture/architecture.md), [Repository Map](../architecture/repository-map.md), [Document Ownership](../architecture/document-ownership.md), and [Capability Discovery](../../../capabilities/capability-discovery.md).

**Complete when:** The intended reader can reach the current operational source through a clear route without being sent to a preserved copy or generated artifact by mistake.

---

## Historical records

Detailed text from earlier procedure drafts is retained for provenance and review. It is not a second current instruction set. Use the [Procedure Record Index](documents/procedure-record-index.md) to locate those records.
