# Sand-Box workspace evolution — discussion record

**Recorded:** 2026-11-17  
**Purpose:** Preserve the design discussion and implementation context for a later return.  
**Status:** Discussion record only. This file does not authorize or implement the proposed step-5 architecture.

## Context

The discussion began with a review of the `brnch` branch against `main`. The direction was to make Sand-Box a small-core, expandable-capabilities workspace, with progressive instruction loading and clear separation between durable repository rules and everyday tools.

The review found that `brnch` was four commits ahead of `main`, with no divergence. Its meaningful changes were in `README.md` and `core/check-core-readme-first/core-readme.md`. The review endorsed the smaller root README and progressive loading, while identifying incomplete README routing, a directory-map entry for a directory that did not exist, unresolved WIP notes, inconsistent branch-policy wording, and a numbering/formatting issue in the core document.

## Steps 1–4: work carried out on `brnch-2`

A new branch, `brnch-2`, was created from `brnch`. The original `brnch` branch was not changed.

The WIP question about identifiers was answered with descriptive, namespaced scope labels. They are intended for architectural discussion, not as a new machine-readable schema or mandatory task registry.

Core scope identifiers:
- `core.bootstrap_routing` — repository bootstrap and agent entrypoints, including `README.md` and `AGENTS.md`.
- `core.instruction_routing` — how applicable instructions and guides are organized, selected, and loaded.
- `core.capability_discovery` — the capability catalog, `scripts/find_tool.py`, and their shared discovery contracts.
- `core.shared_contracts` — stable inputs, outputs, validation, or conventions used by multiple capabilities.
- `core.repository_validation` — repository-wide tests, CI, and validation behavior.
- `core.instruction_system` — durable cross-cutting rules and the structure/authority of the core instruction system.

Non-core scope identifiers:
- `local.standalone_capability` — an isolated script or capability change with no shared-contract impact.
- `local.workflow` — a workflow-local change that does not alter shared workflow behavior or repository-wide validation.
- `local.routine_content` — a routine report, input document, or retained-content update.
- `local.isolated_example` — a one-off example that does not establish a shared convention.

The identifiers describe scope by effect, not by file location or importance. They should not be turned into a registry without a demonstrated recurring need.

### Core documentation structure established on `brnch-2`

The old `core/check-core-readme-first/` directory was removed and replaced with `core/read-core-readme-first/`.

The new directory contains:
- `core-readme.md` — the small router for core-surface work.
- `core-change-gate.md` — the definition of core, scope identifiers, dependency mapping, and required change process.
- `design-principles.md` — architectural principles, separated from the change procedure.
- `instruction-architecture.md` — Instructions versus Guides, progressive loading, document splitting, routing, and authoring conventions.
- `capability-discovery.md` — the dependencies and verification requirements for changes to catalog/discovery contracts.

The router directs agents to load only the specialist document(s) applicable to their task. It also makes clear that ordinary tool discovery/building does not require the core-change gate unless the shared discovery contract itself is changing.

The design principles emphasize:
1. Keep the always-read layer small.
2. Load instructions progressively.
3. Separate requirements from explanation.
4. Keep core small and durable.
5. Prefer composition over duplication.
6. Preserve compatibility deliberately.
7. Avoid speculative infrastructure.
8. Keep documentation actionable.
9. Prefer the smallest coherent structure.

A decision tree is optional. Use one when multiple stable routes make wrong-route loading materially costly; use a short table when that is simpler. Do not create directories or instruction layers for hypothetical future needs.

The root `README.md`, `AGENTS.md`, and `core/clean-up.md` were updated to use the new path and routing. The resulting branch tree was checked: the old directory no longer exists, and no stale references to its old path were found.

**Branch state at the time of this record:** `brnch-2` was two commits ahead of `brnch`, with HEAD `5e24d5614632365f54081f01a5134747aebb807a`. These documentation changes exist on `brnch-2`, not on `main`.

## Step 5: proposed evolving-workspace model (discussion only)

The proposed direction is to treat Sand-Box as an evolving workspace that AI agents can improve over time, while keeping `main` as a consolidated, recoverable state.

The central principle proposed:

> AI agents may develop and improve the workspace on working branches, while changes reach `main` through a controlled maintenance process.

### Candidate branch roles

| Branch family | Intended role |
| --- | --- |
| `main` | Consolidated workspace state |
| `work/*` | Persistent or task-specific agent development |
| `archive/*` | Immutable fallback snapshots of known states |

This is a proposal, not an adopted policy. Branch naming and lifecycle details remain open.

### Cleanup versus workspace maintenance

The discussion distinguished two operations:

- **Ordinary cleanup:** remove specifically eligible temporary artifacts and genuinely obsolete material under retention safeguards.
- **Workspace maintenance:** review accumulated working branches, activity records, tools, workflows, commits, and suggestions; decide what is worth integrating; prepare a coherent update to `main`.

The proposed maintenance sequence:
1. Inspect the current `main` state and working branches.
2. Review suggestions and relevant recorded activity.
3. Decide which changes are worth integrating.
4. Create an archive branch/snapshot from the exact current `main` commit before modifying the consolidated state.
5. Prepare accepted changes on an integration branch.
6. Run relevant validation and inspect the resulting tree.
7. Promote the integration to `main` only through the agreed authorization process.

Avoid force-updating `main`; preserve history and treat the archive as a recovery reference. An archive should never be overwritten as part of routine maintenance.

### Automatic activity recording

A key design requirement is that agents should not have to write narrative progress notes or manually maintain logs. Such a requirement adds context-window overhead and risks incomplete or inconsistent records.

Instead, the proposed system should generate machine-readable event records at the tool/access layer. Candidate event types include:
- `list_tree`
- `search_repository`
- `read_file`
- `create_file`
- `modify_file`
- `delete_file`
- `run_workflow`
- `create_commit`
- `create_branch`

A minimal event could contain:
- session/run identifier;
- timestamp;
- branch/ref;
- operation;
- resource/path;
- tool or integration used;
- result/status.

Record metadata rather than duplicating file contents, prompts, credentials, or sensitive information.

Git commits can show what changed; workflow runs can show which workflows executed; the catalog can show registered capabilities. These do not, by themselves, establish every file or repository location an agent read or navigated. That requires access instrumentation or an instrumented repository access layer. A workflow cannot automatically observe every separate connector/API call an agent makes unless those calls pass through such a layer.

### Suggestion management

The existing `reports/suggestions.md` is a document-specific review note and should not silently become the general workspace backlog.

A separate suggestion mechanism was proposed. Candidate fields:
- unique suggestion ID;
- creation date;
- source branch, commit, or activity session;
- affected paths;
- concise proposal;
- rationale;
- status (proposed, accepted, deferred, rejected, applied).

Agents could record improvement ideas when they encounter them but do not implement them during the current task. Suggestions should be machine-recordable and low-friction, not require long narrative session reports.

### Candidate architectural components

Four possible components were identified:
1. **Workspace activity recorder** — captures repository navigation and tool operations automatically.
2. **Suggestion manager** — retains improvement proposals across sessions.
3. **Workspace maintenance** — reviews accumulated work, activity, and suggestions, and prepares integrations.
4. **Promotion and recovery** — verifies changes, manages authorization, creates recovery points, and updates `main`.

These components should not all be built immediately. First define the contracts and the minimum useful recording/maintenance behavior; add automation only when the recurring need is clear.

### Existing cleanup-workflow concern

The existing `.github/workflows/clean-workflows.yml` has controls for deleting completed workflow runs and optionally deleting branches. Its branch cleanup logic can select branches that are not protected, are not the default branch, are not under reserved prefixes, and are not referenced by an open PR. That does not prove such a branch is finished or disposable.

This conflicts with the idea of persistent working branches. Before expanding cleanup, branch eligibility must account for unfinished or unreviewed work, not just open PRs and protection status. A safe default is to preserve ambiguous branches and report them for review rather than delete them.

Detailed activity logs and workflow artifacts should not be the only permanent history: retention limits and availability can make them unsuitable as the sole audit record. Commit-level history and durable summary records should remain available independently.

## Decisions still open

These questions were intentionally left for discussion before implementing step 5:

1. **Promotion authority:** Should maintenance automatically update `main` after every required check passes, or should it prepare an integration plan/branch for owner approval? The initial recommendation was to begin with explicit approval, while keeping the design extensible toward automated promotion later.
2. **Activity retention:** Should detailed events be retained indefinitely, or retained for a bounded period and periodically summarized into a smaller durable record? The initial recommendation was to keep detailed machine-generated records with controlled retention and preserve permanent commit-level history.
3. **Branch lifecycle:** Which working branches should persist, when can an agent mark a branch complete, and what evidence is sufficient to establish that a branch is safe to archive or delete?
4. **Access instrumentation:** Which tools/connectors must be routed through the recorder, and what events can actually be captured reliably?
5. **Suggestion workflow:** Where should suggestions live, who or what changes their status, and how should maintenance rank or batch them?
6. **Archive and recovery contract:** What exactly is included in a fallback snapshot, how is it named, and how is restoration performed without rewriting history?
7. **Maintenance trigger:** Is maintenance manually initiated, scheduled, or triggered by repository activity?

## Immediate revisit checklist

When returning to this proposal:
- Re-read this report and inspect the current `main` and working branches; do not assume the recorded SHAs are still current.
- Revisit the two promotion/retention decisions above.
- Define the minimum activity-event schema and identify which access paths can be instrumented.
- Define the branch lifecycle and safe cleanup eligibility rules.
- Define suggestion storage and maintenance review behavior.
- Update the core documentation router and relevant task-specific instructions only after the policy is agreed.
- Implement in small, verifiable stages. Do not promote the proposed architecture merely because it is documented here.

---

**Record status:** Design discussion saved for future reference. No step-5 architecture, logging system, suggestion manager, maintenance workflow, branch protection, or promotion policy was implemented by this discussion.
