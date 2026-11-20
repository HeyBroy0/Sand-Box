# Core README — protected workspace guidance

**Status:** Proposed draft for review; not yet adopted as authority. This document does not itself grant permissions or create technical controls.


**Purpose:** Define the entrypoint for core-owned identity, policy, architecture, authority, and protected procedures.

This document is not the repository's always-read entrypoint. Start with the [root README](../../README.md) for ordinary routing. Read this file when the task touches core, authority, shared contracts, protected documents, or a change that can affect repository-wide behavior.

## Core responsibilities

Core owns durable workspace identity, adopted principles, architecture, configuration, authority definitions, protected standards, and procedures for changing or preserving those surfaces. Core does not own every operational guide: externally owned documents remain at their operational destinations.

## Reading routes

| Need | Read |
|---|---|
| Choose the relevant architecture context by task | [Architecture task index](architecture/architecture.md) |
| Understand repository areas and their boundaries | [Repository map](architecture/repository-map.md) |
| Identify canonical document owners and preserved copies | [Document ownership](architecture/document-ownership.md) |
| Determine whether a change is protected | [Change gate](standards/change-gate.md) |
| Understand core principles | [Principles](standards/principles.md) |
| Determine actual permission and authorization boundaries | [Permission model](../authority/permission-model.md) |
| Find current task procedures and implementation status | [DP-C procedure register](procedures/DP-C.md) |
| Apply a protected change | [Protected-change procedure](procedures/protected-change.md) |
| Preserve an externally owned document in core | [Core document preservation](procedures/core-document-preservation.md) |
| Understand document roles and lifecycle | [Document lifecycle](standards/document-lifecycle.md) |
| Find historical procedure records | [Procedure Record Index](procedures/documents/procedure-record-index.md) |
| Find preserved external documents | [Preservation Index](procedures/documents/preservation-index.md) |

## Boundaries

- Root README routes ordinary work. Core README routes core-specific work.
- Working and Maintenance are task responsibilities, not separate technical permission systems.
- A written rule does not prove that GitHub, a connector, or an execution environment technically enforces it.
- Read only the authority and procedure sources relevant to the affected surface.
- Preserve source ownership: operational documents remain at their canonical owner; core copies are explicitly historical or protected records.
- A proposed document or draft is not adopted authority until the responsible approval process says so.

When authority, source ownership, or the required change path is unclear, stop the protected edit and record the unresolved decision rather than silently creating a new rule.
