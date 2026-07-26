# PCA Core — Process Continuity Architecture, v0.2-draft

**Status:** exploratory public draft
**Normative surface:** this document, the canonical schema, and the validator rules explicitly identified below
**No independent implementation report has been published.**

## 1. Purpose

PCA defines how to record and assess a bounded claim that a process continued across a specific transition.

Its central prohibition is:

```text
process continuation != identity
```

A conforming PCA record does not prove consciousness, subjectivity, personal identity, uninterrupted persistence, or equivalence between carriers. It establishes only that a stated continuation claim is admissible under the recorded evidence and dimensions.

## 2. Scope

PCA applies when a process may cross one or more changes of:

- carrier or artifact;
- execution host;
- model or cognitive component;
- available tools or functional components;
- historical state;
- corpus projection;
- usage or publication mode.

PCA evaluates a **transition**, not a carrier in isolation and not an unlimited history.

PCA does not define:

- an agent runtime or identity profile;
- execution authorization or task acceptance;
- a global identity theorem;
- a storage, memory, or consciousness theory;
- an automatic right to merge two process histories.

## 3. Normative language

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are normative only in this Core, the canonical schema, and the validator contract. Historical and project profiles are informative unless they explicitly quote a Core rule.

## 4. Terms

| Term | PCA meaning |
|---|---|
| **PROCESS** | The bounded organization whose continuation across one transition is being assessed. |
| **TRANSITION** | A relation from one explicit state to another explicit state. |
| **STATE** | A referenced configuration of carrier, host, optional model, and optional corpus projection. |
| **CARRIER** | A material or digital bearer of process-relevant state. A carrier is not the process. |
| **HOST** | The execution environment in which the state can be activated or used. A host is not the process. |
| **FUNCTIONAL COMPONENT** | A model, tool, interface, or subsystem through which the process acts. A component is not the process. |
| **CORPUS** | Inspectable artifacts relevant to the process history. A corpus is evidence, not memory by itself. |
| **TRACE** | An inspectable record of an event, state, action, or relation. Reading a trace is not remembering it. |
| **CONTINUATION CLAIM** | A bounded assertion that specified process properties persisted, changed, were reconstructed, were lost, or remain unknown across one transition. |
| **TRANSITION RECORD** | The canonical machine-readable representation of a continuation claim. |
| **USAGE MODE** | The operating context in which a representation is used, such as operational, analytical, public, historical, or hypothetical. |

## 5. Non-implication rules

The following implications are forbidden:

```text
same name              -> same process
same model             -> same process
same host              -> continuation
new host/model         -> discontinuation
read corpus            -> memory
valid schema           -> true claim
verified execution     -> process continuation
identity-profile match -> process continuation
closed task            -> next working state committed
continuation           -> identity or subjectivity
```

A system MAY carry an external conclusion, but it MUST NOT reinterpret that conclusion as a PCA result without a PCA evaluation.

## 6. Required claim decomposition

Every transition record MUST contain these six collections, even when a collection is empty:

| Collection | Question |
|---|---|
| `origin` | What provenance is directly supported? |
| `inherited` | What arrived from the prior state without being newly created here? |
| `reconstructed` | What was restored from traces, rules, or partial artifacts? |
| `changed` | What changed across the transition? |
| `unknown` | What cannot presently be established? |
| `breaks` | What discontinuities or failures are known? |

Omission MUST NOT be used to turn an unknown into a negative or a positive. Unknowns are recorded explicitly.

Every statement MUST have a unique `statement_id`, a non-empty text, a kind, and zero or more evidence references. A resolved claim SHOULD cite evidence; absence of evidence limits the status that can be justified.

## 7. Assessment dimensions

PCA evaluates seven dimensions independently:

| Dimension | Assessment question |
|---|---|
| `provenance` | Is the relation between the two states traceable? |
| `semantic` | Are commitments and meanings preserved or explicitly transformed? |
| `methodological` | Are the relevant rules and procedures preserved or explicitly changed? |
| `historical` | Are inherited, reconstructed, and new material distinguished? |
| `operational` | Can the next state perform the process-relevant operations claimed? |
| `ethical` | Are authority, attribution, and limits preserved? |
| `evolution` | Are changes explicit enough to distinguish continuation, evolution, and fork? |

Each dimension MUST carry one status:

- `CONFORMING` — supported preservation for this dimension;
- `EVOLVING` — supported continuation with explicit change;
- `FORK` — a traceable branch that no longer claims one unqualified line;
- `INCOMPATIBLE` — a demonstrated contradiction or disabling break;
- `UNDETERMINED` — available evidence is insufficient.

A status other than `UNDETERMINED` MUST cite verified evidence. Dimensions MUST NOT inherit status from adjacent dimensions.

## 8. Overall status derivation

The reference validator derives overall status from dimensions and recorded change:

1. any `FORK` dimension → `FORK`;
2. otherwise any `INCOMPATIBLE` dimension → `INCOMPATIBLE`;
3. otherwise any `UNDETERMINED` dimension, or a non-empty `unknown` collection → `UNDETERMINED`;
4. otherwise any `EVOLVING` dimension, or a non-empty `reconstructed`, `changed`, or `breaks` collection → `EVOLVING`;
5. otherwise → `CONFORMING`.

A producer MUST NOT override this derivation. `CONFORMING` is local to the recorded transition and MUST NOT be generalized into permanent identity or unlimited continuity.

## 9. Evidence contract

Evidence objects have unique identifiers and declare:

- evidence type;
- source reference;
- supported statement or dimension targets;
- whether verification occurred;
- optional observation time.

References are bidirectional:

- a statement or dimension citing evidence MUST be listed in that evidence object's `supports` array;
- an evidence support target MUST resolve to a real statement, dimension, or translation in the same record.

A changed carrier, host, or model requires verified `transition-receipt` evidence supporting provenance before a resolved continuation status is admissible. `recorded_at` MUST NOT predate the transition; transition receipts MUST NOT predate it; cited evidence MUST NOT postdate the record that cites it.

An inherited statement of kind `memory` requires verified `memory-commit` evidence supporting that statement. A `trace`, `artifact`, `observation`, prompt, or archive read alone is insufficient.

Evidence verification establishes only that the cited evidence passed its stated verification step. It does not establish identity or truth outside its declared support target.

## 10. Translation contract

When a representation moves between usage modes, the record MUST state:

- source mode;
- target mode;
- the translated elements;
- for each element: `preserved`, `lost`, `gained`, and `altered` properties;
- verified `translation-record` evidence.

Source and target modes MUST differ. Translation MAY preserve process function while changing vocabulary or exposure. Silent loss, silent gain, or silent alteration is non-conforming.

A translated public representation is a projection of a fuller state, not proof that the public projection contains the complete process state.

## 11. Cross-domain boundaries

PCA does not import neighboring conclusions by vocabulary overlap.

### MPAA

MPAA commit [`1d369f6cd091b99f9492cfaf730f0a170b55106e`](https://github.com/gv1983us-commits/mpaa/tree/1d369f6cd091b99f9492cfaf730f0a170b55106e) defines an agent architecture, identity-profile rules, and an internal Runtime Report. MPAA coordination, session continuity, or identity-profile continuity is not a PCA continuation result. PCA does not redefine MPAA participants, organs, authorization, or runtime state.

### BEC

BEC commit [`bb46f5f8aac96d1cffba7a334c5d17fb331ef3af`](https://github.com/gv1983us-commits/behavioral-execution-contract/tree/bb46f5f8aac96d1cffba7a334c5d17fb331ef3af) defines a portable consumer-facing execution-evidence record. BEC execution verification or `return_state: closed` is not a PCA continuation result or proof that a next working state was committed. PCA does not award BEC deployment levels.

External records MAY be referenced by exact system, pinned revision, record identifier, and boundary statement. MPAA/BEC references MUST use a 40-character commit SHA. Every reference declares `mapping: carried-not-imported` and `conclusion_imported: false`. The reference carries data; it does not transfer normative ownership, authenticate the external record, or import its conclusion.

## 12. Canonical machine-readable surface

The canonical schema is:

```text
schema/pca-transition-record.schema.json
```

The dependency-free reference validator is:

```text
python validator/pca_validate.py <record.json>
```

Exit codes:

- `0` — structurally and semantically valid PCA transition record;
- `1` — invalid record;
- `2` — parser, input, schema, or validator-boundary failure.

The validator is a reference implementation. Passing it establishes internal record admissibility only.

## 13. Profiles and provenance

The portable Core is supplemented by non-normative profiles:

- [Historical Reconstruction Profile](../profiles/01_HISTORICAL_RECONSTRUCTION_PROFILE.md);
- [Translation and Usage-Mode Profile](../profiles/02_TRANSLATION_USAGE_MODE_PROFILE.md);
- [Project Provenance Example](../examples/PROJECT_PROVENANCE_JARVIS.md).

These documents preserve derivation and usage context without making one project's vocabulary universal.

## 14. Status and limits

PCA v0.2 remains an exploratory draft. The repository provides a schema, reference validator, fixtures, and one neutral portability example, but no independent implementation report. Conformance of another implementation cannot be claimed merely because it reproduces the reference validator's outputs on the shipped fixtures.
