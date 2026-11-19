# Part 6 — Task execution and workspace operations

**Intended destination:** Shared authority and workspace operation guidance under **core/authority/**; task-specific operating references belong with their owning capability or workflow.

**Applies when:** Discovering or changing repository files, branches, commits, pull requests, workflows, or other GitHub-connected operations.


## General task-execution route

**Use this part whenever the request is to carry out a task and the appropriate execution surface is not yet clear, including when the task does not match one of the examples in the root README.**

1. **Understand the requested outcome.** Identify the target, expected result, systems involved, and boundaries. Do not select a tool solely from the task's wording or from an assumption that all coding work requires Codex.
2. **Check the current execution surfaces.** Determine whether the required operation is supported by the currently available ChatGPT tools, GitHub connector actions, connected plugins, or Codex/local execution environment.
3. **Select the narrowest suitable route.** Use a GitHub connector action for supported GitHub API operations. Use Codex or another execution environment when the task requires a working tree, shell, local filesystem, build, or test execution not exposed by the connector.
4. **Discover a missing or unclear tool.** Load Part 4 when the needed action is not obvious, when a connector or plugin may be required, or when the task reveals a capability gap. Then return here and continue.
5. **Select the operating environment by outcome.** Use Part 1 for feature creation and ordinary task-scoped changes. Use Part 2 when the requested outcome is repository organization, alignment, or improvement. Tool choice does not determine Working versus Maintenance.
6. **Load only the specialist guidance required.** Add the relevant part for capability work, documents, protected changes, recovery, observability, or navigation. Do not load the entire DP C for an ordinary task.
7. **Execute within actual authority and capability.** Available tools and write access do not expand the user's requested scope or override repository authority.
8. **Verify the result and report accurately.** Check the resulting state using the available source of truth. State what was completed, what was verified, and what could not be done.

### Common GitHub task routes

The examples below are common routes, not a complete task catalog or an allowlist:

| Requested operation | Typical route |
| --- | --- |
| Read a repository file or inspect a directory | Use an available GitHub read/fetch action. |
| Search for code, files, or references | Use the available GitHub search action, then fetch the relevant file before relying on full context. |
| Create or update a repository file | Use the corresponding GitHub contents action and verify the resulting file/commit. |
| Inspect repository metadata, branches, commits, or status | Use the matching GitHub repository or Git-data action when available. |
| Work with issues, pull requests, reviews, or comments | Use the corresponding GitHub issue or pull-request action when available and authorized. |
| Inspect workflow runs, jobs, or artifacts | Use the corresponding GitHub Actions action when available. |
| Run a local test suite, build, shell command, or filesystem-dependent process | Use Codex or another execution environment that actually provides that runtime. A GitHub API connector alone should not be assumed to execute arbitrary local commands. |

**Important distinction:** A task involving a GitHub repository is not automatically a Codex-connection task. Standard ChatGPT GitHub connector actions may be enough for supported repository operations. Codex is relevant when the task needs the additional local or agent execution capabilities it actually provides. Check the current connection and available actions rather than assuming either path.

### Unlisted tasks

The task examples and route table are illustrative, not exhaustive. If the exact task is not mentioned:

- Do not stop or reject it solely because it is absent from the examples.
- Identify the closest general operation and the resources it affects.
- Follow the general task-execution route above, select the relevant specialist part, and proceed when the task is authorized and the required capability is available.
- If no suitable capability exists, explain the precise limitation and continue with any safe, supported portion of the task.

An unlisted task is not automatically out of scope.

### Procedure

1. **Inspect the actual target.** Confirm repository, branch/ref, relevant state, and target paths before making changes.
2. **Use the available connector surface.** Work within the operations and permissions actually exposed by the connected GitHub environment.
3. **Keep capabilities distinct.** GitHub access, local or hosted execution, filesystem access, and external-service access are separate. Do not infer one from another.
4. **Use relevant existing routes.** Discover an obvious relevant tool or procedure without turning a small task into exhaustive discovery.
5. **Respect task authority.** Perform only the requested and authorized scope. Convenience, automation, and available write access do not grant broader authority.
6. **Verify before reporting.** Check the resulting file, commit, branch state, workflow result, or other relevant outcome. Report failures and limitations accurately.

Working operations should remain focused on the task. Maintenance operations may inspect a wider affected area when needed to restore coherence. Branch names and promotion routes must follow the current repository entrypoint and actual branch controls.

---