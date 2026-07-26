# PCA Conformance Fixtures

Run the complete executable matrix:

```bash
python -m unittest discover -s validator -p "test_*.py" -v
```

## Canonical fixtures

| Fixture | Expected exit | Boundary |
|---|---:|---|
| `01-valid-continuation-claim.json` | 0 | neutral valid host migration with explicit evolution |
| `02-invalid-identity-from-continuation.json` | 1 | continuation cannot establish identity |
| `03-invalid-reading-as-memory.json` | 1 | archive/trace access is not inherited memory |
| `04-invalid-host-change-without-trace.json` | 1 | changed host requires verified transition receipt |
| `05-valid-usage-mode-translation.json` | 0 | preserved/lost/gained/altered translation record |
| `06-schema-invalid-missing-unknown.json` | 1 | all claim decomposition collections are explicit |
| `07-malformed-duplicate-key.json` | 2 | duplicate JSON keys fail at parser boundary |
| `08-malformed-nan.json` | 2 | non-finite JSON values fail at parser boundary |
| `09-invalid-derived-status.json` | 1 | producer cannot self-award overall status |
| `10-invalid-evidence-attribution.json` | 1 | evidence linkage is bidirectional |

The fixtures test claim boundaries, not metaphysical identity. Passing this matrix does not constitute an independent implementation report.

See [`RESISTANCE_CORPUS.md`](RESISTANCE_CORPUS.md) for the concrete failure pressures preserved by these regressions.
