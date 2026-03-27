---
type: domain_overview
domain: sports
subdomain: baseball
topic: baseball research overview
date_created: 2026-03-25
last_updated: 2026-03-26
agent: orchestrator
status: active
certainty: medium-high
importance: high
upstream_inputs:
  - qualitative-db/40-research/source-notes/by-domain/sports/2026-03-25-baseball-reference-mlb-structure.md
  - qualitative-db/40-research/source-notes/by-source/2026-03-25-mlb-standings-source.md
  - qualitative-db/40-research/source-notes/by-source/2026-03-25-mlb-transactions-source.md
  - qualitative-db/40-research/source-notes/by-source/2026-03-25-mlb-news-source.md
downstream_uses: []
related_entities: []
related_drivers: [performance, injuries-health, seasonality, team-dynamics]
tags: [domain/sports, subdomain/baseball, overview]
---

# Overview summary

Baseball is a long-season, roster-sensitive sport where daily lineup changes, starting pitching, bullpen usage, injuries, and organizational depth can overwhelm simple standings-based judgment. It deserves a standalone overview because its cadence, sample structure, and roster-management demands create a distinct research shape from other major sports.

## Why this subdomain matters

This subdomain matters because baseball markets are unusually sensitive to availability, rotation quality, bullpen state, and transaction churn over a long schedule. Researchers need an orientation layer that foregrounds player-level and staff-level context rather than treating team record as a stable summary of team quality.

## Core conclusions

- Baseball is highly roster- and availability-sensitive because lineups, rotations, and bullpen usage change constantly.
- Team quality should be evaluated through both long-run baselines and current roster state.
- Official standings and news are useful context, but they do not substitute for player and pitcher quality.
- Organizational depth, not just star power, matters because injuries and daily variance accumulate over long seasons.

## Main evidence clusters

- team and player statistical baselines
- rotation and bullpen quality
- lineup strength and injured-list status
- standings, division context, and schedule
- transactions, prospect movement, and roster churn
- official news and role changes

## Important recurring objects

- teams and divisions
- starting pitchers and bullpens
- hitters and lineup cards
- injured-list reports and transactions
- prospects and farm-system call-ups
- standings and schedule context

## Important recurring drivers

- performance
- injuries-health
- seasonality
- team-dynamics

## Common conflicts or failure modes

- treating standings as a sufficient proxy for current team strength
- underweighting rotation injuries, bullpen fatigue, or lineup absences
- reading small hot or cold streaks without enough baseline context
- ignoring prospect promotions and transaction churn in long-season evaluation

## Missing coverage

- stronger rotation- and bullpen-specific source guidance
- better prospect and farm-system source hierarchy
- clearer handling of opponent-adjusted team and player baselines

## Most fragile assumptions

- that roster continuity can be assumed over a long MLB season
- that current record cleanly reflects current roster quality
- that one or two star players summarize team outlook well enough

## Recommended next research steps

- keep game-, injury-, and transaction-specific developments in `40-research/`
- use this note for stable structural orientation around roster management and season context
- deepen substructure only where repeated retrieval demand justifies team- or pitcher-workflow specialization
