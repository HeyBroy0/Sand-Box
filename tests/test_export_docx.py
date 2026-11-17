from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from export_docx import export_docx, resolve_source, validate_docx  # noqa: E402


def write_minimal_docx(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>')
        archive.writestr("_rels/.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>')
        archive.writestr("word/document.xml", '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body/></w:document>')


class DocxExportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "data").mkdir()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_validates_and_copies_docx_byte_for_byte(self) -> None:
        source = self.root / "data" / "Summary.docx"
        write_minimal_docx(source)

        output, manifest = export_docx("data/Summary.docx", self.root / "out", self.root)

        self.assertEqual(source.read_bytes(), output.read_bytes())
        self.assertTrue(manifest["valid_docx_package"])
        self.assertEqual(len(source.read_bytes()), manifest["size_bytes"])
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), manifest["sha256"])
        saved_manifest = json.loads((self.root / "out" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest, saved_manifest)

    def test_rejects_paths_outside_data(self) -> None:
        outside = self.root / "private.docx"
        write_minimal_docx(outside)
        with self.assertRaises(ValueError):
            resolve_source("private.docx", self.root)

    def test_rejects_non_docx_extension(self) -> None:
        source = self.root / "data" / "notes.txt"
        source.write_text("not a document", encoding="utf-8")
        with self.assertRaises(ValueError):
            resolve_source("data/notes.txt", self.root)

    def test_rejects_corrupt_docx(self) -> None:
        source = self.root / "data" / "broken.docx"
        source.write_bytes(b"not a zip archive")
        with self.assertRaises(ValueError):
            validate_docx(source)


if __name__ == "__main__":
    unittest.main()
