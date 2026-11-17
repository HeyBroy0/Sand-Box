#!/usr/bin/env python3
"""Inspect ZIP archives, find members by name, and safely extract one selected file."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIMIT = 100
MAX_LIMIT = 500
DEFAULT_MAX_BYTES = 100 * 1024 * 1024


class ArchiveError(ValueError):
    """An invalid archive operation or unsafe archive member."""


def sha256_stream(stream: Any, destination: Any | None = None, max_bytes: int | None = None) -> tuple[str, int]:
    digest = hashlib.sha256()
    total = 0
    while chunk := stream.read(1024 * 1024):
        total += len(chunk)
        if max_bytes is not None and total > max_bytes:
            raise ArchiveError(f"Member exceeds the configured extraction limit of {max_bytes} bytes.")
        digest.update(chunk)
        if destination is not None:
            destination.write(chunk)
    return digest.hexdigest(), total


def sha256_file(path: Path) -> str:
    with path.open("rb") as stream:
        digest, _ = sha256_stream(stream)
    return digest


def resolve_archive(value: str | Path, repo_root: Path = REPO_ROOT) -> Path:
    """Resolve a ZIP under data/ and reject traversal or external paths."""
    raw = Path(value)
    if raw.is_absolute() or ".." in raw.parts:
        raise ArchiveError("Archive must be a repository-relative path under data/.")
    data_root = (repo_root / "data").resolve(strict=True)
    try:
        source = (repo_root / raw).resolve(strict=True)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Archive not found: {raw}") from exc
    if source == data_root or data_root not in source.parents:
        raise ArchiveError("Archive must resolve to a file inside data/.")
    if not source.is_file() or source.suffix.casefold() != ".zip":
        raise ArchiveError("Archive path must identify a regular .zip file.")
    return source


def member_safety(info: zipfile.ZipInfo) -> tuple[bool, str]:
    name = info.filename
    if not name or "\x00" in name:
        return False, "empty or invalid member name"
    if "\\" in name:
        return False, "backslash in member path"
    member = PurePosixPath(name)
    if member.is_absolute() or ".." in member.parts or re.match(r"^[A-Za-z]:", name):
        return False, "absolute or parent-traversal member path"
    mode = (info.external_attr >> 16) & 0xFFFF
    if stat.S_ISLNK(mode):
        return False, "symbolic links are not extracted"
    if info.flag_bits & 0x1:
        return False, "encrypted members are not supported"
    return True, ""


def is_directory(info: zipfile.ZipInfo) -> bool:
    return info.is_dir() or info.filename.endswith("/")


def member_record(info: zipfile.ZipInfo) -> dict[str, Any]:
    safe, reason = member_safety(info)
    return {
        "path": info.filename,
        "name": PurePosixPath(info.filename).name,
        "extension": PurePosixPath(info.filename).suffix.casefold(),
        "directory": is_directory(info),
        "size_bytes": info.file_size,
        "compressed_bytes": info.compress_size,
        "compression": info.compress_type,
        "crc32": f"{info.CRC:08x}",
        "safe_to_extract": safe and not is_directory(info),
        "safety_note": reason or ("directory entry" if is_directory(info) else ""),
    }


def match_score(info: zipfile.ZipInfo, query: str = "", pattern: str = "", extension: str = "") -> int | None:
    if is_directory(info):
        return None
    path = info.filename.casefold()
    basename = PurePosixPath(info.filename).name.casefold()
    suffix = PurePosixPath(info.filename).suffix.casefold()
    wanted_extension = extension.casefold()
    if wanted_extension and not wanted_extension.startswith("."):
        wanted_extension = "." + wanted_extension
    if wanted_extension and suffix != wanted_extension:
        return None
    if pattern and not fnmatch.fnmatchcase(path, pattern.casefold()):
        return None
    terms = [term for term in re.split(r"\s+", query.casefold().strip()) if term]
    score = 0
    for term in terms:
        if term == path or term == basename:
            score += 12
        elif term in basename:
            score += 8
        elif term in path:
            score += 5
        else:
            return None
    return score + (3 if terms else 0)


def find_members(infos: list[zipfile.ZipInfo], query: str = "", pattern: str = "",
                 extension: str = "", limit: int = DEFAULT_LIMIT) -> list[zipfile.ZipInfo]:
    ranked: list[tuple[int, str, int, zipfile.ZipInfo]] = []
    for index, info in enumerate(infos):
        score = match_score(info, query, pattern, extension)
        if score is not None:
            ranked.append((score, info.filename.casefold(), index, info))
    ranked.sort(key=lambda item: (-item[0], item[1], item[2]))
    return [item[3] for item in ranked[:limit]]


def write_report(path: str | None, payload: dict[str, Any]) -> None:
    if not path:
        return
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def format_members(title: str, matches: list[dict[str, Any]], total: int, limit: int) -> str:
    lines = [f"{title}: showing {len(matches)} of {total} file(s)."]
    if not matches:
        lines.append("No matching files.")
    for item in matches:
        marker = "UNSAFE" if not item["safe_to_extract"] else "FILE"
        lines.append(f"- [{marker}] {item['path']} ({item['size_bytes']:,} bytes; compressed {item['compressed_bytes']:,} bytes)")
        if item["safety_note"]:
            lines.append(f"    Note: {item['safety_note']}")
    if total > limit:
        lines.append(f"... {total - limit} additional file(s) omitted; raise --limit to show more.")
    return "\n".join(lines)


def inventory_archive(archive_path: str | Path, query: str = "", pattern: str = "",
                      extension: str = "", limit: int = DEFAULT_LIMIT,
                      repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    source = resolve_archive(archive_path, repo_root)
    with zipfile.ZipFile(source, "r") as archive:
        infos = archive.infolist()
        matches = find_members(infos, query, pattern, extension, limit)
        total = sum(match_score(info, query, pattern, extension) is not None for info in infos)
        files = [info for info in infos if not is_directory(info)]
        return {
            "operation": "list",
            "archive": source.relative_to(repo_root.resolve()).as_posix(),
            "archive_sha256": sha256_file(source),
            "member_count": len(infos),
            "file_count": len(files),
            "directory_count": len(infos) - len(files),
            "total_uncompressed_bytes": sum(info.file_size for info in files),
            "matching_file_count": total,
            "truncated": total > len(matches),
            "members": [member_record(info) for info in matches],
        }


def search_archive(archive_path: str | Path, query: str = "", pattern: str = "",
                  extension: str = "", limit: int = DEFAULT_LIMIT,
                  repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    if not query.strip() and not pattern.strip() and not extension.strip():
        raise ArchiveError("Provide --query, --pattern, or --extension for a search.")
    source = resolve_archive(archive_path, repo_root)
    with zipfile.ZipFile(source, "r") as archive:
        infos = archive.infolist()
        matches = find_members(infos, query, pattern, extension, limit)
        total = sum(match_score(info, query, pattern, extension) is not None for info in infos)
        return {
            "operation": "find",
            "archive": source.relative_to(repo_root.resolve()).as_posix(),
            "archive_sha256": sha256_file(source),
            "query": query,
            "pattern": pattern,
            "extension": extension,
            "matching_file_count": total,
            "truncated": total > len(matches),
            "members": [member_record(info) for info in matches],
        }


def select_member(infos: list[zipfile.ZipInfo], member_path: str | None,
                  query: str | None) -> zipfile.ZipInfo:
    files = [info for info in infos if not is_directory(info)]
    if member_path:
        candidates = [info for info in files if info.filename == member_path]
        if not candidates:
            candidates = [info for info in files if info.filename.casefold() == member_path.casefold()]
        if len(candidates) == 1:
            return candidates[0]
        if len(candidates) > 1:
            raise ArchiveError(f"Duplicate entries use {member_path!r}; inspect the archive before extraction.")
        raise ArchiveError(f"No exact member named {member_path!r}; use find to inspect candidates.")
    if query:
        candidates = find_members(infos, query=query, limit=2)
        if not candidates:
            raise ArchiveError(f"No member matched query {query!r}.")
        if len(candidates) > 1:
            labels = ", ".join(info.filename for info in candidates)
            raise ArchiveError(f"Query is ambiguous; candidates include: {labels}. Use an exact member path.")
        return candidates[0]
    raise ArchiveError("Extract requires an exact --member path or a --query that returns one unique file.")


def extract_member(archive_path: str | Path, output_dir: str | Path,
                   member_path: str | None = None, query: str | None = None,
                   max_bytes: int = DEFAULT_MAX_BYTES,
                   repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    if max_bytes < 1:
        raise ArchiveError("--max-bytes must be a positive integer.")
    source = resolve_archive(archive_path, repo_root)
    archive_hash = sha256_file(source)
    destination_root = Path(output_dir).resolve()
    destination_root.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(source, "r") as archive:
            info = select_member(archive.infolist(), member_path, query)
            safe, reason = member_safety(info)
            if not safe:
                raise ArchiveError(f"Refusing to extract {info.filename!r}: {reason}.")
            if info.file_size > max_bytes:
                raise ArchiveError(f"Member is {info.file_size} bytes; configured limit is {max_bytes} bytes.")
            relative = PurePosixPath(info.filename)
            destination = destination_root.joinpath(*relative.parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            resolved_destination = destination.resolve()
            if destination_root != resolved_destination and destination_root not in resolved_destination.parents:
                raise ArchiveError("Selected member resolves outside the output directory.")
            if destination.exists():
                raise ArchiveError(f"Output already exists: {destination}")
            partial = destination.with_name(destination.name + ".partial")
            if partial.exists():
                raise ArchiveError(f"Temporary output already exists: {partial}")
            try:
                with archive.open(info, "r") as source_stream, partial.open("xb") as output_stream:
                    member_hash, copied_bytes = sha256_stream(source_stream, output_stream, max_bytes)
                if copied_bytes != info.file_size:
                    raise ArchiveError("Extracted size does not match the ZIP member metadata.")
                if destination.exists():
                    raise ArchiveError(f"Output already exists: {destination}")
                os.replace(partial, destination)
            except Exception:
                partial.unlink(missing_ok=True)
                raise
            return {
                "operation": "extract",
                "archive": source.relative_to(repo_root.resolve()).as_posix(),
                "archive_sha256": archive_hash,
                "member_path": info.filename,
                "output_path": destination.relative_to(destination_root).as_posix(),
                "size_bytes": copied_bytes,
                "crc32": f"{info.CRC:08x}",
                "sha256": member_hash,
                "copy_verified": True,
            }
    except zipfile.BadZipFile as exc:
        raise ArchiveError(f"Invalid or corrupt ZIP archive: {exc}") from exc
    except RuntimeError as exc:
        raise ArchiveError(f"Could not read the selected member: {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="operation", required=True)

    def common(command: argparse.ArgumentParser) -> None:
        command.add_argument("--archive", required=True, help="Repository-relative ZIP file under data/.")
        command.add_argument("--report", help="Optional JSON report output path.")

    listing = subs.add_parser("list", help="List member paths and sizes without extracting.")
    common(listing)
    listing.add_argument("--query", default="")
    listing.add_argument("--pattern", default="", help="Case-insensitive glob, such as '*.pdf'.")
    listing.add_argument("--extension", default="", help="Extension filter, such as pdf or .pdf.")
    listing.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    listing.add_argument("--format", choices=["text", "json"], default="text")

    finding = subs.add_parser("find", help="Find candidate files by name, glob, or extension.")
    common(finding)
    finding.add_argument("--query", default="")
    finding.add_argument("--pattern", default="")
    finding.add_argument("--extension", default="")
    finding.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    finding.add_argument("--format", choices=["text", "json"], default="text")

    extracting = subs.add_parser("extract", help="Extract one selected member only.")
    common(extracting)
    selector = extracting.add_mutually_exclusive_group(required=True)
    selector.add_argument("--member", help="Exact archive member path.")
    selector.add_argument("--query", help="Partial name/path; must resolve to one unique file.")
    extracting.add_argument("--output-dir", default="zip-output/extracted")
    extracting.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if getattr(args, "limit", 1) < 1 or getattr(args, "limit", 1) > MAX_LIMIT:
        parser.error(f"--limit must be between 1 and {MAX_LIMIT}")
    try:
        if args.operation in {"list", "find"}:
            if args.operation == "list":
                payload = inventory_archive(args.archive, args.query, args.pattern, args.extension, args.limit)
                title = f"ZIP inventory for {Path(args.archive).name}"
            else:
                payload = search_archive(args.archive, args.query, args.pattern, args.extension, args.limit)
                title = f"Search results in {Path(args.archive).name}"
            write_report(args.report, payload)
            if args.format == "json":
                print(json.dumps(payload, indent=2))
            else:
                print(format_members(title, payload["members"], payload["matching_file_count"], args.limit))
        else:
            payload = extract_member(args.archive, args.output_dir, args.member, args.query, args.max_bytes)
            write_report(args.report, payload)
            print(json.dumps(payload, indent=2))
    except (OSError, ArchiveError, zipfile.BadZipFile, RuntimeError) as exc:
        print(f"Archive operation failed: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
