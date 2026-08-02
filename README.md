# PCA — Process Continuity Architecture

[![PCA CI](https://github.com/gv1983us-commits/pca/actions/workflows/ci.yml/badge.svg)](https://github.com/gv1983us-commits/pca/actions/workflows/ci.yml)

**PCA** is an exploratory architecture for recording and testing bounded claims that a process continued across a change of carrier, host, model, corpus state, or usage mode.

Its central boundary is:

```text
process continuation != identity
```

A valid PCA record does not prove consciousness, subjectivity, personal identity, or uninterrupted persistence.

## Current repository surfaces

| Surface | Role |
|---|---|
| [`spec/01_PCA_CORE.md`](spec/01_PCA_CORE.md) | portable normative Core |
| [`schema/pca-transition-record.schema.json`](schema/pca-transition-record.schema.json) | canonical Draft 2020-12 transition-record schema |
| [`validator/pca_validate.py`](validator/pca_validate.py) | dependency-free fail-closed reference validator |
| [`profiles/01_HISTORICAL_RECONSTRUCTION_PROFILE.md`](profiles/01_HISTORICAL_RECONSTRUCTION_PROFILE.md) | non-normative reconstruction discipline |
| [`profiles/02_TRANSLATION_USAGE_MODE_PROFILE.md`](profiles/02_TRANSLATION_USAGE_MODE_PROFILE.md) | non-normative translation profile |
| [`examples/PROJECT_PROVENANCE_JARVIS.md`](examples/PROJECT_PROVENANCE_JARVIS.md) | provenance-bearing project example, explicitly non-normative |
| [`conformance/`](conformance/) | positive, negative, parser, and derivation fixtures |
| [`verification/`](verification/) | corpus verification and MPAA/PCA terminology mapping |
| [`spec/00_PCA_SPEC.md`](spec/00_PCA_SPEC.md) | preserved integrated v0.1 source draft, superseded as active Core |

The Core is readable and implementable without knowledge of the originating project vocabulary.

## One verification command

```bash
python -m unittest discover -s validator -p "test_*.py" -v
```

Validate one record:

```bash
python validator/pca_validate.py conformance/fixtures/01-valid-continuation-claim.json
```

Exit codes are `0=VALID`, `1=INVALID record`, and `2=parser/tool/schema boundary failure`.

GitHub Actions compiles the validator, runs the regression and schema-parity suites, and validates canonical positive fixtures on Python 3.10, 3.11, 3.12, and 3.13.

## What is machine-checked

- strict JSON parsing: malformed input, duplicate keys, and non-finite values fail closed;
- canonical schema identity and supported Draft 2020-12 subset;
- required `origin / inherited / reconstructed / changed / unknown / breaks` decomposition;
- all seven independent continuity dimensions;
- unique and bidirectional statement/evidence references;
- verified evidence for resolved dimensions;
- transition-receipt evidence when carrier, host, or model changes;
- temporal ordering between transition, evidence observations, and record creation;
- memory-commit evidence before inherited `memory` can be claimed;
- explicit `PRESERVED / LOST / GAINED / ALTERED` usage-mode translation;
- independent recomputation of overall status;
- structural prohibition of identity, subjectivity, and uninterrupted-persistence claims.

The validator checks record admissibility. It does not establish that the world described by supplied evidence is true.

## Neutral portability example

The primary valid fixture describes migration of a municipal notification service between hosts. It uses no Jarvis/Hermes vocabulary. The project-origin vocabulary remains in a separate example so provenance is preserved without becoming universal canon.

## Neighboring specification boundaries

- **MPAA** owns agent architecture, identity-profile rules, runtime reports, and its own terms. MPAA coordination or identity-profile continuity does not establish PCA process continuation.
- **BEC** owns portable execution-evidence acceptance and deployment-level derivation. Verified execution or `closed` does not establish a committed PCA next state.
- **PCA** owns only the transition-continuity assessment defined here.

The pinned relation is documented in [`verification/terminology-mapping-mpaa-pca.md`](verification/terminology-mapping-mpaa-pca.md). Citation does not transfer normative ownership.

## Status

PCA v0.2 is a **public exploratory draft**. It now has a canonical schema, reference validator, regression fixtures, a neutral portability example, and corpus-verification records. It has **no independent implementation report** and does not claim multi-implementation conformance.

## License

Apache-2.0. See [`LICENSE`](LICENSE).
