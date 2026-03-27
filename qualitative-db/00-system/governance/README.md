---
type: system_index
domain: system
status: active
last_updated: 2026-03-25
owner: orchestrator
tags: [system/index, qualitative-db/governance]
---

# Governance

This folder contains the rules that govern how canonical memory is maintained.

This README is subordinate to `qualitative-db/00-system/README.md`. If there is any conflict, follow the higher-level 00-system rules.

Fresh-instance shortcut:
- read `qualitative-db/00-system/START-HERE.md` first
- read `canonical-entity-policy.md` before `entity-linkage-framework.md`
- read this folder only when you need canon/research boundary or linkage-policy detail

## Active policies

- `canonical-entity-policy.md` — primary rule for deciding what belongs in `20-entities/` versus `40-research/`, how to handle splits, and how to prune or archive low-signal material.
- `entity-linkage-framework.md` — rule for how `related_entities` and `related_drivers` should behave, including the distinction between stable canonical body prose and more fluid graph-maintenance metadata.
- `subdomain-overview-policy.md` — rule for when `10-domains/` subdomain folders and `00-overview.md` files should be created, rewritten, merged, archived, or avoided.

## Terminology note

In governance documents, a **dossier** means a canonical entity note in `qualitative-db/20-entities/`, not a research note.

## Scope

These policies apply most directly to:
- `qualitative-db/20-entities/`
- `qualitative-db/40-research/`
- cleanup, merge, split, archive, and demotion decisions
- template usage when creating new canonical entities

## Default rule

If there is uncertainty:
- prefer one canonical file per real-world object
- prefer stable canon over version churn
- prefer research notes over transient canon
- prefer archive over delete
