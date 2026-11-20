# Workspace Operations

**Status:** Proposed core draft; pending review and adoption.

Before a repository operation, confirm the repository, branch or reference, target paths, current state, and the tool surface that will perform it. Work only within the available capabilities and authorized task scope.

GitHub access, local or hosted execution, workflow execution, filesystem access, and external-service access are separate capabilities. Do not infer one from another.

Use the current branch and promotion practices. Do not force-update a branch or overwrite user-authored material without explicit task authorization. Verify the resulting file, commit, branch state, workflow, or other relevant outcome before reporting.

This guide describes operating expectations. It does not claim that branch protection, required checks, isolation, or other technical controls exist; verify those in the system that would enforce them.
