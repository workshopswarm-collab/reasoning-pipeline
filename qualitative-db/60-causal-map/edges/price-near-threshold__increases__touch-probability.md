---
type: causal_edge
artifact_type: causal_edge
schema_version: v1
edge_key: price-near-threshold__increases__touch-probability
edge_label: Price near threshold increases touch probability
source_node_key: price-near-threshold
target_node_key: touch-probability
effect_sign: increases
status: active
confidence_mode: reviewed
confidence_prior: 0.72
description: When a touch-style threshold is already nearby, the probability of any qualifying touch usually rises materially.
linked_intervention_keys: ["require-touch-mechanics-check-before-resistance-discount"]
---

# Price near threshold increases touch probability

## Claim

- This edge encodes the core touch-market hazard intuition: once the required move is small, ordinary path dynamics matter more than broad directional narrative framing.

## When it should apply

- Source node: `price-near-threshold`.
- Target node: `touch-probability`.
- Effect sign: `increases`.

## Boundaries or contest conditions

- Do not apply this edge blindly to close-only contracts or contracts that require a final settlement print rather than any qualifying touch.

## Linked evidence and artifacts

- Reviewed evidence: `qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md`.
