# Cleanup and retention instructions

Use this guide before removing files, pruning workflows/artifacts, or deleting branches. Cleanup is a maintenance task with potentially irreversible effects; inspect first and keep the default action non-destructive.

## Default retention rules

- Preserve `main`, protected branches, archive/backup branches, and any branch referenced by an open pull request.
- Preserve `data/` and `reports/` unless the repository owner explicitly identifies the specific files for removal.
- Do not delete source documents, user-provided files, review outputs, or offline-rollback material merely because they appear old or unused.
- Do not rewrite Git history, force-update a branch, delete a workflow, or remove a backup as routine housekeeping.
- Do not interpret an old timestamp or an unreferenced-looking path as permission to delete it.

## Required cleanup procedure

1. **Define the scope.** Identify exactly which files, workflows, Actions runs/artifacts, or branches the request covers. Separate eligible candidates from protected material.
2. **Inspect references.** Check open pull requests, branch protection, workflow triggers, catalog entrypoints, README links, tests, and any source files that depend on the target.
3. **Preview first.** Produce a candidate list and explain why each item appears safe to remove. Prefer dry-run or list-only behavior.
4. **Preserve rollback.** Keep an existing archive or offline copy where available. Do not assume that a remote deletion can be undone by an offline save.
5. **Require explicit scope for destructive changes.** If the request does not clearly authorize deletion of a specific class of data, leave it untouched and perform non-destructive pruning only.
6. **Apply the smallest cleanup.** Remove obsolete references together with the exact item they refer to. Do not combine unrelated refactors.
7. **Verify afterward.** Re-list the affected paths/branches/workflows, validate the catalog, run relevant tests, and check that open pull requests still reference existing branches.

## Branch handling

New work starts on `temp/<short-task>` from the latest `main`. Continue an existing PR on its head branch when explicitly asked to continue it. Before deleting any branch, verify that it is not:

- `main` or a protected branch;
- an archive, backup, or rollback branch;
- the head branch of an open pull request;
- the source of an unfinished or unreviewed task.

Do not force-push or delete a branch to resolve a conflict unless the repository owner explicitly requests that operation and the exact target is understood.

## Actions retention

For workflow-run or artifact cleanup, inspect run status, age, workflow ownership, and whether an artifact is still needed for review or rollback. Prefer configurable retention and explicit preview over a broad destructive workflow. Keep cleanup operations separate from normal tool workflows.

When cleanup intersects core instruction routing, catalog structure, or shared CI contracts, start with [the Core documentation router](read-core-readme-first/core-readme.md) and follow its core-change route before proceeding with this guide.
