---
type: governance_policy
domain: system
status: active
last_updated: 2026-03-26
owner: orchestrator
tags: [system/policy, vault/10-domains, subdomains, domain-overviews]
---

# Subdomain overview policy

This policy governs when the vault should create, keep, rewrite, merge, archive, or avoid subdomain folders and `00-overview.md` files inside `vault/10-domains/`.

It exists to prevent `10-domains/` from turning into a large set of thin, repetitive retrieval anchors.

## Core rule

Top-level domain overviews in `vault/10-domains/<domain>/00-overview.md` are domain notes, not subdomain notes, and should normally leave `subdomain:` blank.

A subdomain file should exist only when it adds **distinct structural orientation** that is not already handled well enough by:
- the parent domain overview
- canonical entity notes in `20-entities/`
- driver notes in `30-drivers/`
- research notes in `40-research/`

Default preference:
- **section inside the parent domain overview first**
- standalone subdomain file only after the area proves it deserves one

## When to create a subdomain folder

Create a new subdomain folder only when the area is all of the following:

1. **durable**
   - likely to matter across many future cases
   - not just a one-off event, release, controversy, or temporary narrative

2. **structurally distinct**
   - has a recognizably different evidence stack, institution set, or market structure from the parent domain

3. **retrieval-useful**
   - future researchers are likely to benefit from a dedicated orientation anchor instead of searching only through the parent overview or entities

And at least one of these should also be true:
- the area recurs often in actual market or research demand
- the vault already has enough supporting notes/entities that the subdomain can be written honestly
- the parent domain is getting too broad or noisy without the split

## When to create a subdomain `00-overview.md`

Do **not** create a subdomain `00-overview.md` just because a folder exists.

Create the `00-overview.md` only when you can write a real note that honestly includes most of these without filler:
- a clear overview summary
- why the area matters
- distinct evidence clusters
- distinct recurring objects
- distinct recurring drivers
- distinct failure modes or common misreads
- actual missing-coverage notes

If you cannot do that yet, keep the area as:
- a section in the parent domain overview, or
- a research note in `40-research/`

## Bad reasons to create a subdomain file

Do **not** create a subdomain `00-overview.md` for any of these reasons alone:
- symmetry with sibling folders
- one source note exists
- a handful of entities exist
- you expect the area might matter someday
- you want a placeholder for future work
- a topic is currently trending
- a product version or current event needs a home

## Driver-overlap rule

Some words can validly exist both as:
- a **subdomain** in `10-domains/`, and
- a **driver** in `30-drivers/`

Examples include:
- `polling`
- `elections`
- `trade`
- `sanctions`
- `diplomacy`
- `energy`
- `regulation`

This overlap is allowed only when the layer distinction is clear:

### In `10-domains/`
The subdomain note should focus on:
- institutions
- actors
- evidence sources
- recurring object types
- process structure
- category-specific failure modes

### In `30-drivers/`
The driver note should focus on:
- causal mechanism
- how the force changes outcomes
- when it matters
- how it interacts with other drivers
- how researchers misweight it

If the subdomain note would mostly repeat the driver note, do **not** create or keep it.

## Entity-overlap rule

Do not create a subdomain note when the material is really just an object bucket that is already better handled by `20-entities/`.

Warning signs:
- the note is mostly a list of people, companies, teams, or products
- the note adds little beyond “these objects exist”
- the note has no real evidence architecture beyond the entity set

In those cases, prefer:
- the parent domain overview, plus
- the relevant entity notes

## Naming rule

Use stable, disambiguated names.

Prefer names that reduce ambiguity for retrieval.

Good:
- `american-football`
- `chips-compute`
- `social-media`

Avoid names that are ambiguous across regions or layers when a clearer name exists.

## Maintenance rule

Subdomain notes are canonical background, but they are not sacred.

A subdomain `00-overview.md` should be reviewed when it becomes:
- too thin to justify retrieval weight
- stale relative to current vault structure
- mostly redundant with the parent domain
- mostly redundant with `30-drivers/`
- mostly a to-do list for work already completed elsewhere

## What to do with weak subdomain notes

When a subdomain note no longer earns its place:
1. preserve any still-useful ideas in the parent domain overview if needed
2. repoint obvious source-note `downstream_uses` to the parent overview or a better destination
3. **archive instead of delete**
4. keep the archive path explicit so the history is recoverable

Suggested archive location:
- `vault/60-uncategorized/archive/10-domains-subdomain-stubs/`

## Practical threshold

A subdomain note is usually justified only if it passes most of these tests:
- repeated future retrieval value seems likely
- there is a distinct evidence stack
- there is a distinct recurring object set
- there are distinct failure modes from the parent domain
- the note can be written without generic filler
- the note is not just duplicating a driver file

If it fails several of those tests, keep it out of `10-domains/` for now.

## Fast decision rule for the Orchestrator

Before creating a subdomain file, ask:
1. is this a durable area or just a current topic?
2. does it have structure beyond a list of entities?
3. does it have structure beyond a driver mechanism?
4. would a future researcher actually benefit from a dedicated orientation note?
5. can I write a real overview now without filler?

If the answer to any of 2 through 5 is weak, do not create the file yet.

## One-line policy summary

**Subdomain overviews should be created late, not early: only when the area has durable structure, distinct retrieval value, and enough substance to avoid becoming placeholder noise.**
