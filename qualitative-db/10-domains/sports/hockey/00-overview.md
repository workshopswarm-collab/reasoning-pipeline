---
type: domain_overview
domain: sports
subdomain: hockey
topic: hockey research overview
date_created: 2026-03-25
last_updated: 2026-03-26
agent: orchestrator
status: active
certainty: medium
importance: high
upstream_inputs: []
downstream_uses: []
related_entities: []
related_drivers: [performance, injuries-health, seasonality, team-dynamics]
tags: [domain/sports, subdomain/hockey, overview]
---

# Overview summary

Hockey is a low-scoring, high-variance team sport where goaltending, special teams, roster depth, and playoff randomness can distort simple talent comparisons. It deserves a standalone subdomain because its scoring environment and postseason structure create a distinct research shape from higher-scoring sports.

## Why this subdomain matters

This subdomain matters because hockey outcomes often hinge on variance-sensitive factors that are easy to underweight if a researcher imports assumptions from basketball or football. A useful hockey overview should orient around goal suppression, special teams, goalie performance, and how depth interacts with long regular seasons and volatile playoff series.

## Core conclusions

- Low scoring increases variance and weakens the signal from raw win-loss narratives.
- Goaltending and special teams can swing outcomes far more than casual cross-sport intuition suggests.
- Depth and roster balance matter because line matching and attrition shape long-run performance.
- Playoff hockey should not be read as a simple extension of regular-season hierarchy.

## Main evidence clusters

- goaltending quality and save-driven variance
- special teams performance
- even-strength team and player quality
- injuries and lineup continuity
- depth across forward and defensive units
- schedule, travel, and playoff-series context

## Important recurring objects

- leagues and playoff structures
- teams and line combinations
- star skaters and goaltenders
- special-teams units
- standings, schedules, and injury reports

## Important recurring drivers

- performance
- injuries-health
- seasonality
- team-dynamics

## Common conflicts or failure modes

- overreading short playoff samples as stable quality proof
- treating star power as sufficient without checking goaltending and depth
- ignoring special teams in close, low-scoring environments
- applying assumptions from higher-scoring sports too mechanically

## Missing coverage

- stronger goalie-specific evaluation guidance
- better injury and line-combination source notes
- clearer handling of playoff-series versus regular-season inference

## Most fragile assumptions

- that the better regular-season team should win a short series reliably
- that scoring talent alone explains hockey outcomes well
- that current form cleanly separates signal from puck luck

## Recommended next research steps

- keep game-to-game and playoff-series developments in `40-research/`
- use this note for stable structural orientation rather than rolling season commentary
- deepen team- and goalie-specific substructure only where repeated retrieval demand justifies it
