---
type: source_note
case_key: case-20260413-e8e9e57e
dispatch_id: dispatch-case-20260413-e8e9e57e-20260413T224434Z
analysis_date: 2026-04-13
persona: market-implied
domain: sports
subdomain: hockey
entity: connor-mcdavid
topic: 2025-26 NHL Art Ross Trophy leaderboard status
question: Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?
date_created: 2026-04-13
source_name: Hockey-Reference 2025-26 NHL skater statistics
source_type: statistical reference / secondary aggregator
source_url: https://www.hockey-reference.com/leagues/NHL_2026_skaters.html
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: supports-yes
certainty: medium-high
importance: high
novelty: low
agent: market-implied
related_entities: [connor-mcdavid, nhl]
related_drivers: []
upstream_inputs: []
downstream_uses: [market-implied.md, market-implied.sidecar.json, evidence/market-implied.md]
tags: [source-note, sports, hockey, art-ross, leaderboard]
---

# Summary

Hockey-Reference’s 2025-26 NHL skater table shows Connor McDavid leading the league with 133 points, ahead of Nikita Kucherov at 128 and Nathan MacKinnon at 126. That makes the market’s extreme pricing directionally sensible: with the regular season effectively complete in this dataset, McDavid appears to be the points leader and therefore the presumptive Art Ross winner.

## Key facts extracted

- Hockey-Reference page title: `2025-26 NHL Skater Statistics`.
- Page summary states: `Points Leaders: Connor McDavid (133)`.
- Top rows shown in extracted page text list:
  - Connor McDavid: 80 GP, 47 G, 86 A, 133 PTS.
  - Nikita Kucherov: 74 GP, 43 G, 85 A, 128 PTS.
  - Nathan MacKinnon: 78 GP, 52 G, 74 A, 126 PTS.
- The visible gap from McDavid to the nearest challenger is 5 points.

## Evidence directly stated by source

- McDavid is the listed points leader for the 2025-26 NHL season.
- Kucherov and MacKinnon trail him by multiple points.
- The source presents a completed or nearly completed regular-season leaderboard rather than a speculative forecast.

## What is uncertain

- Hockey-Reference is not the official NHL resolution source.
- The extracted page does not by itself prove the NHL has formally announced the Art Ross winner yet.
- The page does not independently confirm whether any stat corrections or official post-publication changes remain possible.

## Why this source may matter

It is a strong independent contextual verification of the market’s assumption. If an established stats aggregator also shows McDavid leading the league by a meaningful margin late in the season, then a 90%+ market price is much easier to justify.

## Possible impact on the question

This source materially supports a `Yes` lean and supports the idea that the market is mostly pricing already-observable season totals rather than some hidden narrative.

## Reliability notes

- Strong for contextual leaderboard verification.
- Not the governing source of truth under the contract; official NHL information still controls resolution if available.
- Useful as an additional verification pass because it is meaningfully independent from Polymarket’s own page copy.