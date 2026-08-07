# PCA — Process Continuity Architecture

[![PCA CI](https://github.com/gv1983us-commits/pca/actions/workflows/ci.yml/badge.svg)](https://github.com/gv1983us-commits/pca/actions/workflows/ci.yml)

**PCA** is an exploratory architecture for recording and testing bounded claims that a process continued across a change of carrier, host, model, corpus state, or usage mode.

Its central boundary is:

```text
process continuation != identity
```

A valid PCA record does not prove consciousness, subjectivity, personal identity, uninterrupted persistence, causality, or world truth.

## Canonical artifact entry

PCA `0.2` is a **canonical public artifact**, sealed 2026-08-07. Canonical means that the repository now exposes one explicit identity, authority model, relation map, provenance record, and reproducible verification surface. It does not mean that PCA is a finalized standard or externally certified.

Start with:

| Surface | Role |
|---|---|
| [`CANON.md`](CANON.md) | authority model, exact-source rule, acceptance gates, and change discipline |
| [`ARTIFACT.json`](ARTIFACT.json) | machine-readable artifact identity, versions, surfaces, checks, relations, and limits |
| [`RELATIONS.md`](RELATIONS.md) | bounded relations to BEC, MPAA, Review Protocol, ARB, and CDTS |
| [`PROVENANCE.md`](PROVENANCE.md) | derivation, repository authority, corpus representation, and tool-participation record |

## Two-surface normative authority

PCA has exactly two active normative surfaces:

| Normative surface | Owned domain |
|---|---|
| [`spec/01_PCA_CORE.md`](spec/01_PCA_CORE.md) | semantic transition-continuity assessment |
| [`schema/pca-transition-record.schema.json`](schema/pca-transition-record.schema.json) | canonical Transition Record representation |

The reference validator implements both surfaces but is not a third specification:

```text
Core      -> semantic meaning and admissibility rules
Schema    -> machine-readable record shape
Validator -> fail-closed reference implementation
Fixtures  -> expected decisions
```

## Repository surfaces

| Surface | Role |
|---|---|
| [`spec/01_PCA_CORE.md`](spec/01_PCA_CORE.md) | portable normative semantic Core |
| [`schema/pca-transition-record.schema.json`](schema/pca-transition-record.schema.json) | canonical Draft 2020-12 Transition Record Schema |
| [`validator/pca_validate.py`](validator/pca_validate.py) | dependency-free fail-closed reference validator |
| [`conformance/`](conformance/) | positive, negative, malformed-input, reference, and derivation fixtures |
| [`profiles/01_HISTORICAL_RECONSTRUCTION_PROFILE.md`](profiles/01_HISTORICAL_RECONSTRUCTION_PROFILE.md) | non-normative reconstruction discipline |
| [`profiles/02_TRANSLATION_USAGE_MODE_PROFILE.md`](profiles/02_TRANSLATION_USAGE_MODE_PROFILE.md) | non-normative translation profile |
| [`examples/PROJECT_PROVENANCE_JARVIS.md`](examples/PROJECT_PROVENANCE_JARVIS.md) | provenance-bearing project example, explicitly non-normative |
| [`verification/`](verification/) | fixed-revision corpus, terminology, relation, and artifact-canon checks |
| [`spec/00_PCA_SPEC.md`](spec/00_PCA_SPEC.md) | preserved integrated v0.1 source draft, superseded as active Core |

The Core is readable and implementable without knowledge of the originating project vocabulary.

The Linkage Record and six-item trace proposal preserved in v0.1 section 24 are historical precursors to the separate CDTS artifact. They are not active PCA requirements.

## Canonical verification

From the repository root:

```bash
python -m unittest discover -s validator -p "test_*.py" -v
python -m unittest discover -s verification -p "test_*.py" -v
python validator/pca_validate.py conformance/fixtures/01-valid-continuation-claim.json --quiet
python validator/pca_validate.py conformance/fixtures/05-valid-usage-mode-translation.json --quiet
```

Validate one record:

```bash
python validator/pca_validate.py conformance/fixtures/01-valid-continuation-claim.json
```

Exit codes are:

```text
0 = VALID
1 = INVALID record
2 = parser, input, Schema, or validator-boundary failure
```

GitHub Actions compiles the validator and verification checks, validates the machine passport, runs regression and Schema-parity suites, runs artifact and fixed-revision publication gates, and validates canonical positive fixtures on Python 3.10, 3.11, 3.12, and 3.13.

## What is machine-checked

- strict JSON parsing: malformed input, duplicate keys, and non-finite values fail closed;
- canonical Schema identity and supported Draft 2020-12 subset;
- required `origin / inherited / reconstructed / changed / unknown / breaks` decomposition;
- all seven independent continuity dimensions;
- unique and bidirectional statement/evidence references;
- verified evidence for resolved dimensions;
- transition-receipt evidence when carrier, host, or model changes;
- temporal ordering between transition, evidence observations, and record creation;
- memory-commit evidence before inherited `memory` can be claimed;
- explicit `PRESERVED / LOST / GAINED / ALTERED` usage-mode translation;
- independent recomputation of overall status;
- structural prohibition of identity, subjectivity, and uninterrupted-persistence claims;
- artifact identity, two-surface authority, exact neighbor revisions, relation boundaries, provenance correction, and canonical file presence.

The validator checks record admissibility. It does not establish that the world described by supplied evidence is true.

## Neutral portability example

The primary valid fixture describes migration of a municipal notification service between hosts. It uses no Jarvis/Hermes vocabulary.

Project-origin vocabulary remains in a separate non-normative example so provenance is preserved without becoming universal canon.

## Neighboring artifact boundaries

- **BEC** owns task execution evidence, trust anchors, deployment level, and return state. `FULL-for-task` or `closed` does not establish PCA continuation.
- **MPAA** owns portable agent architecture, Identity Profile, runtime semantics, Runtime Report representation, and conformance. Identity-profile or session continuity does not establish PCA continuation.
- **Review Protocol** owns source-selection and bounded review receipts. A completed review does not establish PCA validity.
- **ARB** is a non-normative analytical companion and does not amend PCA.
- **CDTS** owns cross-domain correlation traces. A CDTS linkage or admissibility result does not validate or import a PCA conclusion.

The exact reviewed revisions and permitted/forbidden mappings are recorded in [`RELATIONS.md`](RELATIONS.md), [`verification/terminology-mapping-mpaa-pca.md`](verification/terminology-mapping-mpaa-pca.md), and [`verification/terminology-mapping-bec-pca.md`](verification/terminology-mapping-bec-pca.md).

## Status and limits

```text
artifact_id: claude.pca
artifact_version: 0.2
record_schema_version: 0.2
canonical_status: canonical_public
normative_authority: two surfaces
```

PCA has a canonical Schema, reference validator, regression fixtures, neutral portability examples, profiles, fixed-revision verification, and executable artifact-canon gates.

PCA has **no independent implementation report**, makes no multi-implementation conformance claim, and does not claim external certification.

## License

Apache-2.0. See [`LICENSE`](LICENSE).
