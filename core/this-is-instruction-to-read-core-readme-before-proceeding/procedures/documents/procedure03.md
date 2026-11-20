<!--
Core-preserved procedure record 03.
Source draft: data/DP-C-v3 Edit.md
Current operational route: core/.../procedures/protected-change.md; core standards and authority documents.
Captured: 2026-11-19
Status: historical procedure reference; current task wording and routes are maintained in ../DP-C.md. This file is retained for provenance and review.
-->

# Procedure 03 — Core, authority, and sensitive changes

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

### Main sources and protected historical copies

When a document is operationally owned outside core but also needs a protected core record, keep its main operational copy at its real owner and preserve a clearly identified historical copy in the appropriate core documents area.

The core historical copy must identify the main document's repository-relative source path and may link outward to it. Do not add a reverse link from the main operational document to the core historical copy. Route ordinary readers to the main source; use the core copy for protected history or core-specific work. Update historical copies deliberately rather than silently rewriting them whenever the main source changes.

---
