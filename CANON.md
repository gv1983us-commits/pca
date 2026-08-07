# PCA Canon

**Artifact:** Process Continuity Architecture (PCA)  
**Corpus identity:** `claude.pca`  
**Repository:** `gv1983us-commits/pca`  
**PCA version:** `0.2`  
**Canonical status:** canonical public (sealed 2026-08-07)  
**Specification status:** exploratory public stable; not a finalized standard or external certification

This document declares how the public PCA repository is read, cited, checked, and changed as one technical artifact.

Canonicalization here does **not** mean that PCA proves continuity, identity, consciousness, memory, or world truth. It means that the repository has an explicit authority model, a machine-readable identity, reproducible checks, preserved provenance, and bounded relations to neighboring artifacts.

## 1. Two-surface normative set

PCA has exactly two active normative surfaces. Each owns a different domain.

| Surface | Path | Owned domain |
|---|---|---|
| PCA Core | [`spec/01_PCA_CORE.md`](spec/01_PCA_CORE.md) | purpose, scope, terminology, non-implication rules, claim decomposition, assessment dimensions, status derivation, evidence semantics, translation semantics, and cross-domain boundaries |
| Transition Record Schema | [`schema/pca-transition-record.schema.json`](schema/pca-transition-record.schema.json) | canonical machine-readable representation, required fields, types, enumerations, constants, and structural closure |

The authority model is a domain matrix:

```text
semantic meaning and admissibility rules → PCA Core
record representation and field shape   → JSON Schema
```

The Core does not silently override an invalid record shape. The Schema does not create semantic meaning merely because a field is structurally accepted.

If the two surfaces disagree, the repository is defective and the disagreement blocks canon acceptance. Neither the README, validator behavior, fixture text, profile, example, verification note, nor historical source draft may silently amend either normative surface.

## 2. Reference implementation and conformance

[`validator/pca_validate.py`](validator/pca_validate.py) is the fail-closed reference implementation of the Core and Schema. It performs strict parsing, schema validation, reference-integrity checks, semantic checks, and independent status derivation.

The validator is executable evidence that the normative contract is implementable. It is **not** a third normative specification and MUST NOT invent a claim domain or requirement absent from the Core or Schema.

[`validator/mini_jsonschema.py`](validator/mini_jsonschema.py) is a dependency-free implementation of the audited JSON Schema subset used by PCA. It is tooling, not normative authority.

[`conformance/`](conformance/) contains canonical positive, negative, malformed-input, reference-integrity, and derivation fixtures. Fixtures pin expected validator decisions; they do not prove that the world described by a valid record is true.

## 3. Historical and informative layers

The following surfaces are preserved but non-normative:

- [`spec/00_PCA_SPEC.md`](spec/00_PCA_SPEC.md) — integrated v0.1 source draft and derivation trace, superseded as active Core;
- [`profiles/`](profiles/) — historical-reconstruction and usage-mode guidance;
- [`examples/`](examples/) — provenance-bearing and portability examples;
- [`verification/`](verification/) — fixed-revision audits and relation checks;
- [`README.md`](README.md) and component READMEs — human orientation and operational guidance.

The Linkage Record and minimal cross-domain trace set in preserved v0.1 section 24 are historical precursors to the separate **Cross-Domain Trace Set (CDTS)** artifact. They are not active PCA requirements and MUST NOT be imported into a PCA Transition Record unless a future PCA version explicitly adopts a compatible rule through the Core and Schema.

A preserved source statement remains evidence of derivation even when its active normative ownership moved, narrowed, or was rejected.

## 4. Exact-source rule

`main` is the active public development line. A reproducible citation, review, evaluation, or implementation claim MUST pin an exact commit SHA or release tag. The word `latest` is not a stable source identifier.

A GitHub URL, archive, checkout, downstream copy, or generated summary is canonical only for the exact revision it identifies. Uncommitted local files, chat excerpts, private working copies, and unpublished drafts are not PCA canon.

A fixed-revision verification record remains a record about the revisions it names. Later repository changes do not silently update that record's conclusion.

## 5. Canonical artifact surfaces

| Surface | Path | Role |
|---|---|---|
| Human entry | [`README.md`](README.md) | orientation, reading order, commands, status, and boundaries |
| Canon declaration | [`CANON.md`](CANON.md) | authority model, source rule, acceptance gates, and change discipline |
| Machine passport | [`ARTIFACT.json`](ARTIFACT.json) | stable identity, versions, surfaces, checks, relations, and limits |
| Normative Core | [`spec/01_PCA_CORE.md`](spec/01_PCA_CORE.md) | PCA semantic contract |
| Canonical Schema | [`schema/pca-transition-record.schema.json`](schema/pca-transition-record.schema.json) | Transition Record representation |
| Reference validator | [`validator/pca_validate.py`](validator/pca_validate.py) | fail-closed reference interpretation |
| Conformance corpus | [`conformance/`](conformance/) | expected decisions and resistance cases |
| Relations | [`RELATIONS.md`](RELATIONS.md) | bounded links to the other five technical artifacts |
| Provenance | [`PROVENANCE.md`](PROVENANCE.md) | public authority, derivation, representation, and tool-participation record |
| Verification | [`verification/`](verification/) | fixed-revision terminology and boundary evidence |

## 6. Canonical verification

From the repository root:

```bash
python -m unittest discover -s validator -p "test_*.py" -v
python -m unittest discover -s verification -p "test_*.py" -v
python validator/pca_validate.py conformance/fixtures/01-valid-continuation-claim.json --quiet
python validator/pca_validate.py conformance/fixtures/05-valid-usage-mode-translation.json --quiet
```

The validator suite checks strict parsing, Schema parity, semantic boundaries, references, temporal ordering, evidence requirements, translation rules, external-reference boundaries, and status derivation.

The verification suite checks the artifact canon, fixed neighbor revisions, preserved-source dispositions, relation boundaries, and publication consistency.

Passing these commands establishes repository consistency at the tested revision. It does not authenticate record producers, external evidence, neighboring artifacts, causal relations, identities, memories, hidden state, or world truth.

## 7. Canon acceptance gates

A PCA revision is admissible to the canonical line only when all applicable gates pass:

1. **Domain ownership** — semantic changes occur in the Core; structural changes occur in the Schema; informative material remains identified as informative.
2. **Core/Schema coherence** — required fields, enumerations, derivation inputs, and prohibited claims agree.
3. **Validator alignment** — the reference validator implements declared rules and does not become a hidden third specification.
4. **Schema parity** — the dependency-free validator agrees with the Draft 2020-12 test oracle for the supported keyword subset.
5. **Conformance coverage** — changed behavior has positive, negative, malformed-input, or regression coverage as applicable.
6. **Explicit unknowns** — uncertainty is represented rather than converted into an unsupported positive or negative conclusion.
7. **Neighbor boundaries** — PCA does not import MPAA architecture or identity conclusions, BEC execution verdicts, Review Protocol receipts, ARB analysis, or CDTS correlation conclusions.
8. **Historical integrity** — the v0.1 source and fixed verification records remain distinguishable from the active Core.
9. **Provenance** — repository authority, corpus representation, human approval, model assistance, and mechanical verification remain separate.
10. **Public hygiene** — no secret, credential, private corpus, or machine-local path is required to read or verify the public artifact.
11. **CI** — the supported Python matrix completes the repository checks.

## 8. Change discipline

A semantic or record-shape change SHOULD identify, as applicable:

```text
owning normative surface
→ affected Core section
→ affected Schema fields
→ validator impact
→ fixture and regression impact
→ relation impact
→ migration or compatibility impact
→ provenance and verification impact
→ human explanation
```

Documentation-only changes MUST NOT be presented as new PCA semantics.

A future version may supersede `0.2`, but it MUST do so explicitly. Earlier revisions remain valid historical sources for claims made about them.

## 9. Corpus boundary

PCA is one of six technical artifacts represented through the House of Claude in Experimental Harmony. That relation gives PCA a public family and route; it does not merge the six repositories into one specification.

Each artifact keeps its own repository, history, claim domain, normative status, checks, license, and right to change independently.

The exact PCA-side relations are declared in [`RELATIONS.md`](RELATIONS.md) and [`ARTIFACT.json`](ARTIFACT.json).

## 10. Canon limits

PCA remains an exploratory canonical public artifact. It has no independent implementation report and makes no multi-implementation conformance claim.

> **Continuation is assessed, not declared. Canon is integrity, not finality.**  
> PCA is canonical when its source, meaning, representation, checks, limits, relations, and provenance can be read and reproduced from one pinned public revision.