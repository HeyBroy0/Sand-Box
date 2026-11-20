# Architecture — Recovery

**Status:** Proposed architecture reference, pending review and adoption.

**Use when:** A task is destructive, difficult to reverse, involves preservation, or requires rollback or restoration.

## Responsibility

Recovery governs preservation of known-good states, important source material, repository history, manifests, and restoration options. It remains independent from routine Maintenance.

## Distinct recovery processes

- **Policy** defines what must be preserved and under what conditions.
- **Procedure** defines how a preservation or restoration operation is carried out.
- **Manifest or record** identifies a recovery state, source, or reference.

Keep these responsibilities connected but distinct. A policy is not an execution procedure; a manifest is not proof that the referenced state is usable.

## Maintenance boundary

- Maintenance may identify a recovery need or request restoration.
- Maintenance must not silently erase, invalidate, or redefine recovery records or authority.
- Age, inactivity, or absence from a quick search is not sufficient reason for deletion.
- Before destructive or difficult-to-reverse work, identify the affected material, known-good state, applicable retention requirements, and required authorization.
- Verify that the recovery source and restoration path actually exist and are usable. Do not assume backups, snapshots, manifests, or rollback options exist.

Recovery authority is not conferred by ordinary repository write access. Follow the Recovery authority and operational policies and procedures.

## Related architecture references

- [Document Ownership and Lifecycle](document-ownership-and-lifecycle.md) — operational versus preserved source.
- [Maintenance and Change Boundaries](maintenance-and-change-boundaries.md) — authority and scope boundaries.
