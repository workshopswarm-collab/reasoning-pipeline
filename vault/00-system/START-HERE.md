---
type: system_quickstart
domain: system
status: active
last_updated: 2026-03-26
owner: orchestrator
tags: [system/quickstart, onboarding, fresh-instance]
---

# START HERE

Use this file if you are a fresh-instance LLM and need the minimum operating model for the vault.

## Read order

1. `vault/README.md`
2. `vault/00-system/START-HERE.md` ← this file
3. `vault/00-system/README.md`
4. then only the layer READMEs relevant to your task

Read these next only if needed:
- editing canonical entity notes -> `vault/00-system/governance/canonical-entity-policy.md`
- editing `related_entities` / `related_drivers` -> `vault/00-system/governance/entity-linkage-framework.md`
- deciding whether research should be promoted into canon -> `vault/00-system/methodology/canonical-memory-workflow.md`
- writing a new note -> `vault/00-system/templates/README.md` and the matching template

## Six-layer model

- `00-system/` = rules, workflow, templates
- `10-domains/` = stable domain overviews
- `20-entities/` = stable canonical entity notes
- `30-drivers/` = stable reusable causal mechanisms
- `40-research/` = working research, evidence, and investigations
- `50-retrospectives/` = after-the-fact lessons and evaluation

## First questions to ask

Before editing anything, decide:
1. is this **canon** or **research**?
2. am I editing **body content** or only **linkage metadata**?
3. do I actually need a new file, or does one already exist?
4. am I allowed to write in this layer?

## Role permissions

- **Orchestrator** -> may read/edit any vault document
- **Decision-maker** -> may read/edit any vault document
- **Researchers** -> may read any vault document, but normally edit only `vault/40-research/`

Default rule: ordinary researchers should not directly rewrite stable layers during routine case work.

## Canon vs research

Use **canon** for durable summaries that should still help months later.

Use **research** for:
- new evidence
- source extracts
- short-term developments
- version-specific notes
- temporary narratives
- unresolved conflict

When unsure, write to `40-research/` first.

## Canonical body vs linkage metadata

Inside a canonical entity note:
- **canonical body content** = slow-moving summary prose
- **linkage metadata** = `related_entities` and `related_drivers`

Important rule:
- body content has the higher durability threshold
- linkage metadata may be updated more fluidly when retrieval, reciprocity, or structural navigation improves

Fluid does **not** mean sloppy.
Keep links compact, high-signal, and structurally justified.

## Canonical entity rules

Default rule:
- one canonical file per real-world object unless the split is structurally real

Allowed common splits:
- country vs leader
- company vs product
- protocol/token vs issuer company
- league vs team
- team vs player
- institution vs leader

Taxonomy defaults:
- athletes -> `players/`
- non-athlete public figures -> `people/`
- state bodies -> `agencies/`
- non-state institutions -> `organizations/`
- commercial firms -> `companies/`

## Conflict rule

Preserve conflict early, resolve it late.

Default workflow:
1. preserve disagreement in `40-research/`
2. let the decision-maker adjudicate it
3. record lessons in `50-retrospectives/`
4. promote only durable lessons into stable layers

## Default actions by task

### If you need background context
Read:
- relevant `10-domains/.../00-overview.md`
- relevant `20-entities/.../*.md`
- relevant `30-drivers/*.md`

### If you need recent evidence
Read from `40-research/`.

### If you need to add new information
Default to `40-research/` first.

### If you need to update canon
Only do it when the change is durable, material, or the current canon is clearly misleading.

### If you need to repair links
You may make linkage-only updates without treating them as full canonical rewrites, as long as the links remain high-signal.

## Folder-specific read path

- working in `20-entities/` -> read `vault/20-entities/README.md`
- working in `30-drivers/` -> read `vault/30-drivers/README.md`
- working in `40-research/` -> read `vault/40-research/README.md`
- working in `50-retrospectives/` -> read `vault/50-retrospectives/README.md`

## If uncertain

Prefer this order:
- research over premature canon
- one file over duplicate files
- archive over delete
- explicit provenance over memory by implication
- compact high-signal links over exhaustive graph dumps
