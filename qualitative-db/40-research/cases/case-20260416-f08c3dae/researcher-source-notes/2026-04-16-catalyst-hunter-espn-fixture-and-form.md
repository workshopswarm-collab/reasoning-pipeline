---
type: source_note
case_key: case-20260416-f08c3dae
dispatch_id: dispatch-case-20260416-f08c3dae-20260416T041907Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: sports
subdomain: colombian-football
entity:
topic: Deportes Tolima vs Deportivo Pereira fixture timing and recent form snapshot
question: Will CD Tolima win on 2026-04-18?
driver:
date_created: 2026-04-16
source_name: ESPN fixture/results pages for Deportes Tolima and Deportivo Pereira
source_type: secondary-aggregator
source_url: https://www.espn.com/soccer/match/_/gameId/401850871/deportivo-pereira-deportes-tolima
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [colombia]
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-analyses/2026-04-16/dispatch-case-20260416-f08c3dae-20260416T041907Z/personas/catalyst-hunter.md
tags: [source-note, espn, fixture, form, colombian-primera-a]
---

# Summary

ESPN's embedded match and team event data confirms the market's referenced match is the Colombian Primera A fixture between Deportes Tolima and Deportivo Pereira on Saturday, April 18, 2026 at 7:10 PM EDT, hosted by Tolima at Estadio Manuel Murillo Toro in Ibague. The same ESPN result feeds show Tolima entering off a congested but stronger recent sequence than Pereira.

## Key facts extracted

- Match identified as ESPN gameId `401850871`.
- Fixture timing listed as `2026-04-18T23:10Z` / `Sat, April 18th at 7:10 PM EDT`.
- Venue listed as `Estadio Manuel Murillo Toro`, Ibague, Colombia.
- Competition listed as `Colombian Primera A`.
- Tolima recent results visible in ESPN event feed before this match:
  - Apr 14: lost 3-1 at Nacional in CONMEBOL Libertadores.
  - Apr 10/11: lost 1-0 at Deportivo Pasto in Primera A.
  - Apr 7/8: drew 0-0 vs Universitario in Libertadores.
  - Apr 4/5: drew 2-2 vs Independiente Santa Fe in Primera A.
  - Mar 31/Apr 1: beat Aguilas Doradas (scoreline visible in feed but truncated in extraction context).
- Pereira recent results visible in ESPN event feed before this match:
  - Apr 10: drew 0-0 vs Once Caldas in Primera A.
  - Apr 6: lost 3-2 vs Alianza FC in Primera A.
  - Apr 2: lost 1-0 at Boyaca Chico in Primera A.
  - Mar 28/29: lost 1-0 at Deportivo Cali in Primera A.
  - Mar 24: drew vs Cucuta Deportivo (scoreline not fully captured in extraction snippet).

## Evidence directly stated by source

- The fixture exists on the stated date and venue.
- Tolima is the home side.
- Tolima has extra schedule congestion because it played Libertadores on Apr 14, four days before this league match.
- Pereira's immediately visible domestic run is poor: no win in the extracted April sequence.

## What is uncertain

- ESPN extraction did not cleanly expose full league-table position or all scorelines from the recent blocks without deeper parsing.
- ESPN is not the governing source of truth for market settlement; it is a strong contextual/fixture source.
- No lineup/injury confirmation is visible yet in the extracted feed.

## Why this source may matter

This source anchors the catalyst calendar and identifies the most concrete pre-match mover available now: late team news around a Tolima home league match arriving shortly after a continental fixture. It also provides a quick recent-form baseline favoring Tolima over Pereira.

## Possible impact on the question

If late squad rotation/injury news from Tolima's Apr 14 Libertadores trip is mild, the existing home/form edge likely stays intact or strengthens. If meaningful absences emerge from that short turnaround, the market's current 0.76 price could drift down before kickoff.

## Reliability notes

- Useful as a timely aggregator for schedule, venue, and recent results.
- Medium credibility because ESPN is not the official Colombian competition authority.
- Best used alongside an official/club-level source for source-of-truth and team-news verification.