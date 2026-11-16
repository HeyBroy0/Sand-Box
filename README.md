# Sand-Box

An evolving public workspace for adding useful tools, scripts, and GitHub Actions capabilities. Keep the workspace recoverable with dated archive branches.
**Public repository:** never commit secrets, private information, or confidential files.
## Use
- Inspect the current files and workflows before starting; reuse existing tools when practical.
- **Dataset analysis:** open **Actions → Dataset analysis → Run workflow**, choose an input under `data/`, and download the results artifact.
- **Clean workflows:** open **Actions → Clean workflows → Run workflow**. Check the confirmation box. Set `keep_recent_runs` to the number of newest completed runs to retain (default `0`). Older completed runs and their artifacts are deleted. The cleanup run itself remains visible until a later cleanup.

## Update
- Add reusable scripts under `scripts/`; keep inputs in `data/` and generated reports in `reports/` or workflow artifacts.
- Add one focused workflow per capability under `.github/workflows/`. Keep workflows manual-only with `workflow_dispatch` unless automatic triggers are specifically needed.
- Grant only the permissions each workflow requires. Never hard-code credentials.
- Before substantial or risky changes, create a new branch such as `archive/main-YYYY-MM-DD` from the current `main`. Do not overwrite older archives.
- When a feature is added or changed, update this README with only its purpose and how to run or update it.
