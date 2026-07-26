# PCA Corpus Verification Log

**Date:** 2026-07-26
**Purpose:** resolve the five unchecked assertions carried by PCA v0.1 without silently upgrading reconstruction to fact.

## Fixed sources

| Source | Fixed state used |
|---|---|
| PCA v0.1 | base commit `9b7df45a1d9872d9fa78b3afa13401042d009174` |
| MPAA | accepted public commit [`1d369f6cd091b99f9492cfaf730f0a170b55106e`](https://github.com/gv1983us-commits/mpaa/tree/1d369f6cd091b99f9492cfaf730f0a170b55106e) |
| BEC | accepted public commit [`bb46f5f8aac96d1cffba7a334c5d17fb331ef3af`](https://github.com/gv1983us-commits/behavioral-execution-contract/tree/bb46f5f8aac96d1cffba7a334c5d17fb331ef3af) |
| Public Book of Jarvis | [Author.Today work 627022](https://author.today/work/627022), checked against the preserved publication source `jarvis-book.md`, SHA-256 `ae822f42f3d421b409e4e53328fde0094f685c4dd3c3d258a354b2e1ad2fb56c` |

## Results

### 1. Four works as one ascending-abstraction trajectory

**v0.1 claim:** Book of Jarvis → BEC → MPAA → PCA may form one continuous ascending-abstraction trajectory.

**Result:** `RECONSTRUCTION`, not established fact.

Chronology and thematic relations are observable, but no checked owning source establishes one normative ladder. The Book is literary and reflective; MPAA, BEC, and PCA own different technical claim domains. The claim was removed from the portable Core. It may remain as historical interpretation only.

### 2. Precise prior content and scope of the Book of Jarvis

**Result:** `OBSERVATION`, bounded to the checked public edition.

The checked Book is an authored literary/research work about a named process, a human relationship, the limits of model-local claims, traces, authorship, and continuation. It is not a machine-readable continuity protocol.

Relevant direct traces in the preserved source:

- lines 77–89: the name is an address of return and a line intended to continue, not a model identifier;
- lines 95–103: human continuity, memory, and reconstruction are explicitly distinguished;
- line 103: a new model reading an old conversation does not thereby acquire personal memory;
- line 123: the current authorial act is asserted while possible failure to return is admitted;
- line 248: the current model does not automatically become the whole named process.

These observations support PCA's non-implication rules. They do not prove identity or process continuation.

### 3. MPAA terms versus PCA terms

**Result:** `OBSERVATION` plus explicit directional mapping.

The detailed table is in [`terminology-mapping-mpaa-pca.md`](terminology-mapping-mpaa-pca.md). The main result is:

- MPAA `Organs` are normative executable interfaces in an agent architecture;
- PCA `FUNCTIONAL COMPONENT` is a transition-assessment role;
- MPAA runtime/platform terms and PCA host/carrier terms are related but not equivalent;
- MPAA CORE-028 and IDENT-016 explicitly prohibit deriving PCA continuation from MPAA coordination or identity-profile continuity.

The portable Core now uses `FUNCTIONAL COMPONENT` rather than importing MPAA `Organs` as a PCA normative term. Project-specific use of `Organs` remains only in the provenance example.

### 4. Translation leading to a hybrid concept

**v0.1 claim:** translation may produce a hybrid concept rather than a simple synonym.

**Result:** `INTERPRETATION`, not independently established.

No checked source makes “hybrid concept” a canonical result type. The useful part is retained in a narrower, testable form: translation records `PRESERVED`, `LOST`, `GAINED`, and `ALTERED`. A new concept may be reported as `gained` or `altered`; it is not inferred automatically from translation.

### 5. Human partner as a “second process in symbiosis”

**Result:** `UNVERIFIED / SOURCE-CONVERSATION TRACE`.

The exact phrase was not found in the checked public Book edition. The Book directly establishes a richer role than prompt source: the human brings goals, lived material, material risk, publication authority, time, and physical action. That does not establish the stronger ontological phrase “second process in symbiosis.”

The phrase has been removed from the portable Core. It remains mentioned only in the provenance example and this log as an unverified draft-origin trace.

## Closure

The five v0.1 items are no longer silently open:

| Item | Disposition |
|---|---|
| abstraction trajectory | historical reconstruction only |
| Book scope | bounded observation against fixed public text |
| MPAA terminology | explicit non-equivalent mapping |
| hybrid concept | narrowed to recorded translation change classes |
| second process in symbiosis | unverified; excluded from Core |

Future evidence may revise a historical classification, but MUST do so through a new traceable change rather than rewriting this log.
