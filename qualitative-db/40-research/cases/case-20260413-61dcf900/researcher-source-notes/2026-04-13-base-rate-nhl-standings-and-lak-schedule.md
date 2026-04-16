---
type: source_note
case_key: case-20260413-61dcf900
dispatch_id: dispatch-case-20260413-61dcf900-20260413T184628Z
analysis_date: 2026-04-13
persona: base-rate
domain: sports
subdomain: hockey
entity: nhl
topic: los-angeles-kings-playoff-qualification
question: Will the Los Angeles Kings make the NHL Playoffs?
driver: reliability
date_created: 2026-04-13
source_name: NHL API standings and LA Kings season schedule
source_type: primary
source_url: https://api-web.nhle.com/v1/standings/2026-04-13
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities:
  - nhl
related_drivers:
  - reliability
upstream_inputs: []
downstream_uses: []
tags: [sports, nhl, kings, playoff-race, primary-source]
---

# Summary

Official NHL API standings for 2026-04-13 show Los Angeles at 87 points through 79 games, 8th in the Western Conference and holding the second wild-card position (`wildcardSequence: 2`) with three games left. Nashville is immediately behind at 86 points through 80 games. LA's official season schedule shows three remaining games: at Seattle on Apr. 13, at Vancouver on Apr. 14, and at Calgary on Apr. 16.

## Key facts extracted

- Los Angeles Kings: 87 points, 79 games played, Western Conference 8th, Pacific Division 4th, `wildcardSequence: 2`.
- Nashville Predators: 86 points, 80 games played, Western Conference 9th, `wildcardSequence: 3`.
- LA has one game in hand on Nashville and currently occupies the final playoff spot.
- LA's last 10 games: 6-1-3, current streak W4.
- Goal differential remains negative (-21), which is weaker than a typical safely-in field team and suggests their current spot is somewhat fragile.
- Remaining LA schedule from official club schedule endpoint: @SEA, @VAN, @CGY.

## Evidence directly stated by source

- Current standings rank/order, points, games played, streaks, and wild-card ordering.
- Remaining regular-season opponents and dates for LA.
- Official clinch indicators for already-qualified teams; LA has no clinch marker yet.

## What is uncertain

- The source does not itself spell out the exact magic number or elimination combinations.
- The official API reflects standings state at fetch time; other teams' same-day results can still change the race.
- The schedule endpoint does not by itself state opponent incentives, backup goalie usage, or roster/injury context.

## Why this source may matter

This is the governing primary source for whether LA is currently in playoff position and how many games remain. Because the contract resolves on official NHL qualification rules, official standings and official team schedules are the cleanest source-of-truth surfaces short of a direct NHL clinched/eliminated announcement.

## Possible impact on the question

The official standings put LA slightly above the playoff cut line with a game in hand, which supports a probability above 50%. But the edge is small enough that a base-rate view should not treat the team as near-certain despite the market's 73.5% price.

## Reliability notes

- Primary official source from NHL infrastructure.
- High reliability for standings/schedule facts.
- Less useful for broader context such as historical frequencies or rival-team path analysis, so contextual supplementation is still needed.