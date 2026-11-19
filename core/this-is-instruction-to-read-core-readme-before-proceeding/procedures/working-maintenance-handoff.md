# Working-to-Maintenance Handoff

**Purpose:** Preserve useful local autonomy while ensuring that non-blocking organizational friction reaches Maintenance.

## Working responsibility

A Working task should complete its authorized contribution unless an observed issue blocks correctness, safety, or usability. It should not silently expand into repository-wide cleanup.

When non-blocking friction appears, record only enough context for later evaluation:
- The affected location or component.
- The observed friction or inconsistency.
- Why it matters to usability, correctness, ownership, reachability, or recurring effort.
- Any immediate workaround or dependency, if relevant.

Use an existing issue, backlog, maintenance note, or handoff mechanism when one exists. Do not invent a new tracking system for one observation. If no durable mechanism exists, report the deferred issue with the task result.

## Maintenance responsibility

Maintenance evaluates the observation against other demonstrated friction and chooses the lowest sufficient scope: Minimal, Alignment, or Improvement. A handoff is evidence for prioritization, not an automatic commitment to perform the work.

Maintenance may return a focused implementation task to Working. It should specify the outcome and relevant boundaries rather than impose unrelated organizational work.

## Shared boundaries

Working and Maintenance use the same security, authority, compatibility, preservation, and recovery boundaries. The handoff changes task ownership; it does not change permissions.
