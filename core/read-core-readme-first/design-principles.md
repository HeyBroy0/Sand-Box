# Core design principles

Read this document when defining, evaluating, or changing Sand-Box's architectural principles. For an implementation or documentation change that touches a core surface, start with the [Core documentation router](core-readme.md) and follow the core-change gate as well.

1. **Keep the always-read layer small.** The root README and root agent entrypoint are navigation surfaces, not encyclopedias.
2. **Load instructions progressively.** Read only the task-specific instructions and their relevant dependencies; do not preload every file under `core/`.
3. **Separate requirements from explanation.** Instructions state applicable requirements and constraints. Guides explain procedures, examples, and reference material. Link between them instead of blending them indiscriminately.
4. **Keep core small and durable.** Core contains repository-wide rules and cross-capability contracts. Everyday implementations belong in `scripts/`, workflows in `.github/workflows/`, and capability metadata in `tools/catalog.json`.
5. **Prefer composition over duplication.** Reuse or extend an existing capability when its interface can be extended cleanly; create a separate capability only when it has a distinct purpose or interface.
6. **Preserve compatibility deliberately.** Before changing a shared contract, find its consumers and update the affected callers, workflows, tests, catalog references, and documentation together.
7. **Avoid speculative infrastructure.** Do not add a framework, registry, instruction layer, abstraction, or schema field without a concrete recurring use case.
8. **Keep documentation actionable.** State when a document applies, what it requires, and where to go next. Put task-specific procedures in separately loaded documents when that improves routing; do not copy full manuals into core instructions.
9. **Prefer the smallest coherent structure.** Split documents or create directories only when distinct tasks can benefit from loading the resulting parts independently. Do not add organizational layers merely to anticipate hypothetical future needs.
