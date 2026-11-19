# DP and DP C — alignment review and proposed reorganization

Status: working analysis only. This file records recommendations; it does not authorize or apply changes to the future core, standards, navigation, or operational documents.

## Scope and source handling

The source documents are copied into this branch unchanged as `data/DP` and `data/DP C`. They remain reference material for this review. Do not treat either copy as an adopted policy or overwrite it during the exploratory phase.

The intended eventual destination is the scaffold represented by this branch, then promotion only when separately authorized. The current task is to organize the proposal, not to make it permanent.

## Alignment with the stated design direction

The target is a modular mash: a small, durable alignment layer plus task-specific guidance that can be reached when needed. It should not become a rigid documentation regime.

- Keep the always-read surface short. It should identify the workspace, its essential boundaries, and the next navigation point—not explain every procedure.
- Keep each mandatory rule authoritative in one place. Other documents should link to it rather than paraphrase it.
- Load guidance by task. A routine capability task should not need the full core, all maintenance rules, or every documentation guide.
- Prefer useful connections over elaborate hierarchy. A file should be reachable from an appropriate entrypoint, but need not be loaded by every task.
- Keep implementation and task context primary. Guidance should clarify constraints and choices without consuming the context needed to design or build the tool.
- Make dedicated maintenance responsible for gradual cleanup: deduplication, link repair, stale-route detection, and sensible placement. Do not require every task to perform a repository-wide documentation audit.
- Split material only where a segment has a distinct purpose, audience, or task trigger and can be understood independently.
- Keep the architecture extensible. Proposed directories and fragments are destinations to evaluate, not a mandate to create every possible subsystem immediately.

## Findings from DP

DP contains a useful set of durable design principles, but it is not yet a clean single-place standard.

1. It combines several generations and origins of material: an initial principle set, consolidated additions, new proposals, decision rules, architectural domains, branch roles, and later repeated summaries.
2. Some ideas recur in multiple forms: small always-read layer, progressive loading, core protection, composition over duplication, smallest coherent structure, task authority, recovery independence, and branch promotion.
3. It mixes durable principles with operational detail. For example, branch handling, connector operation, telemetry implementation expectations, and maintenance behavior are useful but are not all core standards.
4. It includes directory diagrams and architectural descriptions that should be maintained as guidance/reference material, not duplicated inside the authoritative principle document.
5. It has useful nuance that should not be lost during deduplication, especially the distinction between repository instructions, authorization, technical enforcement, connector permissions, and execution boundaries.

Recommendation: eventually distill DP into one concise `core/.../standards/principles.md` (or the chosen canonical standards path). Keep only durable cross-repository alignment rules and a small set of decision tests there. Preserve detailed explanations and task procedures in their appropriate destinations.

## Findings from DP C

DP C is more structured and broadly useful as a coverage checklist, but its 15 sections are too large to function as one always-loaded instruction document.

Its sections naturally divide into task-oriented concerns:

| DP C material | Likely eventual home | Load when |
| --- | --- | --- |
| Scope and workspace boundary | Root README and concise core identity/standards | Starting work or evaluating scope |
| Core architecture | Core README/router and core architecture references | Changing or evaluating core |
| Document writing | `capabilities/documentation-Tree/document-creation.md` or a shared documentation guide | Creating or restructuring docs |
| Tool writing and capability registration | Capability discovery and capability-specific build guidance | Finding, creating, or changing a tool |
| Navigation | Core README, capability discovery, and a separate repository map | Finding the next relevant source |
| Protection, access, and authority | `core/authority/*` plus the core change gate | Permission-sensitive or core work |
| Architecture | Core architecture reference and repository map | Structural changes |
| Recovery | `recovery/policies/` and `recovery/procedures/` | Destructive, structural, or restoration work |
| Maintenance | `maintenance/minimal-maintenance/minimal.md` and `maintenance/improvement/improvement.md` | Dedicated maintenance or improvement |
| Telemetry | `observability/analytics/` and `observability/suggestions/` (collection only if implemented) | Observability work |
| Workspace/tool use | Root entrypoint plus the relevant capability contract | Ordinary repository tasks |
| Branch and promotion principles | Authority and improvement guidance | Branch, release, or promotion work |
| Consolidated decision rules | Canonical DP standards, with links to task guidance | Evaluating an architectural choice |
| Overall architectural principle | Short summary in canonical DP; details linked outward | Broad orientation |
| Original directory tree | Separate deduplicated tree/map document | Repository navigation or structural work |

DP C should be treated as source material to decompose, not as a file that must survive intact in the final operational documentation. Preserve the source copy in data during the exploratory phase.

## Proposed end-state shape

This is a routing concept, not a required full implementation checklist.

### 1. One canonical DP standard

Place the adopted, deduplicated principles in the core standards area. Keep it compact and stable. Suggested content groups:

- Workspace purpose and scope.
- Small always-read layer and progressive context.
- Core boundary and authority.
- Modular capabilities and composition.
- Single-source rules and explicit interfaces.
- Smallest coherent architecture; avoid speculative structure.
- Recoverability and preservation.
- Verification and compatibility.
- Proportionate observability and maintenance.
- Promotion discipline.

Keep decision rules as short tests under the relevant principle or as a compact final section. Avoid repeating the same principle in a second summary.

### 2. One separate, deduplicated repository tree/map

Keep the directory diagram out of DP. Place a single maintained map in the architecture/navigation area (for example, `core/.../architecture/repository-map.md`) or another location chosen after the scaffold is reviewed.

The map should:
- Show only real, current top-level responsibilities and meaningful subdirectories.
- Describe each area's purpose in a few words.
- Avoid future placeholders and repeated diagrams.
- Link to authoritative entrypoints, not reproduce their rules.
- Be updated as part of dedicated structural maintenance when paths change.

The map is guidance for orientation; it is not itself a policy document or a substitute for task routing.

### 3. DP C-nav as a lightweight task router

Create a compact `DP C-nav` (likely under the core procedures/router area, subject to final placement). Its purpose is to route a task to the relevant DP C fragment(s), not to reproduce the fragments.

Each route should state:
- The task trigger.
- The one or few documents to load.
- Any required authority gate.
- The next route only if the task expands.

Do not require reading DP C-nav for every task. The root/core entrypoint should point to it only for tasks that need cross-cutting design or documentation guidance. Capability discovery, maintenance, recovery, and authority entrypoints should route directly to their own relevant fragments.

### 4. DP C fragments distributed by ownership

Split DP C into small segments and place them with the subsystem that owns the work. Do not create a central duplicate copy of every segment. DP C-nav should point to the canonical destination.

A fragment should contain only task-relevant guidance, be independently understandable, and link to the canonical DP principle or authority rule where necessary. If a segment is mostly explanation, keep it a guide rather than turning it into mandatory instruction.

## Guardrails against over-structuring

- Do not create a new directory just to mirror every DP C heading.
- Do not make a universal documentation checklist mandatory for ordinary tasks.
- Do not require every AI task to read the tree map, DP C-nav, or all fragments.
- Do not duplicate authority rules in capability guides; link to the authority source.
- Do not add a collection/telemetry layer or other infrastructure merely because DP C mentions it. Implement only when a concrete, authorized mechanism exists.
- Do not turn proposed branch naming or promotion language into enforceable claims unless repository controls actually enforce it.
- Do not move or delete the source copies until the reorganized fragments have been reviewed and their coverage verified.

## Suggested staged approach

1. **Inventory:** retain the two source copies; map each distinct rule or topic to its current source and proposed owner.
2. **Deduplicate DP:** identify repeated statements, resolve wording differences, and produce a concise candidate standard. Preserve distinctions that affect authority or security.
3. **Design routing:** draft the separate repository map and DP C-nav; check that every fragment has a sensible entry route without making the router universal.
4. **Decompose DP C:** create only the fragments needed by actual task categories, placing them with their owning subsystem. Rewrite each segment for its local context rather than mechanically splitting by heading.
5. **Coverage check:** verify every important DP C topic is either represented in a canonical destination, intentionally excluded with rationale, or still marked as a future proposal.
6. **Link and friction check:** test that a typical capability task reaches only capability guidance, a core change reaches core authority and standards, and maintenance/recovery tasks reach their own procedures.
7. **Maintenance handoff:** define lightweight checks for broken links, duplicate authoritative rules, orphaned guidance, and outdated maps. Run these during dedicated maintenance, not on every ordinary task.
8. **Adoption:** only after review and explicit authorization, replace provisional material with the approved documents in the eventual target branch.

## Open decisions for the later design pass

- Whether the canonical DP filename is `principles.md` or another standards filename.
- Exact home and trigger for DP C-nav.
- Whether document-writing guidance belongs under capability documentation or a repository-wide documentation area.
- Which DP C topics are actual requirements versus explanatory guidance or future proposals.
- Whether any telemetry, branch-protection, or execution-isolation proposals are currently implementable; do not imply they already exist.
- Which parts of the existing core authority and maintenance documents should own each fragment.

## Working conclusion

Use DP as the source for a short, canonical alignment standard. Use DP C as a decomposable source checklist, not as a monolithic rulebook. Keep the tree map separate and deduplicated. Use DP C-nav to make task-specific fragments reachable only when relevant. Let dedicated maintenance keep the mesh coherent and remove duplication over time, while ordinary task work remains focused and lightweight.
