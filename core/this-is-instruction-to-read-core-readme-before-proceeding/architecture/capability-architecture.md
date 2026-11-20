# Architecture — Capability Architecture

**Status:** Proposed architecture reference, pending review and adoption.

**Use when:** Discovering, creating, extending, integrating, or maintaining reusable tools, scripts, workflows, and other capabilities.

## Capability contract

A reusable capability should have a defined purpose and, where relevant, clear:
- Inputs and outputs.
- Supported entrypoints and usage.
- Defaults and dependencies.
- Limitations and failure behavior.
- Permissions and data boundaries.
- Verification and ownership.

A catalog entry or filename is a locator and declaration, not proof that the implementation works or is supported. Verify the implementation, documentation, tests, workflow, dependencies, and permissions before relying on it.

## Composition

- Discover before duplicating.
- Extend an existing capability when its purpose and interface still fit.
- Create a separate capability when purpose, owner, interface, or lifecycle is meaningfully different.
- Keep reusable logic in the owning implementation.
- Keep workflows and connector-facing surfaces thin: inputs, permission boundary, invocation, outputs, and clear failure reporting.
- Update catalog metadata, documentation, tests, and entrypoints only where the actual contract requires it.

## Compatibility

Before changing a shared capability or interface, identify its consumers, supported entrypoints, catalog references, workflow callers, tests, and documentation. Prefer compatible extensions when practical. When a breaking change is justified, account for migration and consumer verification.

## Discovery route

Start at the root README and relevant DP-C procedure. Use [Capability Discovery](../../../capabilities/capability-discovery.md), then inspect only the matching catalog entry and its actual implementation, supported entrypoint, tests, and dependencies.

## Related architecture references

- [Responsibilities and Routing](responsibilities-and-routing.md) — where capability work sits in task routing.
- [Maintenance and Change Boundaries](maintenance-and-change-boundaries.md) — shared interfaces and protected boundaries.
