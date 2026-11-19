# Protected Change Gate

**Status:** Proposed core standard, pending explicit adoption.

A change is protected when it materially alters one or more of the following:

- Repository identity, durable purpose, or foundational principles.
- Core authority, permission, recovery, or workspace boundaries.
- Repository entrypoints, shared routes, architecture, or canonical discovery contracts.
- Shared interfaces or requirements with cross-component or cross-repository consumers.
- The meaning, adoption status, or preservation rules of core standards and protected records.

## Gate requirements

Before changing a protected surface:

1. Identify the specific protected material and affected consumers.
2. Read the governing core standard and authority source.
3. Confirm explicit authorization through the actual applicable process.
4. Separate proposals from adopted policy.
5. Preserve prior state when required and define a suitable recovery path.
6. Verify affected routes, consumers, controls, and generated outputs.
7. Report the authorization basis, verification, and unresolved decisions.

## Non-gates

Ordinary local implementation choices, focused documentation updates, and component-level improvements are not protected solely because they occur in the repository. Do not turn this gate into a universal approval process.

Availability of a write operation does not establish authorization. This document describes policy; actual blocking must come from the relevant GitHub or execution controls.
