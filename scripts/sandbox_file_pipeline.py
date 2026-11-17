#!/usr/bin/env python3
"""Build, inspect, verify, and convert small file archives."""

from __future__ import annotations

import argparse
import hashlib
import zipfile
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    seed = sub.add_parser("seed", help="Create an initial ZIP archive.")
    seed.add_argument("--zip", default="picture2.zip")

    add = sub.add_parser("add", help="Add an image to the archive.")
    add.add_argument("--zip", default="picture2.zip")
    add.add_argument("--image", required=True)

    extract = sub.add_parser("extract", help="Extract the archive after checking member paths.")
    extract.add_argument("--zip", default="picture2.zip")
    extract.add_argument("--to", default="extracted")

    pdf = sub.add_parser("pdf", help="Convert an image to PDF (requires Pillow).")
    pdf.add_argument("--image", default="extracted/earthworm.jpg")
    pdf.add_argument("--pdf", default="earthworm.pdf")

    verify = sub.add_parser("verify", help="Validate the ZIP, extracted image, and PDF.")
    verify.add_argument("--zip", default="picture2.zip")
    verify.add_argument("--image", default="extracted/earthworm.jpg")
    verify.add_argument("--pdf", default="earthworm.pdf")

    args = parser.parse_args()
    archive = Path(getattr(args, "zip", "picture2.zip"))

    if args.command == "seed":
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("archive-note.txt", "Temporary ZIP seed for the Sand-Box file-pipeline test.\n")
        print(f"Created {archive} ({archive.stat().st_size} bytes)")
    elif args.command == "add":
        image = Path(args.image)
        if not image.is_file():
            parser.error(f"Image not found: {image}")
        with zipfile.ZipFile(archive, "a", compression=zipfile.ZIP_DEFLATED) as zf:
            zf.write(image, arcname="earthworm.jpg")
        print(f"Added earthworm.jpg; SHA-256={sha256(image)}")
    elif args.command == "extract":
        destination = Path(args.to)
        destination.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(archive) as zf:
            members = zf.namelist()
            if any(Path(name).is_absolute() or ".." in Path(name).parts for name in members):
                raise ValueError("Unsafe archive path detected.")
            zf.extractall(destination)
        print(f"Extracted {len(members)} members to {destination}")
    elif args.command == "pdf":
        try:
            from PIL import Image
        except ImportError as exc:
            raise SystemExit("The pdf command requires Pillow. Install it with: python -m pip install Pillow") from exc
        image_path = Path(args.image)
        with Image.open(image_path) as image:
            image.convert("RGB").save(args.pdf, "PDF", resolution=150.0)
        print(f"Created {args.pdf} ({Path(args.pdf).stat().st_size} bytes)")
    elif args.command == "verify":
        image_path = Path(args.image)
        pdf_path = Path(args.pdf)
        with zipfile.ZipFile(archive) as zf:
            names = zf.namelist()
            assert "earthworm.jpg" in names, f"earthworm.jpg missing from ZIP: {names}"
            assert zf.testzip() is None, "ZIP integrity test failed"
        assert image_path.is_file(), "Extracted image is missing"
        assert pdf_path.is_file(), "PDF is missing"
        assert pdf_path.read_bytes()[:5] == b"%PDF-", "Output is not a valid PDF"
        print(f"PASS: ZIP integrity, extracted image SHA-256={sha256(image_path)}, PDF header valid.")
    else:
        parser.error("Unknown command")


if __name__ == "__main__":
    main()
