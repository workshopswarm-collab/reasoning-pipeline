---
type: system_index
domain: system
status: active
last_updated: 2026-03-25
owner: orchestrator
tags: [system/index, vault/governance, vault/policies]
---

# 00-system

This folder defines how the vault should be maintained.

Use it as the **high-level operating layer** for:
- governance rules
- templates
- source-quality standards
- system-wide maintenance conventions

It should stay small, stable, and easy to scan.

## High-level update policy

### 1) Keep canonical memory stable

`vault/20-entities/` is for durable entities that are worth retrieving repeatedly over time.

Canonical memory should contain:
- institutions
- countries
- leaders
- parties
- core companies/platforms
- long-lived products/protocols
- other durable recurring entities

Canonical files should **not** become rolling news logs.

### 2) Put transient material in research, not canon

`vault/40-research/` is for:
- release notes
- version snapshots
- short-term narratives
- temporary performance changes
- source extracts
- event-driven monitoring notes

If content is likely to stale quickly, default to research first.

### 3) One canonical file per real-world object unless the split is real

Allowed canonical splits include:
- country vs leader
- company vs product/platform
- token/protocol vs issuer company
- league vs team
- team vs player
- institution vs leader

Do **not** create multiple canon files for the same object just because naming differs slightly.

Avoid unless clearly justified:
- legal suffix variants (`inc`, `holdings`, `group`, `markets`)
- same org represented as both company and organization
- near-identical brand/corporate naming variants
- multiple canon files for one product family with no real structural distinction

### 4) Audit before adding or splitting

Before creating a new canonical file:
1. check whether the entity already exists
2. check naming variants
3. check whether it already exists under another type/folder
4. only create a new file if the distinction is real and useful

### 5) Archive instead of delete

When pruning low-signal or redundant material:
- move it to an archive location first
- preserve provenance
- prefer reversibility over destructive cleanup

Current archive locations:
- `vault/60-uncategorized/archive/merged-duplicates/`
- `vault/60-uncategorized/archive/low-signal-media/`

### 6) Prefer fewer better files

The vault should optimize for:
- retrieval quality
- durable relevance
- low duplication
- low taxonomy drift
- high signal-to-noise

When uncertain, prefer:
- broader stable entities over narrow versioned ones
- research notes over speculative canon additions
- archive over delete

## Current policy documents

### Governance
- `vault/00-system/governance/README.md`
- `vault/00-system/governance/canonical-entity-policy.md`

### Templates
- `vault/00-system/templates/entity-overview-template.md`
- `vault/00-system/templates/source-note-template.md`
- other templates in `vault/00-system/templates/`

### Source-quality guidance
- `vault/00-system/source-reliability/README.md`
- source reliability files under `vault/00-system/source-reliability/`

## Practical maintenance checklist

When updating the vault:
1. decide whether the information is **canon** or **research**
2. check for an existing file before creating a new one
3. use the relevant template
4. keep canon durable and concise
5. archive redundancy or low-signal content instead of deleting it
6. repair references after moves or merges

## Default interpretation

If a future update conflicts with stability, prefer:
- stable canon
- transient research notes
- reversible cleanup
- explicit policy over ad hoc expansion
