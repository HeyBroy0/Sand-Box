<!--
Core-preserved procedure record 08.
Source draft: data/DP-C-v3 Edit.md
Current operational route: observability/collection/; observability/analytics/; observability/suggestions/.
Captured: 2026-11-19
Status: historical procedure reference; use DP-C and procedure-navigate.md for current task routing.
-->

# Procedure 08 — Observability and improvement evidence

**Intended destination:** **observability/collection/**, **observability/analytics/**, and **observability/suggestions/**.

**Applies when:** Designing, operating, or reviewing mechanisms that record workspace activity or turn evidence into maintenance suggestions.

### Separate the information lifecycle

- **Collection:** Raw events or activity records captured by a real, authorized mechanism.
- **Analytics:** Derived patterns such as usage, dependencies, or navigation friction.
- **Suggestions:** Persistent, reviewable opportunities for maintenance or improvement.

### Guidance

1. Use automatic structured collection rather than manual self-reporting when a technically supported and authorized mechanism provides real value.
2. Define purpose, data scope, access, and retention boundaries before collecting information.
3. Collect only what is needed; protect credentials, sensitive content, and user material.
4. Keep raw events distinct from interpretation and proposed changes.
5. Make suggestions evidence-based and reviewable; telemetry does not itself authorize repository changes.
6. Verify that a collection or analytics mechanism exists before describing it as operational.

Do not add telemetry speculatively or impose reporting overhead that creates no durable information.

### Deterministic automation suggestions

When collection, analytics, or maintenance work reveals a repeated mechanical action, preserve the opportunity under observability/suggestions/ rather than requiring Maintenance to create a tool.

A suggestion should describe the current sequence, repeat frequency, deterministic inputs and outputs, users, likely savings in context/tokens and manual/tool steps, verification and error reduction, dependencies, permission needs, failure behavior, and ongoing cost. Distinguish measured evidence from estimates. A suggestion records an opportunity; it does not authorize implementation.

---
