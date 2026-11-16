#!/usr/bin/env python3
"""Search the compact Sand-Box tool catalog without loading tool source files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "tools" / "catalog.json"
VALID_KINDS = {"script", "workflow"}
TOKEN_RE = re.compile(r"[a-z0-9]+(?:[._-][a-z0-9]+)*", re.IGNORECASE)
REQUIRED_FIELDS = {"id", "name", "kind", "path", "summary", "tags", "usage"}


def tokens(value: str) -> list[str]:
    return [part.lower() for part in TOKEN_RE.findall(value)]


def load_catalog(path: Path = CATALOG_PATH) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Catalog not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid catalog JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc
    if not isinstance(data, dict) or data.get("version") != 1 or not isinstance(data.get("tools"), list):
        raise ValueError("Catalog must be an object with version=1 and a tools array.")
    return data


def validate_catalog(data: dict[str, Any], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()

    for index, entry in enumerate(data["tools"]):
        label = f"tools[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = sorted(REQUIRED_FIELDS - entry.keys())
        if missing:
            errors.append(f"{label} is missing: {', '.join(missing)}")
            continue

        tool_id = entry["id"]
        path_text = entry["path"]
        if not isinstance(tool_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", tool_id):
            errors.append(f"{label}.id must be lowercase kebab-case")
        elif tool_id in seen_ids:
            errors.append(f"Duplicate tool id: {tool_id}")
        else:
            seen_ids.add(tool_id)

        if not isinstance(entry["kind"], str) or entry["kind"] not in VALID_KINDS:
            errors.append(f"{label}.kind must be one of: {', '.join(sorted(VALID_KINDS))}")

        if not isinstance(path_text, str) or not path_text:
            errors.append(f"{label}.path must be a non-empty repository-relative path")
        else:
            relative = Path(path_text)
            if relative.is_absolute() or ".." in relative.parts:
                errors.append(f"{label}.path must not be absolute or contain '..'")
            elif path_text in seen_paths:
                errors.append(f"Duplicate tool path: {path_text}")
            else:
                seen_paths.add(path_text)
                if not (root / relative).is_file():
                    errors.append(f"{label}.path does not exist: {path_text}")

        for field in ("name", "summary", "usage"):
            value = entry[field]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}.{field} must be a non-empty string")
        if isinstance(entry.get("summary"), str) and len(entry["summary"]) > 180:
            errors.append(f"{label}.summary must be 180 characters or fewer")
        if not isinstance(entry["tags"], list) or not all(isinstance(tag, str) and tag.strip() for tag in entry["tags"]):
            errors.append(f"{label}.tags must be an array of non-empty strings")
        if "aliases" in entry and (not isinstance(entry["aliases"], list) or not all(
            isinstance(alias, str) and alias.strip() for alias in entry["aliases"]
        )):
            errors.append(f"{label}.aliases must be an array of non-empty strings")

    return errors


def search_tools(
    tools: list[dict[str, Any]],
    query: str = "",
    kind: str = "all",
    tags: list[str] | None = None,
    limit: int = 5,
) -> list[dict[str, Any]]:
    query_terms = tokens(query)
    required_tags = {tag.strip().lower() for tag in (tags or []) if tag.strip()}
    ranked: list[tuple[int, str, dict[str, Any]]] = []

    for entry in tools:
        if kind != "all" and entry["kind"] != kind:
            continue
        entry_tags = {tag.lower() for tag in entry["tags"]}
        if not required_tags.issubset(entry_tags):
            continue

        fields = [entry["id"], entry["name"], entry["summary"], entry["path"], entry["usage"]]
        fields.extend(entry["tags"])
        fields.extend(entry.get("aliases", []))
        searchable_tokens = set(tokens(" ".join(fields)))
        if query_terms and not all(term in searchable_tokens for term in query_terms):
            continue

        score = 0
        for term in query_terms:
            if term in tokens(entry["id"]):
                score += 6
            elif term in tokens(entry["name"]):
                score += 5
            elif term in entry_tags:
                score += 4
            elif term in tokens(entry["path"]):
                score += 3
            else:
                score += 1
        if query.strip() and query.strip().lower() in " ".join(fields).lower():
            score += 2
        ranked.append((score, entry["id"], entry))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [entry for _, _, entry in ranked[:limit]]


def format_text(matches: list[dict[str, Any]], query: str) -> str:
    if not matches:
        return "No matching tools."
    heading = f"Tool matches for {query!r}:" if query else "Available tools:"
    lines = [heading]
    for item in matches:
        lines.append(f"- {item['name']} [{item['kind']}] — {item['summary']}")
        lines.append(f"  {item['path']} | {item['usage']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="*", help="Search terms; omit to list tools.")
    parser.add_argument("--kind", choices=["all", *sorted(VALID_KINDS)], default="all")
    parser.add_argument("--tag", action="append", default=[], help="Require a tag; may be repeated.")
    parser.add_argument("--limit", type=int, default=5, help="Maximum matches (1–20; default: 5).")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Use JSON for compact agent consumption.")
    parser.add_argument("--validate", action="store_true", help="Validate catalog metadata and referenced paths.")
    args = parser.parse_args(argv)

    if not 1 <= args.limit <= 20:
        parser.error("--limit must be between 1 and 20")

    try:
        catalog = load_catalog()
        errors = validate_catalog(catalog)
    except ValueError as exc:
        print(f"Catalog error: {exc}", file=sys.stderr)
        return 2

    if args.validate:
        if errors:
            print("Catalog validation failed:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 2
        print(f"Catalog OK: {len(catalog['tools'])} tools; all paths resolve.")
        return 0

    if errors:
        print("Catalog validation failed; run with --validate for details.", file=sys.stderr)
        return 2

    query = " ".join(args.query).strip()
    matches = search_tools(catalog["tools"], query, args.kind, args.tag, args.limit)
    if args.format == "json":
        print(json.dumps(matches, ensure_ascii=False, separators=(",", ":")))
    else:
        print(format_text(matches, query))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
