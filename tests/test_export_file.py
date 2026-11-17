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

from export_file import export_file


def write_minimal_docx(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "[Content_Types].xml",
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>',
        )
        archive.writestr(
            "_rels/.rels",
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>',
        )
        archive.writestr(
            "word/document.xml",
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body/></w:document>',
        )


class FileExportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "data").mkdir()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_generic_file_is_copied_and_hashed(self) -> None:
        source = self.root / "data" / "payload.bin"
        source.write_bytes(b"Sand-Box generic file export")

        output, manifest = export_file("data/payload.bin", self.root / "out", self.root)

        self.assertEqual(source.read_bytes(), output.read_bytes())
        self.assertTrue(manifest["copy_verified"])
        self.assertEqual("bin", manifest["file_type"])
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), manifest["sha256"])
        saved = json.loads((self.root / "out" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest, saved)

    def test_docx_package_is_validated_before_copy(self) -> None:
        source = self.root / "data" / "Summary.docx"
        write_minimal_docx(source)

        output, manifest = export_file("data/Summary.docx", self.root / "out", self.root)

        self.assertEqual(source.read_bytes(), output.read_bytes())
        self.assertTrue(manifest["valid_docx_package"])
        self.assertTrue(manifest["copy_verified"])

    def test_rejects_paths_outside_data(self) -> None:
        outside = self.root / "private.bin"
        outside.write_bytes(b"private")
        with self.assertRaises(ValueError):
            export_file("private.bin", self.root / "out", self.root)

    def test_rejects_parent_directory_traversal(self) -> None:
        with self.assertRaises(ValueError):
            export_file("../private.bin", self.root / "out", self.root)


if __name__ == "__main__":
    unittest.main()
