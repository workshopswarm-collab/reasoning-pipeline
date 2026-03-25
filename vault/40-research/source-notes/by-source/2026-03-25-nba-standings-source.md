---
type: source_note
domain: sports
subdomain: basketball
entity:
topic: NBA standings as official current-state source
driver: seasonality
date_created: 2026-03-25
source_name: NBA Standings
source_type: official-standings
source_url: https://www.nba.com/standings
source_date: 2026
credibility: high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers: [seasonality, injuries-health]
upstream_inputs: []
downstream_uses: []
tags: [source/official-standings, domain/sports, subdomain/basketball]
---

# Summary

NBA standings are the official current-state source for conference position, tiebreak context, and postseason race framing.

## Key facts extracted

- Standings include playoff and play-in positioning context.
- Tiebreak rules are surfaced explicitly.
- Useful as an official snapshot of where teams sit in the regular-season race.

## Why this source may matter

Standings are a core live input for contender and playoff-path evaluation.

## Reliability notes

High-quality official source; pair with injuries, transactions, and player/team performance notes.
