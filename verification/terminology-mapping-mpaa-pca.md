# MPAA ↔ PCA Terminology Mapping

**PCA source:** v0.2-draft Core  
**MPAA source:** public commit [`1d369f6cd091b99f9492cfaf730f0a170b55106e`](https://github.com/gv1983us-commits/mpaa/tree/1d369f6cd091b99f9492cfaf730f0a170b55106e)  
**Reciprocal MPAA record:** [`review/MPAA_PCA_TERMINOLOGY_MAPPING.md`](https://github.com/gv1983us-commits/mpaa/blob/main/review/MPAA_PCA_TERMINOLOGY_MAPPING.md)  
**Preserved-source resolution:** this record resolves item 3 of `spec/00_PCA_SPEC.md` section 22, "What Must Be Checked Against the Existing Project Corpus."

This table documents overlap without transferring normative ownership.

| MPAA term | PCA term | Relation | Allowed mapping | Forbidden inference |
|---|---|---|---|---|
| `Agent` | `PROCESS` | no exact equivalence | an MPAA agent may be the bounded process under a PCA assessment | every PCA process is an MPAA agent; MPAA conformance proves PCA continuation |
| `Runtime` | `HOST` | partial / directional | a specific MPAA runtime may be referenced as one PCA host | runtime identity equals process identity |
| `Platform` | `HOST` or environment context | partial | platform evidence may describe host conditions | platform persistence proves continuation |
| `Model` | `FUNCTIONAL COMPONENT` | partial | a model may be one component involved in a transition | the model is the process; model equality proves continuation |
| `Organs` | `FUNCTIONAL COMPONENTS` | complementary, not equivalent | an MPAA Organ may be described as a PCA component when evaluating one transition | PCA imports MPAA availability, authorization, invocation, or organ semantics |
| `Identity Profile` | no PCA equivalent | separate domain | an identity-profile record may be carried as external evidence with a boundary statement | profile alignment or transition establishes PCA continuation |
| `Continuity Agent` coordination | provenance or operational evidence | evidentiary only | coordination traces may support a PCA dimension | coordination alone establishes continuation |
| session continuity | bounded transition evidence | evidentiary only | session records may be cited | same session or resumed session proves process continuation |
| MPAA Runtime Report | external reference | carrier-only | carry the report and exact revision without reinterpretation | MPAA `task_result: FULL` becomes a PCA status |
| `task_result: FULL` | no PCA equivalent | separate domain | may support an operational observation if explicitly evaluated | execution success proves continuation or identity |
| `extensions` external reference | `external_references` | complementary | carry namespaced record identity and revision | carrying a reference authenticates or imports its conclusion |

## Owning boundaries

MPAA explicitly records the divergence in:

- `CORE-028`: coordination, session continuity, and identity-profile continuity do not establish external process continuation;
- `IDENT-016`: identity-profile continuity must not imply a process-continuity assessment;
- `RUNTIME-039`: internal `task_result: FULL` is not an external task-level classification.

PCA records the reciprocal boundary in Core section 11 and this table. PCA does not redefine MPAA terms. It replaces the v0.1 generic normative use of `ORGANS` with `FUNCTIONAL COMPONENT` and retains `Organs` only in the project-provenance example.

## Direction of reference

```text
MPAA conclusion --carried as data--> PCA external reference
PCA assessment --carried as data--> MPAA namespaced extension
```

Neither direction creates equivalence, authentication, or normative ownership transfer.

## Resolution status

The terminology comparison requested by the preserved v0.1 source is complete
for the fixed revisions above. The result is **complementary with explicit
divergences**, not equivalence. Future changes to either specification require
a new dated comparison rather than silent reuse of this conclusion.
