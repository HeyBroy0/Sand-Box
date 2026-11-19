# Procedure Navigation

**Purpose:** Route each task procedure to its current operational source and its preserved reference record.

Use the root README to select a task. The numbered records and generated full reference preserve detailed procedure text for review; routine work should follow the operational-source links below.

| No. | Task | Operational route | Preserved record | Full reference |
|---|---|---|---|---|
| 01 | Working Environment | Nearest owning component and its local instructions; begin at [root README](../../../../README.md) | [procedure01.md](procedure01.md) | [Procedure 01](full-procedures.md#procedure-01--working-environment-feature-creation-and-ordinary-task-work) |
| 02 | Maintenance Environment | [Minimal](../../../../maintenance/minimal-maintenance/minimal.md), [Alignment draft](../../../../maintenance/alignment-maintenance/alignment.md), [Improvement](../../../../maintenance/improvement/improvement.md) | [procedure02.md](procedure02.md) | [Procedure 02](full-procedures.md#procedure-02--maintenance-environment-organization-and-alignment) |
| 03 | Core and Sensitive Changes | [Core README](../../core-readme.md), [Protected Change](../protected-change.md), [Change Gate](../../standards/change-gate.md), [Permission Model](../../../authority/permission-model.md) | [procedure03.md](procedure03.md) | [Procedure 03](full-procedures.md#procedure-03--core-authority-and-sensitive-changes) |
| 04 | Capability and Tool Work | [Capability discovery](../../../../capabilities/capability-discovery.md) and the owning capability | [procedure04.md](procedure04.md) | [Procedure 04](full-procedures.md#procedure-04--capability-and-tool-work) |
| 05 | Document Creation and Editing | [Document review](../../../../capabilities/documentation-Tree/document-look.md), [Document creation](../../../../capabilities/documentation-Tree/document-creation.md), [Lifecycle standard](../../standards/document-lifecycle.md) | [procedure05.md](procedure05.md) | [Procedure 05](full-procedures.md#procedure-05--document-creation-and-editing) |
| 06 | Workspace Access and Operations | [Permission Model](../../../authority/permission-model.md), [Workspace Authority](../../../authority/workspace.md) | [procedure06.md](procedure06.md) | [Procedure 06](full-procedures.md#procedure-06--workspace-access-and-operations) |
| 07 | Recovery and Preservation | [Recovery Authority](../../../authority/recovery-authority.md), [recovery policies](../../../../recovery/policies/), [recovery procedures](../../../../recovery/procedures/), [recovery manifests](../../../../recovery/manifests/) | [procedure07.md](procedure07.md) | [Procedure 07](full-procedures.md#procedure-07--recovery-and-preservation) |
| 08 | Observability and Improvement Evidence | [Collection guide](../../../../observability/collection/README.md), [Analytics](../../../../observability/analytics/), [Suggestions](../../../../observability/suggestions/) | [procedure08.md](procedure08.md) | [Procedure 08](full-procedures.md#procedure-08--observability-and-improvement-evidence) |
| 09 | Navigation and Capability Discovery | [root README](../../../../README.md), [Repository Map](../../architecture/repository-map.md), [Document Ownership](../../architecture/document-ownership.md), [Capability discovery](../../../../capabilities/capability-discovery.md) | [procedure09.md](procedure09.md) | [Procedure 09](full-procedures.md#procedure-09--navigation-and-capability-discovery) |

## Source and preservation rules

- Operational-source links are the normal task destinations.
- The numbered procedure files are core-preserved historical records of detailed DP-C procedure text from the working draft.
- The full reference is generated from procedure01.md through procedure09.md by [generate_full_procedures.py](../../../../capabilities/scripts/generate_full_procedures.py). Do not edit it manually.
- Run the generator with `--check` to verify that the composite matches its inputs.
- This navigation file identifies routes; it does not grant permissions or replace core authority documents.
- Core-preserved copies of externally owned maintenance and capability documents are listed in [preservation-index.md](preservation-index.md).
