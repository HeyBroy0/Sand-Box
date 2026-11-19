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

## Cross-procedure decision tests

| Question | Default |
|---|---|
| Is the task to create a feature or complete an ordinary local change? | Use Working and the nearest owning component; load only relevant specialist guidance. |
| Is the main outcome improved repository coherence? | Use Maintenance and select the lowest sufficient scope. |
| Does every new feature require repository-wide organization first? | No. Working may make reasonable local decisions and defer non-blocking normalization. |
| Is Maintenance an approval gate for ordinary Working tasks? | No. Maintenance organizes accumulated work; it does not pre-approve each contribution. |
| May Working ignore a directly relevant rule or shared contract? | No. Local autonomy does not override applicable requirements or protected boundaries. |
| Should Working create a navigation hub? | Normally no. Use existing routes and hand broad hub work to Maintenance. |
| What if a broader issue appears during a feature task? | Complete the authorized work unless the issue blocks correctness or safety; route non-blocking friction to Maintenance. |
| Can Working or Maintenance change core or authority automatically? | No. Explicit authorization and the protected-change procedure still apply. |
| Can Maintenance delete original source material because a consolidated copy exists? | No. Follow preservation and recovery requirements. |
| Must every local document and tool use one format? | No. Align only when it improves usability, ownership, reachability, or maintenance. |
| Are Working and Maintenance technical permission boundaries? | No. Actual permissions and enforcement come from the relevant services and execution systems. |

## Operating rule

Route each task to the smallest useful set of instructions and the correct operational owner. Local creation should remain practical; Maintenance should make accumulated work coherent; protected changes should follow their authority process; historical records should preserve rather than compete with operational sources.
