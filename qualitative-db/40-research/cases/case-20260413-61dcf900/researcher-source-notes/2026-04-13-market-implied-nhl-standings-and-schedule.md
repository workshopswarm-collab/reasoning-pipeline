---
type: source_note
case_key: case-20260413-61dcf900
dispatch_id: dispatch-case-20260413-61dcf900-20260413T184628Z
analysis_date: 2026-04-13
persona: market-implied
domain: sports
subdomain: hockey
entity: nhl
topic: will-the-los-angeles-kings-make-the-nhl-playoffs
question: Will the Los Angeles Kings make the 2025-26 NHL Playoffs?
driver: reliability
date_created: 2026-04-13
source_name: NHL official standings and team schedule
source_type: official league standings / schedule
source_url: https://api-web.nhle.com/v1/standings/2026-04-13
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [nhl]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-61dcf900/researcher-analyses/2026-04-13/dispatch-case-20260413-61dcf900-20260413T184628Z/personas/market-implied.md]
tags: [source-note, nhl, standings, schedule, official]
---

# Summary

Official NHL standings dated 2026-04-13 show Los Angeles at 87 points through 79 games, 8th in the Western Conference, with wildcardSequence 2. This places the Kings in the second Western wild-card slot as of the check time, one point ahead of Nashville (86 points through 80 games) and with three games remaining.

## Key facts extracted

- Los Angeles Kings: 87 points in 79 games; Western Conference seed 8; Pacific division sequence 4; wildcardSequence 2.
- Nashville Predators: 86 points in 80 games; Western Conference seed 9; wildcardSequence 3.
- Winnipeg and San Jose were both at 82 points in 79 games, still alive but further back.
- Los Angeles had won 4 straight and had a 6-1-3 last-10 record at the snapshot.
- Remaining Kings regular-season games from official club schedule: at Seattle (Apr 13), at Vancouver (Apr 14), at Calgary (Apr 16).
- Nashville had only two games left: vs San Jose (Apr 13), vs Anaheim (Apr 16).

## Evidence directly stated by source

- The NHL standings endpoint directly encodes conference order and wild-card positioning.
- The official team schedule directly states how many regular-season games remain and against whom.
- The market contract says official NHL information is the primary resolution source.

## What is uncertain

- The standings feed itself does not spell out each team’s exact clinching/elimination paths.
- It does not by itself quantify the probability of Los Angeles converting this position into an actual playoff berth.
- Because same-day games remain, the exact point threshold needed is still path-dependent.

## Why this source may matter

This is the governing source of truth for whether the Kings are presently in playoff position and for what schedule remains before resolution. For this market, the official NHL standings deserve the heaviest weight.

## Possible impact on the question

Being in the final wild-card spot with a one-point cushion and one game in hand on the nearest chaser is directly supportive of a Yes outcome, though not enough to justify near-certainty on its own.

## Reliability notes

Primary official league source. High credibility and direct relevance. Independence is limited because it is the authoritative record rather than an independent forecast, so it should be paired with a contextual probability source for conversion from current standing to implied odds.