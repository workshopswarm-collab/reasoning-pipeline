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

### Linkage rule

Canonical notes should follow the `entity-linkage-framework.md` rules for `related_entities` and `related_drivers`.

Use `related_entities` as a curated high-signal neighborhood, not a synonym list or exhaustive graph dump.

Use `related_drivers` to capture the main recurring mechanisms that explain why the note matters.

Important distinction:
- canonical body content should remain slow-moving and durable
- linkage metadata may be updated more fluidly when that improves retrieval, navigation, reciprocity, or structural context

A linkage-only update does **not** need to clear the same threshold as a substantive rewrite of the canonical body content, provided the new links remain high-signal and structurally justified.

### Sports-athlete classification rule

Within `vault/20-entities/`:

- use `players/` for people whose primary canonical relevance is as athletes competing in sports
- use `people/` for non-athlete public figures such as politicians, executives, creators, commentators, and other general public personalities
- if a person is primarily retrieved because of sports competition, place them in `players/` even though they are literally also a person

This is a retrieval-oriented taxonomy, not a metaphysical one. The goal is to keep sports entities grouped consistently and avoid splitting athletes across both `people/` and `players/`.

Default rule:
- athlete with sports-market relevance -> `players/`
- non-athlete public figure -> `people/`

Do not keep both a `people/<name>.md` and `players/<name>.md` file for the same athlete unless there is an explicit, durable non-sports identity split that is clearly justified in the file body.

### Agencies vs organizations classification rule

Within `vault/20-entities/`:

- use `agencies/` for public-sector authorities or formal state bodies
- use `organizations/` for non-state institutions, multilateral bodies, alliances, foundations, governing bodies, and other institution-like entities that are not ordinary state agencies
- use `companies/` for for-profit commercial firms, including private labs and venture-backed companies, even when they are culturally discussed like institutions

Default rule:
- ministry, department, regulator, central bank, court, legislature, military, intelligence service, election authority, or statutory public office -> `agencies/`
- intergovernmental body, alliance, nonprofit/foundation, standards/governing body, or recurring non-state institution -> `organizations/`
- private commercial firm -> `companies/`

This is also a retrieval-oriented taxonomy. The goal is to separate state power, non-state institutional coordination, and commercial actors cleanly enough that adjacent entities do not collapse into one bucket.

Do not keep the same entity in both `agencies/` and `organizations/`, or both `organizations/` and `companies/`, unless there is an explicit and durable structural split that is clearly justified in the file body.

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
- recurring and material current information contradicts what is in canonical files.
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
