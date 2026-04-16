---
type: causal_node
artifact_type: causal_node
schema_version: v1
node_key: price-near-threshold
label: Price near threshold
node_type: market_state
status: active
description: Reference price is already close enough to a threshold or touch boundary that short-horizon path dynamics matter materially.
tags: ["threshold-touch", "path-risk", "short-horizon"]
---

# Price near threshold

## What this node means

- Reference price is already close enough to a threshold or touch boundary that short-horizon path dynamics matter materially.

## When it applies

- Use when the relevant market is within a small residual distance of the contract threshold.
- Most useful for touch-style markets rather than close-only contracts.

## Boundaries

- Do not treat this as automatically bullish in close-only or end-of-window close markets.
- Distance matters relative to remaining time and volatility, not as an absolute number alone.

## Linked evidence and artifacts

- Seeded as part of the initial reviewed v1 causal-map ontology on 2026-04-15.
