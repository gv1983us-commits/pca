# PCA Reference Validator

The validator checks a PCA `0.2` Transition Record against the canonical Schema and PCA Core semantic boundaries.

The active authority model is declared in [`../CANON.md`](../CANON.md):

```text
PCA Core   -> semantic rules
JSON Schema -> record representation
validator  -> non-normative reference implementation
```

## Command

```bash
python validator/pca_validate.py <record.json>
python validator/pca_validate.py <record.json> --json
python validator/pca_validate.py <record.json> --quiet
```

Canonical Schema override is available for test and audit use:

```bash
python validator/pca_validate.py <record.json> --schema schema/pca-transition-record.schema.json
```

## Exit codes

| Code | Meaning |
|---|---|
| `0` | structurally and semantically valid record |
| `1` | invalid record |
| `2` | malformed or unreadable input, invalid Schema, or validator-boundary failure |

`--quiet` suppresses output without changing the exit code.

## Validation stages

1. **Strict parse** — UTF-8 input, RFC 8259 finite numbers, no duplicate keys.
2. **Schema** — canonical Draft 2020-12 identity and the dependency-free audited keyword subset.
3. **Reference integrity** — unique identifiers, resolved evidence references, and bidirectional support attribution.
4. **Semantic checks** — verified evidence for resolved dimensions, timestamp ordering, transition receipt on carrier/host/model change, memory-commit requirement, and translation evidence.
5. **Derived status** — independent recomputation of `CONFORMING`, `EVOLVING`, `FORK`, `INCOMPATIBLE`, or `UNDETERMINED`.

A failure at an earlier boundary prevents a later interpretation from making the input appear valid.

## Dependency-free Schema engine

`mini_jsonschema.py` was originally vendored from the MPAA implementation state reviewed at historical commit `1d369f6cd091b99f9492cfaf730f0a170b55106e`.

The current canonical MPAA artifact relation is pinned separately in PCA's [`RELATIONS.md`](../RELATIONS.md) and does not change the origin of this copied utility.

The utility is used only as a small auditable implementation of the JSON Schema keywords present in the PCA Schema. Reuse does not import MPAA semantics, normative authority, conformance, or conclusions.

Unknown Schema keywords and malformed local `$ref` targets fail closed.

## Security boundary

Untrusted records must not produce an uncaught traceback. The CLI converts parser, Schema, and unexpected validator-boundary errors into controlled output and exit status.

The reference validator does not authenticate external sources, execute referenced actions, import neighboring verdicts, or prove identity, consciousness, memory, uninterrupted persistence, causality, or world truth.

## Tests

Runtime validation has no third-party dependency. The differential Schema-parity test uses `jsonschema` as a test and CI oracle only; CI installs it explicitly.

```bash
python -m unittest discover -s validator -p "test_*.py" -v
```

Artifact, relation, and fixed-revision publication checks run separately:

```bash
python -m unittest discover -s verification -p "test_*.py" -v
```
