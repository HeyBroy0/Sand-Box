# Sand-Box
Evolving public workspace for tools, scripts, and GitHub Actions capabilities. 
Do not touch archives. Only update `main` with stable and working tools and relevant instructions only with heavy emphasis on reducing context-window overhead, otherwise keep it in a new experimental branch.

**Public repository:** never commit secrets, private information, or confidential files.
## Use
- Inspect the current files in `data/` if necessary; reuse existing tools when practical. maintain the tool use instructions below as necessary.
- **Dataset analysis:** open **Actions → Dataset analysis → Run workflow**, choose an input under `data/`, and download the results artifact.
- **Clean workflows:** open **Actions → Clean workflows → Run workflow**. Check the confirmation box. Set `keep_recent_runs` to the number of newest completed runs to retain (default `0`). Older completed runs and their artifacts are deleted. The cleanup run itself remains visible until a later cleanup.

## Update
- Add reusable scripts under `scripts/`; keep inputs in `data/` and generated reports in `reports/` or workflow artifacts.
- Add one focused workflow per capability under `.github/workflows/`. Keep workflows manual-only with `workflow_dispatch` unless automatic triggers are specifically needed.
- Grant only the permissions each workflow requires. Never hard-code credentials.
- Before substantial or risky changes, create a new branch such as `archive/main-YYYY-MM-DD` from the current `main`. Do not overwrite older archives.
- When a feature is added or changed, update this README with only its purpose and how to run or update it.

Workflows is purposefully a volatile storage location, save any final artifacts deemed important to `reports/` before clean up.
