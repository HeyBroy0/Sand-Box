#!/usr/bin/env python3
"""Copy a file from data/ unchanged and write a SHA-256 integrity manifest."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

from export_docx import sha256_file, validate_docx

REPO_ROOT = Path(__file__).resolve().parents[2]


def resolve_source(value: str | Path, repo_root: Path = REPO_ROOT) -> Path:
    """Resolve one repository-relative file and constrain it to data/."""
    raw = Path(value)
    if raw.is_absolute() or ".." in raw.parts:
        raise ValueError("Input must be a repository-relative path under data/.")

    data_root = (repo_root / "data").resolve(strict=True)
    try:
        source = (repo_root / raw).resolve(strict=True)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Input file does not exist: {raw}") from exc

    if source == data_root or data_root not in source.parents:
        raise ValueError("Input must resolve to a file inside the repository data/ directory.")
    if not source.is_file():
        raise ValueError(f"Input is not a regular file: {raw}")
    return source


def export_file(
    input_path: str | Path,
    output_dir: str | Path,
    repo_root: Path = REPO_ROOT,
) -> tuple[Path, dict[str, Any]]:
    """Copy one file unchanged, verify the copy, and write a machine-readable manifest."""
    source = resolve_source(input_path, repo_root)
    validation = validate_docx(source) if source.suffix.casefold() == ".docx" else {}

    destination_dir = Path(output_dir)
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / source.name
    manifest_path = destination_dir / "manifest.json"

    if destination.name.casefold() == manifest_path.name.casefold():
        raise ValueError("A source named 'manifest.json' conflicts with the export manifest filename.")
    for output in (destination, manifest_path):
        if output.exists() or output.is_symlink():
            raise FileExistsError(f"Refusing to overwrite existing output: {output}")

    created_destination = False
    try:
        with source.open("rb") as source_stream:
            with destination.open("xb") as destination_stream:
                created_destination = True
                shutil.copyfileobj(source_stream, destination_stream)
    except Exception:
        if created_destination:
            destination.unlink(missing_ok=True)
        raise

    source_hash = sha256_file(source)
    exported_hash = sha256_file(destination)
    if source_hash != exported_hash:
        destination.unlink(missing_ok=True)
        raise IOError("Export verification failed: copied file hash differs from source.")

    manifest: dict[str, Any] = {
        "source_path": source.relative_to(repo_root.resolve()).as_posix(),
        "file_name": destination.name,
        "file_type": source.suffix.casefold().lstrip(".") or "unknown",
        "size_bytes": destination.stat().st_size,
        "sha256": exported_hash,
        "copy_verified": True,
        **validation,
    }
    try:
        with manifest_path.open("x", encoding="utf-8") as stream:
            json.dump(manifest, stream, indent=2)
            stream.write("\n")
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    return destination, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Repository-relative file path under data/.")
    parser.add_argument("--output-dir", default="file-export", help="Artifact staging directory.")
    args = parser.parse_args()

    try:
        output, manifest = export_file(args.input, args.output_dir)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps({"output": str(output), **manifest}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
