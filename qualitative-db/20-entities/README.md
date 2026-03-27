---
type: system_guide
domain: entities
status: active
last_updated: 2026-03-26
owner: orchestrator
tags: [entities/guide, qualitative-db/20-entities, linkage]
---

# 20-entities

This README is subordinate to `qualitative-db/00-system/README.md` and related 00-system policy files. If there is any conflict, follow `qualitative-db/00-system/`.

Fresh-instance shortcut:
1. read `qualitative-db/00-system/START-HERE.md`
2. read `qualitative-db/00-system/README.md`
3. read this file only if you are working in `20-entities/`
4. read governance detail only if needed:
   - `qualitative-db/00-system/governance/canonical-entity-policy.md`
   - `qualitative-db/00-system/governance/entity-linkage-framework.md`

This folder stores **canonical entity notes** for durable recurring objects.

Terminology note:
- in this vault, a **dossier** means a canonical entity note in `qualitative-db/20-entities/`
- **canonical dossier** is acceptable shorthand for a canonical entity note
- research-layer notes are not dossiers

Examples:
- countries
- people
- players
- parties
- agencies
- organizations
- companies
- products
- protocols
- tokens
- leagues
- teams

## Core distinction

Inside a canonical entity note, treat these as two different things:

### 1) Canonical body content

The body of the note is part of the stable canon.

It should stay:
- concise
- durable
- summary-oriented
- high-signal

Do **not** turn the body into a rolling news log.

### 2) Linkage metadata

Fields such as:
- `related_entities`
- `related_drivers`

are part of the vault's **graph/navigation layer**.

They should still be curated and high-signal, but they may be updated more fluidly than the body when:
- reciprocity is missing
- structural context is underlinked
- retrieval would improve from a better neighborhood
- cross-domain navigation is weaker than it should be

Important:
- linkage metadata is **not** an excuse for graph spam
- linkage metadata is **not** an exhaustive ontology export
- linkage metadata is **not** a substitute for writing good canonical body content

## Practical rule

Use a higher threshold for changing canonical body prose than for changing links.

That means:
- substantive canon rewrites should remain relatively rare
- linkage-only maintenance is normal and healthy when it improves graph quality

## What good entity notes should do

A strong canonical entity note should:
- explain what the object is
- explain why it matters
- stay useful months later
- connect to the right adjacent entities and drivers

The note does **not** need to explain every link in the body if the linkage is already structurally obvious.

## Default linkage shapes

Common patterns:
- person ↔ party ↔ country/institution
- person ↔ company ↔ product
- player ↔ team ↔ league
- country ↔ leader ↔ ally/adversary/institution
- protocol ↔ token ↔ issuer/company
- company ↔ platform/product ↔ dependency/customer when structurally important

For detailed linkage rules, follow:
- `qualitative-db/00-system/governance/entity-linkage-framework.md`

For canonical-content rules, follow:
- `qualitative-db/00-system/governance/canonical-entity-policy.md`

## Authority rule

Researchers may read all canonical entity notes.

Ordinary researchers should not directly rewrite `20-entities/` during case work.

Researchers may instead:
- note missing links in `40-research/`
- note taxonomy or graph issues in handoff notes
- propose stable-layer updates for later application by the orchestrator or decision-maker

## Fast mental model

- body = durable canon
- links = curated graph infrastructure
- both should be high-signal
- only the body needs the stricter durability threshold
