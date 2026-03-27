---
type: system_guide
domain: domains
status: active
last_updated: 2026-03-26
owner: orchestrator
tags: [domains/guide, qualitative-db/10-domains, workflow]
---

# 10-domains

This README is subordinate to `qualitative-db/00-system/README.md` and related 00-system policy files. If there is any conflict, follow `qualitative-db/00-system/`.

Fresh-instance shortcut:
1. read `qualitative-db/00-system/START-HERE.md`
2. read `qualitative-db/00-system/README.md`
3. read this file only if you are working in `10-domains/` or using domain overviews for background framing

This folder stores **stable domain overviews**.

For rules on whether a new subdomain folder or `00-overview.md` should exist at all, follow:
- `qualitative-db/00-system/governance/subdomain-overview-policy.md`

Use it to answer:
- what kind of area is this?
- what are its main subareas, recurring objects, and background concepts?
- what broad evidence clusters or institutions matter here?
- what coverage is still missing?
- how should a fresh researcher orient before doing case-specific work?

## What belongs here

Use `10-domains/` for:
- durable subject-area overviews
- stable background framing
- recurring evidence clusters and background concepts
- major institutions, structures, and category-level distinctions
- common failure modes in a domain
- coverage maps and durable research priorities

Examples:
- crypto
- culture
- economics
- geopolitics
- politics
- sports
- tech-ai

## What does not belong here

Do **not** use this folder for:
- time-stamped case work
- raw source extraction
- one-off investigations
- temporary narratives
- version-specific product tracking
- entity-specific canonical memory that belongs in `20-entities/`

If it is case-specific, put it in `40-research/`.
If it is object-specific canon, put it in `20-entities/`.
If it is a reusable causal mechanism, put it in `30-drivers/`.

## Structure rule

Default structure:
- one folder per major domain
- one `00-overview.md` per domain by default
- top-level domain `00-overview.md` files should normally leave `subdomain:` blank
- add subdomain folders and subdomain `00-overview.md` files only when the area has distinct structural retrieval value
- keep folders coarse and stable
- avoid over-nesting unless coverage actually justifies it

Do not create subdomain files and folders as symmetry placeholders.
If a topic is still thin, keep it as a section inside the parent domain overview or in `40-research/` until it earns a standalone note.

## Writing rule

Domain notes are canonical background, not research-layer syntheses.

A strong domain overview should help future researchers:
- orient quickly
- understand the shape of the domain
- identify the main evidence clusters, institutions, and recurring object types
- avoid repeated framing mistakes
- see where current memory coverage is thin

## Template

When creating or substantially rewriting a domain overview, use:
- `qualitative-db/00-system/templates/domain-overview-template.md`

The template is meant for:
- top-level domain `00-overview.md` files
- major subdomain overviews when a subfolder has earned one

## Relationship to other layers

- `10-domains/` = durable background framing
- `20-entities/` = durable object-level memory
- `30-drivers/` = durable cross-case mechanisms
- `40-research/` = case-specific evidence and reasoning
- `50-retrospectives/` = after-the-fact lessons

A useful rule of thumb:
- if you are asking **what kind of area is this?** -> `10-domains/`
- if you are asking **what is this thing?** -> `20-entities/`
- if you are asking **what mechanism or recurring force matters?** -> `30-drivers/`
- if you are asking **what happened in this case?** -> `40-research/`
