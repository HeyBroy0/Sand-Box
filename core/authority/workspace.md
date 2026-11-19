# Workspace Authority and Operations

**Purpose:** Define the boundaries for operating on the repository through connected services and execution environments.

## Operational checks

Before a repository operation:
1. Confirm the repository and intended branch or reference.
2. Confirm the exact target paths and current state.
3. Identify which connected tool or execution environment will perform the operation.
4. Check the capabilities and permissions actually available through that surface.
5. Keep the operation within the requested and authorized task scope.
6. Verify the resulting file, commit, branch state, workflow result, or other relevant outcome.

## Distinct surfaces

GitHub repository access, local filesystem access, hosted execution, workflow execution, external-service access, and connector permissions are separate capabilities. Do not infer one from another.

The repository's written instructions describe intended operation but do not technically restrict a connector that already has permission. Enforcement must be verified in the service that provides it.

## Branch and change handling

Follow the repository's current branch and promotion practices. Confirm the current ref before writing. Do not force-update a branch or overwrite user-authored material unless the task explicitly authorizes it. Verify branch-head changes and report the commit or other durable result.

This document does not claim that branch protection, required checks, isolated execution, or other controls are enabled. Verify actual repository settings before relying on them.
