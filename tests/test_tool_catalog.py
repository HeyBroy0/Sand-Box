from __future__ import annotations

import copy
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

    def test_catalog_metadata_and_entrypoints_validate(self) -> None:
        self.assertEqual([], find_tool.validate_catalog(self.catalog, ROOT))

    def test_search_combines_terms_and_ranks_full_matches(self) -> None:
        matches = find_tool.search_tools(self.catalog["tools"], "csv excel")
        self.assertTrue(matches)
        self.assertEqual("dataset-analysis", matches[0]["id"])

    def test_alias_and_partial_word_search(self) -> None:
        matches = find_tool.search_tools(self.catalog["tools"], "library docx")
        self.assertIn("file-handoff", {item["id"] for item in matches})

    def test_kind_filter_matches_grouped_entrypoints(self) -> None:
        script_matches = find_tool.search_tools(self.catalog["tools"], kind="script")
        workflow_matches = find_tool.search_tools(self.catalog["tools"], kind="workflow")
        self.assertTrue(script_matches)
        self.assertTrue(workflow_matches)
        self.assertNotIn("file-pipeline", {item["id"] for item in workflow_matches})
        self.assertIn("dataset-analysis", {item["id"] for item in workflow_matches})

    def test_tag_filter_requires_all_requested_tags(self) -> None:
        matches = find_tool.search_tools(self.catalog["tools"], tags=["library", "docx"])
        self.assertEqual({"file-handoff"}, {item["id"] for item in matches})

    def test_name_sort_is_deterministic(self) -> None:
        matches = find_tool.search_tools(self.catalog["tools"], sort="name", limit=50)
        names = [item["name"].casefold() for item in matches]
        self.assertEqual(sorted(names), names)

    def test_duplicate_entrypoint_path_is_rejected(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["tools"][1]["entrypoints"].append(
            copy.deepcopy(catalog["tools"][0]["entrypoints"][0])
        )
        errors = find_tool.validate_catalog(catalog, ROOT)
        self.assertTrue(any("Duplicate entrypoint path" in error for error in errors))

    def test_unknown_query_returns_no_matches(self) -> None:
        matches = find_tool.search_tools(self.catalog["tools"], "quasar zyzzyva")
        self.assertEqual([], matches)


if __name__ == "__main__":
    unittest.main()
