Sand-Box — Consolidated Design Principles

1. SCOPE
Purpose
- Sand-Box is an evolving toolbox and workspace for ChatGPT/Codex repository operations through GitHub.
- Its purpose is to help complete repository tasks and extend capabilities through reusable tools, scripts, and workflows.
- New capabilities should emerge from demonstrated, recurring needs.
Boundaries
- Focus on the connected GitHub workspace.
- Do not expand into a general-purpose AI-agent platform or orchestration framework.
- Distinguish GitHub connector capabilities from independent execution environments.
- Do not assume repository instructions control external runtime permissions or isolation.

2. CORE ARCHITECTURE
Purpose: Preserve the workspace's identity, foundational rules, and shared contracts.
- Keep the root README small, durable, and focused on navigation and essential guidance.
- Keep core dedicated to repository-wide principles, architecture, authority, configuration, and shared contracts.
- Protect core from ordinary capability development and routine maintenance.
- Load core instructions when changing or evaluating core surfaces, not for unrelated tasks.
- Maintain one authoritative source for each mandatory rule.
- Expand the core only when a genuinely cross-repository requirement justifies it.
Core components:
- Workspace identity and purpose.
- Core documentation router.
- Architectural principles and standards.
- Change authorization and governance.
- Shared configuration and compatibility contracts.

3. DOCUMENT WRITING
Purpose: Make instructions understandable, actionable, and maintainable.
- Instructions define mandatory requirements and restrictions.
- Guides explain procedures, examples, rationale, and references.
- Every instruction document must establish its purpose, applicability, requirements, and next navigation step.
- Documents should be concise and independently understandable.
- Separate documents only when their responsibilities or audiences differ.
- Use navigation to connect related documents rather than duplicating content.
- Keep mandatory rules authoritative in one location.
- Update references and navigation whenever document structures change.
When creating or changing instructions
1. Identify the intended audience and scope.
2. Identify existing authoritative instructions.
3. Check dependencies and potential conflicts.
4. Change the smallest relevant document set.
5. Verify links, routing, and consistency.

4. TOOL WRITING
Purpose: Expand functionality without creating unnecessary complexity.
- Prefer extending an existing capability over creating a duplicate.
- Create a new tool only for a distinct requirement.
- Keep reusable implementation logic in the capability itself.
- Define explicit inputs, outputs, defaults, dependencies, limitations, and failure behavior.
- Validate user inputs and operational assumptions at boundaries.
- Prefer predictable, deterministic, machine-readable outputs.
- Make destructive and network-dependent operations explicit.
- Keep workflows thin: they should expose or orchestrate capabilities rather than duplicate their implementation.
- Test normal, invalid, and edge-case behavior.
Capability registration
Maintain one canonical capability catalog. Catalog entries, documentation, workflow interfaces, implementations, and tests must describe the same capability consistently.

5. NAVIGATION
Purpose: Ensure tasks reach the correct instructions and capabilities without unnecessary context.
- The root README is the initial entrypoint.
- The core documentation router directs core-related changes.
- Task-specific instructions are loaded only when relevant.
- Tool discovery uses the canonical catalog.
- Search is a locator, not proof of a complete repository inventory.
- Follow explicit navigation routes rather than inventing instruction layers.
- Recheck references after reorganizing documents or directories.
Navigation principle: Load the minimum sufficient context, not the maximum available context.

6. PROTECTIONS, ACCESS AND AUTHORITY
Purpose: Separate intended behavior, permission, and actual enforcement.
These are three distinct concepts:
- Policy: What should or should not happen.
- Authorization: Who is permitted to act.
- Enforcement: What technically prevents unauthorized actions.
Protection principles
- Repository instructions communicate policy; they are not security enforcement.
- Use GitHub rulesets, branch protection, permissions, and required checks for enforceable restrictions.
- Use least-privileged permissions for automation.
- Separate connector permissions from execution-environment permissions.
- Never assume a container restricts an already-authorized GitHub connector.
Authority boundaries
Distinguish:
- Read access.
- Development.
- Routine maintenance.
- Improvement and core changes.
- Promotion into the stable workspace.
- Recovery and restoration.
Core modifications require explicit authorization and the applicable core-change procedure. Repository access alone does not grant permission to change core policy.

7. ARCHITECTURE
Purpose: Keep responsibilities distinct without creating unnecessary subsystems.
The architecture has five major domains:
Workspace Core
Identity, rules, architecture, configuration, authority.
Capability System
Tools, scripts, workflows, integrations, catalog, tests.
Workspace Access and Operations
GitHub connector interaction and repository operations.
Observability and Maintenance
Telemetry, analytics, maintenance, improvement.
Recovery System
Preservation, snapshots, history, restoration.
Design principles
- Prefer the smallest coherent structure.
- Separate responsibilities according to ownership, purpose, authority, and lifecycle.
- Use explicit interfaces between components.
- Avoid speculative frameworks, abstractions, schemas, and directory structures.
- Keep architecture extensible without making future possibilities mandatory today.
- Treat shared interfaces as contracts with identifiable consumers.

8. RECOVERY
Purpose: Preserve the ability to return to a known-good state.
- Recovery is a permanent architectural responsibility.
- Preserve archive branches, snapshots, version history, and rollback information.
- Identify and verify recovery points before structural or potentially destructive changes.
- Define explicit retention and restoration policies.
- Protect historical and in-progress work from routine cleanup.
- Recovery authority must remain independent of routine maintenance.
- Maintenance may request recovery but must not silently invalidate recovery options.
Principle: Preservation comes before destructive cleanup.

9. MAINTENANCE
Purpose: Keep the workspace healthy without compromising its architecture.
Routine maintenance
- Inspect repository health.
- Validate existing tools and workflows.
- Check dependencies and documentation.
- Remove genuinely unnecessary material when authorized.
- Preserve core, user data, and recovery resources.
Improvement
- Evaluate architectural changes.
- Introduce or substantially change capabilities.
- Modify shared contracts.
- Propose and authorize core changes.
- Verify changes before promotion.
Rules
- Routine maintenance does not modify core.
- Do not delete files merely because they are old or apparently unused.
- Keep changes scoped.
- Validate affected consumers.
- Promote changes through the authorized process.

10. TELEMETRY
Purpose: Understand workspace usage and identify evidence-based improvements.
- Prefer automatic event collection over manual AI self-reporting.
- Capture relevant tool usage, navigation, and repository changes where technically supported and authorized.
- Use structured, machine-readable records.
- Separate three information layers:
Collection
Raw events and activity records.
Analytics
Usage patterns, dependencies, and navigation analysis.
Suggestions
Persistent improvement opportunities.
Protection requirements
- Collect only information with a defined purpose.
- Establish access and retention boundaries.
- Protect sensitive information.
- Avoid unnecessary logging and reporting overhead.
- Do not claim telemetry exists until the collection mechanism is implemented and verified.

11. WORKSPACE — TOOL USE
Purpose: Enable ChatGPT/Codex to operate effectively within the connected repository.
- Inspect the active target branch and repository state before making changes.
- Discover existing capabilities before creating new ones.
- Use the GitHub connector within its actual available permissions.
- Prefer reusable repository-managed tools over repeated manual procedures.
- Complete sufficiently specified tasks with minimal unnecessary interaction.
- Use sensible defaults and report meaningful failures.
- When an approach fails, diagnose the cause and consider a safe alternative.
- Validate completed work before reporting success.
- Preserve user data and existing repository history.
Operational boundaries
- Tool execution, GitHub access, and independent runtime execution are separate capabilities.
- Do not claim an operation succeeded without verification.
- Do not exceed the authority of the requested task.

12. BRANCH AND PROMOTION PRINCIPLES
These rules apply across the other sections.
main
Purpose: Stable workspace.
Governing principle: Authorized improvement and promotion only.
work/*
Purpose: Isolated development.
Governing principle: Scoped development and verification.
archive/*
Purpose: Historical preservation.
Governing principle: Not routinely modified or deleted.

Promotion into main requires:
1. Explicit authorization.
2. A coherent, scoped change.
3. Appropriate verification. Including explicit user authorization.
4. Applicable repository protection controls.
main is not the ordinary development workspace.

13. CONSOLIDATED DECISION RULES
Does this belong in Sand-Box? It must serve the defined GitHub workspace.
Does it belong in core? It must establish a durable cross-repository rule or contract.
Should core be loaded? Only when relevant to the task.
Should a document be split? Only for meaningful independent responsibilities.
Should a new tool be created? Only when an existing capability cannot serve the recurring need cleanly.
Should an interface change? Identify consumers and preserve compatibility where practical.
Should reusable logic live in workflows? No. Keep implementation logic in capabilities.
Should instructions enforce security? No. Use technical access controls.
Should old material be deleted? Not solely because of age or inactivity.
Should maintenance control recovery? No. Recovery must remain independently protected.
Should telemetry be collected? Only with an authorized purpose and proportionate retention.
Should work go directly into main? No. Follow the authorized promotion process.
Should the architecture anticipate every future need? No. Build for demonstrated requirements.

14. OVERALL ARCHITECTURAL PRINCIPLE
Sand-Box should remain a small, protected, extensible GitHub-connected workspace. Its core defines durable identity and contracts; its capabilities provide reusable functionality; its navigation loads only relevant instructions; its authority model controls changes; its maintenance improves the workspace; its telemetry informs improvements; and its independent recovery system preserves known-good states.
The most important distinction is between Core, Capabilities, Operations, Maintenance, and Recovery. Each has a different responsibility and must not silently inherit another's authority.

15. ORIGINAL DIRECTORY TREE — PRESERVED UNCHANGED

Sand-Box/
├── README.md
├── .github/
│    ├── workflows/
│    ├── CODEOWNERS
│    ...
├── core/
│   ├── this-is-instruction-to-read-core-readme-before-proceeding/
│   │   ├── core-readme.md
│   │   ├── architecture/
│   │   ├── procedures/
│   │   └── standards/
│   │       ├── change-gate.md
│   │       ├── principles.md
│   │       ...
│   └── authority/
│       ├── permission-model.md
│       ├── maintenance-authority.md
│       ├── recovery-authority.md
│       └── workspace.md
├── maintenance/
│   ├── minimal-maintenance/
│   │   ├── minimal.md
│   │   ...
│   └── improvement/
│       ├── improvement.md
│       ├── verification/
│       ...
├── recovery/
│   ├── policies/
│   ├── procedures/
│   └── manifests/
├── capabilities/
│   ├──capability-discovery.md
│   ├──  catalog.json
│   ├── tests/
│   ├── scripts/
│   ├── tools/
│   └── documentation-Tree/
│       ├── document-look.md
│       ├── document-creation.md
│       ...
├── observability/
│   ├── collection/
│   ├── analytics/
│   └── suggestions/
├── temp/
├── data/
└── reports/
