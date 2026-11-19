<!--
Core-preserved procedure record 06.
Source draft: data/DP-C-v3 Edit.md
Current operational route: core/authority/permission-model.md and core/authority/workspace.md.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 06 — Workspace access and operations

**Intended destination:** Shared authority and workspace operation guidance under **core/authority/**; task-specific operating references belong with their owning capability or workflow.

**Applies when:** Discovering or changing repository files, branches, commits, pull requests, workflows, or other GitHub-connected operations.

### Procedure

1. **Inspect the actual target.** Confirm repository, branch/ref, relevant state, and target paths before making changes.
2. **Use the available connector surface.** Work within the operations and permissions actually exposed by the connected GitHub environment.
3. **Keep capabilities distinct.** GitHub access, local or hosted execution, filesystem access, and external-service access are separate. Do not infer one from another.
4. **Use relevant existing routes.** Discover an obvious relevant tool or procedure without turning a small task into exhaustive discovery.
5. **Respect task authority.** Perform only the requested and authorized scope. Convenience, automation, and available write access do not grant broader authority.
6. **Verify before reporting.** Check the resulting file, commit, branch state, workflow result, or other relevant outcome. Report failures and limitations accurately.

Working operations should remain focused on the task. Maintenance operations may inspect a wider affected area when needed to restore coherence. Branch names and promotion routes must follow the current repository entrypoint and actual branch controls.

---
