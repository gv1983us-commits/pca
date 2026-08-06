# MPAA ↔ PCA Terminology Mapping

**Review type:** fixed-revision cross-specification terminology review, not conformance evidence  
**PCA source:** commit [`070c6dcbc399eae82321a8303972a3cee9a81030`](https://github.com/gv1983us-commits/pca/tree/070c6dcbc399eae82321a8303972a3cee9a81030)  
**MPAA source:** canonical commit [`0d1aaf35cc4826622f3312fdd2a1c2d40890b965`](https://github.com/gv1983us-commits/mpaa/tree/0d1aaf35cc4826622f3312fdd2a1c2d40890b965)  
**Historical reciprocal MPAA record:** [`review/MPAA_PCA_TERMINOLOGY_MAPPING.md`](https://github.com/gv1983us-commits/mpaa/blob/0d1aaf35cc4826622f3312fdd2a1c2d40890b965/review/MPAA_PCA_TERMINOLOGY_MAPPING.md)  
**Preserved-source resolution:** this record maintains the resolution of item 3 of `spec/00_PCA_SPEC.md` section 22, “What Must Be Checked Against the Existing Project Corpus.”

The original reciprocal review compared earlier fixed revisions. Those revisions remain preserved in repository history. This PCA-side refresh checks that the same boundary still holds against the accepted canonical MPAA revision without claiming that the historical MPAA review silently changed its own source set.

This table documents overlap without transferring normative ownership.

| MPAA term or surface | PCA term or surface | Relation | Allowed mapping | Forbidden inference |
|---|---|---|---|---|
| `Agent` | `PROCESS` | no exact equivalence | an MPAA Agent may be selected as the bounded process under one PCA transition assessment | every PCA process is an MPAA Agent; MPAA conformance proves PCA continuation |
| `Runtime` | `HOST` | partial / directional | one concrete MPAA Runtime may be referenced as one PCA host | runtime identity equals process identity or continuation |
| `Platform` | host/environment context | partial / directional | platform state may be carried as evidence about transition conditions | platform persistence proves process continuation |
| `Model` | `FUNCTIONAL COMPONENT` | partial / directional | a model may be one component involved in a transition | model equality proves continuation or identity |
| `Organ` | `FUNCTIONAL COMPONENT` | complementary, not equivalent | an MPAA Organ may be described as a PCA component for a bounded assessment | PCA imports MPAA availability, authorization, invocation, or Organ semantics |
| `Identity Profile` | no PCA equivalent | separate domain | an identity-profile record may be carried as external data with an explicit boundary | profile activation or continuity establishes PCA continuation |
| session continuity / coordination | provenance or operational evidence | evidentiary only | addressable traces may support one PCA dimension | resumed session or coordination alone establishes continuation |
| Runtime Report | external reference | carrier-only | carry exact report identity, revision, and bounded facts | a valid Runtime Report authenticates its producer or imports its result into PCA |
| `task_result: FULL` | no PCA equivalent | separate domain | it may support an operational observation if PCA evaluates it independently | execution success proves continuation, identity, persistence, or committed next state |
| namespaced Runtime Report extensions | PCA `external_references` | complementary | carry exact record identity through an explicit boundary | carrying a reference authenticates or adopts the referenced conclusion |
| MPAA identity transition | PCA Transition Record | distinct records | correlate them externally when they concern a bounded change | temporal proximity proves event identity, causality, or matching verdicts |

## Owning boundaries

MPAA owns:

- portable agent architecture and layer separation;
- initialization and readiness;
- Identity Profile structure and profile lifecycle;
- runtime capability, authorization, invocation, evidence, and task-result semantics;
- Runtime Report representation;
- MPAA conformance procedure.

PCA owns:

- transition state decomposition;
- bounded continuation claims;
- seven continuity dimensions;
- PCA evidence and translation contracts;
- PCA status derivation.

MPAA coordination, session continuity, Identity Profile continuity, Runtime Report validity, and internal `task_result` do not establish PCA continuation.

PCA does not redefine MPAA terms. It uses `FUNCTIONAL COMPONENT` rather than importing MPAA `Organ` as a normative PCA type. Project-specific Organ vocabulary remains only in provenance-bearing non-normative material.

## Direction of reference

```text
MPAA conclusion --carried as exact data--> PCA external reference
PCA assessment  --carried as exact data--> MPAA namespaced extension
```

Neither direction creates equivalence, authentication, event identity, causality, conformance transfer, or normative ownership transfer.

## Historical reciprocal boundary

The MPAA repository's reciprocal review at accepted revision `0d1aaf35cc4826622f3312fdd2a1c2d40890b965` preserves its original reviewed sources:

- MPAA `1d369f6cd091b99f9492cfaf730f0a170b55106e`;
- PCA `6ad1a86d7c09b36839d162c580f84f05cfe4a598`.

This PCA-side refresh does not rewrite that historical review. It records that the accepted canonical MPAA revision retains the same domain separation and that PCA's active Core now points to the accepted MPAA artifact revision.

## Resolution status

The preserved v0.1 terminology question remains **resolved with explicit divergences**, not equivalence.

```text
status: RESOLVED
result: complementary terms with directional mappings and separate claim domains
normative ownership transferred: no
MPAA conclusion imported: no
PCA conclusion imported into MPAA: no
```

Future changes to either specification require a new dated fixed-revision comparison rather than silent reuse of this result.
