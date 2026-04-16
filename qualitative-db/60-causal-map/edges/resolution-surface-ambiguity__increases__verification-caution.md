---
type: causal_edge
artifact_type: causal_edge
schema_version: v1
edge_key: resolution-surface-ambiguity__increases__verification-caution
edge_label: Resolution surface ambiguity increases verification caution
source_node_key: resolution-surface-ambiguity
target_node_key: verification-caution
effect_sign: increases
status: hold
confidence_mode: reviewed
confidence_prior: 0.69
description: When proof on the governing surface is incomplete or ambiguous, the workflow usually responds by increasing verification caution.
linked_intervention_keys:
  - capture-governing-source-proof-for-touch-markets
  - separate-unverified-from-not-occurred-for-source-sensitive-markets
lifecycle_stage: hold
lifecycle_stage_updated_at: "2026-04-16T15:31:46Z"
lifecycle_stage_updated_by: advance_live_causal_graph_items.py
lifecycle_transition: active->hold
demotion_reason: "repair_causal_graph.py:cascade_hold:endpoint_stage_change:verification-caution"
---

# Resolution surface ambiguity increases verification caution

## Claim

- This edge captures the intended workflow reaction to missing decisive proof: caution rises before the contract state is treated as settled.

## When it should apply

- Source node: `resolution-surface-ambiguity`.
- Target node: `verification-caution`.
- Effect sign: `increases`.

## Boundaries or contest conditions

- The edge says caution rises, not that the underlying event probability necessarily falls.

## Linked evidence and artifacts

- Reviewed evidence: `qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md`.
