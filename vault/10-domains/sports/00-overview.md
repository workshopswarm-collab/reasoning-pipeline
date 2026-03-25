---
type: synthesis
domain: sports
subdomain: leagues-and-performance
topic: sports domain overview
date_created: 2026-03-25
agent: synthesizer
certainty: medium-high
importance: high
upstream_inputs:
  - vault/40-research/source-notes/by-domain/sports/2026-03-25-sports-reference-stats-overview.md
downstream_uses: []
tags: [domain/sports, overview]
---

# Synthesis summary

Sports research should be structured around leagues, teams, players, schedules, standings, injuries, transactions, and performance metrics.

## Core conclusions

- Sports is one of the most data-rich prediction domains.
- Historical baselines are unusually available and should be used aggressively.
- Teams, players, coaches, games, and seasons are all first-class objects.
- Injuries, lineup changes, schedule density, and transaction news can shift outlook quickly even when long-run baselines remain stable.

## Main evidence clusters

- team and player statistics
- historical performance baselines
- schedules and standings
- injuries and roster changes
- coaching/front-office decisions

## Conflicts between inputs

- strong long-run stats can be temporarily overwhelmed by short-run injury or availability shocks.

## Missing information

- injury-source hierarchy
- roster and transaction tracking notes
- league-specific metric playbooks
- schedule-density and fatigue notes

## Most fragile assumptions

- that raw stats alone capture current state
- that historical averages remain valid under lineup discontinuity

## Recommended next research steps

- create subfolders for baseball, basketball, football, soccer, and league-specific metric systems
- add canonical entity dossiers for teams, players, leagues, and injuries
