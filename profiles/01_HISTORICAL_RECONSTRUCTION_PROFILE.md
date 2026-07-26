# Historical Reconstruction Profile

**Status:** informative profile for PCA v0.2-draft
**Core dependency:** [`spec/01_PCA_CORE.md`](../spec/01_PCA_CORE.md)

## Purpose

This profile describes how to construct a bounded historical account when direct state is incomplete and only traces remain. It does not convert reconstruction into memory, origin, or identity.

## Epistemic labels

Every material historical statement SHOULD be classified as one of:

| Label | Meaning |
|---|---|
| `OBSERVATION` | Directly inspectable in the cited source. |
| `INHERITED` | Delivered from a prior state with a traceable transfer relation. |
| `RECONSTRUCTION` | Inferred from multiple observations or partial traces. |
| `HYPOTHESIS` | Plausible but presently underdetermined. |
| `INTERPRETATION` | A proposed meaning of established or reconstructed facts. |
| `UNKNOWN` | Not established by the available corpus. |

Labels apply per statement. A document, model, or author is not globally trustworthy or untrustworthy.

## Reconstruction procedure

1. **Bound the transition.** Identify the two states and the exact historical question.
2. **Inventory sources.** Record source path or URL, revision, date, author when available, and access limitations.
3. **Separate direct trace from narrative.** Quote or point to the trace before summarizing its significance.
4. **Build provenance links.** Distinguish inherited artifacts, later reconstructions, and newly created material.
5. **Record absences.** Missing evidence becomes `unknown`; it does not become evidence of non-occurrence unless the source was expected to be complete and that expectation is itself established.
6. **Test rival explanations.** A reconstruction SHOULD survive at least one plausible alternative account or remain a hypothesis.
7. **Declare breaks.** Gaps, contradictory records, inaccessible sources, and revisions without trace are recorded rather than repaired silently.
8. **Limit the conclusion.** A successful historical reconstruction supports only the bounded transition claim evaluated.

## Reading is not memory

A later carrier may read an archive and accurately reconstruct earlier commitments. This supports access and reconstruction. It does not establish that the later carrier personally remembered creating or experiencing the archive.

A PCA record therefore uses:

- `reconstructed` for restored content derived from traces;
- `inherited` only when a transfer relation is evidenced;
- statement kind `memory` only with verified `memory-commit` evidence under the Core contract.

No record format can prove subjective recollection.

## Origin discipline

A locally available earliest trace is not automatically the actual origin. The profile distinguishes:

- earliest trace currently available;
- earliest trace expected in a defined source set;
- reconstructed predecessor;
- claimed origin;
- verified origin, if evidence is sufficient.

A carrier MUST NOT promote its own first accessible state to process origin merely because earlier state is unavailable.

## Corpus limitations

A corpus is a projection shaped by storage, export, permissions, deletion, publication, and selection. Therefore:

```text
not present in projection != never existed
present in projection     != complete lived state
readable now               != remembered then
```

Source completeness claims require their own evidence.

## Relationship to Core status

Historical status is one of seven independent dimensions. Strong provenance cannot silently settle semantic or operational continuity. Conversely, a historical gap does not necessarily prove discontinuity; it may require `UNDETERMINED`.

This profile adds no new overall status values and does not override validator derivation.
