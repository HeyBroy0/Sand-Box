# Architecture — Recovery, Observability, and Evolution

**Status:** Proposed architecture reference, pending review and adoption.

**Use when:** A task involves destructive or difficult-to-reverse work, evidence collection, improvement suggestions, or promotion of shared changes.

## Recovery

Recovery is independent from routine Maintenance. Its preservation and restoration responsibilities include known-good states, important source material, repository history, manifests, and restoration options.

- Preservation policy defines what must be retained and under what conditions.
- Recovery procedures define how preservation or restoration is performed.
- Manifests and records identify the relevant recovery state and references.
- Verify the recovery source and its usability; do not assume a backup, snapshot, manifest, or rollback path exists.
- Maintenance may identify a recovery need or request restoration, but must not silently erase, invalidate, or redefine recovery records.

Destructive or difficult-to-reverse work requires an appropriate preservation and recovery assessment before execution. Follow the Recovery authority and operational recovery material.

## Observability

Keep three information stages distinct:

1. **Collection** captures authorized raw events through a real, supported mechanism.
2. **Analytics** derives patterns and evidence from collected records.
3. **Suggestions** records reviewable maintenance or improvement opportunities.

Collection requires a defined purpose, minimized data scope, authorization, access, retention, and failure behavior. Evidence informs decisions; it does not authorize repository changes. A deterministic automation suggestion does not itself authorize tool development.

## Promotion and evolution

Local contributions can be useful before global normalization. Maintenance may integrate proven patterns, repair cross-component fit, or recommend improvements when recurring use or friction demonstrates a need.

Shared or protected changes require explicit authorization and proportionate verification. Stable promotion should represent a coherent, verified workspace under the repository's actual branch and protection controls. Do not claim that branch protection, required checks, or isolation exists without inspecting the enforcing system.

## Related architecture references

- [Maintenance and Change Boundaries](maintenance-and-change-boundaries.md) — responsibility and authority boundaries.
- [Document Ownership and Lifecycle](document-ownership-and-lifecycle.md) — preservation and source lifecycle.
