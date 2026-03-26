---
type: domain_overview
domain: sports
subdomain: baseball
topic: baseball research overview
date_created: 2026-03-25
agent: orchestrator
certainty: medium-high
importance: high
upstream_inputs:
  - vault/40-research/source-notes/by-domain/sports/2026-03-25-baseball-reference-mlb-structure.md
  - vault/40-research/source-notes/by-source/2026-03-25-mlb-standings-source.md
  - vault/40-research/source-notes/by-source/2026-03-25-mlb-transactions-source.md
  - vault/40-research/source-notes/by-source/2026-03-25-mlb-news-source.md
downstream_uses: []
related_entities: []
related_drivers: []
tags: [domain/sports, subdomain/baseball, overview]---

# Overview summary

## Why this subdomain matters

Baseball research should organize around league structure, team quality, lineup and rotation strength, player health/availability, transactions, and season-context signals like standings and prospect movement.

## Core conclusions

- Baseball is extremely roster- and availability-sensitive because daily lineups, rotations, and bullpen state matter over long seasons.
- Team evaluation should combine historical/team baselines with live injured-list and transaction context.
- Official standings and news are useful, but they need to be grounded in team and player quality.
- Baseball memory should treat teams, star players, standings context, transactions, and injuries as first-class retrieval objects.

## Main evidence clusters

- team and player statistical baselines
- standings and division context
- roster and injured-list moves
- official news and prospect/storyline shifts
- schedule and seasonality

## Conflicts between inputs

- strong season-long baselines can be temporarily overwhelmed by rotation injuries or lineup absences.

## Missing information

- pitching/rotation-specific source layer
- bullpen and lineup depth notes
- prospect and farm-system source hierarchy
- team-specific dossiers beyond the Blue Jays starter layer

## Most fragile assumptions

- that standings alone describe underlying team quality
- that roster continuity can be assumed over a long MLB season

## Recommended next research steps

- add canonical team dossiers for Blue Jays, Yankees, Dodgers, and other relevant clubs
- add star-player dossiers and rotation / injury / prospect notes