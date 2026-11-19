# Observability Collection

**Purpose:** Hold the design and documentation for authorized raw activity collection, if and when a supported collection mechanism is established.

## Current status

No active collection mechanism is defined by this directory alone. The existence of this folder does not mean repository activity is being monitored or telemetry is available.

## Before adding a collector

Document and verify:
1. The concrete purpose and decisions the data is intended to support.
2. The exact events and fields to be collected, with a data-minimization rationale.
3. Authorization, access roles, retention, deletion, and review boundaries.
4. Treatment of credentials, personal information, private user content, and other sensitive data.
5. The actual collection mechanism, execution location, failure behavior, and verification method.
6. The route from raw records to analytics, with raw collection kept separate from interpretation and suggestions.

Prefer structured records over repeated narrative reporting only when a supported mechanism provides durable value. Do not collect data speculatively, and do not claim a collector is active until its implementation and permissions have been verified.

## Related routes

- `observability/analytics/` — derived analysis and patterns.
- `observability/suggestions/` — reviewable improvement opportunities.
- [DP-C Procedure 08](../../data/DP-C-v3%20Edit.md#procedure-08--observability-and-improvement-evidence) — task-level routing.
