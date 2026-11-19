# Part 4 — Capability and tool discovery

**Intended destination:** **capabilities/** for implementations, scripts, tools, tests, workflows, and canonical discovery metadata as applicable.

**Applies when:** Adding, extending, integrating, testing, or documenting a reusable capability. This is normally Working work unless the requested outcome is broader capability alignment or integration, in which case use the appropriate Maintenance scope too.


## Tool discovery and selection

**Applies when:** Someone needs to find, choose, or use an existing tool, connector, integration, or execution surface. This is distinct from building a new reusable capability.

1. **Describe the operation, not a presumed product.** Identify what must be done, what system or data it touches, and whether it needs reading, writing, execution, or external access.
2. **Inspect the tools actually available in the current environment.** Consider native ChatGPT tools, connected GitHub actions, connected plugins, and any available Codex or local execution surface. Do not assume a tool is connected merely because it exists as a product.
3. **Choose the narrowest suitable action.** Prefer a directly available action when it supports the required operation and authority. Check its actual description, inputs, limits, and permissions.
4. **Do not treat repository work as automatically Codex-only.** GitHub connector actions may be sufficient for supported repository API operations such as reading or searching files, creating or updating files, and working with supported branches, issues, pull requests, or workflow records. Use Codex or another execution environment when the task genuinely requires a working tree, shell commands, local filesystem access, builds, or test execution that the connector does not provide.
5. **If the required tool is not obvious, search the available tool/capability documentation.** Do not invent tool names, claim unavailable access, or ask for a different connection before checking the current surfaces.
6. **If no suitable tool is available, state the specific gap.** Use a supported alternative when practical, or explain what connection, permission, or execution capability is missing. Do not build a new capability merely to avoid identifying an existing tool.
7. **Return to the task route.** After selecting or connecting the tool, continue the task under Part 6 and the applicable Working or Maintenance procedure.

A task may begin before its tool requirements are known. Tool discovery can therefore occur either before execution or as soon as a capability gap becomes apparent during the task.

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