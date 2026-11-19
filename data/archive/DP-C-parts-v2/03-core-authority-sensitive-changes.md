# Part 3 — Core, authority, and sensitive changes

**Intended destination:** **core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/**; authority references belong under **core/authority/**.

**Applies in either environment when:** A task would change repository identity, core policy, architecture, configuration, authority, entrypoints, shared routing, canonical discovery, or another contract with cross-repository effects.

### Procedure

1. **Confirm explicit authorization.** Verify that the task authorizes the sensitive change and that the applicable procedure permits it. Repository write access is not authorization.
2. **Load governing sources.** Read the current repository entrypoint, relevant core guidance, authority model, and required change procedure. Do not load unrelated core material.
3. **Map the impact.** Identify affected documents, routes, capabilities, workflows, catalog entries, tests, consumers, and branch or release processes.
4. **Make the smallest coherent change.** Preserve boundaries and compatibility where practical. Keep unrelated improvements separate.
5. **Verify affected consumers and controls.** Check references, interfaces, and required repository controls. Do not claim enforcement unless the relevant GitHub or execution system actually provides it.
6. **Stop if authority is unclear.** Do not modify the protected surface. Keep a proposal separate from authoritative instructions and identify the missing decision or authorization.

### Boundaries

- Working allowances do not bypass this procedure.
- Maintenance responsibility does not bypass this procedure.
- Policy, authorization, connector permissions, and technical enforcement are distinct.
- A proposed rule, directory, or control is not an implemented control.

---