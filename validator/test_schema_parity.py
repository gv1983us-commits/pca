#!/usr/bin/env python3
"""Differential structural checks against the canonical Draft 2020-12 oracle.

`jsonschema` is a test/CI dependency only. Runtime validation stays stdlib-only.
"""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:  # pragma: no cover - local runtime may intentionally omit it
    Draft202012Validator = None
    FormatChecker = None

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

import sys
sys.path.insert(0, str(HERE))
from mini_jsonschema import MiniValidator  # noqa: E402


def mutations(base: dict):
    for key in ("pca_version", "record_id", "process_ref", "usage_mode", "recorded_at", "transition", "claim", "evidence", "assertions"):
        value = copy.deepcopy(base)
        value.pop(key)
        yield f"missing-root-{key}", value

    for key, bad in (
        ("pca_version", "9"),
        ("record_id", ""),
        ("process_ref", ""),
        ("usage_mode", "secret"),
        ("recorded_at", "2026-99-99"),
        ("transition", []),
        ("claim", []),
        ("evidence", {}),
        ("assertions", []),
    ):
        value = copy.deepcopy(base)
        value[key] = bad
        yield f"bad-root-{key}", value

    value = copy.deepcopy(base)
    value["unexpected"] = True
    yield "additional-root-property", value

    for side in ("from_state", "to_state"):
        for key in ("state_id", "carrier_ref", "host_ref"):
            value = copy.deepcopy(base)
            value["transition"][side].pop(key)
            yield f"missing-{side}-{key}", value
        value = copy.deepcopy(base)
        value["transition"][side]["extra"] = "x"
        yield f"additional-{side}-property", value

    value = copy.deepcopy(base)
    value["transition"].pop("occurred_at")
    yield "missing-occurred-at", value
    value = copy.deepcopy(base)
    value["transition"]["occurred_at"] = "not-time"
    yield "bad-occurred-at", value

    for key in ("origin", "inherited", "reconstructed", "changed", "unknown", "breaks", "status"):
        value = copy.deepcopy(base)
        value["claim"].pop(key)
        yield f"missing-claim-{key}", value

    for dimension in ("provenance", "semantic", "methodological", "historical", "operational", "ethical", "evolution"):
        value = copy.deepcopy(base)
        value["claim"]["status"]["dimensions"].pop(dimension)
        yield f"missing-dimension-{dimension}", value
        value = copy.deepcopy(base)
        value["claim"]["status"]["dimensions"][dimension]["status"] = "PASS"
        yield f"bad-dimension-status-{dimension}", value

    for key in ("statement_id", "text", "kind", "evidence_refs"):
        value = copy.deepcopy(base)
        value["claim"]["origin"][0].pop(key)
        yield f"missing-statement-{key}", value
    value = copy.deepcopy(base)
    value["claim"]["origin"][0]["kind"] = "identity"
    yield "bad-statement-kind", value

    for key in ("evidence_id", "type", "source_ref", "observed_at", "supports", "verified"):
        value = copy.deepcopy(base)
        value["evidence"][0].pop(key)
        yield f"missing-evidence-{key}", value
    for key, bad in (("type", "memory"), ("supports", []), ("verified", "yes")):
        value = copy.deepcopy(base)
        value["evidence"][0][key] = bad
        yield f"bad-evidence-{key}", value

    for key in ("identity_established", "subjectivity_established", "uninterrupted_persistence_established"):
        value = copy.deepcopy(base)
        value["assertions"].pop(key)
        yield f"missing-assertion-{key}", value
        value = copy.deepcopy(base)
        value["assertions"][key] = True
        yield f"forbidden-assertion-{key}", value


@unittest.skipIf(Draft202012Validator is None, "jsonschema test oracle not installed")
class SchemaParityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / "schema" / "pca-transition-record.schema.json").read_text(encoding="utf-8"))
        cls.base = json.loads((ROOT / "conformance" / "fixtures" / "01-valid-continuation-claim.json").read_text(encoding="utf-8"))
        cls.oracle = Draft202012Validator(cls.schema, format_checker=FormatChecker())
        cls.mini = MiniValidator(cls.schema)

    def test_generated_schema_mutations_match_oracle(self):
        cases = list(mutations(self.base))
        self.assertGreaterEqual(len(cases), 60)
        mismatches = []
        for label, instance in cases:
            oracle_valid = not list(self.oracle.iter_errors(instance))
            mini_valid = not self.mini.validate(instance)
            if oracle_valid != mini_valid:
                mismatches.append((label, oracle_valid, mini_valid))
        self.assertEqual([], mismatches)

    def test_valid_fixture_matches_oracle(self):
        self.assertEqual([], list(self.oracle.iter_errors(self.base)))
        self.assertEqual([], self.mini.validate(self.base))

    def test_external_reference_boundary_matches_oracle(self):
        record = copy.deepcopy(self.base)
        reference = {
            "system": "BEC",
            "record_id": "bec-record-1",
            "revision": "bb46f5f8aac96d1cffba7a334c5d17fb331ef3af",
            "boundary": "Carried as data; not imported as a PCA conclusion.",
            "mapping": "carried-not-imported",
            "conclusion_imported": False,
        }
        record["external_references"] = [reference]
        self.assertEqual([], list(self.oracle.iter_errors(record)))
        self.assertEqual([], self.mini.validate(record))
        bad_cases = []
        for key in reference:
            value = copy.deepcopy(record)
            value["external_references"][0].pop(key)
            bad_cases.append(value)
        for key, bad in (("revision", "main"), ("mapping", "equivalent"), ("conclusion_imported", True)):
            value = copy.deepcopy(record)
            value["external_references"][0][key] = bad
            bad_cases.append(value)
        for value in bad_cases:
            self.assertTrue(list(self.oracle.iter_errors(value)))
            self.assertTrue(self.mini.validate(value))

    def test_unknown_schema_keyword_fails_closed(self):
        errors = MiniValidator({"type": "object", "unevaluatedProperties": False}).validate({})
        self.assertTrue(errors)
        self.assertIn("unsupported schema keyword", errors[0].message)


if __name__ == "__main__":
    unittest.main()
