# PCA Reference Validator

The validator checks a PCA v0.2-draft Transition Record against the canonical schema and PCA semantic boundaries.

## Command

```bash
python validator/pca_validate.py <record.json>
python validator/pca_validate.py <record.json> --json
python validator/pca_validate.py <record.json> --quiet
```

Canonical schema override is available for test/audit use:

```bash
python validator/pca_validate.py <record.json> --schema schema/pca-transition-record.schema.json
```

## Exit codes

| Code | Meaning |
|---|---|
| `0` | structurally and semantically valid record |
| `1` | invalid record |
| `2` | malformed/unreadable input, invalid schema, or validator-boundary failure |

`--quiet` suppresses output without changing the exit code.

## Validation stages

1. **Strict parse** — UTF-8 input, RFC 8259 finite numbers, no duplicate keys.
2. **Schema** — canonical Draft 2020-12 identity and a dependency-free audited keyword subset.
3. **Reference integrity** — unique identifiers, resolved evidence references, and bidirectional support attribution.
4. **Semantic checks** — verified evidence for resolved dimensions, timestamp ordering, transition receipt on carrier/host/model change, memory-commit requirement, and translation evidence.
5. **Derived status** — independently recompute `CONFORMING`, `EVOLVING`, `FORK`, `INCOMPATIBLE`, or `UNDETERMINED`.

A failure at an earlier boundary prevents a later interpretation from making the input appear valid.

## Dependency-free schema engine

`mini_jsonschema.py` is vendored from MPAA accepted commit `1d369f6cd091b99f9492cfaf730f0a170b55106e` and is used only as a small auditable validator for the keywords present in the PCA schema. PCA does not import MPAA semantics by reusing this utility.

Unknown schema keywords and malformed local `$ref` targets fail closed.

## Security boundary

Untrusted records must not produce an uncaught traceback. The CLI converts parser, schema, and unexpected validator-boundary errors into controlled output and exit status.

The reference validator does not authenticate external sources, execute referenced actions, or prove identity, consciousness, memory, or uninterrupted persistence.

## Tests

Runtime validation has no third-party dependency. The differential schema-parity test uses `jsonschema` as a test/CI oracle only; CI installs it explicitly.

```bash
python -m unittest discover -s validator -p "test_*.py" -v
```
