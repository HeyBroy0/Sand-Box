# DP and DP C — alignment review and proposed changes

Status: working analysis only. This file is a proposal for discussion and future adaptation. It does not authorize changes to `main`, and it does not establish new repository policy.

## Scope and handling

The source documents were read from `brnch-2/data/DP` and `brnch-2/data/DP C`. Exact working copies are stored beside this review as `DP` and `DP C`. Keep these source copies unchanged while experimenting with reorganizations here.

The eventual target is the scaffold on `T-brnch-1`. Any later adoption should be selective: DP C is explicitly intended to be decomposed into independently useful parts and partially rewritten, not mechanically copied as one large policy document.

## Overall assessment

The two documents are substantially aligned in intent. Both describe Sand-Box as a focused, evolving ChatGPT/Codex GitHub-connected workspace; favor a small always-read layer and progressive context; distinguish policy, authority, and technical enforcement; protect recovery; and discourage speculative architecture.

The main issue is not a conflict in direction. It is the density and presentation of the material. DP is a broad design record that mixes original principles, consolidated additions, new proposals, decision rules, architectural domains, branch guidance, and a directory tree. DP C is a cleaner topical consolidation, but still reads as a large all-in-one rulebook. If either is installed wholesale as mandatory instructions, it could produce the documentation burden and task friction the target design is meant to avoid.

## Alignment with the requested design

The following should guide the eventual rewrite:

- **Modular mash, not rigid decomposition.** Keep domains understandable, but do not require one directory, document, or subsystem per concept. Group related material when that is easier to use.
- **Small routing surface.** The root README and any short task router should answer where to start and where relevant guidance lives. They should not restate the full design.
- **Reachability over exhaustive navigation.** Important guidance must have a clear route from the entrypoint or relevant capability. Avoid deep navigation trees, repeated indexes, and mandatory cross-reading when a direct link is enough.
- **Progressive loading.** Load only the instructions needed for the task. A tool-design task should not have to absorb maintenance, telemetry, recovery, and branch-governance material unless those topics are actually implicated.
- **Lightweight instructions and guides.** Keep hard requirements short and unambiguous. Put rationale, options, examples, and deeper reference material in optional guides or notes.
- **Maintenance as the organizer.** Dedicated maintenance work can periodically remove duplication, repair links, consolidate scattered notes, and improve discoverability. Do not force every task to perform this cleanup as it works.
- **Explicit authority without blanket friction.** Preserve the distinction between ordinary work, core changes, improvement/promotion, destructive cleanup, and recovery. Apply the relevant boundary when the task touches it rather than loading every authority document for every task.
- **Composable DP C.** Treat each topic as a source module. Later adoption can retain, split, merge, shorten, rewrite, or omit individual sections while preserving provenance and intent.

## DP review

DP is valuable as the broad source of design intent. Its strongest contributions are:

1. A clear scope boundary around the connected GitHub workspace rather than a general agent platform.
2. A small always-read layer and progressive context loading.
3. Separation of mandatory requirements from explanatory guidance.
4. Composition, compatibility, and avoidance of speculative infrastructure.
5. Explicit distinction between connector access, execution environments, policy, authorization, and enforcement.
6. Independent recovery responsibility and protection of user material.
7. A useful set of architectural domains that explicitly do not require one-to-one directory mapping.

Recommended treatment:

- Retain DP as a source/reference document during this design phase; do not make the full document a mandatory read.
- Preserve the origin labels (original intent, consolidated additions, new proposals) when provenance matters, but do not carry that editorial structure into the final operational instruction layer.
- Extract only the durable, broadly applicable decisions into a short principles reference if that proves useful.
- Keep the detailed decision table and architectural-domain descriptions as optional reference material, or reduce them to a small set of practical heuristics.
- Remove duplicate restatements during any later rewrite. In particular, several principles are repeated in the later “Sand-box Design principles,” decision rules, domains, and branch-role sections.
- Treat proposed infrastructure such as telemetry collection, isolated execution, and branch enforcement as aspirations until implemented and verified.

## DP C review

DP C is better organized by topic and is a useful decomposition source. Its sections can be treated as candidate modules rather than one document:

| DP C section | Suggested future treatment |
| --- | --- |
| 1. Scope | Keep a very short workspace identity/scope statement near the entrypoint or core overview. |
| 2. Core architecture | Split only the durable core boundary from optional architecture explanation; keep the core router concise. |
| 3. Document writing | Convert into a lightweight documentation guide, not a universal pre-task checklist. |
| 4. Tool writing | Keep as a capability/tool-design guide loaded when creating or substantially changing tools. |
| 5. Navigation | Retain a few routing principles in the entrypoint; deeper discovery specifics belong with capability discovery. |
| 6. Protections, access and authority | Keep authority requirements concise and link to the relevant permission or change procedure. Explicitly distinguish documented policy from actual GitHub enforcement. |
| 7. Architecture | Keep as a compact conceptual map; do not force five domains into five matching directories. |
| 8. Recovery | Move operational requirements to recovery policy/procedures; keep only the preservation principle in the overview. |
| 9. Maintenance | Separate routine maintenance from improvement. Put actionable steps in the relevant maintenance documents. |
| 10. Telemetry | Keep as a future-facing design note until collection is technically available and authorized. Avoid implying that telemetry already exists. |
| 11. Workspace/tool use | Reduce to a few general operating expectations or place task-specific steps in capability guidance. |
| 12. Branch and promotion | Put actual branch/promotion rules in the applicable authority or improvement procedure; avoid duplicating them in broad principles. |
| 13. Decision rules | Keep a small set of high-value heuristics, not a second full policy layer. |
| 14. Overall principle | Use as a short summary, or omit if the entrypoint already communicates the same idea. |
| 15. Directory tree | Treat as a historical proposal, not a binding architecture. The current target scaffold is the active structural reference for this experiment. |

## Recommended modular shape

Use a small number of reachable clusters. This is a conceptual grouping, not a required directory blueprint:

1. **Entry and routing** — purpose, scope, where to start, and links to the few task-specific routes.
2. **Core and authority** — only durable shared constraints, authority boundaries, and the core-change route.
3. **Capabilities and tool creation** — discovery, capability contracts, tool design, testing, and integration. This should be the easiest path for an AI designing a tool to follow without reading unrelated governance.
4. **Maintenance and improvement** — routine cleanup versus substantive improvement, with verification and promotion guidance as needed.
5. **Recovery** — preservation, known-good points, and restoration.
6. **Optional reference material** — rationale, examples, architectural notes, future proposals, and design history.

These clusters may be combined or distributed across existing folders where that is simpler. Do not create a document merely to fill a slot in this list.

## Proposed lightweight rules

The eventual always-read layer should likely communicate no more than these ideas:

- Stay within Sand-Box's defined GitHub-workspace purpose.
- Start from the relevant entrypoint and follow only applicable links.
- Prefer existing capabilities and composition; create new structure only for a demonstrated need.
- Keep task work scoped and avoid duplicating authoritative rules.
- Respect authority boundaries for core changes, destructive actions, recovery, and promotion.
- Verify changes and preserve recoverability where the task could affect shared or valuable state.

Everything else should be pulled in only when the task needs it.

## Important tensions to resolve during later adoption

1. **Core protection versus flexibility:** protect the small set of truly shared contracts, but do not make every architectural or documentation adjustment a core-governance event.
2. **Self-contained tools versus minimal context:** a tool's own interface and usage contract should be self-contained; users should not need to load its entire development guide to invoke it.
3. **Canonical catalog versus low ceremony:** keep one discoverable source of capability metadata, but avoid adding schema or registration ceremony beyond what actual discovery and integration require.
4. **Reachability versus documentation sprawl:** links should make important material reachable without turning every document into a navigation hub.
5. **Automatic observability versus actual platform limits:** design for useful evidence, but do not mandate or claim collection that the connector/platform cannot provide.
6. **Branch principles versus repository reality:** branch naming and promotion rules must match the actual GitHub controls and workflows, not merely aspirational wording.

## Suggested next steps in this experimental branch

1. Keep `DP` and `DP C` unchanged as source copies.
2. Use this review to decide which DP C topics deserve independent parts.
3. Draft only the smallest useful set of rewritten modules, preserving links back to source sections where helpful.
4. Test the navigation with representative tasks: ordinary repository change, tool creation, documentation change, routine maintenance, core change, and recovery.
5. Check whether a tool-creation task can proceed with low context and without reading unrelated policy.
6. Only after the structure proves usable, consider proposing adoption into the eventual target branch. Nothing in this experiment should be treated as automatically approved for promotion.

## Non-goals

- Do not rewrite all of DP C in one pass.
- Do not create a mandatory instruction for every architectural domain.
- Do not mirror every conceptual domain as a directory.
- Do not add new registries, schemas, workflows, or telemetry systems merely because the source documents mention them.
- Do not promote any of these experimental files to `main` or treat them as final policy.
