# Protected Change Procedure

**Purpose:** Apply changes to core, authority, entrypoints, architecture, and shared contracts without bypassing the repository's authorization requirements.

## Applies to

Use this procedure when a change affects repository identity, core standards, authority, architecture, configuration, root routing, shared discovery, cross-component contracts, or core-preserved records in a way that changes their meaning or status.

## Procedure

1. **Identify the protected surface.** Name the exact files, rules, routes, consumers, and behavior that would change.
2. **Read governing sources.** Read the root README, [Core README](../core-readme.md), the relevant standard, the applicable authority document, and any specialist procedure.
3. **Confirm authorization.** Verify that the task includes permission for this category of change under the actual repository and organizational controls. Connector write access alone is not proof of authorization.
4. **Separate proposal from adoption.** When authority or policy is unsettled, create or update a clearly labeled proposal instead of changing an adopted standard.
5. **Bound the change.** Change only what is necessary. Identify affected references, consumers, workflows, and generated artifacts.
6. **Preserve prior state.** Follow recovery requirements for destructive or difficult-to-reverse changes. Preserve historical records where required.
7. **Verify.** Check links, anchors, consumers, generated outputs, relevant tests, and the actual state of any claimed enforcement control.
8. **Report status accurately.** State what changed, what authorization was relied on, what was verified, and any unresolved or deferred decision.

## Stop conditions

Stop the protected edit when authorization is absent or unclear, the governing source conflicts, a required recovery path is unavailable, or the proposed change would silently alter an adopted rule. Keep the proposal separate and identify the decision needed.

## Boundaries

- This procedure describes a workflow; it does not grant authority.
- Working autonomy and Maintenance responsibility do not override protected-change requirements.
- A proposed document is not adopted merely because it exists in a canonical-looking directory.
- Technical enforcement must be verified in GitHub or the relevant execution system; prose alone does not enforce permissions.
