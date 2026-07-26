#!/usr/bin/env python3
"""Regression tests for the PCA transition-record reference validator."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "validator" / "pca_validate.py"
FIXTURES = ROOT / "conformance" / "fixtures"


def run_fixture(name: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURES / name), "--json"],
        capture_output=True,
        text=True,
        check=False,
    )


def run_record(record: dict, *extra_args: str) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "record.json"
        path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(path), "--json", *extra_args],
            capture_output=True,
            text=True,
            check=False,
        )


class ValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((FIXTURES / "01-valid-continuation-claim.json").read_text(encoding="utf-8"))
    def assert_fixture(self, name: str, expected_exit: int, error_fragment: str | None = None):
        result = run_fixture(name)
        self.assertEqual(expected_exit, result.returncode, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        if error_fragment is not None:
            self.assertIn(error_fragment, "\n".join(payload["errors"]))
        return payload

    def test_valid_continuation_claim_passes(self):
        payload = self.assert_fixture("01-valid-continuation-claim.json", 0)
        self.assertTrue(payload["valid"])
        self.assertEqual([], payload["errors"])
        self.assertEqual("EVOLVING", payload["derived_status"])

    def test_identity_cannot_be_inferred_from_continuation(self):
        self.assert_fixture("02-invalid-identity-from-continuation.json", 1, "identity_established")

    def test_reading_a_trace_is_not_memory(self):
        self.assert_fixture("03-invalid-reading-as-memory.json", 1, "reading a trace is not memory")

    def test_host_change_requires_transition_trace(self):
        self.assert_fixture("04-invalid-host-change-without-trace.json", 1, "transition-receipt")

    def test_usage_mode_translation_records_all_change_classes(self):
        payload = self.assert_fixture("05-valid-usage-mode-translation.json", 0)
        self.assertEqual("CONFORMING", payload["derived_status"])

    def test_missing_unknown_is_schema_invalid(self):
        self.assert_fixture("06-schema-invalid-missing-unknown.json", 1, "unknown")

    def test_duplicate_keys_fail_as_parser_error(self):
        result = run_fixture("07-malformed-duplicate-key.json")
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("duplicate key", json.loads(result.stdout)["tool_error"])

    def test_non_finite_numbers_fail_as_parser_error(self):
        result = run_fixture("08-malformed-nan.json")
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("non-finite", json.loads(result.stdout)["tool_error"])

    def test_declared_status_is_recomputed(self):
        self.assert_fixture("09-invalid-derived-status.json", 1, "does not match derived status")

    def test_explicit_unknown_forces_undetermined_overall_status(self):
        def mutate(record):
            record["claim"]["unknown"] = [{
                "statement_id": "unknown-1",
                "text": "Whether an unexported queue survived is unknown.",
                "kind": "other",
                "evidence_refs": [],
            }]
        self.assert_mutation_rejected(mutate, "UNDETERMINED")

    def test_evidence_links_are_bidirectional(self):
        self.assert_fixture("10-invalid-evidence-attribution.json", 1, "does not support")

    def assert_mutation_rejected(self, mutate, fragment: str):
        record = copy.deepcopy(self.base)
        mutate(record)
        result = run_record(record)
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn(fragment, "\n".join(json.loads(result.stdout)["errors"]))

    def test_resolved_statement_requires_evidence(self):
        self.assert_mutation_rejected(
            lambda x: x["claim"]["inherited"][0].__setitem__("evidence_refs", []),
            "resolved statement",
        )

    def test_evidence_cannot_claim_unreferenced_support(self):
        def mutate(record):
            record["evidence"][0]["supports"].append("dimension:operational")
        self.assert_mutation_rejected(mutate, "does not cite it back")

    def test_translation_target_must_match_record_usage_mode(self):
        record = json.loads((FIXTURES / "05-valid-usage-mode-translation.json").read_text(encoding="utf-8"))
        record["usage_mode"] = "operational"
        result = run_record(record)
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn("target_mode", "\n".join(json.loads(result.stdout)["errors"]))

    def test_transition_state_ids_must_differ(self):
        self.assert_mutation_rejected(
            lambda x: x["transition"]["to_state"].__setitem__("state_id", x["transition"]["from_state"]["state_id"]),
            "state_id",
        )

    def test_recorded_at_is_required(self):
        self.assert_mutation_rejected(lambda x: x.pop("recorded_at"), "recorded_at")

    def test_occurred_at_is_required(self):
        self.assert_mutation_rejected(lambda x: x["transition"].pop("occurred_at"), "occurred_at")

    def test_record_cannot_predate_transition(self):
        self.assert_mutation_rejected(
            lambda x: x.__setitem__("recorded_at", "2026-07-26T11:00:00Z"),
            "recorded_at predates",
        )

    def test_transition_receipt_cannot_predate_transition(self):
        self.assert_mutation_rejected(
            lambda x: x["evidence"][0].__setitem__("observed_at", "2026-07-26T11:00:00Z"),
            "transition-receipt",
        )

    def test_evidence_cannot_postdate_record(self):
        self.assert_mutation_rejected(
            lambda x: x["evidence"][1].__setitem__("observed_at", "2026-07-26T13:00:00Z"),
            "postdates recorded_at",
        )

    def test_evidence_observed_at_is_required(self):
        self.assert_mutation_rejected(
            lambda x: x["evidence"][0].pop("observed_at"),
            "observed_at",
        )

    def test_quiet_preserves_invalid_exit_without_output(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), str(FIXTURES / "02-invalid-identity-from-continuation.json"), "--quiet"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertEqual("", result.stderr)

    def test_invalid_utf8_is_controlled_tool_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_bytes(b"\xff")
            result = subprocess.run(
                [sys.executable, str(VALIDATOR), str(path), "--json"],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("cannot read", json.loads(result.stdout)["tool_error"])

    def test_unsupported_custom_schema_fails_as_tool_error(self):
        schema = json.loads((ROOT / "schema" / "pca-transition-record.schema.json").read_text(encoding="utf-8"))
        schema["unevaluatedProperties"] = False
        with tempfile.TemporaryDirectory() as tmp:
            schema_path = Path(tmp) / "bad-schema.json"
            schema_path.write_text(json.dumps(schema), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    str(FIXTURES / "01-valid-continuation-claim.json"),
                    "--schema",
                    str(schema_path),
                    "--json",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("unsupported schema keyword", json.loads(result.stdout)["tool_error"])

    def test_external_record_can_be_carried_without_importing_conclusion(self):
        record = copy.deepcopy(self.base)
        record["external_references"] = [{
            "system": "MPAA",
            "record_id": "runtime-report-17",
            "revision": "1d369f6cd091b99f9492cfaf730f0a170b55106e",
            "boundary": "Carried as data; MPAA identity-profile continuity is not a PCA result.",
            "mapping": "carried-not-imported",
            "conclusion_imported": False,
        }]
        result = run_record(record)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("EVOLVING", json.loads(result.stdout)["derived_status"])

    def test_external_conclusion_import_is_forbidden(self):
        def mutate(record):
            record["external_references"] = [{
                "system": "BEC",
                "record_id": "bec-17",
                "revision": "bb46f5f8aac96d1cffba7a334c5d17fb331ef3af",
                "boundary": "BEC closed is carried, not a PCA next-state commitment.",
                "mapping": "carried-not-imported",
                "conclusion_imported": True,
            }]
        self.assert_mutation_rejected(mutate, "conclusion_imported")

    def test_neighbor_revision_must_be_pinned_commit(self):
        def mutate(record):
            record["external_references"] = [{
                "system": "MPAA",
                "record_id": "runtime-report-17",
                "revision": "main",
                "boundary": "Moving branch references are insufficient for normative mapping.",
                "mapping": "carried-not-imported",
                "conclusion_imported": False,
            }]
        self.assert_mutation_rejected(mutate, "revision")


if __name__ == "__main__":
    unittest.main()
