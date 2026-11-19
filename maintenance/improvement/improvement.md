# Improvement Maintenance

**Purpose:** Evaluate and integrate broader improvements when a concrete need or demonstrated use justifies changes beyond documentation alignment.

## Use Improvement Maintenance when

- A recurring problem needs a capability, integration, or shared implementation change.
- Proven local patterns should be integrated into a reusable workspace capability.
- A cross-component issue cannot be resolved by clarifying ownership, wording, or navigation alone.
- A shared interface or architecture needs a justified evolution.

## Evidence and scope

Prefer demonstrated use, repeated demand, measurable friction, successful trials, or a clear reduction in operational cost. Treat speculative ideas as proposals, not implementation commitments.

Before beginning, identify:
- The problem and evidence supporting the change.
- Affected components, users, interfaces, and consumers.
- The smallest viable implementation and reasonable alternatives.
- Dependencies, permission needs, failure behavior, and lifecycle costs.
- Required authorization, compatibility, and verification.

## Working method

1. Confirm that Minimal or Alignment Maintenance cannot solve the actual problem.
2. Define the intended improvement and the evidence by which it can be evaluated.
3. Inspect the affected capability and its direct consumers.
4. Prefer extending a suitable existing capability over duplicating it.
5. Keep implementation, workflow integration, and documentation responsibilities clear.
6. Use least privilege and protect sensitive data.
7. Verify normal behavior, relevant failures, and affected consumers proportionately.
8. Record unresolved risks, rollout needs, or follow-up work.

## Boundaries

Improvement Maintenance is not permission for speculative frameworks, broad rewrites, or unrequested architectural expansion. Changes to core, authority, protected entrypoints, or shared contracts still require the applicable protected-change authorization. A maintenance suggestion does not itself authorize implementation.
