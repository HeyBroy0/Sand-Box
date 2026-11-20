# Protected Change Procedure

**Status:** Proposed core procedure; pending review and adoption.

Use this procedure for changes that meet the [Protected Change Gate](../standards/change-gate.md).

1. **Locate the boundary.** Identify the exact principles, architecture, authority, entrypoints, interfaces, routes, or preserved records affected.
2. **Align the design.** Read the relevant principles and architecture. Identify owners, consumers, compatibility effects, and dependencies.
3. **Confirm authority.** Read the applicable authority source and verify explicit authorization. Connector write access alone is not authorization.
4. **Plan preservation.** Check recovery, historical-copy, migration, and rollback implications before destructive or difficult-to-reverse work.
5. **Bound the change.** Change only the authorized scope. Keep proposals separate from adopted standards.
6. **Verify.** Check affected consumers, references, anchors, generated outputs, relevant tests, and any actual technical controls.
7. **Report.** State the authorization basis, changes, checks, unresolved decisions, and deferred work.

Stop before editing when authority is unclear, governing sources conflict, the impact is not understood, or the recovery path required for the change is unavailable. Record the decision needed rather than inferring it.

This procedure does not grant authority or create technical enforcement.
