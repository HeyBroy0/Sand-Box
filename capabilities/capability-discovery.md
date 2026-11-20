# Capability Discovery

**Status:** Initial operational draft for review.

Start with the task route and nearest owning component. Check the catalog when useful, then verify the actual implementation, documentation, tests, supported entrypoints, dependencies, and permissions before relying on a candidate.

Prefer extending an existing capability when its purpose and interface still fit. Create a separate capability only when its purpose, owner, interface, or lifecycle is meaningfully different.

Treat names, search results, and catalog entries as locators, not proof of availability. The catalog at `capabilities/catalog.json` indexes the initial imported capability set. Verify the implementation, tests, workflow, dependencies, and permissions before relying on a candidate. Run `python capabilities/scripts/find_tool.py --validate` to check the catalog, then search with `python capabilities/scripts/find_tool.py "your search terms"`.

For shared interfaces, check affected consumers and compatibility before changing them. Discovery does not grant permission to execute a capability.
