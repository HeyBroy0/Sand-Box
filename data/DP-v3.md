# DP — Sand-Box Design Principles

**Purpose:** Define the durable identity, boundaries, and design principles of Sand-Box. DP states what the workspace should be and why; DP C translates these principles into task-specific operating guidance.

**Status:** DP v3 working draft for review. It uses DP-final and DP-final-v2 as its main bases, carrying forward their useful material and strengthening document lifecycle, local usability, routing, and operational-efficiency principles. This draft is staged in data; its intended canonical destination is standards/principles.md. It does not claim that every described directory, workflow, or control is implemented.

## Operating approach

Working and Maintenance describe different responsibilities and types of work, not separate technical sandboxes, credentials, or security levels. Their distinction should normally be implemented through task routing and the placement of useful guidance.

- Ordinary feature creation and task-scoped changes should route to the nearest owning component and its local instructions. This keeps Working self-contained and avoids unnecessary repository-wide context.
- Cleanup, consolidation, alignment, and broad navigation work should route to the relevant Maintenance guidance. Maintenance is the main organizing force for accumulated coherence.
- A task may cross responsibilities. Load additional guidance when the actual work crosses its boundary; do not impose a universal mode preamble or require every task to load both environments.
- Both types of work remain subject to the same repository-wide authority, security, compatibility, preservation, and recovery requirements.

## Principles

### 1. Serve the real Sand-Box workspace
Sand-Box should improve practical repository work in its supported ChatGPT/Codex and GitHub-connected context.
- Prioritize demonstrated repository needs over unrelated agent-runtime or orchestration ambitions.
- Design for connector operations, permissions, and execution capabilities that actually exist.
- Keep GitHub access, automation, and separate execution environments distinct as system capabilities and boundaries.

### 2. Keep the always-read layer small and durable
Entrypoints should establish identity, essential constraints, and navigation without becoming encyclopedias.
- Keep root-level guidance focused on purpose, routing, and genuinely workspace-wide essentials.
- Put durable shared principles and authority in canonical locations; keep task detail elsewhere.
- Add to the always-read layer only when a rule or route is genuinely needed across the workspace.

### 3. Express work responsibilities through task routing
Working creates and extends locally; Maintenance organizes and aligns across accumulated work. The distinction should be visible in the routes and ownership model rather than repeated as a universal prerequisite.
- Route ordinary feature work to its owning component and local guidance, keeping the contribution self-contained.
- Route consolidation, alignment, and cross-document organization to Maintenance and the affected specialist guidance.
- Do not make Maintenance a precondition or approval gate for ordinary feature creation; do not require every local task to load repository-wide maintenance instructions.

### 4. Give Working deliberate local allowances
Ordinary work should not have to solve the whole repository's organizational structure before producing a useful contribution.
- Permit reasonable local choices about placement, format, explanation, and implementation when they do not violate a shared contract.
- Require only proportionate discovery, dependencies, documentation, navigation, and verification for the task.
- Allow non-blocking normalization, deduplication, and broad alignment to be deferred to Maintenance.

### 5. Make Maintenance responsible for accumulated coherence
Maintenance should continuously reduce the organizational friction that naturally accumulates as the workspace grows.
- Own broad alignment of canonical sources, document placement, terminology, navigation, and cross-component consistency.
- Consolidate genuine duplication and clarify ownership while preserving meaningful differences in scope, authority, and behavior.
- Prioritize observed friction and recurring repairs; do not pursue uniformity or structure for its own sake.

### 6. Protect core and shared authority in both environments
Core owns durable identity, policy, architecture, configuration, authority, and shared contracts whose change can affect the repository as a whole.
- Treat core, entrypoints, shared authority, and cross-repository routing or discovery contracts as sensitive surfaces.
- Neither Working allowances nor Maintenance responsibility grants permission to change protected surfaces without explicit authorization and the applicable procedure.
- Use enforceable repository or execution controls where available; do not mistake written guidance for technical enforcement.

### 7. Load context progressively and by relevance
Correct work requires reliable access to relevant context, not universal loading of all documentation.
- Use the current entrypoint to route by requested outcome, affected owner, and actual boundary.
- Follow direct routes to relevant specialist sources; do not load unrelated branches of documentation.
- Keep local creation task-scoped and maintenance context limited to the affected area, its ownership, and its cross-document effects.

### 8. Separate requirements from explanation
Mandatory constraints must remain distinguishable from recommendations, rationale, and examples.
- Give each mandatory rule one identifiable authoritative home.
- Use instructions for requirements and boundaries; use guides for procedures, examples, and explanation.
- Link to authoritative rules instead of creating competing copies or silently turning preferences into requirements.

### 9. Make documents and capabilities understandable at their point of use
A component should be usable without undocumented assumptions or unrelated repository history.
- State a document's purpose, audience, applicability, and useful next reference.
- Give capabilities clear purposes, interfaces, inputs, outputs, defaults, dependencies, limitations, and failure behavior.
- Make assumptions and external dependencies visible rather than relying on hidden runtime or file context.

### 10. Preserve document authority and lifecycle
Documents with different purposes and lifecycles must remain distinguishable even when some content overlaps.
- Distinguish an operational source, a historical or protected copy, a generated composite, and a navigation document; they are not interchangeable.
- Treat the designated main source as the operational copy. A historical copy preserves a state or protected record and must not silently become a competing source of current instructions.
- When an externally located document also needs a protected core record, preserve a clearly identified historical copy in core and link from that copy to the main source path. Do not create a reverse dependency from the main source to its core historical copy.
- Keep generation and routing artifacts derived from their inputs; do not edit generated composites as if they were source documents. DP C defines the precise locations and maintenance process.

### 11. Allow necessary repetition for independent usability
Conciseness should reduce total context and maintenance cost, not make every document depend on a large set of other documents.
- Repeat a short explanation when an independently used procedure needs it to be understood and applied correctly.
- Keep repeated explanations specific to the local task and its consequences.
- Do not duplicate mandatory authority, create competing rules, or replicate boilerplate across every entrypoint. Prefer a canonical requirement plus concise local explanation.

### 12. Reduce total operational effort
The workspace should make recurring work less expensive in context, tokens, manual effort, execution, verification, and future maintenance.
- Prefer reliable, deterministic automation for repetitive mechanical operations when its total lifecycle cost is justified.
- Evaluate savings across context loaded, model/tool calls, manual steps, execution time, errors prevented, verification effort, and maintenance burden; token count alone is not a sufficient measure.
- Keep judgment-intensive decisions with the responsible human or AI. Automation should remove mechanical effort, not silently assume authority or make unreviewed architectural decisions.

### 13. Compose and extend before duplicating
Grow capability by improving and combining useful components rather than accumulating near-identical alternatives.
- Extend an existing capability when its purpose and interface can accommodate the need cleanly.
- Create a distinct capability or document when purpose, audience, interface, ownership, or lifecycle genuinely differs.
- Keep shared behavior and mandatory rules canonical; avoid duplicate implementations and competing authoritative records.

### 14. Preserve compatibility deliberately
Shared interfaces are contracts with consumers, not isolated implementation details.
- Identify affected callers, workflows, catalog entries, tests, and documents before changing a shared contract.
- Prefer compatible extensions when practical.
- When a breaking change is justified, account for consumer impact, migration, and verification.

### 15. Let structure earn its complexity
The repository should use the smallest coherent organization that solves demonstrated needs.
- Add directories, registries, schemas, abstractions, and routing layers only when their practical benefit exceeds their ongoing cost.
- Keep related responsibilities together unless distinct ownership, purpose, authority, or lifecycle justifies separation.
- Promote patterns and infrastructure based on demonstrated use, not hypothetical completeness.

### 16. Keep local creation practical
A useful contribution should be possible without first solving repository-wide organization.
- Choose the nearest sensible owner and keep the result focused and locally understandable.
- Working may use locally appropriate formats, explanations, and direct references without waiting for global normalization.
- Leave broad cleanup, deduplication, naming alignment, and navigation redesign to Maintenance unless they directly block the task.

### 17. Keep automation reusable, thin, and least-privileged
Automation should expose capability without duplicating its implementation or acquiring unnecessary authority.
- Keep reusable logic in maintainable capability implementations; use workflows as thin integration or execution surfaces.
- Grant automation only the permissions and dependencies required for its defined purpose.
- Keep credentials and sensitive information out of source, inputs, logs, and generated artifacts.

### 18. Maintain one canonical capability-discovery model
Capabilities should have a consistent, authoritative discovery identity.
- Use one canonical catalog or discovery model when adopted by the repository.
- Keep catalog metadata, supported entrypoints, implementation, documentation, and tests consistent.
- Treat filenames and search results as locators, not proof that a capability is registered, complete, or supported.

### 19. Verify important behavior proportionately
Correctness should be checked at the boundaries that matter, without imposing needless universal overhead.
- Give shared behavior testable contracts, including relevant invalid and edge cases.
- Scale verification to behavior, risk, and affected consumers; Working does not need a repository-wide audit for a local change.
- Describe capability status honestly; do not claim tests, controls, or support that have not been checked.

### 20. Distinguish policy, authorization, and enforcement
These concepts are related but not interchangeable.
- Policy describes intended behavior; authorization determines who may act; enforcement technically prevents disallowed actions.
- Use GitHub rulesets, branch protection, permissions, required checks, and appropriate execution controls for enforceable restrictions.
- Never imply that repository instructions or container settings restrict an already-authorized connector unless the relevant system actually enforces that boundary.

### 21. Preserve user material and recoverability
User material, source references, working changes, repository history, and known-good states are assets.
- Age, inactivity, or absence from a quick search is not sufficient reason for deletion.
- Scope destructive cleanup explicitly and preserve a suitable, verified recovery path.
- Keep recovery records and authority independent from routine maintenance; maintenance may request recovery but must not silently invalidate it.

### 22. Keep observability truthful and proportionate
Evidence can support improvement when it is useful, authorized, and technically available.
- Prefer structured, durable event records over repeated narrative reporting when a supported mechanism exists.
- Separate raw collection, derived analytics, and persistent improvement suggestions.
- Use the suggestions area to record observed deterministic tasks that may be worth automating; a suggestion is not an instruction to build a tool.
- Collect only what has a defined purpose and appropriate access and retention boundaries; never claim proposed telemetry is implemented.

### 23. Protect the stable workspace through deliberate promotion
The stable line should represent a coherent, verified workspace rather than ordinary task development.
- Keep stable, task-development, and historical-preservation branch roles distinct, following current repository controls and naming conventions.
- Promote broad or shared changes only through explicit authorization, applicable verification, and repository protection controls.
- Treat archive branches and recovery snapshots as preservation resources, not routine working branches.

## Architectural responsibility domains

These domains describe responsibilities, not a mandatory one-to-one directory structure. Create or split directories only when ownership and lifecycle justify them.

| Domain | Responsibility | Boundary |
| --- | --- | --- |
| Workspace Core | Identity, durable principles, architecture, configuration, authority, shared contracts | Protected from ordinary feature work and routine maintenance |
| Working Environment | New features, local tools, task-scoped documents, implementation, proportionate checks | Optimizes local progress; does not own repository-wide organization |
| Maintenance Environment | Canonical ownership, alignment, consolidation, placement, navigation, long-term coherence | Main organizing force; does not inherit core or recovery authority |
| Capability System | Reusable tools, scripts, workflows, integrations, tests, discovery metadata | Implements capability; does not redefine core policy |
| Workspace Access & Operations | ChatGPT/Codex interaction with the repository through the GitHub connector | Limited to actual connector capabilities; not an independent agent runtime |
| Recovery System | Preservation, snapshots, history, rollback, restoration | Independent from routine cleanup and maintenance |
| Observability | Authorized evidence, analytics, and reviewable suggestions | Proportionate; does not itself authorize changes |

## Core decision tests

| Question | Decision criterion |
| --- | --- |
| Is this a new feature or ordinary task change? | Route to the nearest owning component and its locally relevant guidance. |
| Is the requested outcome organizational coherence? | Route to Maintenance and select the lowest sufficient maintenance scope. |
| Should Working perform repository-wide cleanup because it noticed an issue? | No. Address blockers; record or route non-blocking friction to Maintenance. |
| Is Maintenance an approval gate for ordinary creation? | No. It organizes accumulated work and does not pre-approve every local contribution. |
| Does either environment have looser security or authority boundaries? | No. Shared core, security, compatibility, preservation, and authorization boundaries apply in both. |
| Does this belong in core? | Only when it establishes durable repository-wide identity, policy, architecture, authority, or a shared contract. |
| Must every task load all guidance? | No. Load the current entrypoint and the relevant mode/task sources. |
| Should a new tool, abstraction, or schema be created? | Prefer composition; create it for a distinct, demonstrated need. Record observed deterministic automation opportunities for later evaluation rather than expanding an unrelated task. |
| Should a shared interface change? | Identify consumers and account for compatibility, migration, and verification. |
| Should old material be deleted? | Not solely because it is old, inactive, or absent from a quick search. |
| Can instructions enforce security? | No. Actual enforcement belongs to the relevant permission or execution layer. |
| How should work reach the stable branch? | Through the explicitly authorized promotion process and applicable controls. |

## Relationship to DP C

DP C is the operational companion to this document. It implements the principles through task routes, local ownership, maintenance guidance, and specialist procedures. Load only the route and procedure relevant to the actual task; DP is not a universal task checklist.

## Overall principle

Working should make useful creation easy and locally practical. Maintenance should be the main organizing force that turns accumulated contributions into a coherent and discoverable workspace. Both operate within the same durable authority, security, compatibility, and preservation boundaries.