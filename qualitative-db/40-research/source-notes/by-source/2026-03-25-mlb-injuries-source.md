---
type: source_note
domain: sports
subdomain: baseball
entity:
topic: MLB injuries and availability context
question:
driver: injuries-health
date_created: 2026-03-25
source_name: MLB Injury Report
source_type: official-injuries
source_url: https://www.mlb.com/injuries
source_date: 2026
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [injuries-health, seasonality]
upstream_inputs: []
downstream_uses: []
tags: [source/official-injuries, domain/sports, subdomain/baseball]---

# Summary

The MLB injuries layer is an official source for tracking player health, injured-list status, and availability changes that can quickly alter team quality.

## Key facts extracted

- Baseball team strength changes materially when starting pitchers, catchers, or core middle-of-order bats become unavailable.
- Injury tracking should be treated as a core live-input layer rather than an optional annotation.
- Availability information is especially important in baseball because lineup, rotation, and bullpen roles compound over time.

## Why this source may matter

Baseball team strength can change materially through attrition, so a reliable injury source is necessary for any forward-looking read.

## Possible impact on the question

Useful when pricing a team or player market where current availability and replacement quality matter more than season-average statistics.

## Evidence directly stated by source

- The source directly reports injured-list placements, injury designations, and availability-related updates.
- It supports claims about whether a player is currently unavailable or returning.

## What is uncertain

- Return timelines, effectiveness after return, and true team-level impact are often uncertain.
- Injury labels alone do not capture depth-replacement quality.

## Reliability notes

Use as a primary official availability source; pair with transactions logs, team news, and player role context.
