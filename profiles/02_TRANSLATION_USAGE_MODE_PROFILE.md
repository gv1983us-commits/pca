# Translation and Usage-Mode Profile

**Status:** informative profile for PCA v0.2-draft
**Core dependency:** [`spec/01_PCA_CORE.md`](../spec/01_PCA_CORE.md)

## Purpose

The same process-relevant material may appear differently in operational, analytical, external-research, public, historical, or hypothetical contexts. This profile makes those transformations explicit without treating one projection as the whole process state.

## Usage modes

| Mode | Typical function | Typical constraint |
|---|---|---|
| `operational` | coordinate current action | may contain local references and active state |
| `analytical` | inspect architecture or evidence | may abstract away immediate action |
| `external-research` | compare with outside sources | requires public or shareable vocabulary |
| `public` | publish a bounded representation | excludes private state and unsupported claims |
| `historical` | preserve provenance and chronology | may not represent current operation |
| `hypothetical` | explore alternatives | must not be reported as established state |

Modes are not trust levels. Public does not mean complete; operational does not mean true; historical does not mean remembered.

## Required translation record

For each translated element, record:

- `preserved` — functions or constraints retained;
- `lost` — functions or distinctions no longer represented;
- `gained` — functions or clarity newly introduced;
- `altered` — features retained in changed form.

All four arrays are explicit even when empty. A valid record cites verified `translation-record` evidence supporting the translation.

## Translation procedure

1. Name the source and target modes.
2. Identify the element's function in the source mode.
3. Choose target vocabulary appropriate to the target mode.
4. Record preservation, loss, gain, and alteration separately.
5. Check whether altered wording creates a new claim.
6. Preserve provenance for non-neutral or project-specific vocabulary.
7. Validate the transition record.

## Prohibited shortcuts

The profile forbids these silent substitutions:

```text
metaphor removed   -> provenance removed
word retained      -> function preserved
public projection  -> full internal state
new clarity        -> original meaning
readable summary   -> committed working state
translated record  -> identity proof
```

When a metaphor is retained, its operational meaning and limits SHOULD be stated. When it is replaced, the translation record SHOULD state what function was preserved and what associations were lost.

## Fork versus translation

A translation is not automatically a fork. It becomes a fork when the target representation adopts commitments incompatible with the source or claims an independent lineage that can no longer be represented as one bounded evolution.

A translation with explicit alteration may remain `EVOLVING`. Contradictory commitments may require `FORK` or `INCOMPATIBLE`. Insufficient evidence requires `UNDETERMINED`.

## Neutral example

The shipped fixture [`05-valid-usage-mode-translation.json`](../conformance/fixtures/05-valid-usage-mode-translation.json) translates a service-migration assessment from analytical to public mode. It records preserved evidence references, lost internal shorthand, gained public scope, and altered host identifiers. No project-specific vocabulary is required to understand or validate it.
