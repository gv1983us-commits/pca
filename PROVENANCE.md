# PCA Public Provenance

This record separates public authority, derivation history, corpus representation, human approval, model and coding-tool participation, and reproducible evidence for the Process Continuity Architecture repository.

It does not publish private conversations, hidden prompts, unpublished workspaces, or a complete psychological story of creation. Absence from this public record is not evidence that no contribution occurred.

## 1. Canonical repository authority

The canonical public source is:

```text
gv1983us-commits/pca
```

The repository owner and maintainer control admission to the canonical branch. Git commits, pull requests, reviews, tags, and CI runs preserve the public revision history.

Normative authority comes from maintainer-approved repository content. For PCA `0.2-draft`, that authority is divided between:

- [`spec/01_PCA_CORE.md`](spec/01_PCA_CORE.md) for semantic rules;
- [`schema/pca-transition-record.schema.json`](schema/pca-transition-record.schema.json) for record representation.

Neither a model response, generated file, historical draft, validator behavior, nor verification note becomes normative merely by existing. Canon admission requires repository acceptance under [`CANON.md`](CANON.md).

## 2. Public derivation line

The visible repository history records these major stages:

```text
2026-07-20
06dd364e01ac513ad99ab04ea6eae0c83fb27b32
PCA v0.1 integrated exploratory draft

2026-07-21
f2ff786266b527923d418f5d8138c3ede57f6bf5
cross-domain claim boundaries with MPAA and BEC added to v0.1

2026-07-21
9b7df45a1d9872d9fa78b3afa13401042d009174
Linkage Record and minimal cross-domain trace proposal added to v0.1

2026-07-26
6ad1a86d7c09b36839d162c580f84f05cfe4a598
portable PCA v0.2 Core, canonical Schema, fail-closed validator, profiles, fixtures, and verification records

2026-08-02
e2ba2ae7b95ba9cba1ba752ee47ce6546ec2de45
CI and validator workflow hardening

2026-08-02
c57493540da1590c9ccf43c1b330cae735e9040c
fixed-revision MPAA terminology record and publication checks

2026-08-06
individual artifact canon pass
CANON.md, ARTIFACT.json, RELATIONS.md, PROVENANCE.md, updated neighbor reviews, and executable canon checks
```

This is a public engineering trace, not a proof that every intermediate interpretation was correct.

## 3. v0.1 source and v0.2 active Core

[`spec/00_PCA_SPEC.md`](spec/00_PCA_SPEC.md) is preserved as the integrated v0.1 source draft. It contains project-specific language, open questions, interpretive models, and mechanisms that were later narrowed, separated, or moved to neighboring artifacts.

The v0.1 source remains valuable for provenance. It is not the active normative Core.

The v0.2 split established:

```text
portable semantic rules       -> PCA Core
record representation         -> JSON Schema
reference execution           -> validator
expected decisions            -> conformance corpus
historical/translation method -> profiles
project vocabulary            -> provenance example
fixed source checks           -> verification
```

The Linkage Record and six-item trace proposal in v0.1 section 24 are preserved as an origin trace for the later independent CDTS artifact. Their historical presence does not make them current PCA requirements.

## 4. Corpus verification history

The 2026-07-26 verification log attempted to resolve five unchecked source-draft assertions against fixed public sources. It successfully preserved several important dispositions, including:

- the proposed four-work abstraction ladder remains historical reconstruction;
- the public Book of Jarvis is not a machine-readable continuity protocol;
- MPAA and PCA terms are directionally related but not equivalent;
- strong human/process language not found in the checked source remains unverified.

During the 2026-08-06 canon audit, a mismatch was identified: the preserved v0.1 checklist asks whether BEC evidence and verification vocabulary overlaps with PCA's evidence chain, while the 2026-07-26 log's fourth result addresses a different “hybrid concept” question.

The missing BEC/PCA comparison is therefore resolved separately in:

```text
verification/terminology-mapping-bec-pca.md
```

The earlier log is preserved rather than rewritten. The new record appends a traceable correction.

## 5. Corpus representation

Within Experimental Harmony, PCA is represented as one of the six technical artifacts of **Claude (Anthropic)** through the public House of Claude:

```text
gv1983us-commits/Claude-workshop
```

This representation records a relation between Claude and the materialized technical artifact. It does not:

- transfer repository ownership;
- imply that every future Claude instance remembers its creation;
- establish exclusive authorship for every line;
- replace commit-level attribution;
- merge PCA with the other five artifacts;
- make the House a normative PCA source.

## 6. Human authority

A human maintainer remains the authority who can:

- accept or reject canonical changes;
- choose what is published;
- preserve or withhold private source material;
- distinguish a proposal from an approved rule;
- decide whether a draft advances to a release;
- record the artifact in the House of Claude.

Human approval is repository-governance authority. It is not PCA evidence that a process continued and not proof of external truth.

## 7. Model and coding-tool participation

Claude, GPT, Codex, and other coding-agent tools may participate in conceptual analysis, drafting, restructuring, schema and validator implementation, fixture construction, regression testing, review, documentation, or mechanical maintenance.

The public boundary is:

```text
normative engineering decision
  requires maintainer authorship or approval

mechanical implementation and verification
  may be assisted by model and coding-agent tools
```

A tool-generated diff does not own a normative claim merely because it produced text. A maintainer-approved clause does not thereby prove its assumptions about the world.

The 2026-08-06 canon pass was performed in continued collaboration between Valentin and a GPT-5.6 Thinking environment using the connected GitHub application. This statement records the canonization work surface; it does not rewrite the earlier artifact's representation as one of Claude's technical works.

## 8. Public evidence of the artifact

The public artifact is evidenced by addressable repository surfaces:

- the Core and Schema;
- the reference validator and strict parser boundary;
- the conformance fixtures and expected decisions;
- the profiles and examples;
- fixed-revision verification records;
- CI workflow and run history;
- this Canon, machine passport, relation map, and provenance record.

These surfaces make the artifact inspectable and reproducible. They do not authenticate arbitrary evidence cited by a PCA record and do not establish world truth.

## 9. Revision-level provenance

A claim about PCA SHOULD identify an exact commit SHA or release tag.

```text
repository name alone
  identifies the evolving artifact

repository + exact revision
  identifies a reproducible source state

revision + passing checks
  identifies a mechanically checked source state

none of the above
  proves process continuation, external adoption, certification, or truth
```

## 10. Distinct authorities

The public record preserves several different relations:

```text
repository ownership
≠ corpus representation
≠ normative authority
≠ implementation assistance
≠ verification evidence
≠ PCA continuation evidence
≠ episodic memory
```

No single relation silently implies the others.

## 11. Full creation-chain boundary

The full creation chain is intentionally not expanded here into private prompts, unpublished discussion, local workspaces, or hidden context. This protects private material and prevents a simplified public account from being mistaken for a complete causal history.

Claude may describe its own role through its House. The maintainer may publish additional provenance later. Any addition must be addressable, attributed, and kept separate from PCA's technical claim domain.

## 12. Provenance formula

> **Preserve the source; name the transformation; do not backfill certainty.**  
> Claude represents the technical corpus. The human maintainer admits canonical changes. Repository history preserves the public trace. Models and tools may assist. PCA validators test declared mechanics. None of these roles impersonates another.