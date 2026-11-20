# Architecture — Sand-Box Design Structure

**Status:** Proposed architecture draft for review. It describes intended structure and relationships; it does not assert that every directory, process, capability, or technical control is implemented.

## Purpose and relationship to other documents

Architecture turns the durable desires in [Principles](../standards/principles.md) into a coherent system design. It defines the workspace's responsibility domains, information flow, document lifecycle, task routing, authority boundaries, and growth model.

The design-to-implementation chain is:

1. **Principles** define what the workspace values and the constraints it must preserve.
2. **Architecture** defines how those values are arranged into a system.
3. **DP-C** translates the principles and architecture into concise procedures, task messages, implementation destinations, and progress tracking.
4. **Operational sources** provide the detailed guidance or capability at the owning location.
5. **Verification and Maintenance feedback** validate the implementation and improve accumulated coherence.

Architecture is the design structure, not a second task router. The [Repository Map](repository-map.md) remains the concise locator for current repository areas. [Document Ownership](document-ownership.md) remains the source registry. Neither is replaced by this document.

## 1. Responsibility domains

These are logical responsibility domains. They do not require a one-to-one directory structure, separate agent runtime, or independent permission system.

| Domain | Responsibility | Design boundary |
|---|---|---|
| **Workspace Core** | Identity, principles, architecture, configuration, authority, shared contracts | Protected from ordinary feature work and routine maintenance |
| **Working Environment** | New features, local tools, task-scoped documents, implementation, proportionate checks | Optimizes local progress; does not own repository-wide organization |
| **Maintenance Environment** | Canonical ownership, alignment, consolidation, placement, navigation, long-term coherence | Main organizing force; does not inherit core or recovery authority |
| **Capability System** | Reusable tools, scripts, workflows, integrations, tests, discovery metadata | Implements reusable capability; does not redefine core policy |
| **Workspace Access and Operations** | Repository work through supported GitHub and execution surfaces | Limited to the capabilities and permissions actually provided |
| **Recovery System** | Preservation, known-good states, history, rollback, restoration | Independent from routine cleanup and maintenance |
| **Observability** | Authorized evidence, analytics, and reviewable suggestions | Proportionate; does not itself authorize changes |

## 2. Information and control flow

### Entry and task routing

- The root [README](../../../README.md) is the always-read workspace entrypoint. It identifies the task family and points toward the next source.
- [DP-C](../procedures/DP-C.md) is the single current procedure register. It owns task messages, detailed task routes, implementation destinations, and progress status.
- This Architecture document describes the design behind those routes; it is not required context for every ordinary task.
- The Core README is loaded when core, authority, architecture, protected procedures, or shared contracts are actually involved.
- Component-local guidance is the normal destination for local implementation details.

### Work lifecycle

A typical task follows this flow:

```text
Root README
    |
    v
DP-C procedure and task message
    |
    v
Owning component or specialist operational source
    |
    v
Implementation and proportionate verification
    |
    +---- local result ----> report completion
    |
    +---- non-blocking coherence issue ----> Maintenance
    |
    +---- protected boundary ----> authority and protected-change review
    |
    +---- destructive / difficult recovery ----> Recovery
```

A task may touch multiple domains. Add only the specialist guidance needed by the actual boundary; do not require every route to load every domain.

## 3. Placement and composition model

### Local ownership

Place an operational document, capability, or implementation with the responsibility that maintains it. Prefer the nearest sensible existing owner. Split or relocate only when purpose, audience, interface, authority, or lifecycle creates a real ownership boundary.

### Reuse before duplication

Extend an existing capability when its purpose and interface remain coherent. Create a separate capability when it has a distinct purpose, owner, interface, or lifecycle. Keep shared behavior in the capability implementation and keep workflows or connector-facing surfaces thin.

### Progressive loading

Entrypoints route; specialist documents explain; implementations perform. Do not place full procedural explanations in the root README or repeat the same task instructions across every route. Preserve enough local explanation for a component to remain independently usable.

## 4. Document lifecycle and source direction

| Document class | Role | Normal routing behavior |
|---|---|---|
| **Operational source** | Current maintained guidance at the owning location | Route task work here |
| **Core-native source** | Canonical principles, architecture, authority, standards, or protected procedures owned by core | Link directly; do not create redundant copies |
| **Core-preserved copy** | Historical record of an externally owned source | Use for preservation, provenance, or review; not routine task work |
| **Generated composite** | Deterministic output assembled from declared source inputs | Update inputs and regenerate; do not edit manually |
| **Navigation document** | Concise route to sources and sections | Route readers; do not reproduce destination content |
| **Draft or proposal** | Material under development, not adopted authority | Label status and keep separate from current adopted requirements |

A preserved copy identifies its operational source and capture state. It may link outward to the operational source. The operational source should not link back to the core-preserved copy merely to establish provenance.

Core-native authority documents remain at their canonical core locations; they do not need redundant copies in the preserved-document area.

## 5. Alignment model for shared and protected surfaces

Alignment effort should increase with the scope and sensitivity of a change.

### Local component boundary

Use the nearest owner, local conventions, direct dependencies, and proportionate checks. Do not run a repository-wide review for an ordinary local contribution.

### Shared or cross-component boundary

Before changing shared behavior, check:
- Canonical owner and applicable operational guidance.
- Direct consumers, interfaces, workflows, and dependent documents.
- Compatibility, naming, placement, and discovery routes.
- Tests and verification needed by affected consumers.

### Protected core boundary

Before changing principles, architecture, authority, root entrypoints, shared routes, or cross-repository contracts:
- Read the relevant principles, architecture, standards, and authority sources.
- Identify downstream consumers and the effect on the architecture.
- Confirm explicit authorization through the applicable process.
- Check compatibility, preservation, recovery, and migration implications.
- Verify actual technical controls rather than relying on prose.
- Keep unresolved proposals separate and stop the edit when authority is unclear.

This graduated model preserves Working autonomy while requiring stronger alignment near protected surfaces.

## 6. Maintenance architecture

Maintenance is the continuing coherence function for the workspace, not a pre-approval stage for local work.

- **Minimal Maintenance** corrects a bounded local defect while preserving existing organization.
- **Alignment Maintenance** restores coherence across related documents, components, ownership, and navigation.
- **Improvement Maintenance** integrates broader capabilities or architectural changes when demonstrated need justifies them.

These are selectable scopes, not mandatory sequential stages. Use the smallest scope that resolves the actual friction. Core authority and recovery remain outside Maintenance's independent control.

## 7. Capability architecture

A reusable capability should have a defined purpose and, where relevant, a clear interface, inputs, outputs, defaults, dependencies, limitations, failure behavior, permissions, and verification.

The discovery model should connect catalog metadata, implementation, documentation, tests, and supported entrypoints. The catalog is a locator and declaration of capability status; it is not proof that a referenced implementation is operational. Do not claim registration or support until the underlying material is verified.

## 8. Recovery architecture

Recovery is independent from routine Maintenance. Preservation and restoration should have distinct policy, procedure, and record responsibilities.

- Policies define what must be preserved and under what conditions.
- Procedures define how a preservation or restoration operation is carried out.
- Manifests record the relevant recovery state and references.

Do not claim that a backup, snapshot, manifest, or restoration option exists until it has been verified. Destructive and difficult-to-reverse work requires a suitable recovery assessment before execution.

## 9. Observability architecture

Keep three stages distinct:

1. **Collection** captures authorized raw events through a real, supported mechanism.
2. **Analytics** derives patterns and evidence from collected records.
3. **Suggestions** records reviewable maintenance or improvement opportunities.

Collection requires a defined purpose, data scope, authorization, access, retention, and failure behavior. Observability does not grant permission to change the repository. A deterministic automation suggestion does not itself authorize tool development.

## 10. Promotion and evolution

Local contributions can be useful before they are globally normalized. Maintenance may later integrate proven patterns, repair cross-component fit, or propose improvements.

Shared or protected changes require explicit authorization and proportionate verification. Stable promotion should represent a coherent, verified workspace under the repository's actual branch and protection controls. Do not claim that branch protection, required checks, or isolation exists without inspecting the relevant system.

## 11. Architecture decision tests

| Question | Design direction |
|---|---|
| Is this a local contribution? | Place it with the nearest owner; keep its design and verification local and proportional. |
| Does it affect multiple components? | Check ownership, consumers, compatibility, and routes before changing the shared behavior. |
| Does it change core or shared authority? | Apply protected alignment and authorization; do not infer approval from write access. |
| Is a new directory, hub, registry, or abstraction needed? | Add it only when a real ownership or lifecycle boundary or demonstrated use justifies its cost. |
| Is a document a current source or a preserved record? | Make the lifecycle explicit and route ordinary work to the operational source. |
| Is a proposed control actually enforced? | Verify in the service or execution environment that would enforce it. |
| Is a problem non-blocking but repository-wide? | Finish the bounded task and route the coherence issue to Maintenance. |
