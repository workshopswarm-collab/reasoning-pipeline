---
type: source_note
case_key: case-20260416-e5b42460
dispatch_id: dispatch-case-20260416-e5b42460-20260416T051736Z
analysis_date: 2026-04-16
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: fenerbahce-vs-rizespor
question: Will Fenerbahçe SK win on 2026-04-17?
driver: performance
date_created: 2026-04-16
source_name: TheSportsDB event search and team/event endpoints
source_type: sports-data-aggregator
source_url: https://www.thesportsdb.com/api/v1/json/3/searchevents.php?e=Fenerbahce%20vs%20Rizespor
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers:
  - performance
upstream_inputs: []
downstream_uses: []
tags:
  - soccer
  - super-lig
  - h2h
---

# Summary

TheSportsDB confirms a Turkish Super Lig fixture on 2026-04-17 between Fenerbahçe and Rizespor and provides recent head-to-head results plus each club's most recent league result.

## Key facts extracted

- TheSportsDB lists `Fenerbahçe vs Rizespor` for `2026-04-17T17:00:00` UTC in the Turkish Super Lig, round 30, venue Ülker Stadium.
- Recent listed head-to-head results are strongly favorable to Fenerbahçe:
  - 2025-11-23: Rizespor 2-5 Fenerbahçe
  - 2025-02-02: Fenerbahçe 3-2 Rizespor
  - 2024-08-25: Rizespor 0-5 Fenerbahçe
  - 2024-02-17: Rizespor 1-3 Fenerbahçe
  - 2023-10-01: Fenerbahçe 5-0 Rizespor
- Fenerbahçe's latest listed league result was a 1-0 home win over Beşiktaş on 2026-04-05.
- Rizespor's latest listed league result was a 2-1 home win over Gaziantep on 2026-04-13.

## Evidence directly stated by source

- The fixture exists on the target date and is not started.
- Historical match results in this pairing have recently been lopsided toward Fenerbahçe.
- Both teams enter off wins in their most recent listed league matches.

## What is uncertain

- TheSportsDB is not the governing source of truth for market resolution.
- The endpoint sample accessed here did not expose injuries, suspensions, likely lineups, or deeper form tables.
- Aggregator data can lag or omit corrections.

## Why this source may matter

It provides a clean, machine-readable check that the scheduled event exists on the correct date and gives enough recent matchup context to anchor a baseline football-strength view.

## Possible impact on the question

The source supports a pro-Fenerbahçe directional lean, but it also leaves meaningful residual uncertainty because football wins are vulnerable to draw risk and roster/timing shocks.

## Reliability notes

Useful as a contextual and cross-check source, not as the final governing settlement source. Reliability is medium: broad coverage and current fixture availability are helpful, but it is still an aggregator rather than the official league or the market operator.