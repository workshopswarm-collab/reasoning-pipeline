---
type: source_note
domain: sports
subdomain: baseball
entity:
topic: MLB projections, playing time, and roster-shape expectations
question:
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
tags: [source/projections, domain/sports, subdomain/baseball]---

# Summary

FanGraphs Depth Charts is a high-value projection layer for expected team strength, player WAR, and playing-time assumptions entering or during a season.

## Key facts extracted

- Combines talent expectations with playing-time assumptions, making it useful for separating true-skill priors from current standings.
- Team-level projection shifts can reveal where health, role, or roster-construction assumptions are doing most of the work.
- Player projection baselines help identify which stars and regulars are actually carrying a club's expected edge.

## Why this source may matter

It helps separate current record from expected roster strength, which is important in baseball where injuries and depth matter heavily.

## Possible impact on the question

Useful when a baseball futures or team-strength question depends on likely roster quality going forward rather than backward-looking results.

## Evidence directly stated by source

- The source directly provides projected lineups, rotations, playing-time assumptions, and model-driven performance expectations.
- It supports claims about expected roster usage rather than just current standings.

## What is uncertain

- Projections depend on model assumptions, health, and playing-time estimates that can break quickly.
- Projected depth is not the same thing as realized in-season performance.

## Reliability notes

Useful model-based baseline, but projections should not be treated as ground truth; pair with official injuries, transactions, and realized performance.
