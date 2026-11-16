from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import find_tool  # noqa: E402


class ToolCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = find_tool.load_catalog(ROOT / "tools" / "catalog.json")

    def test_catalog_paths_and_metadata_validate(self) -> None:
        self.assertEqual([], find_tool.validate_catalog(self.catalog, ROOT))

    def test_search_matches_terms_across_metadata(self) -> None:
        matches = find_tool.search_tools(self.catalog["tools"], "csv excel")
        ids = {item["id"] for item in matches}
        self.assertIn("dataset-analyzer", ids)
        self.assertIn("dataset-analysis", ids)

    def test_kind_filter(self) -> None:
        matches = find_tool.search_tools(self.catalog["tools"], "cleanup", kind="workflow")
        self.assertTrue(matches)
        self.assertTrue(all(item["kind"] == "workflow" for item in matches))

    def test_tag_filter_requires_all_requested_tags(self) -> None:
        matches = find_tool.search_tools(self.catalog["tools"], tags=["lookup", "catalog"])
        self.assertEqual({"tool-lookup", "tool-search"}, {item["id"] for item in matches})

    def test_unknown_query_returns_no_matches(self) -> None:
        matches = find_tool.search_tools(self.catalog["tools"], "not-a-real-tool")
        self.assertEqual([], matches)


if __name__ == "__main__":
    unittest.main()
