---
type: system_index
domain: system
status: active
last_updated: 2026-03-25
owner: orchestrator
tags: [system/index, vault/governance]
---

# Governance

This folder contains the rules that govern how canonical memory is maintained.

## Active policies

- `canonical-entity-policy.md` — primary rule for deciding what belongs in `20-entities/` versus `40-research/`, how to handle splits, and how to prune or archive low-signal material.

## Scope

These policies apply most directly to:
- `vault/20-entities/`
- `vault/40-research/`
- cleanup, merge, split, archive, and demotion decisions
- template usage when creating new canonical entities

## Default rule

If there is uncertainty:
- prefer one canonical file per real-world object
- prefer stable canon over version churn
- prefer research notes over transient canon
- prefer archive over delete
