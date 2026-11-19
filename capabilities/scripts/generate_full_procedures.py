#!/usr/bin/env python3
"""Generate the numbered DP-C historical procedure composite."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCUMENTS = (
    ROOT
    / "core"
    / "this-is-instruction-to-read-core-readme-before-proceeding"
    / "procedures"
    / "documents"
)
OUTPUT = DOCUMENTS / "full-procedures.md"
INPUTS = tuple(DOCUMENTS / f"procedure{number:02d}.md" for number in range(1, 10))

HEADER = """# Full Procedures — Generated Reference

**Generated artifact:** This file is assembled by [generate_full_procedures.py](../../../../capabilities/scripts/generate_full_procedures.py) from procedure01.md through procedure09.md in numeric order. Edit the individual inputs and run the generator; do not edit this composite manually.

**Role:** Historical integrated reference for review. Current task routing and operational sources are listed in [procedure-navigate.md](procedure-navigate.md).

---

"""


def build_document() -> str:
    sections: list[str] = []
    for expected_number, path in enumerate(INPUTS, start=1):
        if not path.is_file():
            raise FileNotFoundError(f"Required procedure input is missing: {path}")

        content = path.read_text(encoding="utf-8").strip()
        headings = re.findall(r"(?m)^# Procedure (\d{2}) —", content)
        expected = f"{expected_number:02d}"
        if headings != [expected]:
            raise ValueError(
                f"{path.name} must contain exactly one top-level "
                f"'Procedure {expected}' heading; found {headings!r}"
            )
        sections.append(content)

    return HEADER + "\n---\n\n".join(sections) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that full-procedures.md matches the current inputs",
    )
    args = parser.parse_args()

    try:
        generated = build_document()
        if args.check:
            if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != generated:
                print("full-procedures.md is stale; run this script to regenerate it.", file=sys.stderr)
                return 1
            print("full-procedures.md matches procedure01.md through procedure09.md.")
            return 0

        OUTPUT.write_text(generated, encoding="utf-8", newline="\n")
        print(f"Generated {OUTPUT.relative_to(ROOT)} from {len(INPUTS)} procedure files.")
        return 0
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Could not generate full-procedures.md: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
