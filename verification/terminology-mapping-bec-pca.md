# BEC ↔ PCA Evidence and Verification Mapping

**Review type:** fixed-revision cross-specification boundary review, not conformance evidence  
**PCA source:** commit [`070c6dcbc399eae82321a8303972a3cee9a81030`](https://github.com/gv1983us-commits/pca/tree/070c6dcbc399eae82321a8303972a3cee9a81030)  
**BEC source:** canonical commit [`62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261`](https://github.com/gv1983us-commits/behavioral-execution-contract/tree/62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261)  
**Preserved-source resolution:** this record resolves item 4 of `spec/00_PCA_SPEC.md` section 22, “What Must Be Checked Against the Existing Project Corpus.”

This review answers whether BEC evidence and verification vocabulary overlaps with or duplicates PCA's evidence chain.

## Result

The domains are **partially overlapping at the generic record level and non-duplicative at the claim level**.

Both systems use addressable evidence, reverse support links, verification state, temporal information, validators, and derived results. They apply those mechanisms to different questions and preserve different semantics.

```text
BEC question:
  what task execution occurred, with what capability, authority, evidence,
  trust, risk, validation, and task-scoped result?

PCA question:
  what process-relevant properties continued, changed, forked, broke,
  or remain unknown across one explicit transition?
```

A BEC record may be carried into PCA as external data. Its verdict is not a PCA verdict.

## Side-by-side mapping

| BEC surface or term | PCA surface or term | Relation | Allowed use | Forbidden inference |
|---|---|---|---|---|
| task `Claim` | claim statement in `origin / inherited / reconstructed / changed / unknown / breaks` | generic overlap only | a BEC claim may be cited as external data for a PCA statement | BEC claim text becomes a resolved PCA statement automatically |
| `Evidence` | PCA evidence object | partial structural overlap | addressable BEC evidence may support a PCA target after PCA evaluates it | BEC evidence validity proves PCA continuation |
| `supports_capabilities` / `supports_claims` | PCA `supports` plus bidirectional evidence references | analogous integrity mechanism | preserve exact attribution and reject dangling links in each local domain | matching link structure makes the record types equivalent |
| evidence `strength` | PCA `verified` boolean | non-equivalent | BEC strength may be carried as a fact about a BEC record | BEC strength maps mechanically to PCA verification |
| `Trust anchor` and `confidence` | no PCA equivalent | BEC-owned | a trust-anchor receipt may be cited through an explicit source reference | anchored or reproduced BEC evidence establishes PCA truth, memory, or identity |
| evidence freshness / expiry | PCA `observed_at`, `recorded_at`, transition ordering | complementary temporal controls | BEC timestamps may contribute to a PCA temporal assessment | BEC freshness alone proves transition provenance |
| required capability and invocation | PCA `operational` dimension evidence | directional | verified BEC execution may support a bounded PCA operational observation | effective capability or invocation proves process continuation |
| BEC Validator | PCA reference validator | same general role, different contracts | each validates its own record and computes its own result | one validator may issue the other domain's verdict |
| `deployment_level` | PCA overall status | no equivalence | carry the BEC result as external data with a boundary | `FULL-for-task` becomes `CONFORMING`; `PARTIAL` becomes `EVOLVING` |
| `return_state: closed` | no PCA equivalent | separate domain | record that BEC's task claim tree is closed | a PCA next state is committed or continuity is established |
| BEC external reference | PCA `external_references` | complementary boundary mechanism | carry exact record identity without importing conclusion | carrying a reference authenticates the external record |
| BEC policy and risk thresholds | no PCA equivalent | BEC/deployment-owned | cite policy context when relevant to external evidence | PCA inherits BEC policy or risk classification |
| PCA `transition-receipt` | no direct BEC equivalent | PCA-owned evidence type | a BEC API receipt or execution trace may be referenced by a PCA transition receipt after PCA records and verifies it locally | any BEC receipt automatically satisfies PCA provenance |
| PCA `memory-commit` | no direct BEC equivalent | PCA-owned evidence type | an external durable write receipt may be part of a PCA memory-commit evaluation | BEC file-write success proves inherited memory |
| PCA seven dimensions | no BEC equivalent | PCA-owned | BEC material may support one dimension after local evaluation | BEC deployment level fills PCA dimensions |

## Evidence ownership

BEC owns:

- capability existence, authorization, availability, invocation, and effectiveness;
- execution evidence type, strength, freshness, expiry, and trust anchors;
- policy inputs and risk-sensitive acceptance;
- deployment level and task return state.

PCA owns:

- transition state decomposition;
- `origin / inherited / reconstructed / changed / unknown / breaks`;
- seven independent continuity dimensions;
- transition-receipt and memory-commit requirements;
- usage-mode translation record;
- PCA overall status derivation.

The word `evidence` is shared vocabulary. The evidence objects are not interchangeable schemas and their validators do not compute interchangeable conclusions.

## Carrying BEC into PCA

A PCA record may carry a BEC record through `external_references` when it names:

- `system: BEC`;
- an addressable BEC record identifier;
- an exact 40-character BEC revision;
- a boundary statement;
- `mapping: carried-not-imported`;
- `conclusion_imported: false`.

If a PCA statement or dimension relies on facts observed through the BEC record, PCA still creates a local evidence object with its own `source_ref`, `observed_at`, support target, and verification state.

```text
BEC record --carried as exact external data--> PCA record
BEC conclusion ----------------------------X PCA conclusion
BEC evidence --locally evaluated and attributed--> PCA support target
```

## Preserved-source correction

The 2026-07-26 corpus verification log says that five v0.1 unchecked assertions were closed, but its fourth result addresses a “hybrid concept” translation question rather than section 22 item 4's BEC/PCA evidence comparison.

This record appends the missing review instead of rewriting the earlier log.

Disposition of preserved section 22 item 4:

```text
status: RESOLVED
result: partial generic overlap; separate record semantics and claim domains
normative ownership transferred: no
BEC conclusion imported: no
PCA conclusion imported into BEC: no
```

## Review limits

This review does not:

- validate a particular BEC or PCA record;
- prove that evidence referenced by either system is true;
- authenticate a producer, validator, or trust anchor;
- establish a real transition;
- establish identity, memory, causality, or uninterrupted persistence;
- create a shared conformance program.

Future changes to BEC or PCA require a new fixed-revision review rather than silent reuse of this result.
