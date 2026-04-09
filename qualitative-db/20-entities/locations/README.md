---
type: system_guide
domain: entities
status: active
last_updated: 2026-04-07
owner: orchestrator
tags: [entities/guide, qualitative-db/20-entities, locations]
---

# locations

This folder stores canonical notes for **durable subnational places and geographically anchored strategic locations** that do not fit cleanly into `countries/`.

Use it for things like:
- states or provinces
- cities when they have recurring market/research relevance
- ports, chokepoints, and named strategic places
- emirates, regions, and other subnational place entities

Do **not** use it for:
- ordinary one-off event venues
- temporary battlefield labels
- generic geographic descriptions
- infrastructure objects that fit better as `products/`

Practical rule:
- if the object is primarily a **place**, use `locations/`
- if the object is primarily an **infrastructure asset or platform**, consider `products/`
- if the object is a sovereign state, keep it in `countries/`

Keep notes durable, compact, and retrieval-oriented.
