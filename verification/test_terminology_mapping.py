"""Publication checks for fixed-revision PCA neighbor boundary reviews."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MPAA_MAPPING = ROOT / "verification" / "terminology-mapping-mpaa-pca.md"
BEC_MAPPING = ROOT / "verification" / "terminology-mapping-bec-pca.md"

PCA_CORE_REVISION = "070c6dcbc399eae82321a8303972a3cee9a81030"
MPAA_CANONICAL_REVISION = "0d1aaf35cc4826622f3312fdd2a1c2d40890b965"
BEC_CANONICAL_REVISION = "62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261"


class TerminologyMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mpaa = MPAA_MAPPING.read_text(encoding="utf-8")
        cls.bec = BEC_MAPPING.read_text(encoding="utf-8")

    def test_fixed_current_revisions_are_present(self):
        self.assertIn(PCA_CORE_REVISION, self.mpaa)
        self.assertIn(PCA_CORE_REVISION, self.bec)
        self.assertIn(MPAA_CANONICAL_REVISION, self.mpaa)
        self.assertIn(BEC_CANONICAL_REVISION, self.bec)

    def test_preserved_source_items_are_explicitly_resolved(self):
        for text, item in ((self.mpaa, "item 3"), (self.bec, "item 4")):
            with self.subTest(item=item):
                self.assertIn(item, text)
                self.assertIn("section 22", text)
                self.assertIn("What Must Be Checked Against the Existing Project Corpus", text)
                self.assertIn("status: RESOLVED", text)

    def test_historical_reciprocal_mpaa_record_is_preserved(self):
        self.assertIn("review/MPAA_PCA_TERMINOLOGY_MAPPING.md", self.mpaa)
        self.assertIn("historical", self.mpaa.lower())
        self.assertIn("1d369f6cd091b99f9492cfaf730f0a170b55106e", self.mpaa)
        self.assertIn("6ad1a86d7c09b36839d162c580f84f05cfe4a598", self.mpaa)

    def test_mpaa_divergences_remain_explicit(self):
        for phrase in (
            "no exact equivalence",
            "partial / directional",
            "complementary, not equivalent",
            "separate domain",
            "carrier-only",
            "not equivalence",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.mpaa)

    def test_bec_evidence_overlap_does_not_transfer_verdicts(self):
        for phrase in (
            "partially overlapping at the generic record level",
            "non-duplicative at the claim level",
            "FULL-for-task",
            "return_state: closed",
            "carried-not-imported",
            "conclusion_imported: false",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.bec)

    def test_bec_mapping_records_the_log_mismatch(self):
        self.assertIn("2026-07-26 corpus verification log", self.bec)
        self.assertIn("hybrid concept", self.bec)
        self.assertIn("appends the missing review", self.bec)


if __name__ == "__main__":
    unittest.main()
