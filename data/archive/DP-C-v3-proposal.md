# DP C — Operating Guidance and Procedures

**Status:** Proposed consolidated revision for review. This document is a proposal, not an adopted authority document.

**Purpose:** Translate Sand-Box's design principles into practical working behavior. DP defines the workspace's durable principles and boundaries; DP C explains how to apply them during repository work. Repository-specific authority documents, technical contracts, and actual platform controls remain authoritative in their own domains.

**Design intent:** DP C should prevent misaligned behavior and promote good repository etiquette. It is not intended to enumerate every possible task, prescribe a workflow for every action, or make ordinary work carry a repository-wide maintenance burden.

## How to use DP C

1. Start with the root `README.md` and follow the route for the requested outcome.
2. Load only the numbered procedure or procedures that materially apply.
3. Apply sensitive-change, shared-contract, or recovery procedures whenever their triggers are present, even if the task began elsewhere.
4. Treat examples as common cases, not an exhaustive task catalog or allowlist.
5. Do not read the entire DP C for ordinary work. A full review is appropriate only when the task genuinely requires integrated review of the operating model.

The numbering is intended to remain stable if this document is later separated into independently stored procedures. For now, all procedures remain in this one document.

## Operating model

Sand-Box has two operating environments. These describe the outcome and responsibility of the work; they do not imply separate technical sandboxes, credentials, or permission systems.

### Working Environment

Working is the default for creating or editing features and completing ordinary task-scoped work. Its objective is to produce a useful, locally understandable result with minimal unnecessary organizational overhead.

Working may make reasonable local decisions about implementation, placement, format, and immediate supporting material. It should inspect the target and obvious dependencies rather than audit the whole repository. It may defer non-blocking normalization, deduplication, naming alignment, and broad navigation work to Maintenance.

Working remains subject to task scope, correctness, directly relevant instructions, security, shared contracts, explicit authorization, and preservation requirements.

### Maintenance Environment

Maintenance is the repository's main organizing force. It turns independently created contributions into a coherent, understandable, discoverable, and maintainable workspace.

Maintenance owns broad organization: canonical ownership, consolidation, sensible placement, terminology where consistency matters, navigation, cross-document coherence, and recurring organizational friction. It is not a gatekeeper for ordinary feature creation and should not impose its full process on every Working task.

### Select by requested outcome

| Requested outcome | Operating environment |
| --- | --- |
| Create or edit a feature, tool, script, workflow, test, or task-scoped document | Working |
| Correct a bounded local defect or cleanup issue | Maintenance — Minimal |
| Align related documents, ownership, terminology, or navigation | Maintenance — Alignment |
| Integrate a proven broader capability or make a justified architectural improvement | Maintenance — Improvement |
| Change protected core, authority, entrypoints, or shared contracts | Apply Procedure 01 and/or 02, regardless of environment |
| Preserve, restore, or perform potentially destructive work | Apply Procedure 03 as relevant |

Choose by the requested outcome, not by the AI's identity, the tool being used, or an incidental issue discovered along the way. A task may cross environments, but the transition should be deliberate. Complete the authorized task-scoped work and route separate, non-blocking organizational friction to Maintenance rather than silently expanding scope.

## Shared repository etiquette

These expectations apply across the procedures:

- **Start local, expand only when needed.** Inspect the target, its obvious owner, and immediate dependencies. Broaden discovery when an actual dependency, conflict, or shared contract requires it.
- **Use the nearest sensible owner.** Put a contribution where its purpose and responsibility fit. Do not create a new hierarchy merely to make a small contribution look complete.
- **Extend before duplicating.** Reuse or extend an existing component when its purpose and interface remain clear. Separate it when purpose, interface, ownership, audience, or lifecycle is genuinely distinct.
- **Keep local work usable.** Include the explanation, references, tests, or navigation needed at the point of use, but do not make every contribution a repository-wide integration project.
- **Keep one authoritative home for shared rules.** Link to canonical requirements rather than creating competing copies. Local explanation may clarify a rule without replacing its authority.
- **Do not normalize for appearance alone.** Different formats or local conventions are not automatically defects. Align them when inconsistency causes confusion, duplicated authority, broken reachability, or real maintenance cost.
- **Keep navigation as navigation.** A route should help a reader choose the next useful source; it should not reproduce the destination's instructions.
- **Verify proportionately and report truthfully.** Check the behavior, references, and consumers that the change actually affects. Never claim tests, permissions, controls, files, or infrastructure that have not been checked.

---

## Procedure 01 — Core, authority, and sensitive changes

**Applies when:** A task changes or evaluates repository identity, durable principles, core policy, authority, protected core material, or another surface whose effect is repository-wide.

**Typical destination:** `core/` for durable policy, authority, architecture, and shared contracts; follow the current core entrypoint for the exact owner.

### Procedure

1. **Confirm explicit authorization.** Verify that the task explicitly authorizes the sensitive change and that the applicable authority procedure permits it. Repository write access is not authorization.
2. **Read the governing sources.** Load the current root entrypoint, relevant core instructions, applicable authority documents, and the required change procedure. Do not load unrelated core material.
3. **Identify the boundary.** Determine whether the proposed change affects policy, identity, authority, security assumptions, shared contracts, or a protected document.
4. **Make the smallest coherent change.** Preserve existing meaning and compatibility where practical. Keep unrelated cleanup or redesign separate.
5. **Verify the affected boundary.** Check direct consumers and required controls. Do not claim that a written instruction technically prevents an action unless the relevant platform or execution layer actually enforces it.
6. **Stop when authority is unclear.** Do not modify the protected surface. Keep the proposed change separate from authoritative instructions and identify the missing decision or authorization.

### Boundaries

- Working allowances do not bypass this procedure.
- Maintenance responsibility does not bypass this procedure.
- Policy, authorization, connector permissions, and technical enforcement are different things.
- A proposed rule, directory, workflow, or control is not an implemented control merely because it is documented.

---

## Procedure 02 — Entrypoints and shared contracts

**Applies when:** Changing the root README, core entrypoints, task routers, navigation hubs, shared schemas, catalog contracts, public interfaces, or other routes and interfaces relied on by multiple parts of the repository.

**Typical destination:** Follow the current core and capability ownership structure. Entrypoints and shared contracts may have different owners; do not assume every such file belongs in one directory.

### Procedure

1. **Identify all direct consumers.** Determine which tasks, documents, capabilities, workflows, catalog entries, or users rely on the route or contract.
2. **Confirm the canonical owner.** Keep the shared definition in one authoritative location. Other documents should link to it or contain clearly identified snapshots where those are deliberately required.
3. **Preserve compatibility where practical.** Prefer compatible extensions. When a breaking change is justified, make the affected consumers, migration needs, and verification part of the same change.
4. **Keep entrypoints small.** The root README should be an always-read router for identity, essential workspace-wide boundaries, and task destinations—not a copy of every procedure.
5. **Use layered routing only when it helps.** A maintenance pre-hub may route to Minimal, Alignment, and Improvement Maintenance. A task-specific hub may route to specialist instructions. Do not add an extra layer unless it reduces the effort of finding the right source.
6. **Keep routes concise.** State the task trigger, destination, and useful scope. Avoid copying the destination's content into the hub.
7. **Verify reachability.** Check that new and changed destinations exist, links work, routes do not become circular, and the next step is clear.

### Document and procedure relationships

- The root README should route to the task guides and instructions needed for the requested outcome. It should not become an index of every historical or full reference document.
- A maintenance pre-hub should route Maintenance work to the appropriate maintenance scope rather than forcing the root README to explain each scope.
- When procedures are eventually stored separately, each main procedure should have one actively maintained canonical source in its owning location.
- A protected copy inside core, when genuinely needed, should be identified as a historical or controlled snapshot and link back to its canonical source path. It must not silently become a second independently maintained authority.
- If a full compilation is later generated from separated procedures, treat it as a generated reading copy, not a second source of truth. Do not manually edit the generated compilation.

These are architectural rules for keeping navigation and shared contracts coherent; they do not require splitting the current DP C document now.

---

## Procedure 03 — Recovery and preservation

**Applies when:** A change is destructive, structurally significant, difficult to reverse, or involves restoration, archival material, user material, source history, or a known-good state.

**Typical destination:** `recovery/policies/` and `recovery/procedures/`; use the current recovery structure and authority.

### Before a risky change

1. Identify the material, paths, history, and consumers that may be affected.
2. Check the applicable retention and recovery policy.
3. Identify a suitable known-good recovery point and verify that it is usable when the risk warrants it.
4. Define the exact scope of the change and what must remain preserved.
5. Narrow or stop the operation when authority or a usable recovery path is unclear.

### Preservation rules

- Treat user material, source references, in-progress work, branches, archives, snapshots, and version history as assets.
- Age, apparent inactivity, or absence from a quick search is not sufficient reason for deletion.
- Do not delete original source material merely because a consolidated copy exists; follow explicit retention and recovery policy.
- Keep recovery authority and records independent from routine maintenance.
- Maintenance may request or perform an authorized recovery action, but it must not silently invalidate the recovery options the repository depends on.
- Do not claim that a backup, archive, snapshot, or recovery mechanism exists unless it has been verified.

---

## Procedure 04 — Maintenance

**Applies when:** The requested outcome is to clean, align, consolidate, reorganize, or improve repository coherence beyond the immediate needs of one local contribution.

**Typical destination:** Use the maintenance pre-hub and the current guides under `maintenance/`.

### Maintenance responsibility

Maintenance is the main organizing force of the repository. It gradually turns local contributions into a coherent whole by clarifying ownership, consolidating genuine duplication, improving placement, aligning terminology where useful, repairing navigation, and reducing recurring organizational friction.

Maintenance is not an approval gate for ordinary creation. Working contributions do not need to be globally normalized before they can be useful.

### Select the lowest sufficient scope

The scopes are alternatives, not mandatory sequential stages. A larger scope requires a concrete reason.

**Minimal Maintenance — bounded correction**

Use for a specific local defect, broken reference, small inconsistency, or clearly unnecessary local clutter that can be corrected without reorganizing the wider area.

Avoid unrelated consolidation, navigation redesign, speculative architecture, and deletion of uncertain or historical material.

**Alignment Maintenance — coherence across related material**

Use when documents overlap, ownership is unclear, instructions conflict or are difficult to follow, terminology causes confusion, or navigation is stale, redundant, or hard to use.

Alignment may clarify canonical ownership, consolidate genuinely overlapping material, improve placement, repair routes, and create or restructure a hub when that materially improves reachability.

Avoid turning alignment into major capability development, speculative infrastructure, or broad architectural redesign not required by the alignment problem.

**Improvement Maintenance — broader proven change**

Use when the problem requires a broader capability, cross-component integration, shared-interface change, or architectural improvement supported by actual use, recurring demand, a successful trial, or a concrete need.

Improvement is not a license for speculative expansion and does not itself grant authority to change protected surfaces or promote changes.

### Bounded maintenance method

1. Name the concrete friction and the area it affects.
2. Choose the lowest sufficient scope; do not expand just because related issues exist.
3. Inspect the affected sources, their ownership, routes, and immediate dependencies.
4. Identify authoritative sources and preserve meaningful differences in scope, authority, and behavior.
5. Make the smallest change that improves correctness, usability, reachability, or ongoing maintenance.
6. Check that ordinary Working tasks can still load only the context they need.
7. Verify the changed references and affected consumers; preserve recovery options when relevant.
8. Keep unresolved policy or architecture decisions explicit rather than silently deciding them during cleanup.

This is a flexible method, not a mandatory checklist for every small correction.

### Working-to-Maintenance handoff

When Working discovers non-blocking organizational friction, it should complete its authorized task, preserve enough context to explain the issue, and route it through an existing maintenance channel when one exists. If no tracker or handoff mechanism exists, report the issue at task completion rather than inventing a tracking system for one observation. A handoff is not an automatic commitment to perform the work.

---

## Procedure 05 — Editing a feature

**Applies when:** Changing, repairing, extending, or refactoring an existing feature or capability while keeping the task focused on that feature.

### Procedure

1. **Understand the requested behavior.** Identify what should change, what must remain unchanged, and the feature's current expected behavior.
2. **Inspect the local implementation.** Read the target files, the nearest relevant documentation, and the immediate callers or dependencies. Expand the search when a shared interface or cross-component effect is likely.
3. **Respect the existing contract.** Identify inputs, outputs, defaults, errors, dependencies, and consumers before changing behavior. Do not silently introduce a breaking interface change.
4. **Make a focused change.** Prefer the smallest coherent modification. Keep unrelated cleanup, style normalization, and repository-wide redesign out of the task.
5. **Verify relevant behavior.** Check the changed path and directly affected cases, including important invalid or edge cases where appropriate. Run broader checks when the risk or affected surface warrants them.
6. **Update immediate supporting material.** Correct documentation or tests that are now inaccurate. Do not update every repository index unless the shared route or catalog contract changed.
7. **Report accurately.** State what changed, what was checked, and any known limitation or deferred maintenance issue.

Use Procedure 01 or 02 as well if the edit crosses protected core or a shared contract. Use Procedure 03 when the change is difficult to reverse or may destroy material.

---

## Procedure 06 — Creating a feature

**Applies when:** Creating a new feature, reusable tool, script, workflow, test capability, integration, or other new component.

### Procedure

1. **Confirm the intended outcome and owner.** Identify the user-facing result and place the work in the nearest sensible existing area.
2. **Check for an obvious existing fit.** Inspect the closest relevant capability and its interface. Keep discovery proportionate; a small feature does not require an exhaustive architecture audit.
3. **Choose extension or separation.** Extend an existing component when purpose and interface remain clear. Create a separate component when purpose, interface, owner, or lifecycle is genuinely distinct.
4. **Define a usable contract.** State purpose, inputs, outputs, defaults, dependencies, limitations, and meaningful failure behavior at a level appropriate to the feature.
5. **Validate important boundaries.** Check paths, file types, user-supplied values, external dependencies, and privilege-sensitive assumptions where relevant.
6. **Keep implementation reusable.** Put shared logic in its maintainable implementation. Keep workflows and connector-facing surfaces thin; do not duplicate the same behavior across entrypoints.
7. **Respect least privilege.** Use only permissions and dependencies needed for the defined purpose. Keep credentials and sensitive information out of source, inputs, logs, and artifacts.
8. **Add immediate documentation and proportionate verification.** Make the feature usable and check normal behavior plus important invalid or edge cases.
9. **Keep discovery consistent where a catalog applies.** Align its entry with the real implementation, supported entrypoints, documentation, and tests. A filename or search result alone does not prove a capability is registered or supported.

### Avoid

- Building a general framework, registry, abstraction, or new directory system for a one-off need without demonstrated recurring value.
- Creating a near-duplicate because the existing capability was not inspected.
- Turning a local feature into a repository-wide cleanup or integration project.
- Claiming unavailable connector, runtime, network, or filesystem capabilities.

Maintenance may later align naming, placement, catalogs, tests, and documentation across components when actual use demonstrates a coherence problem.

---

## Procedure 07 — Creating or changing text and documentation

**Applies when:** Creating, editing, restructuring, or consolidating instructions, guides, references, procedural documents, or other repository text.

**Typical destination:** Shared documentation guidance belongs with the documentation capability; task-specific documents normally belong with their owning component.

### Procedure

1. **Identify purpose and audience.** State what the document is for, who needs it, and when it applies.
2. **Find the nearest sensible owner.** Check the target area and an obvious existing source. Do not audit the entire repository before writing a local document.
3. **Choose a locally suitable format.** Follow useful local conventions without forcing an elaborate metadata block, universal template, or exhaustive cross-reference structure.
4. **Write for practical use.** Include enough context, requirements, steps, limitations, and next references for the intended reader.
5. **Separate authority from explanation.** Distinguish mandatory requirements from recommendations, examples, rationale, and proposals. Link to canonical shared rules instead of creating a competing authority.
6. **Keep it focused.** Split content only when parts have distinct tasks, audiences, owners, or maintenance boundaries and can be understood or loaded independently.
7. **Add only useful navigation.** A direct local reference may be enough. Do not create a full hub during ordinary task work.
8. **Verify changed references and claims.** Check links added or modified and ensure statements about tools, files, permissions, or implemented behavior are supported.

### Documentation quality checks

- Can the intended reader tell when the document applies?
- Is it clear what is required and what is only recommended?
- Is the authoritative source for shared rules identifiable?
- Can the relevant content be used without loading unrelated material?
- Does the document avoid unsupported claims or needless duplication?

Maintenance may later align terminology, canonical ownership, placement, and navigation across related documents. Do not rewrite useful local material solely for stylistic uniformity.

---

## Procedure 08 — Tool lookup and selection

**Applies when:** Finding or choosing a tool, connector, plugin, integration, capability, or execution surface for a task. Tool discovery can happen before a task starts or when a capability gap becomes apparent during execution.

### Procedure

1. **Describe the operation, not a presumed product.** Identify what must be done, what system or data it touches, and whether it requires reading, writing, code execution, local files, or external access.
2. **Inspect the tools actually available.** Consider native ChatGPT tools, connected GitHub actions, connected plugins, and any available Codex or local execution surface. Do not assume a product is connected or that a connection exposes every possible action.
3. **Choose the narrowest suitable action.** Check the tool's actual description, inputs, limits, and permissions. Prefer a direct supported action over an unnecessary layer.
4. **Distinguish repository API work from local execution.** GitHub connector actions may be sufficient for supported repository operations such as reading, searching, creating or updating files, and working with supported branches, issues, pull requests, or workflow records. Use Codex or another execution environment when the task actually requires a working tree, shell, local filesystem, build, or test execution that the connector does not provide.
5. **Search available capability documentation when needed.** Discover the relevant tool before claiming it is unavailable or asking for a different connection. Do not invent tool names or capabilities.
6. **State a real capability gap precisely.** If no suitable action is available, identify the missing permission, connection, or execution capability and use a supported alternative when practical.
7. **Return to the task.** Once the tool is selected, continue under Procedure 10 and the relevant task procedure.

Do not build a new capability merely to avoid checking whether an existing tool can perform the operation.

---

## Procedure 09 — Telemetry and observability

**Applies when:** Designing, operating, or reviewing mechanisms that record workspace activity or turn evidence into maintenance and improvement suggestions.

**Typical destination:** Use the current `observability/` structure and its ownership rules.

### Separate the information lifecycle

- **Collection:** Raw events or activity records captured by a real, authorized mechanism.
- **Analytics:** Derived patterns such as usage, dependencies, repeated failures, or navigation friction.
- **Suggestions:** Persistent, reviewable opportunities for maintenance or improvement.

### Guidance

1. Define the purpose before collecting anything. The information should support a real maintenance, reliability, or improvement decision.
2. Use automatic structured collection when a technically supported and authorized mechanism provides durable value; do not impose manual reporting overhead without a clear benefit.
3. Define data scope, access, security, and retention boundaries. Collect only what is needed and protect credentials, sensitive content, and user material.
4. Keep raw collection distinct from interpretation and proposed changes.
5. Make suggestions evidence-based and reviewable. Telemetry does not itself authorize repository changes.
6. Verify that a collection, analytics, or suggestion mechanism actually exists before describing it as operational.

Do not add telemetry speculatively, collect information without a defined purpose, or imply that a proposed mechanism is already implemented.

---

## Procedure 10 — Running a task and workspace operations

**Applies when:** Carrying out a repository task and the execution path, applicable guidance, or required tools are not yet clear. This is the general route for unlisted tasks as well as common GitHub-connected operations.

**Typical route:** Root README → common task lookup or closest task guide → this general execution procedure → only the specialist guidance that materially applies.

### General task-execution route

1. **Understand the requested outcome.** Identify the expected result, target resources, systems involved, and user-stated boundaries. Do not choose a tool solely from the wording of the request.
2. **Consult the task lookup.** Use the root README and any relevant task lookup to find a clear route. Common task examples are aids to selection, not an exhaustive list or allowlist.
3. **Do not force-fit unclear guidance.** If a task-specific guide is unclear, absent, or unrelated, it may be skipped while proceeding under this general procedure and the closest clearly relevant guidance. Skipping a guide must not bypass a clear authority, security, recovery, or shared-contract requirement, and must not expand the task's scope.
4. **Inspect the actual target.** Confirm the repository, branch or ref, current state, target paths, and relevant constraints before changing anything.
5. **Identify the execution surface.** Check the tools and permissions actually available. Use Procedure 08 when the right tool is not obvious or a capability gap appears.
6. **Select the operating environment.** Use Working for feature creation and ordinary task-scoped changes. Use Maintenance when the requested outcome is repository organization, alignment, or improvement. Tool choice does not determine the operating environment.
7. **Load only the specialist procedures needed.** Apply Procedures 01 and 02 for protected or shared surfaces, Procedure 03 for preservation risks, and Procedures 04–09 when their task scopes apply. Do not load the full DP C for an ordinary task.
8. **Execute within authority and capability.** Perform only the requested and authorized work. Available tools, write access, automation, or convenience do not grant broader authority.
9. **Verify the resulting state.** Check the changed file, commit, branch state, workflow result, feature behavior, references, or other source of truth relevant to the task.
10. **Report accurately.** State what was completed, what was verified, and any limitation or deferred issue. Do not claim a tool, test, permission, workflow, or control succeeded unless it did.

### Common task lookup

These are common routes, not a complete inventory:

| Task type | Typical route |
| --- | --- |
| Read a file or inspect a directory | Use an available repository read/fetch action; inspect the relevant content before relying on it. |
| Search code, files, or references | Use the available search action, then fetch the relevant source for full context. |
| Create or update a repository file | Use the matching GitHub contents action when available; verify the resulting file and commit. |
| Inspect branches, commits, metadata, or status | Use the matching repository or Git-data action when available. |
| Work with issues, pull requests, reviews, or comments | Use the relevant GitHub issue or pull-request action when available and authorized. |
| Inspect workflow runs, jobs, or artifacts | Use the relevant GitHub Actions action when available. |
| Run a local build, test suite, shell command, or filesystem-dependent process | Use Codex or another execution environment that actually provides the required runtime. A GitHub API connector alone should not be assumed to execute arbitrary local commands. |
| Perform another task not listed here | Identify the closest general operation, discover the required capability, load only clearly relevant specialist guidance, and proceed when authorized and supported. |

**Important distinction:** A task involving a GitHub repository is not automatically a Codex-connection task. Standard GitHub connector actions may be sufficient for supported repository API operations. Codex or another execution environment is relevant when the task needs local or agent execution capabilities that are actually available. Check the current connection and action surface rather than assuming either route.

### Unlisted tasks

An unlisted task is not automatically out of scope. Identify the resource and operation, follow the general route above, and use the closest relevant procedure. If no suitable capability exists, state the specific limitation and continue with any safe, supported portion of the task.

---

## Cross-procedure boundaries

- **A task can trigger more than one procedure.** Use the task's main outcome to select its primary procedure, then add only the procedures required by affected boundaries.
- **Sensitive changes remain sensitive in every environment.** Working allowances and Maintenance responsibility do not waive authorization.
- **Task lookup is not an allowlist.** An absent example is not a reason to reject otherwise authorized work.
- **Tools do not confer authority.** Available actions and repository write access do not expand the requested scope.
- **Context should remain proportional.** Read enough to do the task correctly, not everything that might be related.
- **Preserve meaning and history.** Consolidation should not silently erase source material, meaningful distinctions, or recovery options.
- **Be accurate about implementation.** Do not describe proposals, intended directories, or documented controls as implemented capabilities until verified.

## Overall operating rule

Working should make useful creation and ordinary task completion practical, with low unnecessary overhead. Maintenance should be the main organizing force that turns accumulated contributions into a coherent and discoverable workspace. Both remain subject to the same authority, security, compatibility, user-material preservation, and recovery boundaries.
