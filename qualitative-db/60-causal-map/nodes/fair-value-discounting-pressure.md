---
type: causal_node
artifact_type: causal_node
schema_version: v1
node_key: fair-value-discounting-pressure
label: Fair-value discounting pressure
node_type: workflow_condition
status: hold
description: Pressure inside the workflow to pull estimated fair value downward because uncertainty or caution is being priced conservatively.
tags:
  - calibration
  - underconfidence
  - workflow-pricing
lifecycle_stage: hold
lifecycle_stage_updated_at: "2026-04-16T15:31:46Z"
lifecycle_stage_updated_by: advance_live_causal_graph_items.py
lifecycle_transition: active->hold
demotion_reason: "repair_causal_graph.py:mark_hold:utility_live_stage_conflicts_with_stats"
---

# Fair-value discounting pressure

## What this node means

- Pressure inside the workflow to pull estimated fair value downward because uncertainty or caution is being priced conservatively.

## When it applies

- Use when the pipeline appears directionally correct but still prices the case lower than the mechanism seems to justify.
- This node is useful for underconfidence and overweighted caution patterns.

## Boundaries

- Discounting pressure may be justified in truly ambiguous or hard-to-verify cases.
- This node should not be read as a blanket recommendation to increase probabilities.

## Linked evidence and artifacts

- Seeded as part of the initial reviewed v1 causal-map ontology on 2026-04-15.
