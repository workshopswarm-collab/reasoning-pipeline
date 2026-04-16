---
type: causal_edge
artifact_type: causal_edge
schema_version: v1
edge_key: verification-caution__increases__fair-value-discounting-pressure
edge_label: Verification caution increases fair-value discounting pressure
source_node_key: verification-caution
target_node_key: fair-value-discounting-pressure
effect_sign: increases
status: hold
confidence_mode: reviewed
confidence_prior: 0.63
description: When verification caution is active, the workflow often pulls fair value downward unless the path-risk case is made explicitly and separately.
linked_intervention_keys:
  - capture-governing-source-proof-for-touch-markets
  - separate-unverified-from-not-occurred-for-source-sensitive-markets
  - require-touch-mechanics-check-before-resistance-discount
lifecycle_stage: hold
lifecycle_stage_updated_at: "2026-04-16T15:31:46Z"
lifecycle_stage_updated_by: advance_live_causal_graph_items.py
lifecycle_transition: active->hold
demotion_reason: "repair_causal_graph.py:cascade_hold:endpoint_stage_change:fair-value-discounting-pressure+verification-caution"
---

# Verification caution increases fair-value discounting pressure

## Claim

- This edge represents a workflow tendency, not a market law: unresolved verification state can become a pricing discount rather than a separately tracked proof-state issue.

## When it should apply

- Source node: `verification-caution`.
- Target node: `fair-value-discounting-pressure`.
- Effect sign: `increases`.

## Boundaries or contest conditions

- The edge can be contested when the caution is justified or when the contract is genuinely hard to verify in real time.

## Linked evidence and artifacts

- Reviewed evidence: `qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md`.
