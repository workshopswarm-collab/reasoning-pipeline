---
type: causal_edge
artifact_type: causal_edge
schema_version: v1
edge_key: settlement-source-specificity__increases__resolution-surface-ambiguity
edge_label: Settlement source specificity increases resolution surface ambiguity
source_node_key: settlement-source-specificity
target_node_key: resolution-surface-ambiguity
effect_sign: increases
status: active
confidence_mode: reviewed
confidence_prior: 0.7
description: When the contract depends on a particular venue or governing source, ambiguity about proof capture and qualifying events tends to increase.
linked_intervention_keys: ["capture-governing-source-proof-for-touch-markets", "separate-unverified-from-not-occurred-for-source-sensitive-markets"]
---

# Settlement source specificity increases resolution surface ambiguity

## Claim

- Venue-specific or publication-specific settlement surfaces create extra operational ambiguity even when the directional mechanism is understood.

## When it should apply

- Source node: `settlement-source-specificity`.
- Target node: `resolution-surface-ambiguity`.
- Effect sign: `increases`.

## Boundaries or contest conditions

- This edge is weaker in simple consensus-reporting markets with no named governing benchmark.

## Linked evidence and artifacts

- Reviewed evidence: `qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md`.
