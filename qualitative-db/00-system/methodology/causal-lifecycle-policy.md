---
type: system_policy
domain: methodology
status: active
last_updated: 2026-04-15
owner: evaluator
tags: [methodology/policy, causal-map, lmd, recursive-improvement, lifecycle]
---

# Causal Map Lifecycle Policy

This document defines the bounded lifecycle for causal-map topology and LMD-recallable mechanism structure.

It exists to make the recursive-learning layer:
- automatically improvable
- automatically repairable
- resistant to ontology sprawl
- auditable and reversible

## Core rule

Evaluator memory, freeform summaries, or one-off qualitative suggestions must **not** directly create LMD-recallable canon.

The only allowed promotion path is:

```text
reviewed case evidence
-> structured proposal occurrence
-> aggregated proposal stats
-> proposal-stage advancement
-> live graph trial item
-> live active graph item
-> LMD recall
```

## Canonical storage split

- `qualitative-db/50-learnings/` = reviewed evidence, interventions, case reviews, aggregate notes
- `qualitative-db/60-causal-map/` = reviewed live mechanism registry
- proposal-layer DB tables = candidate topology that is **not yet live graph canon**
- LMD bundles = compact retrieval products derived from the reviewed live graph + reviewed learnings

## Live-graph operating rule

The causal map is a finite-state mechanism registry.
It is not an unconstrained ontology scratchpad.

Every live node or edge should carry:
- `mechanism_family`
- `source_kind`
- `lifecycle_stage`
- optional supersession / merge metadata
- decayed runtime stats in DB

## Proposal lifecycle

Proposal-layer candidates may move through these stages:
- `observed`
- `aggregated`
- `shadow_candidate`
- `trial_candidate`
- `promotion_ready`
- `rejected`
- `duplicate_of_live_graph`

Proposal-layer items are not injected into runtime prompts.

## Live graph lifecycle

Live graph nodes and edges may move through these stages:
- `draft`
- `trial`
- `active`
- `hold`
- `retired`
- `archived`

LMD recall policy:
- `active` = recallable by default
- `trial` = only recallable in explicit trial / treatment / shadow modes
- `draft` = visible for review, not default prompt-time recall
- `hold`, `retired`, `archived` = not injected

## Promotion rule

Recurrence alone is insufficient for promotion.

Promotion toward live graph requires:
- repeated reviewed-case support
- bounded genericity
- duplicate-merge check
- mechanism-family assignment
- acceptable contestation profile
- positive or non-negative trial / shadow evidence when available
- active-budget availability within the relevant family

## Decay / anti-sprawl rule

Live graph items should decay when they stop being useful.

Decay should consider:
- time since last seen
- time since last matched
- time since last injection
- time since last helpful outcome
- repeated non-use despite matching opportunities
- negative learned utility
- contestation growth
- family crowding / sibling competition

Decay should demote or retire items rather than silently leaving them active forever.

## Family budget rule

Every node and edge must belong to a bounded mechanism family.

Examples:
- `threshold_touch`
- `source_resolution`
- `workflow_pricing`
- `publication_timing`

Family assignment exists to:
- constrain graph growth
- support sibling comparison
- support automatic demotion of weak variants
- prevent unlimited one-off concept accretion

## Evidence and provenance rule

Keep these layers distinct:
- observed case facts
- projected case state
- proposed reusable mechanism claims
- live reviewed mechanism canon

Intervention-derived or heuristic-derived support may inform retrieval and proposal tracking, but should not on its own justify durable promotion.

## Repair rule

Self-healing means:
- stale items can be demoted
- broken references can be detected and repaired
- duplicate concepts can be merged
- orphaned or superseded topology can be removed from runtime recall

Self-healing does **not** mean unconstrained self-rewriting.

## Operational implication

Any future automation that promotes, merges, demotes, retires, or repairs graph topology should treat this policy as the canonical guardrail.
