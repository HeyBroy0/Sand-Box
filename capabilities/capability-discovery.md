# Capability Discovery

**Status:** Initial operational draft for review.

Start with the task route and nearest owning component. Check the catalog when useful, then verify the actual implementation, documentation, tests, supported entrypoints, dependencies, and permissions before relying on a candidate.

Prefer extending an existing capability when its purpose and interface still fit. Create a separate capability only when its purpose, owner, interface, or lifecycle is meaningfully different.

Treat names, search results, and catalog entries as locators, not proof of availability. The current catalog is empty; do not claim that a capability is registered or operational until its implementation and contract have been checked.

For shared interfaces, check affected consumers and compatibility before changing them. Discovery does not grant permission to execute a capability.
