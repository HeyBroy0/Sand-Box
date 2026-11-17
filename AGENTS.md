# Repository agent entrypoint

Before starting repository work, read the root [README.md](README.md). Then inspect the current target ref, working tree or open pull request, and repository file tree; do not assume an earlier conversation describes the current state.

Use the README task-routing table and load only the instruction file relevant to the task. Do not preload or recursively read all of `core/`.

**Required core gate:** before planning, editing, or reviewing a change to a core surface, read the complete `core/check-core-readme-first/core-readme.md` file.

For tool discovery, read `core/finding-tools/README.md`. Before creating or substantially changing a reusable tool, also read `core/tool-building-instructions.md`. Before cleanup or deletion, read `core/clean-up.md`.

Do not commit new work directly to `main`. Start new work from the latest `main` on a `temp/<short-task>` branch, unless continuing an existing pull request on its head branch. Preserve user data and protected/referenced branches. Run the relevant validation and clearly report what was and was not verified.
