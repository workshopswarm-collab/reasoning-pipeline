---
type: domain_overview
domain: politics
subdomain: polling
topic: polling research overview
date_created: 2026-03-25
last_updated: 2026-03-26
agent: orchestrator
status: active
certainty: medium-high
importance: high
upstream_inputs:
  - qualitative-db/40-research/source-notes/by-domain/politics/2026-03-25-polling-basics.md
downstream_uses: []
related_entities: []
related_drivers: [polling, elections, media-narratives]
tags: [domain/politics, subdomain/polling, overview]
---

# Overview summary

The polling subdomain is the institutional and measurement layer around surveys, aggregators, turnout models, methodology, and polling ecosystems. It is distinct from the `polling` driver note, which explains how polling moves outcomes; this note explains what polling is made of and how researchers should orient around the measurement stack itself.

## Why this subdomain matters

Polling matters because it is one of the most reused political evidence classes, but it is easy to misread when sample quality, weighting, house effects, mode effects, and turnout assumptions are not explicit. The value of a polling subdomain is that it gives researchers a place to organize the measurement architecture rather than treating every poll as an isolated headline.

## Core conclusions

- Polls are inputs into political inference, not direct forecasts.
- Polling quality depends heavily on methodology, turnout assumptions, and firm-specific bias.
- Aggregation and trend interpretation usually matter more than isolated releases.
- Polling should be interpreted alongside institutions, candidate quality, and electoral rules.

## Main evidence clusters

- survey methodology and sample design
- likely-voter and turnout modeling
- house effects and pollster track records
- aggregation and trend interpretation
- mode effects and timing effects
- polling-market and media interaction

## Important recurring objects

- pollsters and polling firms
- aggregators and averages
- likely-voter models
- demographic weighting assumptions
- election administrators and official results
- media outlets that frame poll releases

## Important recurring drivers

- polling
- elections
- media-narratives
- sentiment

## Common conflicts or failure modes

- treating one poll as the current truth
- ignoring methodology differences across firms
- confusing polling movement with statistical noise
- comparing polls across different likely-voter assumptions as if they were identical

## Missing coverage

- pollster-quality notes by country or election type
- stronger guidance on house effects and mode effects
- better links from polling sources to actual election-result validation

## Most fragile assumptions

- that a polling average is automatically well calibrated
- that turnout assumptions are stable cycle to cycle
- that polling error is independent across firms or over time

## Recommended next research steps

- keep dated poll-release reactions in `40-research/`
- use this note for measurement structure and source orientation, not rolling campaign commentary
- expand source-quality notes before adding more polling-specific subfolders
