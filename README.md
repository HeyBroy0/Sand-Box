# Sand-Box — workspace entrypoint

This is the **always-read layer** for Sand-Box. Read it first, then follow only the route needed for the current task. It is a router, not a replacement for specialist instructions.

## How to route work

1. Identify the requested outcome and the systems or files it affects.
2. Choose the operating environment from the outcome: **Working** for feature creation and ordinary task-scoped work; **Maintenance** when the requested outcome is broader organization, alignment, or improvement.
3. Open the relevant task module below. Load only the parts needed for the task.
4. Check the actual available tools and permissions before choosing an execution path. Do not assume that a repository task requires Codex or that a product connection guarantees a specific capability.

## Task routes

| When the task is… | Read this route |
| --- | --- |
| **Run a task**, or determine how to execute it when the right tool is not yet clear | [Part 6 — Task execution and workspace operations](data/DP-C-parts-v2/06-task-execution-and-workspace-operations) |
| **Find or choose a tool**, connector, plugin, or execution surface | [Part 4 — Capability and tool discovery](data/DP-C-parts-v2/04-capability-and-tool-discovery) |
| Create a feature, script, workflow, test, or ordinary local change | [Part 1 — Working Environment](data/DP-C-parts-v2/01-working-environment) |
| Perform repository cleanup, documentation alignment, consolidation, or broader improvement | [Part 2 — Maintenance Environment](data/DP-C-parts-v2/02-maintenance-environment) |
| Create or edit a document | [Part 5 — Document creation and editing](data/DP-C-parts-v2/05-document-creation-and-editing), plus Part 1 or Part 2 according to the task outcome |
| Change protected core, authority, entrypoints, or shared contracts | [Part 3 — Core, authority, and sensitive changes](data/DP-C-parts-v2/03-core-authority-sensitive-changes) |
| Preserve, restore, archive, or perform potentially destructive work | [Part 7 — Recovery and preservation](data/DP-C-parts-v2/07-recovery-and-preservation) |
| Design or assess telemetry, usage evidence, or improvement signals | [Part 8 — Observability and improvement evidence](data/DP-C-parts-v2/08-observability-and-improvement-evidence) |
| Find guidance or maintain navigation and capability discovery | [Part 9 — Navigation and capability discovery](data/DP-C-parts-v2/09-navigation-and-capability-discovery) |

A GitHub repository task should normally begin at **Part 6**, not with an assumption that Codex must be connected. Supported GitHub connector actions can handle repository API operations; use Codex or another execution environment when the task actually requires a working tree, shell, local filesystem, build, or test execution. Part 6 gives the decision path and common examples.

**The task examples are not exhaustive.** When a task is not listed, use Part 6's general execution route, identify the closest relevant specialist guidance, and continue when the task is authorized and the required capability is available. Do not reject a task merely because it is not named here.

## Progressive loading

- **Always read:** this root README only.
- **Working:** Part 1 plus only the specialist part(s) needed.
- **Maintenance:** Part 2 plus only the specialist part(s) affected by the maintenance scope.
- **Sensitive changes:** Part 3 whenever protected core, authority, entrypoints, or shared contracts are involved.
- **Task/tool routing:** Parts 6 and 4 when execution-path or tool discovery is needed.
- **Other specialist guidance:** Parts 5 and 7–9 only when relevant.

Do not load every module by default. Working tasks should not inherit a repository-wide maintenance audit. Maintenance should inspect enough context to restore coherence without making every routine task carry the full organizational process.

## Shared boundaries

Both environments remain subject to applicable security, authority, compatibility, user-material preservation, and recovery requirements. The Working/Maintenance distinction is an operating model, not a technical permission boundary. Actual access and enforcement come from the connected services and execution environment.

## Full reference documents

The complete DP and the combined full DP C are not routine entrypoints and are intentionally **not linked here**. They are reserved for full Improvement maintenance when their broader principles and integrated guidance are needed. Part 2 identifies those references for that case.
