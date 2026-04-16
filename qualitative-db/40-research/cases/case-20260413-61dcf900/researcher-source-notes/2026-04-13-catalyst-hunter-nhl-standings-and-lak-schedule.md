---
type: source_note
case_key: case-20260413-61dcf900
dispatch_id: dispatch-case-20260413-61dcf900-20260413T184628Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: sports
subdomain: hockey
entity: nhl
topic: western conference playoff race
question: Will the Los Angeles Kings make the NHL Playoffs?
driver: reliability
date_created: 2026-04-13
source_name: NHL standings API and club schedule API
source_type: official league data
source_url: https://api-web.nhle.com/v1/standings/2026-04-13
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities:
  - nhl
related_drivers:
  - reliability
upstream_inputs: []
downstream_uses: []
tags:
  - source-note
  - nhl
  - standings
  - schedule
---

# Summary

Official NHL data on 2026-04-13 shows Los Angeles at 87 points through 79 games, eighth in the Western Conference and second wild card by `wildcardSequence: 2`. The same official API also shows Los Angeles has three remaining games: at Seattle on 2026-04-13, at Vancouver on 2026-04-14, and at Calgary on 2026-04-16.

## Key facts extracted

- LAK: 87 points, 79 games played, 34-26-19, four-game winning streak, `wildcardSequence: 2`.
- West race around the cutoff:
  - ANA 90 points in 80 games
  - LAK 87 points in 79 games
  - NSH 86 points in 80 games
  - WPG 82 points in 79 games
  - SJS 82 points in 79 games
- Maximum remaining points from current standings:
  - LAK max 93
  - NSH max 90
  - WPG max 88
  - SJS max 88
- Relevant remaining schedule from official club schedule endpoints:
  - LAK: SEA, VAN, CGY
  - NSH: SJS, ANA
  - ANA: MIN, NSH
  - WPG: VGK, UTA, SJS
  - SJS: NSH, CHI, WPG

## Evidence directly stated by source

- Official standings data identifies current point totals, games played, conference order, division order, and wild-card ordering.
- Official schedule data identifies the remaining opponents and dates.

## What is uncertain

- The API output does not by itself state the exact clinch/elimination combinatorics for LAK on 2026-04-13.
- Tiebreak details are not embedded in this note, though the NHL standings page links to official playoff-format and tie-breaking procedure pages.

## Why this source may matter

This is the governing primary source for both terminal truth and near-term catalyst timing. With only three games left, the market is mostly about whether LAK converts a narrow but real edge at the cutoff line before the schedule closes.

## Possible impact on the question

The official standings imply LAK is currently in a qualifying slot, but not safely. The remaining games on Apr. 13, 14, and 16 are the main repricing catalysts. NSH-SJS on Apr. 13 is especially important because at least one direct pursuer must fail to take a full two points.

## Reliability notes

This is the highest-quality source in the set because it is official NHL data and aligns with the market resolution source. It is direct evidence for standings state and game timing, but not a full explicit settlement notice by itself.