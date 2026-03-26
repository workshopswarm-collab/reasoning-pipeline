---
type: domain_overview
domain: sports
subdomain: american-football
topic: american football research overview
date_created: 2026-03-25
last_updated: 2026-03-26
agent: orchestrator
status: active
certainty: medium
importance: high
upstream_inputs:
  - vault/40-research/source-notes/by-domain/sports/2026-03-25-american-football-basics.md
downstream_uses: []
related_entities: []
related_drivers: [injuries-health, performance, leadership-changes, seasonality]
tags: [domain/sports, subdomain/american-football, overview]
---

# Overview summary

American football is a leverage-heavy team sport where quarterback play, line quality, coaching, injuries, and schedule context interact more sharply than raw season averages often suggest. It deserves a distinct subdomain because role concentration, play segmentation, and game-state leverage create a different research shape from other sports.

## Why this subdomain matters

This subdomain matters because football markets are unusually sensitive to a few key positions, scheme fit, and availability shocks. Researchers need an orientation layer that foregrounds leverage concentration and structure rather than treating football like a generic team sport with bigger rosters.

## Core conclusions

- Quarterback quality and availability can dominate almost every other input.
- Coaching, line play, and situational efficiency often matter more than casual narrative suggests.
- Role specialization and substitution make roster construction and injury interpretation unusually important.
- Small numbers of games increase noise, so baseline quality and current-state context both matter.

## Main evidence clusters

- quarterback and passing efficiency
- offensive and defensive line quality
- injuries and position-level availability
- coaching, scheme, and play-calling
- schedule strength and opponent context
- turnover variance and game-state leverage

## Important recurring objects

- quarterbacks and skill-position players
- offensive and defensive lines
- coaches and coordinators
- schedules, standings, and seeding context
- injury reports and roster transactions

## Important recurring drivers

- injuries-health
- performance
- leadership-changes
- seasonality

## Common conflicts or failure modes

- reading team record without adjusting for quarterback and line context
- treating one-score results as pure proof of stable quality
- overweighting highlight narratives while underweighting role concentration
- flattening scheme or coaching changes into generic talent updates

## Missing coverage

- deeper injury and position-value source guidance
- stronger coaching and scheme notes
- cleaner handling of schedule and opponent-adjusted efficiency

## Most fragile assumptions

- that team record alone captures true strength
- that skill-position narrative is more important than quarterback or line play
- that current health can be inferred from season averages

## Recommended next research steps

- keep current injury, lineup, and game-week changes in `40-research/`
- use this note for stable structural orientation rather than weekly market commentary
- expand only where repeated retrieval demand justifies deeper football substructure
