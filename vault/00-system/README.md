---
type: system_index
domain: system
status: active
last_updated: 2026-03-26
owner: orchestrator
tags: [system/index, vault/governance, vault/policies]
---

# 00-system

This folder is the vault's rule layer.

If a lower-level README conflicts with `vault/00-system/`, follow `vault/00-system/`.

## Fresh-instance read path

If you are new to this vault, read in this order:
1. `vault/README.md`
2. `vault/00-system/START-HERE.md`
3. `vault/00-system/README.md`
4. then only the layer READMEs relevant to your task

Read detailed policy files only when needed:
- canon vs research / splits / archive rules -> `governance/canonical-entity-policy.md`
- linkage behavior -> `governance/entity-linkage-framework.md`
- whether research should be promoted into canon -> `methodology/canonical-memory-workflow.md`
- exact canonical update threshold -> `methodology/canonical-dossier-update-policy.md`
- writing a note -> `templates/README.md` and the matching template

## What 00-system is for

Use `00-system/` for:
- governance rules
- editing and promotion workflow
- templates
- source-reliability guidance
- system-wide maintenance conventions

## Non-negotiable operating rules

### 1) Canon vs research

- `10-domains/`, `20-entities/`, and `30-drivers/` are stable layers
- `40-research/` is the working evidence layer
- `50-retrospectives/` is the resolved-case lesson layer

Default rule:
- if information is new, fast-changing, provisional, or unresolved -> put it in `40-research/`
- if information is durable and should still matter later -> it may belong in a stable layer

### 2) Roles

- **Orchestrator** -> may read/edit any vault document
- **Decision-maker** -> may read/edit any vault document
- **Researchers** -> may read any vault document, but normally edit only `vault/40-research/`

### 3) Canonical body vs linkage metadata

In a canonical entity note:
- **canonical body content** is slow-moving canon prose
- **linkage metadata** (`related_entities`, `related_drivers`) is curated graph/navigation infrastructure

Important distinction:
- body content has the higher durability bar
- linkage metadata may be updated more fluidly when retrieval, reciprocity, or structural navigation improves

### 4) Conflict handling

Preserve conflict early, resolve it late, learn from it afterward.

Default workflow:
1. preserve disagreement in `40-research/`
2. let the decision-maker adjudicate it
3. record lessons in `50-retrospectives/`
4. promote only durable cross-case lessons into stable layers

### 5) Duplicate / split rule

Default rule:
- one canonical file per real-world object unless the split is structurally real

Common valid splits:
- country vs leader
- company vs product/platform
- protocol/token vs issuer company
- league vs team
- team vs player
- institution vs leader

## Terminology rule

In vault policy language:
- a **dossier** means a **canonical entity note** in `vault/20-entities/`
- **canonical dossier** is acceptable shorthand for a canonical entity note
- research notes in `vault/40-research/` are not dossiers

## What to do before editing anything

1. decide whether the information is **canon** or **research**
2. check whether the file already exists
3. check whether you are editing **body content** or only **linkage metadata**
4. confirm you are allowed to write in that layer
5. use the matching template when creating a new note

## Default decisions if uncertain

Prefer:
- research over premature canon
- one file over duplicate files
- archive over delete
- explicit provenance over undocumented memory
- compact high-signal links over exhaustive graph dumps

## Folder map inside 00-system

### `START-HERE.md`
Minimal onboarding for a fresh-instance LLM.

### `governance/`
Rules for:
- what belongs in canon vs research
- how canonical entities should be split, merged, or archived
- how `related_entities` and `related_drivers` should behave

### `methodology/`
Workflow for:
- when research should stay in `40-research/`
- when it should be promoted into stable layers
- how to think about canonical update thresholds

### `templates/`
Templates for:
- source notes
- findings
- evidence maps
- investigations
- syntheses
- retrospectives
- canonical entity notes
- canonical update proposals

### `source-reliability/`
Short reference notes about source classes and metric sources.

## Detailed docs map

### Read first for policy
- `governance/README.md`
- `governance/canonical-entity-policy.md`
- `governance/entity-linkage-framework.md`

### Read when deciding whether to update canon
- `methodology/canonical-memory-workflow.md`
- `methodology/canonical-dossier-update-policy.md`

### Read when writing
- `templates/README.md`
- matching template file

### Read when checking source classes
- `source-reliability/README.md`
- matching source-reliability note

## One-line operating model

Write new evidence into research first, keep canonical body content strict, keep linkage metadata high-signal but more fluid, and promote only durable lessons into stable layers.
