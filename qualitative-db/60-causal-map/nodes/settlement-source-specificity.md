---
type: causal_node
artifact_type: causal_node
schema_version: v1
node_key: settlement-source-specificity
label: Settlement source specificity
node_type: source_condition
status: active
description: The contract depends on a specific governing source, venue, or benchmark rather than broad consensus reporting.
tags: ["source-truth", "settlement-mechanics", "venue-specific"]
---

# Settlement source specificity

## What this node means

- The contract depends on a specific governing source, venue, or benchmark rather than broad consensus reporting.

## When it applies

- Use when the contract names a specific exchange, publication, authority, or benchmark as decisive.
- This node is especially important when secondary reporting can diverge from the governing source.

## Boundaries

- Do not activate this in plain consensus-reporting markets with no special benchmark surface.
- Specificity increases operational risk even when directional reasoning is straightforward.

## Linked evidence and artifacts

- Seeded as part of the initial reviewed v1 causal-map ontology on 2026-04-15.
