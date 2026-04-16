---
type: causal_edge
artifact_type: causal_edge
schema_version: v1
edge_key: time-remaining-nontrivial__increases__touch-probability
edge_label: Time remaining increases touch probability
source_node_key: time-remaining-nontrivial
target_node_key: touch-probability
effect_sign: increases
status: active
confidence_mode: reviewed
confidence_prior: 0.67
description: When meaningful time remains in a permissive touch window, ordinary volatility has more opportunity to produce a qualifying touch.
linked_intervention_keys: ["require-touch-mechanics-check-before-resistance-discount"]
---

# Time remaining increases touch probability

## Claim

- Residual window matters mechanically in 24/7 touch markets because the contract can resolve early on any qualifying print.

## When it should apply

- Source node: `time-remaining-nontrivial`.
- Target node: `touch-probability`.
- Effect sign: `increases`.

## Boundaries or contest conditions

- This edge weakens quickly once the remaining window becomes very short.

## Linked evidence and artifacts

- Reviewed evidence: `qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md`.
