# Sand-Box

A lightweight, public workspace for reproducible file handling, temporary project work, and GitHub Actions-assisted transfers between ChatGPT sessions.

This repository is also an instruction sheet for future assistant sessions. Read this file before using the repository.

## Repository facts

- Repository: `HeyBroy0/Sand-Box`
- Default branch: `main`
- Visibility: **Public**
- Intended use: scratch space, file conversion, packaging, validation, and artifact handoff
- Do not assume that a workflow exists just because GitHub Actions is enabled. A workflow runs only when a workflow file defines a matching trigger.

**Public-repository warning:** committed files, commit history, issues, and workflow artifacts may be accessible to other people. Never put passwords, API keys, access tokens, private personal information, confidential documents, or other sensitive material here. Use an appropriately private and authorized location for sensitive files.

## Start here on every task

Before changing anything:

1. Read this README.
2. Inspect the default branch, repository tree, recent commits, and `.github/workflows/`.
3. Check whether a workflow already does the required job. Reuse or improve it rather than creating duplicate workflows.
4. Identify the input files and intended outputs. Preserve original inputs unless the user explicitly asks for replacement or deletion.
5. Choose the smallest safe change. Use a task-specific branch when work should not go directly to `main`.

Do not assume the repository is empty or unchanged just because an earlier session found it that way.

## What this repository is for

Use GitHub as an independent place to store and process files when a task can be handled reliably through repository operations or a scripted GitHub Actions workflow.

Typical uses:

- Store and version small text files, source files, configuration, and documentation.
- Convert, inspect, checksum, package, or validate files using a reproducible script.
- Run a manually triggered workflow that creates an output file and uploads it as a GitHub Actions artifact.
- Retrieve a workflow artifact later using the GitHub integration's artifact-download capability.
- Keep a durable handoff record when a ChatGPT session ends.

GitHub is a storage and automation route, not a replacement for every ChatGPT capability. A workflow can perform deterministic scripted processing, but it does not provide ChatGPT's reasoning, web research, or source evaluation automatically.

## File-handling procedure

### Small text files

Use the GitHub file operations to create or update text files. Before updating an existing file, fetch its current contents and blob SHA. Avoid overwriting a file based on an outdated copy.

Prefer descriptive paths, for example:

- `inputs/README.md`
- `scripts/convert_text.py`
- `outputs/summary.txt`

Keep original inputs separate from generated outputs.

### Binary files and larger transfers

The GitHub file-content interface is primarily useful for text. For binary files, archives, or files that are awkward to transfer through the text interface:

1. Use a workflow to obtain or process the input using an authorized method.
2. Write generated results into a dedicated output directory.
3. Upload the result with the GitHub Actions artifact-upload action.
4. Record the workflow run and artifact name in the task notes.
5. Download the artifact through the GitHub integration when the file needs to be brought back into the conversation.

Do not assume that an artifact is a permanent archive. Workflow artifacts have retention and storage limits. For durable results, preserve an appropriate copy in the repository only when it is safe for a public repository, or use another authorized storage location.

### Preserve and verify

For file transformations:

- Keep the source file unchanged.
- Write results to a new path or artifact.
- Record the operation, tool or script version, and relevant options.
- Where practical, record file sizes and SHA-256 checksums before and after transfer.
- Verify the output can be read and that the file type and expected contents are correct.
- Do not claim a transfer or conversion succeeded until the output has been checked.

Do not silently truncate, normalize, re-encode, or modify binary data. For a pass-through transfer, compare checksums.

## GitHub Actions conventions

Workflow files belong in `.github/workflows/` and must use YAML.

- **Default for this repository: manual-only workflows.** Use `workflow_dispatch` as the only trigger unless the user explicitly requests automation.
- Do not add `push`, `pull_request`, `schedule`, `workflow_run`, or other automatic event triggers without explicit authorization.
- Keep workflow files focused and reusable; separate unrelated jobs into separate workflow files.
- Give each workflow a clear name and document its inputs and outputs.
- Set the minimum necessary `permissions:` for the job. Do not grant write access when read access is sufficient.
- Do not put credentials directly in workflow files or committed configuration. Use GitHub Secrets only when a workflow genuinely needs a secret, and never print secret values in logs.
- Give artifacts clear names and sensible retention periods.
- Make jobs safe to rerun. Avoid workflows that repeatedly overwrite or delete unrelated repository content.

Actions being enabled is not the same as a workflow being scheduled. The `on:` section in each workflow determines which events start it. Check that section before predicting whether a commit, pull request, or manual action will trigger a run.

GitHub Actions usage, artifact storage, and retention are governed by GitHub's current plan and service limits. Do not describe usage as unconditionally unlimited; check current GitHub billing and limits when that matters.



### Ensure workflows run only when explicitly requested

GitHub Actions being enabled does not mean every workflow runs automatically. Each workflow's YAML trigger controls when it starts.

For this repository, keep useful workflows **manual-only by default**. A manual-only workflow should have this trigger and no other event triggers:

```yaml
on:
  workflow_dispatch:
    inputs:
      input_path:
        description: Repository-relative input file
        required: true
        default: data/example.csv
        type: string
```

To remove automatic execution from an existing workflow:

1. Open the relevant `.github/workflows/*.yml` file.
2. Find its top-level `on:` section.
3. Remove automatic event triggers such as `push:`, `pull_request:`, `schedule:`, and `workflow_run:`.
4. Keep only `workflow_dispatch:` (and any manual inputs it needs).
5. Commit the change and inspect the workflow file again to verify that no automatic trigger remains.

To run a manual workflow, open the repository's **Actions** tab, select the workflow (currently **Dataset analysis**), select **Run workflow**, choose the branch and inputs, then confirm **Run workflow**.

**Do not disable Actions entirely under Settings → Actions → General** when you still want manual runs. Disabling Actions at repository level also prevents the manual workflow from running. The correct setting for “only when I call it” is to leave Actions enabled and restrict each useful workflow to the `workflow_dispatch` trigger.

A run that has already started will finish even after its trigger is removed. Removing a workflow file also does not erase its historical run entry from the Actions page.

## Fact-checking and research

Use this repository to preserve research notes, datasets, source lists, and reproducible calculations. Do not treat a file in this repository as proof that a factual claim is correct.

For claims that may have changed, use current primary or otherwise reliable sources. Record:

- The claim being checked.
- The source title and URL.
- The publication or update date, when available.
- The date the source was accessed.
- What the source actually establishes, including limitations.

Prefer primary sources for laws, policies, standards, official product documentation, scientific papers, and published datasets. Distinguish verified facts from estimates, interpretation, and unresolved questions. Keep source quotations brief and respect copyright.

## Working across ChatGPT sessions

A future assistant session should:

1. Open this README and inspect the current repository state.
2. Check whether the GitHub connection can read and write this repository.
3. Use GitHub for repository operations and Actions for tasks that benefit from reproducible automation.
4. Use ChatGPT's web research for current external fact-checking, with citations.
5. Use built-in file upload or analysis tools when they are available and materially better suited to the task.
6. If a ChatGPT tool is unavailable or rate-limited, consider whether the task can safely be completed with GitHub and a deterministic script. Be explicit about what was and was not performed.
7. Check that useful workflows remain manual-only unless the user requested automatic triggers. Report the branch, files changed, commit, workflow run, and artifact name when relevant.

Do not claim that GitHub Actions bypasses ChatGPT limits. It runs independently on GitHub, with its own permissions, quotas, billing, and storage rules. A successful GitHub operation does not establish that a ChatGPT upload or analysis quota is available.

## Change discipline

- Do not delete files, branches, artifacts, or workflow runs unless the user specifically asks.
- Do not modify unrelated projects or repositories.
- Do not force-push or rewrite history unless explicitly requested.
- Keep changes small and explain their purpose in the commit message.
- After a change, verify the resulting file or commit through GitHub.
- Report failures plainly; never describe an unverified operation as successful.

---

This README is the starting point, not a substitute for inspecting the live repository and current GitHub documentation before each task.
