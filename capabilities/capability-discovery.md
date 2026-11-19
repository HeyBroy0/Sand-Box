# Capability Discovery

**Status:** Initial operational draft for review; not yet adopted as repository-wide authority.


**Purpose:** Find reusable capabilities and determine whether they are actually present, supported, and suitable for a task.

## Discovery order

1. Start with the task route and the nearest owning component.
2. Inspect the capability catalog when it contains usable entries.
3. Follow a catalog entry to its declared implementation, documentation, tests, and supported entrypoints.
4. If the catalog does not resolve the need, inspect the obvious local capability area or ask for the missing context.
5. Treat search results, filenames, and directory presence as locators only; verify the actual implementation and interface before relying on it.

## Assessing a candidate

Check the candidate's:
- Purpose and fit with the requested task.
- Inputs, outputs, defaults, dependencies, and limitations.
- Supported entrypoints and actual runtime requirements.
- Permission scope and handling of credentials or user data.
- Failure behavior and available verification.
- Consumers and compatibility requirements if its interface will change.

Prefer extending an existing capability when its purpose and interface remain coherent. Create a separate capability when purpose, ownership, interface, or lifecycle genuinely differs.

## Registration and status

Keep catalog metadata, implementation, documentation, tests, and supported entrypoints consistent when the repository's catalog schema is defined. Do not invent catalog fields or claim registration when the catalog does not establish it. The current catalog may be empty or incomplete; report that state accurately.

## Boundaries

Discovery is not authorization to execute every capability found. Confirm that the selected tool and its permissions are appropriate for the task. Avoid broad architecture audits for small local work.
