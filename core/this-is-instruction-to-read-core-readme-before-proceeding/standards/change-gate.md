# Protected Change Gate

**Status:** Proposed core standard; pending explicit adoption.

A change requires protected review when it materially affects:

- Repository identity, durable purpose, or foundational principles.
- Core architecture, authority, permission, recovery, or workspace boundaries.
- Root entrypoints, shared routes, or canonical discovery contracts.
- Shared interfaces or requirements with cross-component or cross-repository consumers.
- The meaning, adoption status, or preservation rules of core standards and protected records.

Ordinary local implementation, focused component documentation, and local maintenance are not protected solely because they occur in this repository.

A protected change requires review against the relevant principles, architecture, authority, affected consumers, compatibility, and recovery implications, plus explicit authorization through the actual applicable process. The [Protected Change Procedure](../procedures/protected-change.md) defines how to carry out that review.

Write access is not proof of authorization. This standard describes the policy boundary; technical enforcement must be verified in the relevant GitHub or execution controls.
