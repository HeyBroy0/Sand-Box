# Document Ownership and Source Registry

**Status:** Proposed draft for review; not yet adopted as authority. This document does not itself grant permissions or create technical controls.


**Purpose:** Identify where current operational documents live and how core-preserved copies relate to them.

## Ownership model

- **Operational source:** The maintained document that current task work should follow. It lives with the component or responsibility that owns the work.
- **Core-preserved copy:** A protected record of an externally owned source at a particular point in time. It is not a competing current instruction.
- **Core-native source:** A document whose canonical owner is core, such as an authority model, standard, or protected-change procedure.
- **Generated composite:** A mechanically assembled reference produced from declared inputs. Edit the inputs, not the output.
- **Navigation document:** A route to sources, sections, or artifacts. It should not replicate their contents.

## Current source routes

| Subject | Operational source | Core-preserved copy or core-native reference |
|---|---|---|
| Minimal Maintenance | `maintenance/minimal-maintenance/minimal.md` | `core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preserved/maintenance/minimal.md` |
| Alignment Maintenance | `maintenance/alignment-maintenance/alignment.md` | `core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preserved/maintenance/alignment.md` |
| Improvement Maintenance | `maintenance/improvement/improvement.md` | `core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preserved/maintenance/improvement.md` |
| Capability discovery | `capabilities/capability-discovery.md` | `core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preserved/capabilities/capability-discovery.md` |
| Document look and review | `capabilities/documentation-Tree/document-look.md` | `core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preserved/capabilities/documentation-Tree/document-look.md` |
| Document creation | `capabilities/documentation-Tree/document-creation.md` | `core/this-is-instruction-to-read-core-readme-before-proceeding/procedures/documents/preserved/capabilities/documentation-Tree/document-creation.md` |
| Architecture task index and modules | `core/this-is-instruction-to-read-core-readme-before-proceeding/architecture/architecture.md` and its linked task references | Core-native; linked through the architecture task index |\n| Core principles | `core/this-is-instruction-to-read-core-readme-before-proceeding/standards/principles.md` | Core-native; no duplicate preservation copy |
| Change gate | `core/this-is-instruction-to-read-core-readme-before-proceeding/standards/change-gate.md` | Core-native; no duplicate preservation copy |
| Permission model | `core/authority/permission-model.md` | Core-native; no duplicate preservation copy |
| Maintenance authority | `core/authority/maintenance-authority.md` | Core-native; no duplicate preservation copy |
| Recovery authority | `core/authority/recovery-authority.md` | Core-native; no duplicate preservation copy |
| Workspace authority | `core/authority/workspace.md` | Core-native; no duplicate preservation copy |

## Change control

When an operational source changes, do not silently rewrite its preserved copy. Record the source revision and decide whether a new preserved version is required. Update this registry and the preservation index when ownership or preserved paths change.

Repository-relative paths are authoritative for these references. Verify them when moving or renaming files.
