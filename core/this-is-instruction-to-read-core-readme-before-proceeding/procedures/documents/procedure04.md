<!--
Core-preserved procedure record 04.
Source draft: data/DP-C-v3 Edit.md
Current operational route: capabilities/capability-discovery.md and the relevant capability implementation.
Captured: 2026-11-19
Status: historical procedure reference; current task wording and routes are maintained in ../DP-C.md. This file is retained for provenance and review.
-->

# Procedure 04 — Capability and tool work

**Intended destination:** **capabilities/** for implementations, scripts, tools, tests, workflows, and canonical discovery metadata as applicable.

**Applies when:** Adding, extending, integrating, testing, or documenting a reusable capability. This is normally Working work unless the requested outcome is broader capability alignment or integration, in which case use the appropriate Maintenance scope too.

### Working procedure

1. **Check for an obvious existing fit.** Inspect the nearest relevant capability and its interface. Do not perform an exhaustive architecture audit for a small feature.
2. **Choose extension or separation.** Extend when purpose and interface remain clear. Create a distinct capability when its purpose, interface, owner, or lifecycle genuinely differs.
3. **Define the usable contract.** State purpose, inputs, outputs, defaults, dependencies, limitations, and meaningful failure behavior at a level appropriate to the capability.
4. **Validate relevant boundaries.** Check paths, file types, sizes, user-supplied values, external dependencies, and privilege-sensitive assumptions as relevant.
5. **Keep implementation reusable.** Put shared logic in the capability implementation. Keep workflows and connector-facing surfaces thin; avoid duplicated implementations.
6. **Respect least privilege.** Use only permissions and dependencies required for the defined purpose. Keep credentials and sensitive data out of source, inputs, logs, and artifacts.
7. **Add proportionate verification.** Check normal behavior and relevant invalid or edge cases. Identify consumers before changing a shared interface.
8. **Leave broad alignment to Maintenance.** Make the requested capability usable and locally understandable. Do not create a repository-wide registry, navigation system, or cleanup project unless the task requires and authorizes it.

### Maintenance follow-through

Maintenance may later align capability naming, placement, catalogs, documentation, tests, and shared interfaces across multiple components. It should do this when the accumulated system demonstrates a real coherence problem, not as a reason to burden every feature task with repository-wide integration.

### Do not

- Build a general framework or registry for a one-off need without demonstrated recurring value.
- Treat a filename or search result as proof that a capability is registered or supported.
- Claim unavailable connector, runtime, network, or filesystem capabilities.
- Expand local capability work into broad cleanup without a separate maintenance scope.

---
