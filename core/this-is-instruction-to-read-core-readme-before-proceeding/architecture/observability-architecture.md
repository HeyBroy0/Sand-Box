# Architecture — Observability and Feedback

**Status:** Proposed architecture reference, pending review and adoption.

**Use when:** A task concerns evidence collection, analytics, recurring friction, or reviewable improvement suggestions.

## Information flow

Keep three stages distinct and connected:

1. **Collection** captures authorized raw events through a real, supported mechanism.
2. **Analytics** derives patterns and evidence from collected records.
3. **Suggestions** records reviewable maintenance or improvement opportunities.

The flow is:

```text
Supported activity
    |
    v
Authorized collection
    |
    v
Analytics and pattern review
    |
    v
Suggestions for human or governed review
    |
    v
Authorized Maintenance or Improvement task
```

## Process boundaries

- Collection needs a defined purpose, minimized data scope, authorization, access, retention, and failure behavior.
- Analytics must distinguish measured evidence from estimates, assumptions, and missing data.
- Suggestions are proposals for review, not task authorization or implementation instructions.
- A deterministic automation suggestion does not itself authorize tool development.
- Evidence does not grant permission to change repository content or capability interfaces.

Do not merge raw collection, derived analysis, and suggestions into one undifferentiated store or process. Their purposes, data needs, retention, and review responsibilities differ.

## Operational status

Verify that collection mechanisms, analytics, and suggestion records actually exist before describing them as active. See the operational collection guide and the owning analytics or suggestions materials.

## Related architecture references

- [Responsibilities and Routing](responsibilities-and-routing.md) — task routes and handoffs.
- [Maintenance and Change Boundaries](maintenance-and-change-boundaries.md) — how evidence can inform authorized maintenance.
- [Recovery Architecture](recovery-architecture.md) — preservation is separate from ordinary evidence retention.
