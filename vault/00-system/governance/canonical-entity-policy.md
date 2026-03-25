---
type: system_policy
domain: system
status: active
last_updated: 2026-03-25
owner: orchestrator
applies_to: [20-entities, 40-research, templates]
tags: [system/policy, memory/canonical, vault/governance]
---

# Canonical Entity Policy

This policy governs what belongs in `vault/20-entities/` versus `vault/40-research/`.

## Purpose

Keep canonical memory stable, compact, and high-signal.

Canonical entities should represent durable real-world objects that are likely to recur in forecasting, retrieval, and synthesis. High-churn material should live in the research layer instead.

## Core rule

**One canonical file per real-world object unless there is a real type distinction.**

### Allowed canonical splits

These are valid reasons to maintain separate canonical files:

- token/protocol vs issuer company
- country vs leader
- company vs product/platform
- league vs team
- team vs player
- institution vs leader

### Not allowed unless explicitly justified in the file body

These should normally be merged or avoided:

- company vs legal-suffix variant (`inc`, `holdings`, `group`, `markets`, etc.)
- same org represented as both `company` and `organization`
- same brand with slightly different corporate naming
- same product represented by multiple nearly identical canon files

If an exception is kept, the file must clearly explain why the split is structurally meaningful.

## What belongs in canonical memory (`20-entities`)

Canonical memory should contain durable, reusable entities such as:

- institutions
- countries
- leaders
- parties
- major companies/platforms
- long-lived products
- long-lived protocols
- sports leagues, teams, and durable player entities when sports markets are in scope

Canonical files should be written as relatively stable overviews, not rolling news feeds.

## What belongs in research (`40-research`)

Research should contain transient or fast-changing material such as:

- release notes
- model/version snapshots
- product-change notes
- temporary performance changes
- short-term narratives
- event-driven updates
- source extracts and factual monitoring notes

If the content is likely to stale quickly, it probably belongs in research, not canon.

## Stable-canon rule

If a file is primarily about a named release/version rather than a durable product family, default to `40-research/`.

Examples of content that should usually live in research rather than canon:

- specific model version notes
- product launch deltas
- temporary benchmark or performance claims
- short-lived narrative surges

## Archive instead of delete

When pruning low-signal or redundant material:

- prefer moving files to an archive location first
- do not destroy information unless there is a clear reason
- preserve provenance and the ability to recover past decisions

Recommended archive locations:

- `vault/60-uncategorized/archive/merged-duplicates/`
- `vault/60-uncategorized/archive/low-signal-media/`

## Duplicate-handling procedure

Before adding a new canonical entity:

1. search the target entity folder for the obvious name
2. check for close naming variants
3. check whether the object already exists under another type/folder
4. only create a new file if the split is real and useful

If a duplicate is found:

1. choose one canonical survivor
2. merge useful distinctions into that file if needed
3. archive the redundant file instead of deleting it
4. repair references after the move

## Canon update rule

Canonical files should update rarely.

New information should usually go into the research layer first. Only promote it into canon when:

- the change is durable
- it materially changes the long-run understanding of the entity
- the update improves future retrieval rather than merely reflecting recency

## Quality bar for canon

A canonical entity should be:

- durable
- high-signal
- likely to recur in prediction-market or research workflows
- distinct from adjacent entities
- worth retrieving months later

If it is mostly noise, hype, or short-horizon chatter, it should be archived or kept in research instead.

## Enforcement guidance

When uncertain:

- prefer fewer canonical files
- prefer broader stable entities over narrow versioned ones
- prefer research notes over speculative canon additions
- prefer archive over deletion
