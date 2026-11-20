from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "capabilities" / "scripts"))

from zip_archive import ArchiveError, extract_member, inventory_archive, search_archive


class ZipArchiveTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "data").mkdir()
        self.archive_path = self.root / "data" / "sample.zip"
        with zipfile.ZipFile(self.archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("docs/Annual Report.pdf", b"annual report contents")
            archive.writestr("images/earthworm.png", b"PNG fixture")
            archive.writestr("notes/readme.txt", b"notes")
            archive.writestr("notes/report.txt", b"another report")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_inventory_lists_paths_and_sizes_without_extraction(self) -> None:
        result = inventory_archive("data/sample.zip", repo_root=self.root)
        self.assertEqual(4, result["file_count"])
        self.assertTrue(any(item["path"] == "docs/Annual Report.pdf" for item in result["members"]))
        self.assertFalse((self.root / "docs").exists())

    def test_find_supports_partial_name_and_extension(self) -> None:
        result = search_archive("data/sample.zip", query="annual", extension="pdf", repo_root=self.root)
        self.assertEqual(["docs/Annual Report.pdf"], [item["path"] for item in result["members"]])

    def test_find_supports_glob(self) -> None:
        result = search_archive("data/sample.zip", pattern="*.png", repo_root=self.root)
        self.assertEqual(["images/earthworm.png"], [item["path"] for item in result["members"]])

    def test_extracts_only_exact_selected_member(self) -> None:
        result = extract_member(
            "data/sample.zip", self.root / "out",
            member_path="docs/Annual Report.pdf", repo_root=self.root
        )
        extracted = self.root / "out" / "docs" / "Annual Report.pdf"
        self.assertEqual(b"annual report contents", extracted.read_bytes())
        self.assertTrue(result["copy_verified"])
        self.assertEqual(22, result["size_bytes"])

    def test_extract_query_requires_unique_match(self) -> None:
        with self.assertRaises(ArchiveError):
            extract_member("data/sample.zip", self.root / "out", query="report", repo_root=self.root)

    def test_extract_enforces_member_size_limit(self) -> None:
        with self.assertRaises(ArchiveError):
            extract_member(
                "data/sample.zip", self.root / "out",
                member_path="docs/Annual Report.pdf", max_bytes=5, repo_root=self.root
            )

    def test_rejects_archives_outside_data(self) -> None:
        with self.assertRaises(ArchiveError):
            inventory_archive(str(self.archive_path.resolve()), repo_root=self.root)

    def test_rejects_parent_traversal_member(self) -> None:
        unsafe = self.root / "data" / "unsafe.zip"
        with zipfile.ZipFile(unsafe, "w") as archive:
            archive.writestr("../escape.txt", b"unsafe")
        with self.assertRaises(ArchiveError):
            extract_member(
                "data/unsafe.zip", self.root / "out",
                member_path="../escape.txt", repo_root=self.root
            )

    def test_does_not_overwrite_existing_file(self) -> None:
        output = self.root / "out" / "docs" / "Annual Report.pdf"
        output.parent.mkdir(parents=True)
        output.write_bytes(b"keep")
        with self.assertRaises(ArchiveError):
            extract_member(
                "data/sample.zip", self.root / "out",
                member_path="docs/Annual Report.pdf", repo_root=self.root
            )
        self.assertEqual(b"keep", output.read_bytes())


if __name__ == "__main__":
    unittest.main()
