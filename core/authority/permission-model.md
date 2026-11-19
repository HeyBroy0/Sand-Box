# Permission Model

**Status:** Proposed draft for review; not yet adopted as authority. This document does not itself grant permissions or create technical controls.


**Purpose:** Distinguish written policy, task authorization, connector permissions, and technical enforcement.

## Permission concepts

- **Policy** states what should or should not be done.
- **Task authorization** establishes that a particular requested action is within the authority granted for the task.
- **Service permissions** are the access rights actually granted by GitHub, connectors, accounts, or other connected systems.
- **Execution capabilities** describe what a runtime or workspace can actually read, write, execute, or access.
- **Enforcement** is a technical control that prevents an action or requires a condition before it proceeds.

These concepts must not be treated as interchangeable. A policy document does not reduce an already-authorized connector's permissions. A successful write operation does not prove that the action was authorized.

## Operating requirements

1. Use only the repository, branch, services, and capabilities actually exposed to the task.
2. Confirm the target and the scope of the requested action before changing shared or protected material.
3. Do not infer permission to change policy, authority, entrypoints, recovery records, or cross-component contracts from general write access.
4. Use least privilege when configuring capabilities or workflows.
5. Never claim that a policy is technically enforced unless the relevant service control has been inspected.
6. When authorization is unclear, stop the protected action and identify the decision required.

## Related authority

- [Protected Change Gate](../this-is-instruction-to-read-core-readme-before-proceeding/standards/change-gate.md)
- [Protected Change Procedure](../this-is-instruction-to-read-core-readme-before-proceeding/procedures/protected-change.md)
- [Workspace Authority](workspace.md)
