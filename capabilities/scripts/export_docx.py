#!/usr/bin/env python3
"""Validate and export a DOCX unchanged from the repository data/ directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = (REPO_ROOT / "data").resolve()
REQUIRED_MEMBERS = {
    "[Content_Types].xml",
    "_rels/.rels",
    "word/document.xml",
}


def resolve_source(value: str | Path, repo_root: Path = REPO_ROOT) -> Path:
    """Resolve a repository-relative DOCX path and constrain it to data/."""
    raw = Path(value)
    if raw.is_absolute():
        raise ValueError("Input must be a repository-relative path under data/.")

    data_root = (repo_root / "data").resolve()
    try:
        source = (repo_root / raw).resolve(strict=True)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Input file does not exist: {raw}") from exc

    if source == data_root or data_root not in source.parents:
        raise ValueError("Input must resolve to a file inside the repository data/ directory.")
    if not source.is_file():
        raise ValueError(f"Input is not a regular file: {raw}")
    if source.suffix.casefold() != ".docx":
        raise ValueError("Only .docx files are supported.")

    return source


def validate_docx(path: Path) -> dict[str, Any]:
    """Check the ZIP package and parse the core XML parts without extracting files."""
    try:
        with zipfile.ZipFile(path, "r") as archive:
            names = set(archive.namelist())
            missing = sorted(REQUIRED_MEMBERS - names)
            if missing:
                raise ValueError(f"Not a valid DOCX package; missing members: {', '.join(missing)}")

            bad_member = archive.testzip()
            if bad_member is not None:
                raise ValueError(f"DOCX ZIP CRC check failed for: {bad_member}")

            for member in ("[Content_Types].xml", "word/document.xml"):
                try:
                    ET.fromstring(archive.read(member))
                except ET.ParseError as exc:
                    raise ValueError(f"Invalid XML in DOCX member {member}: {exc}") from exc
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Input is not a readable DOCX ZIP package: {exc}") from exc

    return {"valid_docx_package": True, "required_members": sorted(REQUIRED_MEMBERS)}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def export_docx(
    input_path: str | Path,
    output_dir: str | Path,
    repo_root: Path = REPO_ROOT,
) -> tuple[Path, dict[str, Any]]:
    """Copy one validated DOCX unchanged and write a JSON integrity manifest."""
    source = resolve_source(input_path, repo_root)
    validation = validate_docx(source)

    destination_dir = Path(output_dir)
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / source.name
    shutil.copyfile(source, destination)

    source_hash = sha256_file(source)
    exported_hash = sha256_file(destination)
    if source_hash != exported_hash:
        destination.unlink(missing_ok=True)
        raise IOError("Export verification failed: copied file hash differs from source.")

    manifest: dict[str, Any] = {
        "source_path": source.relative_to(repo_root.resolve()).as_posix(),
        "file_name": destination.name,
        "size_bytes": destination.stat().st_size,
        "sha256": exported_hash,
        **validation,
    }
    manifest_path = destination_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return destination, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Repository-relative .docx path under data/.")
    parser.add_argument("--output-dir", default="docx-export", help="Artifact staging directory.")
    args = parser.parse_args()

    try:
        output, manifest = export_docx(args.input, args.output_dir)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps({"output": str(output), **manifest}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
