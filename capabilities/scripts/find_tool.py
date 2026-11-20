#!/usr/bin/env python3
"""Search the grouped Sand-Box catalog without importing tool source files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "capabilities" / "catalog.json"
TOKEN_RE = re.compile(r"[a-z0-9]+", re.IGNORECASE)
SLUG_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
REQUIRED_TOOL_FIELDS = {"id", "name", "summary", "tags", "entrypoints"}
REQUIRED_ENTRYPOINT_FIELDS = {"kind", "path", "usage"}
MAX_LIMIT = 50


def tokens(value: str) -> list[str]:
    return [part.lower() for part in TOKEN_RE.findall(value)]


def load_catalog(path: Path = CATALOG_PATH) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Catalog not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid catalog JSON at line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}"
        ) from exc

    if not isinstance(data, dict) or data.get("version") != 2:
        raise ValueError("Catalog must be an object with version=2.")
    if not isinstance(data.get("tools"), list):
        raise ValueError("Catalog must contain a tools array.")
    return data


def _nonempty_strings(value: Any) -> bool:
    return isinstance(value, list) and all(
        isinstance(item, str) and item.strip() for item in value
    )


def validate_catalog(data: dict[str, Any], root: Path = ROOT) -> list[str]:
    """Validate metadata, unique entrypoints, and safe repository-relative paths."""
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    resolved_root = root.resolve()

    if not isinstance(data, dict) or data.get("version") != 2:
        return ["Catalog must be an object with version=2."]
    if not isinstance(data.get("tools"), list):
        return ["Catalog must contain a tools array."]

    for index, entry in enumerate(data["tools"]):
        label = f"tools[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = sorted(REQUIRED_TOOL_FIELDS - entry.keys())
        if missing:
            errors.append(f"{label} is missing: {', '.join(missing)}")
            continue

        tool_id = entry["id"]
        if not isinstance(tool_id, str) or not SLUG_RE.fullmatch(tool_id):
            errors.append(f"{label}.id must be lowercase kebab-case")
        elif tool_id in seen_ids:
            errors.append(f"Duplicate tool id: {tool_id}")
        else:
            seen_ids.add(tool_id)

        for field in ("name", "summary"):
            value = entry[field]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}.{field} must be a non-empty string")
        if isinstance(entry.get("summary"), str) and len(entry["summary"]) > 220:
            errors.append(f"{label}.summary must be 220 characters or fewer")

        tags = entry["tags"]
        if not _nonempty_strings(tags) or not tags:
            errors.append(f"{label}.tags must be a non-empty array of strings")
        elif len({tag.casefold() for tag in tags}) != len(tags):
            errors.append(f"{label}.tags must not contain duplicates")

        aliases = entry.get("aliases", [])
        if not _nonempty_strings(aliases):
            errors.append(f"{label}.aliases must be an array of non-empty strings")

        entrypoints = entry["entrypoints"]
        if not isinstance(entrypoints, list) or not entrypoints:
            errors.append(f"{label}.entrypoints must be a non-empty array")
            continue

        for ep_index, point in enumerate(entrypoints):
            ep_label = f"{label}.entrypoints[{ep_index}]"
            if not isinstance(point, dict):
                errors.append(f"{ep_label} must be an object")
                continue

            missing_ep = sorted(REQUIRED_ENTRYPOINT_FIELDS - point.keys())
            if missing_ep:
                errors.append(f"{ep_label} is missing: {', '.join(missing_ep)}")
                continue

            kind = point["kind"]
            if not isinstance(kind, str) or not SLUG_RE.fullmatch(kind):
                errors.append(f"{ep_label}.kind must be lowercase kebab-case")

            usage = point["usage"]
            if not isinstance(usage, str) or not usage.strip():
                errors.append(f"{ep_label}.usage must be a non-empty string")

            path_text = point["path"]
            if not isinstance(path_text, str) or not path_text.strip():
                errors.append(f"{ep_label}.path must be a non-empty repository-relative path")
                continue

            relative = Path(path_text)
            if relative.is_absolute() or ".." in relative.parts or relative.as_posix() != path_text:
                errors.append(f"{ep_label}.path must be a normalized relative path")
                continue
            if path_text in seen_paths:
                errors.append(f"Duplicate entrypoint path: {path_text}")
                continue
            seen_paths.add(path_text)

            resolved_path = (resolved_root / relative).resolve()
            if resolved_root not in resolved_path.parents:
                errors.append(f"{ep_label}.path resolves outside the repository: {path_text}")
            elif not resolved_path.is_file():
                errors.append(f"{ep_label}.path does not exist: {path_text}")

    return errors


def _quality(term: str, candidate: str) -> float:
    if term == candidate:
        return 1.0
    if len(term) >= 3 and candidate.startswith(term):
        return 0.82
    if len(term) >= 4 and term in candidate:
        return 0.62
    return 0.0


def _entrypoint_kinds(entry: dict[str, Any]) -> set[str]:
    return {
        point["kind"]
        for point in entry.get("entrypoints", [])
        if isinstance(point, dict) and isinstance(point.get("kind"), str)
    }


def _search_score(entry: dict[str, Any], query_terms: list[str]) -> int:
    weighted_fields: list[tuple[int, str]] = [
        (12, entry["id"]),
        (10, entry["name"]),
        (8, entry["summary"]),
    ]
    weighted_fields.extend((9, alias) for alias in entry.get("aliases", []))
    weighted_fields.extend((8, tag) for tag in entry.get("tags", []))
    for point in entry.get("entrypoints", []):
        weighted_fields.extend(
            [
                (5, point["kind"]),
                (5, point["path"]),
                (3, point["usage"]),
            ]
        )

    field_tokens = [(weight, tokens(value)) for weight, value in weighted_fields]
    score = 0
    matched = 0
    for term in query_terms:
        best = max(
            (weight * _quality(term, candidate) for weight, values in field_tokens for candidate in values),
            default=0.0,
        )
        if best > 0:
            matched += 1
            score += round(best)

    if query_terms and matched == len(query_terms):
        score += 3
    elif query_terms:
        score += matched
    return score


def search_tools(
    tools: list[dict[str, Any]],
    query: str = "",
    kind: str = "all",
    tags: list[str] | None = None,
    limit: int = 5,
    sort: str = "relevance",
) -> list[dict[str, Any]]:
    """Multiword queries match any term; records matching more terms rank higher."""
    query_terms = tokens(query)
    required_tags = {tag.strip().casefold() for tag in (tags or []) if tag.strip()}
    ranked: list[tuple[int, str, dict[str, Any]]] = []

    for entry in tools:
        if kind != "all" and kind not in _entrypoint_kinds(entry):
            continue
        entry_tags = {tag.casefold() for tag in entry.get("tags", [])}
        if not required_tags.issubset(entry_tags):
            continue

        score = _search_score(entry, query_terms) if query_terms else 0
        if query_terms and score == 0:
            continue
        ranked.append((score, entry["name"].casefold(), entry))

    if sort == "name":
        ranked.sort(key=lambda item: (item[1], item[2]["id"]))
    else:
        ranked.sort(key=lambda item: (-item[0], item[1], item[2]["id"]))
    return [entry for _, _, entry in ranked[:limit]]


def format_text(matches: list[dict[str, Any]], query: str) -> str:
    if not matches:
        return "No matching tools."

    heading = f"Tool matches for {query!r}:" if query else "Available tools:"
    lines = [heading]
    for item in matches:
        lines.append(f"- {item['name']} — {item['summary']}")
        for point in item["entrypoints"]:
            lines.append(f"  [{point['kind']}] {point['path']}")
            lines.append(f"    {point['usage']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="*", help="Search terms; omit to list tools.")
    parser.add_argument("--kind", default="all", help="Filter by entrypoint kind (or 'all').")
    parser.add_argument("--tag", action="append", default=[], help="Require a tag; may be repeated.")
    parser.add_argument("--limit", type=int, default=5, help=f"Maximum matches (1–{MAX_LIMIT}; default: 5).")
    parser.add_argument("--sort", choices=["relevance", "name"], default="relevance")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--list-tags", action="store_true", help="List the catalog's unique tags.")
    parser.add_argument("--validate", action="store_true", help="Validate metadata and all entrypoint paths.")
    args = parser.parse_args(argv)

    if not 1 <= args.limit <= MAX_LIMIT:
        parser.error(f"--limit must be between 1 and {MAX_LIMIT}")

    try:
        catalog = load_catalog()
    except ValueError as exc:
        print(f"Catalog error: {exc}", file=sys.stderr)
        return 2

    errors = validate_catalog(catalog)
    if args.validate:
        if errors:
            print("Catalog validation failed:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 2
        print(f"Catalog OK: {len(catalog['tools'])} tools; all entrypoints resolve.")
        return 0

    if errors:
        print("Catalog validation failed; run with --validate for details.", file=sys.stderr)
        return 2

    kinds = set().union(*(_entrypoint_kinds(entry) for entry in catalog["tools"]))
    if args.kind != "all" and args.kind not in kinds:
        parser.error(f"Unknown kind {args.kind!r}; available kinds: {', '.join(sorted(kinds))}")

    if args.list_tags:
        print("\n".join(sorted({tag for entry in catalog["tools"] for tag in entry["tags"]})))
        return 0

    query = " ".join(args.query).strip()
    matches = search_tools(
        catalog["tools"],
        query=query,
        kind=args.kind,
        tags=args.tag,
        limit=args.limit,
        sort=args.sort,
    )
    if args.format == "json":
        print(json.dumps(matches, ensure_ascii=False, separators=(",", ":")))
    else:
        print(format_text(matches, query))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
