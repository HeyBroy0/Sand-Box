# Document Lifecycle Standard

**Status:** Proposed core standard, pending explicit adoption.

## Document classes

### Operational source
The canonical maintained document used for current work. It belongs with the component or responsibility that owns the subject. Ordinary task routes should point here.

### Core-preserved copy
A deliberate historical capture of an externally owned operational source. It records a source path and capture point, remains clearly labeled as historical, and does not become a second current authority.

### Core-native source
A document whose canonical owner is core because it defines repository-wide identity, authority, architecture, standards, or protected procedures.

### Generated composite
An output mechanically assembled from explicit source inputs. It is not edited manually; update its inputs and regenerate it. Generation should fail visibly when required inputs are missing or inconsistent.

### Navigation document
A concise map to sources and sections. It identifies task triggers and destinations without duplicating full instructions.

### Working draft or proposal
Material under development that has not been adopted as an operational requirement or authority. Its status must remain visible, and routes must not present it as adopted policy.

## Lifecycle requirements

1. Each operational source has one identifiable owner.
2. Shared mandatory rules have one canonical authority.
3. Core-preserved copies identify their operational source and capture state.
4. Generated composites identify their inputs and generation method.
5. Navigation routes ordinary work to operational sources, not historical or generated copies.
6. Status changes from proposal to adoption require an explicit decision by the responsible authority.
7. Deletion, replacement, or supersession follows applicable preservation and recovery rules.
8. Links and indexes are updated when ownership or paths change.

## Source direction

A core-preserved copy may point outward to its operational source. The operational source should not link back to its preserved copy merely to establish provenance. Core-native sources are linked directly and are not duplicated under the preserved-copy directory.
