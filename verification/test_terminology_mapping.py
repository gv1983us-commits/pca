"""Publication checks for the reciprocal MPAA/PCA terminology record."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "verification" / "terminology-mapping-mpaa-pca.md"


class TerminologyMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = MAPPING.read_text(encoding="utf-8")

    def test_fixed_mapped_revision_is_present(self):
        self.assertIn("1d369f6cd091b99f9492cfaf730f0a170b55106e", self.text)

    def test_preserved_source_item_is_explicitly_resolved(self):
        self.assertIn("item 3", self.text)
        self.assertIn("section 22", self.text)
        self.assertIn("What Must Be Checked Against the Existing Project Corpus", self.text)

    def test_reciprocal_mpaa_record_is_linked(self):
        self.assertIn("review/MPAA_PCA_TERMINOLOGY_MAPPING.md", self.text)

    def test_divergences_remain_explicit(self):
        for phrase in (
            "no exact equivalence",
            "partial / directional",
            "complementary, not equivalent",
            "separate domain",
            "carrier-only",
            "not equivalence",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)


if __name__ == "__main__":
    unittest.main()
