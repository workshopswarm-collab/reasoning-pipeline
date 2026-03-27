---
type: domain_overview
domain: sports
subdomain:
topic: sports domain overview
date_created: 2026-03-25
last_updated: 2026-03-26
agent: orchestrator
status: active
certainty: medium-high
importance: high
related_entities: []
related_drivers: []
upstream_inputs:
  - qualitative-db/40-research/source-notes/by-domain/sports/2026-03-25-sports-reference-stats-overview.md
downstream_uses: []
tags: [domain/sports, overview]
---

# Overview summary

Sports is a performance-and-competition domain built around leagues, teams, players, schedules, standings, injuries, transactions, and large amounts of historical data. Good sports research should combine strong quantitative baselines with constant attention to availability, context, and changing roster conditions.

## Why this area matters

Sports matters because it is one of the most data-rich forecasting domains, but also one where injuries, lineup changes, schedule effects, and other contextual shifts can quickly overwhelm stable historical baselines. It rewards disciplined use of data without ignoring current-state disruptions.

## Core conclusions

- Sports research works best when strong quantitative baselines are combined with disciplined current-state adjustment.
- The current sports split is intentionally broad because different competitions have genuinely different structures: `american-football`, `baseball`, `basketball`, `formula-one`, `hockey`, and `soccer` each earn standalone orientation notes.
- Injuries, roster continuity, and schedule context are cross-sport necessities, but their meaning differs by sport.
- Cross-sport intuition transfers poorly when scoring environment, roster concentration, or format structure changes.

## Main evidence clusters

- team and player statistics
- historical performance baselines
- schedules and standings
- injuries and roster changes
- coaching and front-office decisions
- transactions and lineup context

## Important recurring objects

- leagues
- teams
- players
- coaches
- standings
- schedules
- injuries reports
- transaction logs

## Important recurring drivers

- injuries-health
- performance
- seasonality
- team-dynamics
- leadership-changes
- sentiment

## Common conflicts or failure modes

- relying on raw stats without adjusting for lineup discontinuity or role changes
- treating historical averages as stable when current availability has changed sharply
- overweighting recent streaks without enough baseline context
- ignoring league-specific structure and incentives

## Missing coverage

- injury-source hierarchy
- roster and transaction tracking notes
- league-specific metric playbooks
- schedule-density and fatigue notes
- broader coach and management coverage

## Most fragile assumptions

- that raw stats alone capture current state
- that historical averages remain valid under lineup discontinuity
- that league-level comparisons transfer cleanly across sports

## Recommended next research steps

- keep sport-specific current developments in `40-research/`
- use the existing sport subdomains rather than creating new ones prematurely
- deepen source hierarchies and metric playbooks before expanding the sports branch further
