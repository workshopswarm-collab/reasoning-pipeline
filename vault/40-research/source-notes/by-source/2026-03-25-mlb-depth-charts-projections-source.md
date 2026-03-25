---
type: source_note
domain: sports
subdomain: baseball
entity:
topic: MLB projections, playing time, and roster-shape expectations
driver: seasonality
date_created: 2026-03-25
source_name: FanGraphs Depth Charts
source_type: projections
source_url: https://www.fangraphs.com/depthcharts.aspx?position=Standings
source_date: 2026
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [seasonality, injuries-health, sentiment]
upstream_inputs: []
downstream_uses: []
tags: [source/projections, domain/sports, subdomain/baseball]
---

# Summary

FanGraphs Depth Charts is a high-value projection layer for expected team strength, player WAR, and playing-time assumptions entering or during a season.

## Key facts extracted

- Combines talent expectations with playing-time assumptions, making it useful for separating true-skill priors from current standings.
- Team-level projection shifts can reveal where health, role, or roster-construction assumptions are doing most of the work.
- Player projection baselines help identify which stars and regulars are actually carrying a club's expected edge.

## Why this source may matter

It adds a forward-looking neutral baseline that complements historical stats and official current-state sources.

## Reliability notes

Useful model-based baseline, but projections should not be treated as ground truth; pair with official injuries, transactions, and realized performance.
