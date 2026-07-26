#!/usr/bin/env python3
"""Fail-closed reference validator for PCA Transition Records.

Exit codes: 0=VALID, 1=INVALID record, 2=tool/parser failure.
The validator establishes record consistency and PCA admissibility only. It
cannot prove identity, subjectivity, uninterrupted persistence, or conclusions
owned by MPAA/BEC.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from mini_jsonschema import MiniValidator

HERE = Path(__file__).resolve().parent
DEFAULT_SCHEMA = HERE.parent / "schema" / "pca-transition-record.schema.json"
SCHEMA_DIALECT = "https://json-schema.org/draft/2020-12/schema"
SCHEMA_ID = "https://github.com/gv1983us-commits/pca/schema/pca-transition-record.schema.json"
DIMENSIONS = ("provenance", "semantic", "methodological", "historical", "operational", "ethical", "evolution")
CLAIM_FIELDS = ("origin", "inherited", "reconstructed", "changed", "unknown", "breaks")


class DuplicateKeyError(ValueError):
    pass


def _object_no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate key {key!r}")
        result[key] = value
    return result


def _reject_non_finite(value: str):
    raise ValueError(f"non-finite JSON number {value!r} is forbidden")


def parse_json_strict(text: str) -> tuple[Any | None, str | None]:
    try:
        return json.loads(text, object_pairs_hook=_object_no_duplicates, parse_constant=_reject_non_finite), None
    except (DuplicateKeyError, ValueError, json.JSONDecodeError) as exc:
        return None, f"invalid JSON: {exc}"


@dataclass
class ValidationReport:
    valid: bool = False
    errors: list[str] = field(default_factory=list)
    tool_error: str | None = None
    derived_status: str | None = None

    def as_dict(self) -> dict:
        return {
            "valid": self.valid,
            "derived_status": self.derived_status,
            "errors": self.errors,
            "tool_error": self.tool_error,
        }


def _load_json(path: Path) -> tuple[Any | None, str | None]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return None, f"cannot read {path}: {exc}"
    return parse_json_strict(text)


def _statement_index(record: dict) -> tuple[dict[str, dict], list[str]]:
    index: dict[str, dict] = {}
    errors: list[str] = []
    claim = record.get("claim", {})
    if not isinstance(claim, dict):
        return index, errors
    for field_name in CLAIM_FIELDS:
        values = claim.get(field_name, [])
        if not isinstance(values, list):
            continue
        for position, statement in enumerate(values):
            if not isinstance(statement, dict):
                continue
            statement_id = statement.get("statement_id")
            if not isinstance(statement_id, str):
                continue
            if statement_id in index:
                errors.append(f"duplicate statement_id {statement_id!r} at claim.{field_name}[{position}]")
            else:
                index[statement_id] = statement
    return index, errors


def _evidence_index(record: dict) -> tuple[dict[str, dict], list[str]]:
    index: dict[str, dict] = {}
    errors: list[str] = []
    evidence = record.get("evidence", [])
    if not isinstance(evidence, list):
        return index, errors
    for position, item in enumerate(evidence):
        if not isinstance(item, dict):
            continue
        evidence_id = item.get("evidence_id")
        if not isinstance(evidence_id, str):
            continue
        if evidence_id in index:
            errors.append(f"duplicate evidence_id {evidence_id!r} at evidence[{position}]")
        else:
            index[evidence_id] = item
    return index, errors


def _check_reference_integrity(record: dict) -> list[str]:
    statements, errors = _statement_index(record)
    evidence, evidence_errors = _evidence_index(record)
    errors.extend(evidence_errors)
    claim = record.get("claim", {})

    def require_evidence(ref: Any, owner: str, support_target: str):
        if not isinstance(ref, str):
            return
        item = evidence.get(ref)
        if item is None:
            errors.append(f"{owner} references unknown evidence {ref!r}")
            return
        supports = item.get("supports", [])
        if support_target not in supports:
            errors.append(f"{owner} references evidence {ref!r} that does not support {support_target!r}")

    if isinstance(claim, dict):
        for field_name in CLAIM_FIELDS:
            for statement in claim.get(field_name, []) if isinstance(claim.get(field_name, []), list) else []:
                if not isinstance(statement, dict):
                    continue
                sid = statement.get("statement_id")
                for ref in statement.get("evidence_refs", []) if isinstance(statement.get("evidence_refs", []), list) else []:
                    require_evidence(ref, f"statement {sid!r}", sid)
        status = claim.get("status", {})
        dimensions = status.get("dimensions", {}) if isinstance(status, dict) else {}
        if isinstance(dimensions, dict):
            for name in DIMENSIONS:
                dimension = dimensions.get(name, {})
                if not isinstance(dimension, dict):
                    continue
                for ref in dimension.get("evidence_refs", []) if isinstance(dimension.get("evidence_refs", []), list) else []:
                    require_evidence(ref, f"dimension {name!r}", f"dimension:{name}")

    translation = record.get("translation")
    if isinstance(translation, dict):
        for ref in translation.get("evidence_refs", []) if isinstance(translation.get("evidence_refs", []), list) else []:
            require_evidence(ref, "translation", "translation")

    target_refs: dict[str, set[str]] = {}
    for statement_id, statement in statements.items():
        refs = statement.get("evidence_refs", [])
        target_refs[statement_id] = set(refs) if isinstance(refs, list) else set()
    if isinstance(dimensions, dict):
        for name in DIMENSIONS:
            dimension = dimensions.get(name, {})
            refs = dimension.get("evidence_refs", []) if isinstance(dimension, dict) else []
            target_refs[f"dimension:{name}"] = set(refs) if isinstance(refs, list) else set()
    if isinstance(translation, dict):
        refs = translation.get("evidence_refs", [])
        target_refs["translation"] = set(refs) if isinstance(refs, list) else set()

    valid_targets = set(target_refs)
    for evidence_id, item in evidence.items():
        for target in item.get("supports", []) if isinstance(item.get("supports", []), list) else []:
            if target not in valid_targets:
                errors.append(f"evidence {evidence_id!r} supports unknown target {target!r}")
            elif evidence_id not in target_refs[target]:
                errors.append(f"evidence {evidence_id!r} supports {target!r}, but that target does not cite it back")
    return errors


def _parse_timestamp(value: Any) -> dt.datetime | None:
    if not isinstance(value, str):
        return None
    try:
        normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
        return dt.datetime.fromisoformat(normalized)
    except ValueError:
        return None


def _verified_evidence(record: dict, evidence_type: str | None = None) -> list[dict]:
    values = record.get("evidence", [])
    if not isinstance(values, list):
        return []
    return [
        item for item in values
        if isinstance(item, dict)
        and item.get("verified") is True
        and (evidence_type is None or item.get("type") == evidence_type)
    ]


def _derive_status(record: dict) -> str | None:
    claim = record.get("claim")
    if not isinstance(claim, dict):
        return None
    status = claim.get("status")
    dimensions = status.get("dimensions") if isinstance(status, dict) else None
    if not isinstance(dimensions, dict):
        return None
    values = [dimensions.get(name, {}).get("status") for name in DIMENSIONS if isinstance(dimensions.get(name), dict)]
    if len(values) != len(DIMENSIONS):
        return None
    if "FORK" in values:
        return "FORK"
    if "INCOMPATIBLE" in values:
        return "INCOMPATIBLE"
    if "UNDETERMINED" in values or bool(claim.get("unknown")):
        return "UNDETERMINED"
    if "EVOLVING" in values or any(claim.get(name) for name in ("reconstructed", "changed", "breaks")):
        return "EVOLVING"
    return "CONFORMING"


def _check_semantics(record: dict) -> tuple[list[str], str | None]:
    errors: list[str] = []
    evidence, _ = _evidence_index(record)
    claim = record.get("claim", {})
    status = claim.get("status", {}) if isinstance(claim, dict) else {}
    dimensions = status.get("dimensions", {}) if isinstance(status, dict) else {}

    if isinstance(dimensions, dict):
        for name in DIMENSIONS:
            dimension = dimensions.get(name)
            if not isinstance(dimension, dict):
                continue
            if dimension.get("status") != "UNDETERMINED":
                refs = dimension.get("evidence_refs", [])
                if not refs:
                    errors.append(f"dimension {name!r} has a resolved status without evidence")
                for ref in refs if isinstance(refs, list) else []:
                    item = evidence.get(ref)
                    if isinstance(item, dict) and item.get("verified") is not True:
                        errors.append(f"dimension {name!r} relies on unverified evidence {ref!r}")

    if isinstance(claim, dict):
        for field_name in ("origin", "inherited", "reconstructed", "changed", "breaks"):
            values = claim.get(field_name, [])
            for statement in values if isinstance(values, list) else []:
                if not isinstance(statement, dict):
                    continue
                refs = statement.get("evidence_refs", [])
                if not refs:
                    errors.append(
                        f"resolved statement {statement.get('statement_id')!r} in {field_name!r} requires evidence"
                    )

    transition = record.get("transition", {})
    from_state = transition.get("from_state", {}) if isinstance(transition, dict) else {}
    to_state = transition.get("to_state", {}) if isinstance(transition, dict) else {}
    if isinstance(from_state, dict) and isinstance(to_state, dict):
        if from_state.get("state_id") == to_state.get("state_id"):
            errors.append("transition from_state.state_id and to_state.state_id must differ")

    recorded_at = _parse_timestamp(record.get("recorded_at"))
    occurred_at = _parse_timestamp(transition.get("occurred_at")) if isinstance(transition, dict) else None
    if recorded_at is not None and occurred_at is not None and recorded_at < occurred_at:
        errors.append("recorded_at predates transition.occurred_at")
    for evidence_id, item in evidence.items():
        observed_at = _parse_timestamp(item.get("observed_at"))
        if observed_at is None:
            continue
        if recorded_at is not None and observed_at > recorded_at:
            errors.append(f"evidence {evidence_id!r} observed_at postdates recorded_at")
        if item.get("type") == "transition-receipt" and occurred_at is not None and observed_at < occurred_at:
            errors.append(f"transition-receipt evidence {evidence_id!r} predates transition.occurred_at")

    changed_carrier = any(
        from_state.get(key) != to_state.get(key)
        for key in ("carrier_ref", "host_ref", "model_ref")
        if key in from_state or key in to_state
    ) if isinstance(from_state, dict) and isinstance(to_state, dict) else False
    if changed_carrier:
        receipts = [item for item in _verified_evidence(record, "transition-receipt") if "dimension:provenance" in item.get("supports", [])]
        if not receipts:
            errors.append("carrier/host/model changed without verified transition-receipt evidence for provenance")

    if isinstance(claim, dict):
        inherited = claim.get("inherited", [])
        for statement in inherited if isinstance(inherited, list) else []:
            if not isinstance(statement, dict) or statement.get("kind") != "memory":
                continue
            sid = statement.get("statement_id")
            refs = statement.get("evidence_refs", [])
            supported = any(
                isinstance(evidence.get(ref), dict)
                and evidence[ref].get("type") == "memory-commit"
                and evidence[ref].get("verified") is True
                and sid in evidence[ref].get("supports", [])
                for ref in refs if isinstance(refs, list)
            )
            if not supported:
                errors.append(f"inherited memory statement {sid!r} lacks verified memory-commit evidence; reading a trace is not memory")

    translation = record.get("translation")
    if isinstance(translation, dict):
        if translation.get("source_mode") == translation.get("target_mode"):
            errors.append("translation source_mode and target_mode must differ")
        if translation.get("target_mode") != record.get("usage_mode"):
            errors.append("translation target_mode must equal the record usage_mode")
        refs = translation.get("evidence_refs", [])
        if not any(
            isinstance(evidence.get(ref), dict)
            and evidence[ref].get("type") == "translation-record"
            and evidence[ref].get("verified") is True
            and "translation" in evidence[ref].get("supports", [])
            for ref in refs if isinstance(refs, list)
        ):
            errors.append("translation lacks verified translation-record evidence")

    derived = _derive_status(record)
    declared = status.get("overall") if isinstance(status, dict) else None
    if derived is not None and declared != derived:
        errors.append(f"declared overall status {declared!r} does not match derived status {derived!r}")
    return errors, derived


def validate_record(record_path: Path, schema_path: Path = DEFAULT_SCHEMA) -> ValidationReport:
    report = ValidationReport()
    record, record_error = _load_json(record_path)
    if record_error:
        report.tool_error = record_error
        return report
    schema, schema_error = _load_json(schema_path)
    if schema_error:
        report.tool_error = schema_error
        return report
    if not isinstance(schema, dict) or schema.get("$schema") != SCHEMA_DIALECT or schema.get("$id") != SCHEMA_ID:
        report.tool_error = "schema is not the canonical PCA Draft 2020-12 schema"
        return report
    schema_errors = MiniValidator(schema).validate(record)
    schema_definition_errors = [error for error in schema_errors if error.path.startswith("$schema")]
    if schema_definition_errors:
        report.tool_error = "; ".join(
            f"{error.path}: {error.message}" for error in schema_definition_errors
        )
        return report
    if schema_errors:
        report.errors.extend(f"{error.path}: {error.message}" for error in schema_errors)
        return report
    if not isinstance(record, dict):
        report.errors.append("record root must be an object")
        return report
    report.errors.extend(_check_reference_integrity(record))
    semantic_errors, derived = _check_semantics(record)
    report.errors.extend(semantic_errors)
    report.derived_status = derived
    report.valid = not report.errors
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a PCA Transition Record")
    parser.add_argument("record", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = validate_record(args.record, args.schema)
    except Exception as exc:  # final boundary: never traceback on untrusted input
        report = ValidationReport(tool_error=f"validator boundary failure: {type(exc).__name__}: {exc}")
    if not args.quiet:
        if args.as_json:
            print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2))
        elif report.tool_error:
            print(f"TOOL-ERROR: {report.tool_error}")
        elif report.valid:
            print(f"VALID ({report.derived_status})")
        else:
            print("INVALID")
            for error in report.errors:
                print(f"- {error}")
    if report.tool_error:
        return 2
    return 0 if report.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
