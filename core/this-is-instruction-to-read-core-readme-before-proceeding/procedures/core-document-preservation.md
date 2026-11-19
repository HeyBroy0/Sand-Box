# Core Document Preservation Procedure

**Purpose:** Preserve selected externally owned operational documents in core without creating a second current source of instructions.

## When preservation is appropriate

Preserve an external document when it is designated as important to core history, repository-wide governance, architectural understanding, or the ability to review how an operational rule developed. Do not copy every local guide automatically.

## Preservation requirements

A preserved copy must:
- Identify itself clearly as a core-preserved historical record.
- Name its operational source using a repository-relative path.
- Record the source revision or capture date when known.
- Retain the captured source content without silently rewriting its requirements.
- Distinguish draft, proposed, adopted, and superseded status as shown by the source.
- Be indexed in `procedures/documents/preservation-index.md`.

## Procedure

1. Confirm the operational source and its owner.
2. Confirm that core preservation is warranted and that the copy does not create competing authority.
3. Capture the source content. Add a preservation header outside the captured content; do not edit its substantive text merely to make it resemble a core standard.
4. Record the source path, source revision or date, and status in the preservation header and index.
5. Check that the preserved copy is complete and that its source path resolves.
6. Keep ordinary task routes pointed to the operational source. The preserved copy may link outward to the source; the operational source must not link back to the preserved copy solely for provenance.
7. When the operational source changes, compare the new version with the preserved record. Create a new deliberate capture or update the record only through an authorized preservation decision. Do not silently synchronize it.

## Boundaries

- A preserved copy is not a backup of the whole repository and does not replace recovery manifests or version history.
- A preserved draft remains a draft; preservation does not adopt it.
- Core-native authority documents do not need a second preserved copy under this directory.
- Generated composites are regenerated from their declared inputs and are not preservation inputs unless explicitly designated.
