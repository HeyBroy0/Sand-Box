# DP — Sand-Box Design Principles

**Purpose:** Define the durable identity, design principles, and architectural decision criteria for Sand-Box. DP states what the workspace should be and why; it does not prescribe task procedures. Apply the relevant task guidance in [DP C](DP%20C) when turning these principles into work.

**Status:** Consolidated design document integrating the original DP and DP-v2. It is a design reference, not proof that every described mechanism or directory currently exists.

## Scope and identity

Sand-Box is an evolving toolbox and repository workspace for ChatGPT/Codex work through the connected GitHub environment. It helps complete repository tasks and extend practical capability through reusable, repository-managed tools, scripts, documentation, and workflows.

Sand-Box is not a general-purpose AI-agent platform, orchestration framework, or independent agent runtime. GitHub connector access, repository-owned automation, and any separate execution environment are distinct capabilities and security boundaries.

## Principles

### 1. Serve the real Sand-Box workspace
Sand-Box should become more capable by improving real repository work in its supported ChatGPT/Codex and GitHub context.
- Prioritize recurring, demonstrated repository needs over unrelated agent-runtime ambitions.
- Design against the connector operations, permissions, and execution capabilities that actually exist.
- Treat connector access, automation, and execution environments as separate system boundaries.

### 2. Keep the always-read layer small and durable
Entrypoints should establish identity, essential constraints, and navigation without becoming encyclopedias.
- Keep the root README focused on purpose, routing, and genuinely repository-wide essentials.
- Put durable cross-repository principles and contracts in their canonical core locations; keep task detail elsewhere.
- Add to the always-read layer only when a rule or route is genuinely needed across the workspace.

### 3. Protect core and shared authority
Core owns the durable identity, policy, architecture, configuration, authority, and shared contracts whose change can affect the repository as a whole.
- Treat core, repository entrypoints, shared authority, and cross-repository routing or discovery contracts as sensitive surfaces.
- Ordinary task work and routine maintenance do not gain authority to change protected surfaces merely because repository write access exists.
- Use explicit authorization, applicable change procedures, and enforceable repository controls where available.

### 4. Load context progressively and by relevance
Correct work requires reliable access to relevant context, not universal loading of all documentation.
- Separate entrypoints, shared principles, task instructions, specialist references, and examples by purpose.
- Make the next relevant source reachable through concise routes and direct references.
- Treat unnecessary context, duplicated rules, and forced universal loading as maintenance costs.

### 5. Separate requirements from explanation
Mandatory constraints must remain distinguishable from recommendations, rationale, and examples.
- Give each mandatory rule one identifiable authoritative home.
- Use instructions for requirements and boundaries; use guides for procedures, examples, and explanation.
- Link to authoritative rules instead of creating competing copies or silently turning preferences into requirements.

### 6. Make documents and capabilities understandable at their point of use
A component should be usable without undocumented assumptions or unrelated repository history.
- State a document's purpose, audience, applicability, and useful next reference.
- Give capabilities explicit purposes, interfaces, inputs, outputs, defaults, dependencies, limitations, and failure behavior.
- Make assumptions and external dependencies visible rather than relying on hidden runtime or file context.

### 7. Compose and extend before duplicating
Grow capability by improving and combining useful components rather than accumulating near-identical alternatives.
- Extend an existing capability when its purpose and interface can accommodate the need cleanly.
- Create a distinct capability or document when purpose, audience, interface, ownership, or lifecycle genuinely differs.
- Keep shared behavior and mandatory rules canonical; avoid duplicate implementations and alternate authoritative records.

### 8. Preserve compatibility deliberately
Shared interfaces are contracts with consumers, not isolated implementation details.
- Identify affected callers, workflows, catalog entries, tests, and documents before changing a shared contract.
- Prefer compatible extensions when practical.
- When a breaking change is justified, include its consumer impact, migration path, and verification in the change.

### 9. Let structure earn its complexity
The repository should use the smallest coherent organization that solves demonstrated needs.
- Add directories, registries, schemas, abstractions, and routing layers only when their practical benefit exceeds their ongoing cost.
- Keep related responsibilities together unless distinct ownership, purpose, authority, or lifecycle justifies separation.
- Promote patterns and infrastructure based on demonstrated use, not hypothetical completeness.

### 10. Make creation locally practical
Ordinary work should be able to produce useful results without first solving repository-wide organization.
- Choose the nearest sensible owner and keep a contribution focused and locally understandable.
- Allow proportionate local formats, explanations, and direct references without requiring universal templates or perfect indexing.
- Leave broad normalization, deduplication, and navigation redesign to dedicated maintenance, while respecting shared rules and contracts.

### 11. Keep automation reusable, thin, and least-privileged
Automation should expose capability without duplicating its implementation or acquiring unnecessary authority.
- Keep reusable logic in maintainable capability implementations; use workflows as thin integration or execution surfaces.
- Grant automation only the permissions and dependencies required for its defined purpose.
- Keep credentials and sensitive information out of source, inputs, logs, and generated artifacts.

### 12. Maintain one canonical capability-discovery model
Capabilities should have a consistent, authoritative discovery identity.
- Use one canonical catalog or discovery model when adopted by the repository.
- Keep catalog metadata, supported entrypoints, implementation, documentation, and tests consistent.
- Treat filenames and search results as locators, not proof that a capability is registered, complete, or supported.

### 13. Verify important behavior proportionately
Correctness should be checked at the boundaries that matter, without imposing needless universal overhead.
- Give shared behavior testable contracts, including relevant invalid and edge cases.
- Scale verification to the behavior, risk, and consumers affected.
- Describe capability status honestly; do not claim tests, controls, or support that have not been checked.

### 14. Distinguish policy, authorization, and enforcement
These concepts are related but not interchangeable.
- Policy describes intended behavior; authorization determines who may act; enforcement technically prevents disallowed actions.
- Use GitHub rulesets, branch protection, permissions, required checks, and appropriate execution controls for enforceable restrictions.
- Never imply that repository instructions or container settings restrict an already-authorized connector unless the relevant system actually enforces that boundary.

### 15. Preserve user material and recoverability
User material, source references, working changes, repository history, and known-good states are assets.
- Age, inactivity, or absence from a quick search is not sufficient reason for deletion.
- Scope destructive cleanup explicitly and preserve a suitable, verified recovery path.
- Keep recovery records and authority independent from routine maintenance; maintenance may request recovery but must not silently invalidate it.

### 16. Maintain coherence through dedicated maintenance
Coherence should grow through focused maintenance, not through burdensome upfront requirements on every contribution.
- Use Minimal Maintenance for bounded local cleanup, Alignment Maintenance for documentation and navigation coherence, and Improvement Maintenance for proven broader changes.
- Let observed friction—duplication, unclear ownership, broken routes, conflicting guidance, or repeated repair—guide maintenance priorities.
- Preserve meaningful differences in scope, authority, and behavior instead of forcing visual or structural uniformity.

### 17. Keep observability truthful and proportionate
Evidence can support improvement when it is useful, authorized, and technically available.
- Prefer structured, durable event records over repeated narrative reporting when a supported mechanism exists.
- Separate raw collection, derived analytics, and persistent improvement suggestions.
- Collect only what has a defined purpose and appropriate access and retention boundaries; never claim proposed telemetry is implemented.

### 18. Protect the stable workspace through deliberate promotion
The stable line should represent a coherent, verified workspace rather than ordinary task development.
- Keep stable, task-development, and historical-preservation branch roles distinct, following the repository's current branch controls and naming conventions.
- Promote broad or shared changes only through explicit authorization, applicable verification, and repository protection controls.
- Treat archive branches and recovery snapshots as preservation resources, not routine working branches.

## Architectural responsibility domains

These domains describe responsibilities, not a mandatory one-to-one directory structure. Create or split directories only when ownership and lifecycle justify them.

| Domain | Responsibility | Boundary |
| --- | --- | --- |
| Workspace Core | Identity, durable principles, architecture, configuration, authority, shared contracts | Protected from ordinary capability work and routine maintenance |
| Capability System | Reusable tools, scripts, workflows, integrations, tests, discovery metadata | Implements capability; does not redefine core policy |
| Workspace Access & Operations | ChatGPT/Codex interaction with the repository through the GitHub connector | Limited to actual connector capabilities; not an independent agent runtime |
| Observability & Maintenance | Authorized evidence, analytics, suggestions, routine maintenance, improvement | Maintenance does not inherit core or recovery authority |
| Recovery System | Preservation, snapshots, history, rollback, restoration | Independent from routine cleanup and maintenance |

## Core decision tests

| Question | Decision criterion |
| --- | --- |
| Does this belong in Sand-Box? | It improves the defined GitHub-connected workspace or a real responsibility within it. |
| Does it belong in core? | It establishes durable repository-wide identity, policy, architecture, authority, or a shared contract. |
| Must every task load core? | No. Load it when the task touches a core surface or a governing contract. |
| Should a document or directory be split? | Only when parts have distinct responsibilities or audiences and benefit from independent use or maintenance. |
| Should a new tool, abstraction, or schema be created? | Prefer composition; create it for a distinct, demonstrated need that cannot be served cleanly otherwise. |
| Should a shared interface change? | Identify consumers, justify the compatibility cost, and account for migration and verification. |
| Can instructions enforce security? | No. Instructions express policy; actual enforcement belongs to the relevant permission or execution layer. |
| Should old material be deleted? | Not solely because it is old, inactive, or absent from a quick search. Preserve recovery. |
| Should maintenance change core or control recovery? | No, not without separate explicit authority; recovery remains independently protected. |
| Should telemetry or infrastructure be assumed to exist? | No. Verify implementation, authorization, and actual capability. |
| How should work reach the stable branch? | Through the explicitly authorized promotion process and applicable protection and verification controls. |

## Relationship to DP C

DP C is the operational companion to this document. It translates these principles into independently loadable task guidance. Read only the DP C part relevant to the task; do not treat DP as a universal task checklist.

## Overall principle

Sand-Box should remain a focused, extensible GitHub-connected workspace: easy to use and extend locally, coherent through reachable shared guidance and dedicated maintenance, governed by explicit authority, and able to preserve and restore known-good work.
