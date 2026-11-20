# Architecture — Maintenance and Change Boundaries

**Status:** Proposed architecture reference, pending review and adoption.

**Use when:** Aligning related components, changing shared behavior, repairing cross-document routes, or deciding when routine maintenance reaches a protected boundary.

## Graduated alignment

Alignment effort grows with the number of affected owners and the sensitivity of the surface. The size of the repository alone does not determine the required context.

### Local component boundary

Use the nearest owner, local conventions, direct dependencies, and proportionate checks. Do not run a repository-wide review for an ordinary local contribution or a bounded local correction.

### Shared or cross-component boundary

Before changing shared behavior, identify:
- The canonical owner and applicable operational guidance.
- Direct consumers, interfaces, workflows, and dependent documents.
- Compatibility, naming, placement, and discovery routes.
- Tests and verification required by affected consumers.

Inspect the affected connection paths, not every unrelated component.

### Protected Core boundary

Principles, architecture, authority, root entrypoints, shared routes, and cross-repository contracts require the protected-change route. Before editing:
- Identify the precise protected surface and its consumers.
- Read the relevant architecture reference and applicable authority or standard.
- Consult principles only when the change concerns a principle, exposes a conflict, or the protected-change procedure requires it.
- Confirm explicit authorization through the applicable process.
- Check compatibility, preservation, recovery, and migration implications.
- Verify actual service controls rather than relying on written guidance.

Stop when authority, source status, impact, or required recovery is unclear. Maintenance responsibility does not grant authority over Core or Recovery.

## Maintenance scopes

These are selectable scopes, not mandatory sequential stages.

- **Minimal Maintenance** corrects one bounded local defect while preserving the existing organization.
- **Alignment Maintenance** restores coherence across related documents, components, ownership, processes, and navigation.
- **Improvement Maintenance** integrates a broader capability, workflow, interface, or design change when demonstrated need justifies it.

Use the smallest scope that resolves the actual friction. Maintenance is not an approval gate for ordinary Working tasks.

## Alignment decision tests

| Question | Direction |
|---|---|
| Is the defect local and bounded? | Use Minimal Maintenance; preserve surrounding organization. |
| Are several related sources or routes inconsistent? | Use Alignment Maintenance; trace their ownership and connections. |
| Does the problem require a new shared capability or interface? | Evaluate Improvement Maintenance using demonstrated need and lifecycle cost. |
| Does the change affect a protected Core surface? | Stop routine maintenance and follow the protected-change route. |
| Does the change affect recovery records or restoration? | Involve the Recovery owner; Maintenance must not redefine or invalidate recovery authority. |
| Is a new hub, directory, registry, or abstraction proposed? | Require a concrete navigation, ownership, or lifecycle benefit that exceeds its recurring cost. |

## Evolution and promotion

Local contributions can be useful before global normalization. Maintenance may integrate proven patterns, repair cross-component fit, or recommend improvements when recurring use or friction demonstrates a need.

Shared or protected changes require explicit authorization and proportionate verification. Stable promotion should represent a coherent, verified workspace under the repository's actual branch and protection controls. Do not claim branch protection, required checks, or isolation exists without inspecting the enforcing system.

## Related architecture references

- [Responsibilities and Routing](responsibilities-and-routing.md) — task boundaries and handoffs.
- [Document Ownership and Lifecycle](document-ownership-and-lifecycle.md) — canonical source, status, and preservation checks.
- [Capability Architecture](capability-architecture.md) — shared capability and interface boundaries.
- [Recovery Architecture](recovery-architecture.md) — preservation and restoration boundaries.
- [Observability Architecture](observability-architecture.md) — evidence and improvement feedback.
