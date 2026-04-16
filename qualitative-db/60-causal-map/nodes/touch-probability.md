---
type: causal_node
artifact_type: causal_node
schema_version: v1
node_key: touch-probability
label: Touch probability
node_type: risk_state
status: active
description: Latent probability that any qualifying touch or intraperiod event occurs before the contract window ends.
tags: ["threshold-touch", "hazard-rate", "path-probability"]
---

# Touch probability

## What this node means

- Latent probability that any qualifying touch or intraperiod event occurs before the contract window ends.

## When it applies

- Use for markets that resolve on any qualifying touch, print, or intraperiod extreme.
- Treat as a path-sensitive state rather than a thesis-quality narrative state.

## Boundaries

- Do not conflate this with directional conviction in close-only contracts.
- This node should be conditioned by mechanics, time remaining, and source constraints.

## Linked evidence and artifacts

- Seeded as part of the initial reviewed v1 causal-map ontology on 2026-04-15.
