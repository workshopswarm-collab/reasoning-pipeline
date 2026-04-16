---
type: governance_rule
domain: vault-governance
status: active
last_updated: 2026-04-14
owner: orchestrator
tags: [governance, linkage, related-entities, related-drivers]
---

# Entity linkage framework

This file is subordinate to `qualitative-db/00-system/README.md`. If there is any conflict, follow the higher-level 00-system rules.

## Purpose

This framework defines how `related_entities` and `related_drivers` should be used across the vault.

The goal is to make the vault:
- easier to retrieve from
- easier to navigate semantically
- more consistent across canonical entity notes
- better for multi-hop reasoning
- better for downstream quant and learning review

`related_entities` is a **curated high-signal neighborhood**, not an exhaustive list of every possible connection.

## Core rule

Every canonical note should link to the **smallest set of entities/drivers needed to recover its structural context quickly**.

## Fluidity rule

Linkage metadata is **not** governed by exactly the same update threshold as canonical body prose.

Treat this distinction explicitly:
- canonical body content = stable summary content with a higher durability bar
- linkage fields = curated retrieval/navigation infrastructure that can be revised more fluidly when graph quality improves

This means:
- a note may receive a linkage-only update without requiring a substantive rewrite of the body
- reciprocal repairs, structural graph cleanup, and improved neighborhood selection are usually legitimate maintenance even when the underlying canonical note thesis has not changed
- linkage edits should still stay high-signal, compact, and intentional

Do not confuse "more fluid" with "unconstrained".

Linkages should be easier to refine than canonical body prose, but they should still reflect real structural relationships rather than incidental adjacency.

Priority order for links:
1. primary structural relationship
2. primary institutional or organizational relationship
3. primary competitive or adversarial relationship
4. one or two especially important contextual anchors

Do **not** use `related_entities` as a tag dump or a weak synonym list.

## Link quality standard

A good link should satisfy at least one of these:
- the entity directly governs, employs, contains, fields, issues, or owns the subject
- the entity is the subject’s primary team, party, company, country, institution, league, or protocol
- the entity is a main counterparty, rival, or strategic opponent
- the entity is necessary to understand why this subject matters in markets
- the entity is one of the first places a researcher would need to jump next

If a link is merely adjacent, incidental, or trivia-level, omit it.

## Size rule

Default target:
- `related_entities`: usually **3 to 8** items
- `related_drivers`: usually **2 to 5** items

Exceptions are allowed when justified, but the default should stay compact.

Too few links:
- makes retrieval brittle
- weakens graph navigation

Too many links:
- dilutes signal
- turns the field into a soft tag list

## Reciprocity rule

Important links should usually be reciprocal.

If:
- player A links to team B

then team B should usually also link back to player A if that player is one of the team’s defining figures.

Reciprocity is most important for:
- person ↔ team
- person ↔ party
- person ↔ company
- company ↔ product
- country ↔ leader
- protocol ↔ token (when distinct)
- team ↔ league

Reciprocity is **not** mandatory for every weak or secondary connection.

## Type-specific linkage rules

### Person

Usually link to:
- primary team / party / company / institution
- relevant country or state when politically or strategically important
- 1 to 2 especially important counterparties, rivals, or co-stars when structurally relevant

Examples:
- athlete -> team, league, maybe rival/co-star
- politician -> party, country/state, key rival or institution
- executive/founder -> company, flagship product if central, key rival only if highly relevant

### Team

Usually link to:
- league or competition organizer
- 1 to 3 defining players
- coach/manager only if canonized and materially important
- country/city only if necessary for market context

### League / organization / competition

Usually link to:
- the central teams, countries, or participants that define the market surface
- governance body if distinct and important
- a few flagship figures only when the event/league is unusually star-driven

### Party

Usually link to:
- country
- current key leader(s)
- main rival party or coalition opponent when structurally relevant
- election authority or institution only if repeatedly useful

### Company

Usually link to:
- flagship product(s) or platform(s)
- central founder/CEO only if canonically important
- primary dependency, partner, or competitor only when strategically important
- country only if regulation/geopolitics meaningfully matter

### Product

Usually link to:
- parent company
- main competitor(s) if they define the market comparison set
- key platform or ecosystem dependency when necessary

### Country

Usually link to:
- current or dominant leader when leader-centric
- major governing party if highly relevant
- key supranational body, ally, or adversary when necessary to explain significance
- one or two institutions only if repeatedly important to market interpretation

### Agency / central bank / ministry

Usually link to:
- country or supranational parent body
- central leader only if materially important
- key policy counterpart or institution only if repeatedly useful

### Protocol

Usually link to:
- token if analytically distinct
- issuer/foundation/company if distinct and important
- main ecosystem anchor or competitor only if structurally useful

### Token

Usually link to:
- underlying protocol
- issuing company/foundation if distinct
- key market-structure entity only when necessary

## Driver linkage rule

`related_drivers` should capture the main recurring mechanisms that explain why the note matters.

Use:
- only the most relevant drivers
- stable driver names from `qualitative-db/30-drivers/`
- compact lists that improve retrieval and later review

Do not add speculative driver names just because they sound adjacent.

## Update rule

When creating or revising a canonical note:
1. add the minimum high-signal `related_entities`
2. add the main `related_drivers`
3. check whether one-way links should be made reciprocal
4. do not expand the list unless a new link improves retrieval or interpretation

## Authority rule

Researchers may identify missing linkages in `40-research/` or learning notes.

Stable-layer linkage updates should normally be applied by:
- orchestrator
- decision-maker
- designated canonical maintainer

## Fast checklist

Before finalizing a note, ask:
- what is this entity’s primary organization, institution, or context?
- what is the single most important jump a future researcher would need next?
- what rival, counterparty, or governing body is structurally necessary?
- are the current links reciprocal where they should be?
- is the list compact enough to stay high-signal?
