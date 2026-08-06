"""Executable publication gates for the PCA artifact canon."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SURFACES = {
    "README.md",
    "CANON.md",
    "ARTIFACT.json",
    "RELATIONS.md",
    "PROVENANCE.md",
    "spec/00_PCA_SPEC.md",
    "spec/01_PCA_CORE.md",
    "schema/pca-transition-record.schema.json",
    "validator/pca_validate.py",
    "verification/terminology-mapping-mpaa-pca.md",
    "verification/terminology-mapping-bec-pca.md",
}

EXPECTED_RELATIONS = {
    "claude.bec": "62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261",
    "claude.mpaa": "0d1aaf35cc4826622f3312fdd2a1c2d40890b965",
    "claude.review_protocol": "e2ff9182014d8a8f3c3e7ea1ea269eecb8679035",
    "claude.arb": "6b6c32cd467a4b5e4863d082b9da5bdd40d7dced",
    "claude.cdts": "f91dbc003519efd5264655d905d0530dbfeac2fd",
}


class ArtifactCanonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.passport = json.loads((ROOT / "ARTIFACT.json").read_text(encoding="utf-8"))
        cls.canon = (ROOT / "CANON.md").read_text(encoding="utf-8")
        cls.core = (ROOT / "spec" / "01_PCA_CORE.md").read_text(encoding="utf-8")
        cls.relations = (ROOT / "RELATIONS.md").read_text(encoding="utf-8")
        cls.provenance = (ROOT / "PROVENANCE.md").read_text(encoding="utf-8")
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.schema = json.loads(
            (ROOT / "schema" / "pca-transition-record.schema.json").read_text(encoding="utf-8")
        )

    def test_required_surfaces_exist(self):
        missing = sorted(path for path in REQUIRED_SURFACES if not (ROOT / path).is_file())
        self.assertEqual([], missing)

    def test_machine_passport_identity(self):
        self.assertEqual("claude.pca", self.passport["artifact_id"])
        self.assertEqual("gv1983us-commits/pca", self.passport["repository"])
        self.assertEqual("0.2-draft", self.passport["artifact_version"])
        self.assertEqual("0.2-draft", self.passport["record_schema_version"])
        self.assertEqual("canonical_public_draft", self.passport["artifact_status"])
        self.assertEqual("exploratory_public_draft", self.passport["specification_status"])
        self.assertEqual("Apache-2.0", self.passport["license"])

    def test_two_surface_normative_authority(self):
        self.assertEqual("two_surface_domain_ownership_matrix", self.passport["normative_authority_model"])
        self.assertEqual(2, self.passport["normative_surface_count"])
        surfaces = self.passport["normative_surfaces"]
        self.assertEqual(
            ["spec/01_PCA_CORE.md", "schema/pca-transition-record.schema.json"],
            [item["path"] for item in surfaces],
        )
        self.assertFalse(self.passport["reference_implementation"]["normative"])
        self.assertIn("exactly two active normative surfaces", self.canon)
        self.assertIn("validator implements both", self.core)
        self.assertIn("does not become a third specification", self.core)

    def test_schema_identity_matches_passport(self):
        self.assertEqual("0.2-draft", self.schema["properties"]["pca_version"]["const"])
        self.assertEqual(
            "https://github.com/gv1983us-commits/pca/schema/pca-transition-record.schema.json",
            self.schema["$id"],
        )

    def test_assertion_boundaries_remain_false(self):
        boundaries = self.passport["assertion_boundaries"]
        self.assertTrue(boundaries)
        self.assertTrue(all(value is False for value in boundaries.values()))
        for phrase in (
            "identity_established",
            "subjectivity_established",
            "uninterrupted_persistence_established",
        ):
            self.assertIn(phrase, json.dumps(self.passport, ensure_ascii=False))

    def test_neighbor_revisions_and_no_import(self):
        actual = {item["artifact_id"]: item for item in self.passport["relations"]}
        self.assertEqual(set(EXPECTED_RELATIONS), set(actual))
        for artifact_id, revision in EXPECTED_RELATIONS.items():
            with self.subTest(artifact_id=artifact_id):
                self.assertRegex(revision, r"^[0-9a-f]{40}$")
                self.assertEqual(revision, actual[artifact_id]["reviewed_revision"])
                self.assertFalse(actual[artifact_id]["conclusion_imported"])
                self.assertIn(revision, self.relations)

    def test_cdts_owns_cross_domain_correlation(self):
        historical = self.passport["historical_boundaries"]
        self.assertFalse(historical["v0_1_linkage_record_is_current_pca_requirement"])
        self.assertTrue(historical["v0_1_linkage_record_is_cdts_precursor"])
        self.assertIn("historical precursors to the separate **Cross-Domain Trace Set (CDTS)** artifact", self.canon)
        self.assertIn("CDTS owns portable cross-domain correlation traces", self.relations)
        self.assertIn("They are not active PCA rules", self.core)

    def test_canonical_checks_are_declared(self):
        checks = self.passport["canonical_checks"]
        self.assertEqual(4, len(checks))
        self.assertIn('python -m unittest discover -s validator -p "test_*.py" -v', checks)
        self.assertIn('python -m unittest discover -s verification -p "test_*.py" -v', checks)
        self.assertTrue(any("01-valid-continuation-claim.json" in command for command in checks))
        self.assertTrue(any("05-valid-usage-mode-translation.json" in command for command in checks))

    def test_active_core_uses_current_canonical_neighbor_revisions(self):
        self.assertIn(EXPECTED_RELATIONS["claude.mpaa"], self.core)
        self.assertIn(EXPECTED_RELATIONS["claude.bec"], self.core)
        self.assertNotIn("1d369f6cd091b99f9492cfaf730f0a170b55106e", self.core)
        self.assertNotIn("bb46f5f8aac96d1cffba7a334c5d17fb331ef3af", self.core)

    def test_provenance_records_gap_without_rewriting_history(self):
        self.assertIn("mismatch was identified", self.provenance)
        self.assertIn("terminology-mapping-bec-pca.md", self.provenance)
        self.assertIn("earlier log is preserved rather than rewritten", self.provenance)

    def test_readme_exposes_canonical_entry(self):
        for path in ("CANON.md", "ARTIFACT.json", "RELATIONS.md", "PROVENANCE.md"):
            with self.subTest(path=path):
                self.assertIn(path, self.readme)
        self.assertIn("canonical public draft", self.readme.lower())
        self.assertIn("two", self.readme.lower())

    def test_no_machine_local_or_secret_markers_in_canon_surfaces(self):
        combined = "\n".join((self.canon, self.relations, self.provenance, self.readme))
        forbidden = (
            r"[A-Za-z]:\\Users\\",
            r"/home/[^/\s]+/",
            r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY",
            r"ghp_[A-Za-z0-9]{20,}",
        )
        for pattern in forbidden:
            with self.subTest(pattern=pattern):
                self.assertIsNone(re.search(pattern, combined))


if __name__ == "__main__":
    unittest.main()
