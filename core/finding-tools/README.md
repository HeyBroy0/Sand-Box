# Finding an existing tool

Use this guide when asked to find a capability, choose an existing workflow, or decide whether the repository needs another tool.

## Search the capability catalog first

The catalog is the fast index. Search by the user's goal, common synonyms, file type, or operation:

```bash
python scripts/find_tool.py "spreadsheet profiling"
python scripts/find_tool.py "zip archive"
python scripts/find_tool.py "export document" --kind workflow
python scripts/find_tool.py --tag files --tag export
python scripts/find_tool.py --format json
```

A catalog record groups related entrypoints under one capability. Check its summary, aliases, tags, and every listed script/workflow path. Do not mistake multiple entrypoints for multiple tools.

## Verify the match

Before selecting or extending a result:

1. Open the exact script or workflow path from the catalog on the active target ref.
2. Read the relevant help text, inputs, outputs, and limitations; do not load every file in the repository.
3. Inspect nearby tests and any workflow that wraps the script.
4. Check whether another existing capability already covers part of the task.

Use the repository tree when you need to understand where code lives. Use code search for targeted symbols or text. Neither a search excerpt nor an empty search result proves the repository has no matching implementation.

## If no catalog result fits

Do not immediately stop, and do not immediately create a duplicate. Inspect the tracked file tree and search likely script, workflow, and test locations for an unregistered or partially implemented capability. If something close exists, prefer extending it and then correcting the catalog.

If no suitable implementation exists, decide whether the task warrants a reusable tool. For a one-time task, a direct, reviewable operation may be simpler than adding permanent infrastructure. For a recurring or broadly useful task, read [Tool-building instructions](../tool-building-instructions.md) and design one composable capability with the smallest useful interface.

## Discovery output

Give a concise result containing:

- Best matching capability (or state that no existing tool fits).
- The exact entrypoint to use and how to invoke it.
- Important input, output, and safety limitations.
- Whether the existing capability should be used as-is, extended, or replaced.

Do not invent capability names or claim that a tool exists based only on a filename or a search snippet.
