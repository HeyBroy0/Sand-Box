Sand-Box — Design Principles & Core Decision Rules
Purpose: Keep the development of Sand-Box aligned with its intended role as a focused, evolving workspace for ChatGPT/Codex repository work through the GitHub connector. These principles describe what the workspace should remain and become; they are not operating procedures. Task-specific procedures belong in the relevant instructions, guides, scripts, and workflows.

Scope and design boundary
Sand-Box is an evolving toolbox and repository workspace intended to help ChatGPT/Codex complete tasks and extend its capabilities through reusable, repository-managed tools and workflows.
The supported environment in scope is ChatGPT/Codex working with GitHub through the connected repository/connector environment. Sand-Box is not a general-purpose AI-agent platform, agent orchestration framework, or independent agent runtime project. Its design must not assume that repository instructions or container settings control the permissions or isolation of the already-authorized ChatGPT/GitHub connector.
The principles below are grouped by origin so that the original design intent, additions from the cross-branch consolidation, and new proposals remain distinguishable.

1. Keep Sand-Box focused on the ChatGPT/Codex GitHub workspace
Sand-Box should evolve into a more capable, reusable workspace for ChatGPT/Codex repository work without expanding into a general agent platform.
- Prioritize capabilities that improve real repository tasks in the connected GitHub environment.
- Let recurring needs justify new tools and workspace capabilities; avoid building for unrelated agent runtimes or orchestration systems.
- Treat connector access, repository-owned automation, and any execution environment as distinct parts of the system.

2. Keep the always-read layer small and durable
The repository entrypoints should communicate the workspace's identity, essential constraints, and navigation without becoming encyclopedias.
- Keep the root `README.md` concise and focused on purpose, routing, and repository-wide essentials; do not make it an encyclopedia.
- Keep durable cross-repository principles and contracts in the core; place task-specific detail elsewhere.
- Expand the always-read layer only when a rule genuinely applies across the workspace.

3. Protect the core as the workspace's policy and contract layer
The core should contain only the durable rules, architecture, identity, configuration, and shared contracts whose change could alter the workspace as a whole.
- Core changes require explicit authorization and the applicable core-change or improvement governance; merely having repository access is not authorization.
- Ordinary capability work and routine maintenance should not change core policy or structure.
- Core protection must be reflected in both clear policy and enforceable repository controls where available.

4. Load context progressively and by relevance
The instruction architecture should provide enough context for correct work without making every task carry the entire repository's documentation.
- Separate the always-read entrypoints from task-specific instructions, specialist references, and examples.
- Keep each document focused on a distinct concern or task audience.
- Treat unnecessary context and duplicated guidance as maintenance costs, not as extra safety.

5. Separate requirements from explanation
Mandatory requirements and explanatory material should be distinguishable so that guidance does not accidentally become policy.
- Instructions define applicable requirements, constraints, and authority.
- Guides provide procedures, examples, rationale, and reference information.
- Keep each mandatory rule authoritative in one place and link to it rather than copying it across documents.

6. Make documentation actionable and capabilities self-contained
A capability should be understandable and usable from its own clearly stated contract, without relying on undocumented context.
- Documents should state their purpose, applicability, and relationship to the next relevant source.
- Tool and workflow interfaces should expose their purpose, inputs, outputs, dependencies, and limitations.
- Avoid hidden assumptions about unlisted files, undocumented runtime behavior, or context that a connected ChatGPT/Codex session may not have.

7. Prefer composition and extension over duplication
The workspace should gain capability by composing and improving useful parts rather than accumulating near-identical tools, instructions, and contracts.
- Extend an existing capability when its purpose and interface can accommodate the behavior cleanly.
- Create a separate capability when it has a genuinely distinct purpose, interface, or maintenance boundary.
- Keep one authoritative definition for shared behavior and avoid duplicate records for alternate entrypoints of the same capability.

8. Preserve compatibility deliberately
Shared interfaces should evolve predictably because multiple tools, workflows, and documents may depend on them.
- Treat callers, workflows, catalog entries, tests, and documentation as consumers of shared contracts.
- Prefer compatible extensions over unnecessary breaking changes.
- When a breaking change is justified, its migration path and affected consumers are part of the change, not later cleanup.

9. Avoid speculative infrastructure
Architecture should be driven by demonstrated, recurring needs rather than hypothetical future complexity.
- Do not add frameworks, registries, schemas, abstractions, or instruction layers without a concrete use case.
- Prefer the simplest design that solves the real problem and leaves a clear path for later extension.
- Do not turn a possible future directory or subsystem into a required architectural layer prematurely.

10. Prefer the smallest coherent structure
The repository's organization should make responsibilities clear while keeping related concerns together when separation would add more overhead than value.
- Split a document when its parts have distinct purposes or audiences and can be maintained or loaded independently.
- Create directories and subsystem boundaries only when they represent real ownership or lifecycle differences.
- Prefer a small number of clear navigation routes over elaborate documentation hierarchies.

11. Design for low-friction task completion within authority
The workspace should help ChatGPT/Codex complete sufficiently specified repository tasks with minimal avoidable interaction, while never treating convenience as permission to exceed the task's authority.
- Favor reusable capabilities, explicit interfaces, sensible defaults, and clear failure signals.
- Support safe diagnosis and alternative approaches when an initial method fails.
- Do not let automation, autonomy, or convenience bypass authorization, core protection, or explicit destructive-action boundaries.

12. Preserve recoverability as a permanent workspace property
The ability to restore a known-good state should be designed into the workspace rather than treated as an afterthought of maintenance.
- Preserve archive branches, known-good snapshots, version history, and rollback information according to explicit retention policy.
- Keep recovery authority and recovery records independent from routine maintenance authority.
- A maintenance or improvement process may request recovery, but must not silently erase or invalidate the recovery options it may need.

B. Additional principles incorporated from the consolidated core-principles file
These principles were present in the cross-branch core material but were not fully represented in the original DP. They are included because they directly support Sand-Box's intended long-term design.
1. Give capabilities small, explicit, and predictable interfaces
A reusable capability should be easy to discover, invoke, validate, and connect to other repository functions.
- Define clear inputs, outputs, defaults, limitations, and failure behavior.
- Validate assumptions at the boundary, including paths, file types, sizes, and user-supplied options.
- Prefer deterministic and machine-readable outputs where downstream tools or workflows depend on them; make destructive or networked behavior explicit.
2. Maintain one canonical capability-discovery model
The workspace should have one authoritative way to describe capabilities and their supported entrypoints.
- Group related scripts and workflows under one capability identity in the catalog.
- Keep catalog metadata, discovery behavior, workflow interfaces, documentation, and tests consistent as one connected contract.
- Do not treat a filename or a search result as proof that a capability is registered, complete, or supported.
3. Keep automation reusable, thin, and least-privileged
Automation should expose capabilities without duplicating their core logic or introducing unnecessary authority.
- Keep reusable behavior in maintainable capability implementations and use workflows as thin integration or execution surfaces.
- Grant automation only the permissions and dependencies required for its defined purpose.
- Keep credentials and sensitive information out of source, inputs, logs, and artifacts.
4. Make important behavior verifiable
Workspace capabilities and shared contracts should be designed so that correctness and regressions can be checked rather than inferred.
- Give shared behavior testable boundaries, including normal, invalid, and edge-case behavior.
- Keep verification expectations aligned with the actual contract and the parts of the repository that consume it.
- Make the state of important capabilities understandable, distinguishing stable, experimental, and deprecated behavior when that distinction is useful.
5. Preserve user material and repository history by default
Repository data, source material, review outputs, and rollback history should be treated as assets rather than disposable clutter.
- Age, lack of recent references, or apparent inactivity alone should not make material eligible for deletion.
- Destructive cleanup should have explicit scope and preserve an appropriate recovery path.
- Protect mainline, archive, backup, and in-progress work from routine housekeeping.
6. Favor durable, machine-observable handoff over duplicated narrative
The workspace should make meaningful state and results discoverable without requiring each capability to invent its own reporting format.
- Prefer structured, durable records for events and results when an authorized mechanism exists.
- Keep capability purpose, interfaces, dependencies, limitations, and verification status understandable to maintainers.
- Do not create mandatory progress-reporting overhead when it adds no durable information.

C. New proposed principles to close remaining design gaps
These are new design proposals synthesized from the stated goal and the gaps identified in the DP. They should be treated as proposed principles, not as claims that the corresponding infrastructure already exists.
1. Design to the real connector boundary
The workspace should be designed around the capabilities and permissions actually available to ChatGPT/Codex through the connected GitHub environment.
- Distinguish repository read/write access from the ability to execute code, access a local filesystem, or reach an external service.
- Do not promise or depend on connector operations that are unavailable or not authorized.
- Where a task needs execution or a privileged action, make the supported repository-owned mechanism and its permission boundary explicit.
2. Treat policy, authorization, and enforcement as different things
A documented rule expresses intended behavior; authorization determines who may act; technical controls prevent actions that should not occur.
- Use GitHub rulesets, branch protection, repository permissions, and required checks for repository invariants; use ephemeral, least-privileged execution for Sand-Box-owned automation where available.
- Keep instruction documents as guidance and routing, not as a substitute for technical access controls.
- Do not claim that the ChatGPT/GitHub connector or a separate execution environment is restricted unless that restriction is actually enforced at that layer.
3. Separate operational authority by responsibility
Read access, development, routine maintenance, improvement, promotion, and recovery should not silently inherit one another's authority.
- Keep ordinary maintenance distinct from changes that alter core policy, architecture, or shared contracts.
- Require explicit authority for core changes and promotion into the stable workspace.
- Keep recovery authority capable of preserving or restoring known-good states independently of routine maintenance.
4. Make observability automatic, structured, and proportionate
Observability should help the workspace improve through reliable evidence, without depending on manual self-reporting or collecting unnecessary information.
- Where technically supported and authorized, prefer automatic event capture over asking ChatGPT/Codex to narrate its own activity.
- Separate raw telemetry, derived analytics, and persistent improvement suggestions.
- Collect only information needed for maintenance and improvement; protect sensitive content and define access and retention boundaries.
5. Keep the workspace's major domains distinct
The architecture should separate responsibilities that have different purposes, authority, or lifecycles while allowing them to interact through explicit contracts.
- Workspace Core owns identity, durable rules, architecture, configuration, and shared contracts; the Capability System owns reusable tools, scripts, workflows, integrations, and discovery metadata.
- Workspace Access & Operations describes the ChatGPT/Codex GitHub connector surface and repository interaction model—not a separate agent runtime.
- Observability & Maintenance owns usage evidence and improvement processes; Recovery owns preservation and restoration independently.
6. Protect the stable workspace through explicit promotion
The stable branch should represent a coherent, verified workspace rather than an unrestricted working area.
- Keep `main` as the stable line and use isolated task branches (currently `work/<short-task>`) for development.
- Treat `archive/* branches and designated recovery snapshots as historical fallbacks, not routine working branches.
- Update `main` only through the explicitly authorized Improvement process and the repository's applicable protection and verification controls.

D. Core decision rules
These rules translate the principles into stable architectural choices. They are decision criteria, not step-by-step operating procedures.
Decision. Default rule
Is a proposal within Sand-Box's scope? It should directly improve the ChatGPT/Codex GitHub-connected repository workspace or one of its defined capability, operations, observability, maintenance, or recovery domains. General agent runtimes and agent orchestration are out of scope.
Does something belong in `core/`? Only when it defines durable repository-wide identity, architecture, policy, or a contract relied on across capabilities. Importance or file location alone is insufficient.
May an ordinary task change core? No. Core changes require explicit task authorization and the applicable improvement/core-change governance; routine maintenance and ordinary capability work remain outside core.
Should every task load the core instructions? No. Context should be proportional to the task; core material is relevant when a core surface or its governing contract is being changed.
Should a document or directory be split? Only when the resulting parts have distinct responsibilities or audiences and can be independently understood, maintained, or loaded.
Should a new tool, abstraction, or schema be created? Prefer extending a suitable existing capability. Create something new only for a distinct, recurring need that cannot be served cleanly by composition.
Should a shared interface change? Only when the benefit justifies the compatibility cost; preserve consumers where practical and make necessary migration behavior part of the same change.
Where should reusable behavior live? In the capability implementation; workflows and connector-facing surfaces should expose or orchestrate that behavior without duplicating it. The catalog remains the canonical capability index.
Can instructions be treated as security enforcement? No. Instructions communicate policy; actual restrictions must come from the relevant connector permissions, GitHub controls, or execution boundary.
Can connector permissions be assumed to be sandboxed by repository code? No. Treat connector authorization and any separate execution environment as distinct security boundaries.
Should telemetry be collected? Only when it has a defined maintenance or improvement purpose, can be collected through an authorized mechanism, and has proportionate data, access, and retention boundaries.
Can routine maintenance remove old data or recovery material? No, not merely because it is old or appears unused. Destructive removal requires explicit scope and must respect preservation and recovery policy.
Should maintenance control recovery points? No. Maintenance may request recovery actions, but the recovery system must retain independent preservation authority.
How should work reach `main`? Through the explicitly authorized Improvement process from an isolated task branch, with applicable verification and repository protection; `main` is not the routine development workspace.
---

E. Architectural domains
The following domains describe responsibility boundaries. They do not require a one-to-one directory structure; directory creation remains subject to the smallest-coherent-structure principle.
Domain. Responsibility. Boundary
01 — Workspace Core. Identity, durable principles, architecture, configuration, authority, and shared compatibility contracts. Protected from ordinary capability work and routine maintenance.
02 — Capability System. Reusable tools, scripts, workflows, integrations, tests, and the canonical capability catalog. Capabilities remain modular and discoverable; they do not redefine core policy.
03 — Workspace Access & Operations. ChatGPT/Codex interaction with the repository through the GitHub connector; repository discovery, file and branch operations, and connector-facing workflows. Limited to the actual connected GitHub environment; excludes general agent runtimes and assumptions about independent process isolation.
04 — Observability & Maintenance. Authorized telemetry, structured events, analytics, suggestions, routine maintenance, and improvement proposals. Routine maintenance cannot silently change core or destroy recovery points.
05 — Recovery System. Archive branches, known-good snapshots, version history, rollback policy, and recovery verification. Independent from routine maintenance; preservation material is not ordinary cleanup inventory.

Branch roles
Branch class Design role Governing principle
`main`. Stable, consolidated workspace. Updated only through the explicitly authorized Improvement process, not routine maintenance or direct development.
`work/<short-task>`. Isolated task development, following the repository's current branch convention. Work remains scoped and reviewable before promotion.
`archive/*`. Historical fallback and preservation.Not routinely modified or deleted; governed by recovery and retention policy.
---

Sand-box Design principles
1. An evolving tool-box and workspace that grows with use, for AI A-sync use to complete tasks or create its own missing tools.
2. Small always-read layer.	Keep README.md focused on entrypoints, routing, and essential repository-wide guidance.
3. Core protection scheme. `core/` is a protected folder for repository-wide rules and shared contracts that need special access before writing to. 
4. Progressive and relevant documents loading. Write concise and specific documents relevant to the task; Do not create large documentation, use navigation to separate notes. 
5. Separate requirements from explanation. Instructions establish mandatory rules; guides explain procedures, examples, and reference material.
6. Actionable documentation.	Every instruction document should explain when it applies, what it requires, and where to go next.
7. self-contained interfaces. Endpoint Documents and tools (different from routing) should be stand-alone not requiring outside information to understand.
8. Composition over duplication.	Prefer extending an existing capability when it can be done cleanly. Avoid duplicate tools, instructions, and contracts.
9. Deliberate compatibility.	Before changing a shared contract, identify its consumers and account for migration or compatibility.
10. Avoid speculative infrastructure. Do not introduce frameworks, registries, schemas, abstractions, or instruction layers without a concrete recurring need.
11. Smallest coherent structure	Split. documents or create directories only when the separation provides a real benefit to independent loading or maintenance.
12. asynchronous execution. Complete sufficiently specified tasks without unnecessary user interaction within the priveledge/authority. If an attempt fails, diagnose the failure and try an appropriate alternative when safe. Creating or modifying capabilities must remain within the task's authority. Core changes require the core-change procedure and explicit authorization.

## Core-specific decision rules
I would make these particularly prominent because they prevent architectural drift.
Question.	Preferred decision
Does this belong in core? Only if it establishes a cross-repository rule, structure, or contract.
Should a document be split? Only when the resulting parts have distinct purposes and can be loaded independently.
Should a new abstraction be created? Only when an actual recurring need justifies it.
Should an existing interface be changed? Only after identifying consumers and handling compatibility.
Should a core change expand into adjacent improvements? No, unless those improvements are necessary for a coherent change.
Should all instructions be loaded for safety? No. Load the required instructions and relevant dependencies.
Should every task require the core gate? No. Ordinary capability work should remain lightweight.
Core instructions only needed while changing and analyzing core features, not when doing unrelated tasks 
Preserve recoverability. Before structural or potentially destructive changes, identify a known-good recovery point and verify that it is usable.
Only during specific user instructions is core changes allowed or explicit permission to follow Maintenence/improvement.md, basic maintenence doesn't touch core

Proposed security boundaries
Layer 1 — GitHub rulesets Enforcement
Protect main, restrict deletion and force-pushing, and require successful checks for promotion.
Layer 2 — Isolated execution Enforcement
Use ephemeral execution environments for scripts, with restricted filesystem and network access.
Layer 3 — Permission boundaries Enforcement
Separate read, development, maintenance and promotion credentials.
Layer 4 — Repository instructions Guidance
Define intended behavior, architectural constraints and task routing.
Current ChatGPT connector's permissions are distinct from the permissions of a agent runtime. We should not assume containerization can restrict an already-authorized connector.

01 — Workspace Core
Foundational - The identity, rules, architecture, configuration and compatibility contracts of Sand-Box.
- README.md
- core/this-is-instruction-to-read-core-readme-before-proceeding/core-readme.md and its Core decision tree
- Design principles and core standards
- Shared configuration and identity contracts

02 — Capability System
Expandable - The actual functionality available to AI systems.
- tools/
- scripts/
- tools/catalog.json
- .github/workflows/
- Future integrations and capability interfaces

03 — Workspace Access & Operations
Interaction — How connected AI systems access and operate within Sand-Box.
This system defines the interface and operating procedures through which AI systems use the repository as a workspace.
Current scope is the ChatGPT GitHub Connector environment only. Do not assume that Sand-Box controls the AI runtime or provides independent process isolation.
- Repository access and connector capabilities
- File discovery and instruction navigation
- Branch, commit, and change workflows
- Capability invocation and integration procedures
- Operation permissions and authorization boundaries
- Verification and reporting requirements
- Connector limitations and unavailable operations
AI agents are not the same as ChatGPT GitHub Connected. AI agents are a different project.

04 — Observability / Maintenance
Intelligence - The ability to understand how the workspace is used and improve it over time.
- Telemetry collection
- Structured event storage
- Usage analytics
- Dependency analysis
- Navigation analysis
- Suggestions
- Maintenance procedures
- Cleanup and verification
Telemetry automation: AIs should not track their footsteps itself. Instead an automatic system should detect when AI systems use tools, navigate and make changes. Stored in a useful format, not just text that must be interpreted if possible. 
I would distinguish raw telemetry, analytical outputs and persistent suggestions rather than placing everything indiscriminately in reports/.

05 — Recovery System
Preservation - The ability to recover from unsuccessful changes and preserve workspace history.
- Archive branches
- Known-good snapshots
- Version history
- Rollback procedures
- Recovery verification
- Preservation policies
This should be independent of the maintenance system. Maintenance can request recovery, but it should not be able to silently destroy recovery points.

Branch	    Purpose	Handling
main	      Consolidated, stable workspace	Updated through Improvement-specific maintenance only
work/*	    Ongoing AI development	Agents can create, modify and commit
archive/*	  Historical fallback snapshots	Never routinely modified or deleted


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
