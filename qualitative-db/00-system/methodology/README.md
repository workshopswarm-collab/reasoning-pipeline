---
type: system_guide
domain: methodology
status: active
last_updated: 2026-03-26
owner: orchestrator
tags: [methodology/guide, qualitative-db/00-system, workflow]
---

# Methodology

This folder is subordinate to `qualitative-db/00-system/README.md`.

Use this folder when you need the **workflow rules** for moving information through the vault.

## Fresh-instance shortcut

Read in this order:
1. `qualitative-db/00-system/START-HERE.md`
2. `qualitative-db/00-system/README.md`
3. then this folder only if you need canon-promotion or update-threshold detail

## Files in this folder

- `canonical-memory-workflow.md`
  - shortest workflow for deciding whether research should stay in `40-research/` or be promoted into canon
- `canonical-dossier-update-policy.md`
  - stricter detail on when a canonical entity note or major domain overview should actually be rewritten
- `recursive-learning-system-spec.md`
  - concrete target spec for activating `50-learnings/` as a live recursive-improvement layer, including resolved-case learning packets, reviewed case notes, intervention tracking, and LMD runtime injection analogous to QMD
- `causal-map-lmd-integration-spec.md`
  - concrete target spec for adding a causal-map layer on top of the qualitative DB and using it to drive mechanism-aware LMD retrieval, intervention applicability, exposure logging, and learned retrieval-policy updates
- `causal-lifecycle-policy.md`
  - bounded promotion / decay / anti-sprawl policy for live causal-map topology and LMD-recallable mechanism structure
- `causal-map-lmd-implementation-roadmap.md`
  - phased implementation plan and current-status roadmap for the bounded self-improving LMD + causal-map system, including implemented phases, upcoming trial / promotion phases, and later repair / decay / retrieval-tuning work

## Rule of thumb

- if you are asking **where should this information live?** -> read `canonical-memory-workflow.md`
- if you are asking **is this change big enough to rewrite canon?** -> read `canonical-dossier-update-policy.md`

## Default rule

When unsure:
- write to research first
- do not rewrite canon early
- promote only durable, material changes into stable layers
