# Repository Map

**Status:** Proposed core architecture reference, pending review and adoption. Update through the protected-change process when repository ownership or major boundaries change.

## Top-level responsibilities

| Area | Responsibility | Typical contents |
|---|---|---|
| `core/` | Durable identity, principles, architecture, authority, protected procedures, and preserved records | Standards, authority definitions, core procedures, protected historical copies |
| `maintenance/` | Ongoing coherence of accumulated workspace material | Minimal, Alignment, and Improvement maintenance guides |
| `recovery/` | Preservation and restoration independent from routine cleanup | Policies, procedures, manifests |
| `capabilities/` | Reusable tools, scripts, workflows, tests, discovery, and capability documentation | Catalog, discovery guide, implementations, document-writing guides |
| `observability/` | Authorized evidence, analysis, and reviewable suggestions | Collection, analytics, suggestions |
| `temp/` | Temporary working material | Short-lived files with an explicit cleanup/recovery consideration |
| `data/` | Active intake for source documents and other inputs to repository work | User-provided files to be processed, edited, analyzed, or otherwise worked on through repository tasks and capabilities |
| `reports/` | Durable task or system reports when required | Reports and review outputs |
| `.github/` | GitHub-native repository configuration | Workflows, CODEOWNERS, repository automation |

## Ownership rules

1. The directory closest to the responsibility normally owns the operational source.
2. Core owns shared authority and the rules that govern protected changes; it does not automatically own every guide that core references.
3. Maintenance owns repository-wide organization and alignment, while each component retains its useful local organization.
4. Capability implementations and their operational documentation belong under `capabilities/` or the relevant component owner.
5. Recovery records and authority remain separate from routine maintenance.
6. `data/` is the active intake area for user-provided documents and other source inputs to be worked on from the repository. Add input material here, then use the relevant task route or capability to work on it. Files left in `data/` from initial repository construction are proposal/design artifacts, not current operational instructions or canonical sources. Do not use them as governing guidance unless a task explicitly identifies them as source material. Put maintained instructions and durable outputs with their owning component, not in `data/`.
7. A preserved copy under core does not change the operational owner.

This map is intentionally high-level. Use [document ownership](document-ownership.md) for source-level routing and the root README for task selection.
