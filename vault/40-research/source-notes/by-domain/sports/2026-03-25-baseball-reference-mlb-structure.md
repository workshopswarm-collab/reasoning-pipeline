---
type: source_note
domain: sports
subdomain: baseball
entity:
topic: MLB ecosystem structure and baseball metrics coverage
question:
driver: injuries-health
date_created: 2026-03-25
source_name: Baseball Reference
source_type: stats-database
source_url: https://www.baseball-reference.com/
source_date: 2026
credibility: high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: orchestrator
related_entities: [toronto-blue-jays, new-york-yankees, los-angeles-dodgers]
related_drivers: [injuries-health, leadership-changes, seasonality]
upstream_inputs: []
downstream_uses: [vault/10-domains/sports/baseball/00-overview.md]
tags: [domain/sports, subdomain/baseball, source/stats-database]
---

# Summary

Baseball Reference is the core structured source for MLB seasons, teams, player pages, standings, leaders, schedules, and transactions, making it a foundational neutral source for baseball memory.

## Key facts extracted

- Team, player, season, standings, leaders, and transactions are all first-class objects.
- Baseball research can lean heavily on historical and league-structured data.
- The site exposes both league-wide and team-specific pathways, which fit well with entity dossiers.

## Evidence directly stated by source

- The site surfaces MLB summary pages, scores, schedules, leaders, standings, and transactions.
- It presents every major league team as a navigable statistical object.

## What is uncertain

- Standings and leader snapshots are time-sensitive and should not be treated as permanent facts.

## Why this source may matter

It is the backbone source for baseball metrics, team history, player baselines, and current standings context.

## Possible impact on the question

It is the backbone source for baseball metrics, team history, player baselines, and current standings context.

## Reliability notes

Strong neutral baseline for baseball statistics and historical context; should be paired with official MLB news, transactions, and injury/availability reporting.
