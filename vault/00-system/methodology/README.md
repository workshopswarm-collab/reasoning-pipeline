---
type: system_guide
domain: methodology
status: active
last_updated: 2026-03-26
owner: orchestrator
tags: [methodology/guide, vault/00-system, workflow]
---

# Methodology

This folder is subordinate to `vault/00-system/README.md`.

Use this folder when you need the **workflow rules** for moving information through the vault.

## Fresh-instance shortcut

Read in this order:
1. `vault/00-system/START-HERE.md`
2. `vault/00-system/README.md`
3. then this folder only if you need canon-promotion or update-threshold detail

## Files in this folder

- `canonical-memory-workflow.md`
  - shortest workflow for deciding whether research should stay in `40-research/` or be promoted into canon
- `canonical-dossier-update-policy.md`
  - stricter detail on when a canonical entity note or major domain overview should actually be rewritten

## Rule of thumb

- if you are asking **where should this information live?** -> read `canonical-memory-workflow.md`
- if you are asking **is this change big enough to rewrite canon?** -> read `canonical-dossier-update-policy.md`

## Default rule

When unsure:
- write to research first
- do not rewrite canon early
- promote only durable, material changes into stable layers
