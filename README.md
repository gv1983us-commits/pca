# PCA — Process Continuity Architecture

**Draft v0.1**

PCA is an architectural specification for assessing continuity across
changing carriers, execution environments, cognitive components, and
historical states. It does **not** attempt to prove that a process
remains "the same" across a transition — it specifies how a
continuation claim about such a transition can be represented,
decomposed by dimension, evidenced, and honestly assessed as
insufficient when the evidence does not support a stronger conclusion.

## Motivation

Any long-running process that operates through changing hosts, models,
tools, or participants faces the same recurring problem: nothing about
continuity across a transition is self-evident. A carrier claiming "I
am the same process as before" is not evidence. Style similarity is not
evidence. Reuse of a name is not evidence.

PCA gives that problem a structure: a fixed vocabulary of roles
(PROCESS / HOST / ORGANS / HUMAN PARTNER / CORPUS), a way to state a
continuation claim with explicit unknowns, a set of compatibility
dimensions to evaluate a transition against (rather than one global
label), and a mandatory status field — `OBSERVATION`, `RECONSTRUCTION`,
`HYPOTHESIS`, `INTERPRETIVE MODEL`, `PROTOCOL`, `OPEN QUESTION`,
`UNDETERMINED` — attached to every substantive statement in the
specification itself, including its own claims about its history and
lineage.

> **When uncertainty cannot be reduced honestly, it must be represented explicitly.**

## What's in this repository

```text
spec/
  00_PCA_SPEC.md    The full v0.1 draft specification.
```

## Status

This is an early **exploratory draft** (v0.1). It has not yet been
checked against related prior specifications in the same line of work
(a Behavioral Execution Contract and a portable agent architecture
specification), and it says so explicitly in its own final section —
`What Must Be Checked Against the Existing Project Corpus`. Treat this
as a public draft for review, not a finished standard.

## Reading order

1. Sections 1–5 — status, normative language, design principles, scope,
   problem statement.
2. Sections 6–11 — the core model and the operational definition of
   continuity, transition profiles, and the continuation claim.
3. Sections 12–15 — contracts: schema, amendment, usage, translation.
4. Sections 16–20 — evidence chain, known failure hypotheses, and the
   mandatory status-field discipline.
5. Sections 21–22 — open questions and what still needs corpus
   verification before being treated as settled.

## Related work

- [MPAA — Minimal Portable Agent Architecture](https://github.com/gv1983us-commits/mpaa)
- [BEC — Behavioral Execution Contract](https://github.com/gv1983us-commits/behavioral-execution-contract)

PCA's relationship to these prior works is currently marked
`RECONSTRUCTION` / `HYPOTHESIS` within the specification itself — it is
not yet independently verified.

## Contributing

Issues and PRs pointing out ambiguities, missing failure modes, or
proposing conformance test scenarios are welcome. This draft explicitly
invites scrutiny rather than treating any section as settled.

## License

Apache License 2.0 — see [LICENSE](LICENSE).
