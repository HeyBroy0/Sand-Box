# Sand-Box — workspace entrypoint

This is the **always-read layer** for Sand-Box. Read it first, then follow only the route needed for the current task. It is a router, not a replacement for specialist instructions.

## How to route work

1. Identify the requested outcome and the files, systems, or repository boundaries it affects.
2. Use the ordered task routes below. Load only the guidance needed for the task.
3. Check the actual available tools and permissions before choosing an execution path. Do not assume that a repository task requires Codex or that a product connection guarantees a specific capability.
4. Keep ordinary task-scoped work in the Working environment. Use Maintenance when the requested outcome is broader organization, alignment, consolidation, or improvement.

## Task routes

1. **Core, authority, and sensitive changes**  
   Read [Part 3 — Core, authority, and sensitive changes](data/DP-C-parts-v2/03-core-authority-sensitive-changes) when changing protected core material, authority, security boundaries, or other sensitive repository structures.

2. **Entrypoints and shared-contract changes**  
   Use [Part 3 — Core, authority, and sensitive changes](data/DP-C-parts-v2/03-core-authority-sensitive-changes) for entrypoint, navigation-boundary, or shared-contract changes as well. This is currently the existing combined guide; this README separates the route without assuming a separate procedure file already exists.

3. **Recovery and preservation**  
   Read [Part 7 — Recovery and preservation](data/DP-C-parts-v2/07-recovery-and-preservation) before restoration, archival, destructive operations, or other work where preservation and recoverability matter.

4. **Maintenance**  
   Start with [Part 2 — Maintenance Environment](data/DP-C-parts-v2/02-maintenance-environment) for repository-wide organization, alignment, consolidation, or improvement. Maintenance should inspect enough context to restore coherence without making every routine task carry the full organizational process.

5. **Editing a feature**  
   Use [Part 1 — Working Environment](data/DP-C-parts-v2/01-working-environment) for ordinary, task-scoped feature edits. Load only additional specialist guidance relevant to the change.

6. **Creating a feature**  
   Use [Part 1 — Working Environment](data/DP-C-parts-v2/01-working-environment) for feature creation and ordinary local development. Feature work does not require a repository-wide maintenance pass.

7. **Creating or changing text and documentation**  
   Read [Part 5 — Document creation and editing](data/DP-C-parts-v2/05-document-creation-and-editing), together with Part 1 or Part 2 when the task's scope calls for the Working or Maintenance environment.

8. **Tool lookup and selection**  
   Read [Part 4 — Capability and tool discovery](data/DP-C-parts-v2/04-capability-and-tool-discovery) to identify available tools, connectors, plugins, permissions, and execution surfaces. For finding the right repository guidance or navigating capability information, also use [Part 9 — Navigation and capability discovery](data/DP-C-parts-v2/09-navigation-and-capability-discovery).

9. **Telemetry and observability**  
   Read [Part 8 — Observability and improvement evidence](data/DP-C-parts-v2/08-observability-and-improvement-evidence) when designing or assessing telemetry, usage evidence, or improvement signals.

10. **Running a task**  
    Follow the common task lookup and then the execution route in [Part 6 — Task execution and workspace operations](data/DP-C-parts-v2/06-task-execution-and-workspace-operations). The lookup is a starting point, not an exhaustive catalogue: an unlisted task should still proceed through the general execution route when it is authorized and the required capability is available. An unclear or inapplicable secondary guide may be skipped while following a lookup route, provided the work stays within the same task scope and does not bypass a relevant authority, security, compatibility, shared-contract, preservation, or recovery boundary.

A GitHub repository task should normally begin with the Part 6 execution route, not with an assumption that Codex must be connected. Supported GitHub connector actions can handle repository API operations; use Codex or another execution environment when the task actually requires a working tree, shell, local filesystem, build, or test execution.

## Progressive loading

- **Always read:** this root README only.
- **Working and feature tasks:** Part 1 plus only the specialist guidance needed.
- **Maintenance:** Part 2 plus only the specialist guidance affected by the maintenance scope.
- **Protected or sensitive changes:** Part 3.
- **Recovery and preservation:** Part 7.
- **Documentation:** Part 5.
- **Tool lookup and navigation:** Parts 4 and 9.
- **Telemetry:** Part 8.
- **Task execution:** Part 6.

Do not load every module by default. Working tasks should not inherit a repository-wide maintenance audit. Maintenance is not an approval prerequisite for ordinary feature creation or task-scoped work.

## Shared boundaries

Both environments remain subject to applicable security, authority, compatibility, user-material preservation, and recovery requirements. The Working/Maintenance distinction is an operating model, not a technical permission boundary. Actual access and enforcement come from the connected services and execution environment.

## Full reference documents

The complete DP and the combined full DP C are not routine entrypoints and are intentionally **not linked here**. They are reserved for full Improvement Maintenance when their broader principles and integrated guidance are needed. Part 2 identifies those references for that case.
