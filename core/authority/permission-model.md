# Permission Model

**Status:** Proposed core authority draft; pending review and adoption.

Keep four concepts distinct:

- **Policy:** what should or should not be done.
- **Authorization:** whether this task is permitted to perform the requested action.
- **Service permissions:** the access actually granted by GitHub, a connector, account, or external service.
- **Enforcement:** a technical control that blocks an action or requires a condition before it proceeds.

Do not infer authorization from write access, or infer technical restrictions from repository instructions. A successful operation proves only that the service allowed it, not that it was within the task's authority.

For protected work, verify the applicable authorization and service controls. Use least privilege when configuring capabilities or workflows. When authority is unclear, stop the protected action.

See [Workspace Operations](workspace.md) for practical repository operations and the [Protected Change Gate](../this-is-instruction-to-read-core-readme-before-proceeding/standards/change-gate.md) for protected surfaces.
