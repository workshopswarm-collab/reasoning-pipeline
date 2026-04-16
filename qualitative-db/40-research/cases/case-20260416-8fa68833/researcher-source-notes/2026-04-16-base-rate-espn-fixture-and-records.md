---
type: source_note
case_key: case-20260416-8fa68833
dispatch_id: dispatch-case-20260416-8fa68833-20260416T163913Z
analysis_date: 2026-04-16
persona: base-rate
domain: sports
subdomain: soccer
entity: barcelona
topic: case-20260416-8fa68833 | base-rate
question: Will FC Barcelona win on 2026-04-22?
driver:
date_created: 2026-04-16
source_name: ESPN LaLiga scoreboard and team schedule endpoints
source_type: sports schedule / standings API
source_url: https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard?dates=20260422
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [barcelona]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [sports, soccer, laliga, barcelona, celta-vigo, base-rate, source-note]
---

# Summary

ESPN's public soccer endpoints show the scheduled La Liga fixture on 2026-04-22 as Celta Vigo at Barcelona at Spotify Camp Nou, and show current season records/standings consistent with a strong base-rate edge for Barcelona.

## Key facts extracted

- The 2026-04-22 La Liga scoreboard lists `Celta Vigo at Barcelona` for 2026-04-22 19:30Z / 3:30 PM EDT.
- Venue is `Spotify Camp Nou`, so Barcelona is the home side.
- Barcelona is listed with a `26-1-4` record and `1st in Spanish LALIGA`.
- Celta Vigo is listed with an `11-11-9` record and `6th in Spanish LALIGA`.
- Recent Barcelona results in the schedule feed are strongly positive: wins over Espanyol, Atlético Madrid, Rayo Vallecano, Sevilla, and Athletic Club.
- Recent Celta Vigo results are mixed: draw vs Real Oviedo, win at Valencia, draw vs Alavés, loss at Betis, loss vs Real Madrid.

## Evidence directly stated by source

- The match exists on the stated date and is scheduled.
- Barcelona is at home.
- Barcelona has a materially better season record and league position than Celta Vigo.
- Recent form entering the match is better for Barcelona than for Celta Vigo.

## What is uncertain

- ESPN does not by itself prove the exact governing resolution source for the prediction market.
- The feed does not provide bookmaker probabilities or injury/news context.
- Schedule feeds can still change if a fixture is postponed or materially altered.

## Why this source may matter

This is the cleanest direct source for the basic structural setup of the match: same league, same date, home/away assignment, and current team-level performance context. Those are the core outside-view inputs for a base-rate assessment.

## Possible impact on the question

This source supports a high win probability for Barcelona relative to a generic La Liga match, because the favorite is both the home team and the league leader by record/standing.

## Reliability notes

- Good for fixture confirmation and current records.
- Public ESPN endpoints are useful but not the formal competition authority; they are better treated as strong contextual evidence than sole governing truth.
- Best paired with an official competition/team surface or market rules when source-of-truth ambiguity matters.
