# PCA Relations

**Artifact:** Process Continuity Architecture (PCA)  
**Corpus identity:** `claude.pca`  
**Local claim domain:** bounded process-continuity assessment across one explicit transition

This document records PCA-side relations to the other five technical artifacts represented through the House of Claude. It does not merge their specifications or import their conclusions.

## 1. Relation rule

```text
reference a neighboring record
≠ validate that record
≠ import its verdict
≠ transfer normative ownership
≠ prove that two records concern the same event
```

PCA may carry an addressable external record as evidence or context only through an explicit boundary. The owning artifact remains authoritative for its own record and conclusion.

The canonical Transition Record enforces this for MPAA and BEC through `external_references`:

```text
mapping = carried-not-imported
conclusion_imported = false
```

For Review Protocol, ARB, and CDTS, the same boundary is declared at artifact level even though those systems are not enumerated as native PCA external-reference systems.

## 2. BEC — execution evidence, not continuation

**Artifact:** `claude.bec`  
**Repository:** `gv1983us-commits/behavioral-execution-contract`  
**Reviewed canonical revision:** `62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261`

BEC owns task execution, capability, authorization, invocation, evidence strength, trust anchors, validation, deployment level, and task return state.

PCA owns only the transition-continuity assessment defined by its Core and Schema.

Allowed relation:

- a pinned BEC record may be carried as an external reference;
- addressable BEC evidence may support a PCA statement or dimension after PCA evaluates that support under its own rules;
- BEC execution traces may contribute to PCA's `operational` or `provenance` evidence without becoming PCA conclusions.

Forbidden inference:

```text
BEC FULL-for-task       -> PCA CONFORMING
BEC return_state closed -> next PCA state committed
valid BEC record        -> process continuation
strong BEC trust anchor -> PCA identity or memory
```

The fixed PCA-side vocabulary review is [`verification/terminology-mapping-bec-pca.md`](verification/terminology-mapping-bec-pca.md).

## 3. MPAA — architecture and runtime records, not continuation

**Artifact:** `claude.mpaa`  
**Repository:** `gv1983us-commits/mpaa`  
**Reviewed canonical revision:** `0d1aaf35cc4826622f3312fdd2a1c2d40890b965`

MPAA owns its six-document architecture: bootstrap, Agent Core, Identity Profile, Runtime Contract, Conformance, and Runtime Report representation.

PCA does not redefine MPAA Agent, Runtime, Platform, Model, Organ, Identity Profile, authorization, task-result, or conformance semantics.

Allowed relation:

- a pinned Runtime Report or identity-transition record may be carried as external data;
- runtime, host, model, and profile observations may support one PCA transition assessment after PCA performs its own evaluation;
- exact MPAA terms may be mapped directionally for a bounded review.

Forbidden inference:

```text
MPAA identity-profile continuity -> PCA continuation
MPAA session continuity          -> PCA continuation
MPAA task_result FULL            -> PCA CONFORMING
MPAA conformance                 -> PCA conformance
same Runtime or Model            -> same process
```

The historical reciprocal mapping remains in [`verification/terminology-mapping-mpaa-pca.md`](verification/terminology-mapping-mpaa-pca.md). Its original fixed revisions remain provenance. The current artifact relation is pinned here to the accepted MPAA canonical revision above.

## 4. Review Protocol — source-selection discipline only

**Artifact:** `claude.review_protocol`  
**Repository:** `gv1983us-commits/repository-canon-review-protocol`  
**Reviewed revision:** `e2ff9182014d8a8f3c3e7ea1ea269eecb8679035`

The Review Protocol owns reproducible source selection, review procedures, and bounded review receipts.

A Review Protocol receipt may establish what source was selected and what review steps were recorded. It does not establish PCA continuation, evidence truth, record admissibility, or a PCA status.

Forbidden inference:

```text
review completed -> PCA record valid
source pinned    -> source claim true
receipt valid    -> transition continued
```

PCA's exact-source rule is compatible with the Review Protocol but remains locally owned by PCA's Canon.

## 5. ARB — analytical map, not normative input

**Artifact:** `claude.arb`  
**Repository:** `gv1983us-commits/agent-runtime-boundaries`  
**Reviewed revision:** `6b6c32cd467a4b5e4863d082b9da5bdd40d7dced`

ARB is a descriptive and analytical companion. It maps distinctions among models, runtimes, platforms, working state, persistence, evidence, closure, and next action.

ARB may help a reviewer formulate a PCA question or notice a boundary. It does not amend the PCA Core, Schema, validator, dimensions, evidence contract, or status derivation.

Forbidden inference:

```text
ARB distinction or proposal -> PCA requirement
ARB mapping                 -> PCA record result
ARB closure analysis        -> committed PCA next state
```

## 6. CDTS — correlation between domains, not PCA transition semantics

**Artifact:** `claude.cdts`  
**Repository:** `gv1983us-commits/cdts`  
**Reviewed revision:** `f91dbc003519efd5264655d905d0530dbfeac2fd`

CDTS owns portable cross-domain correlation traces, qualified external references, typed absence, conflict disclosure, unresolved questions, linkage assertions, and amendment history.

PCA owns the meaning and admissibility of one PCA Transition Record. CDTS may correlate a PCA record with MPAA, BEC, or other addressable records, but it does not validate or import the PCA conclusion.

The Linkage Record and minimal six-item trace set in preserved PCA v0.1 section 24 are historical precursors to CDTS. They are not active PCA requirements.

Forbidden inference:

```text
CDTS ADMISSIBLE              -> PCA record valid
shared correlation key       -> same event
CDTS linkage                 -> causality established
PCA record present in CDTS   -> PCA conclusion imported
PCA v0.1 Linkage Record text -> current PCA schema requirement
```

## 7. Corpus relation

The six artifacts are related by public creation history and representation through the House of Claude. They are not one normative stack and do not form an automatic hierarchy.

```text
BEC             owns execution-evidence acceptance
MPAA            owns portable agent architecture and runtime reporting
PCA             owns bounded process-continuity assessment
Review Protocol owns source-selection and review procedure
ARB             owns non-normative analytical distinctions
CDTS            owns cross-domain correlation traces
```

A combined workflow may use several artifacts. Each result must remain named, addressable, and owned by its source domain.

## 8. Relation formula

> **Carry the record; preserve the boundary; recompute the local conclusion.**

A relation is canonical only when the neighboring source, reviewed revision, permitted use, forbidden inference, and local owner are explicit.