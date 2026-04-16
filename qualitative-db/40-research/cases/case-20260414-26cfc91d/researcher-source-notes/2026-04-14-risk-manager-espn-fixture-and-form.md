---
type: source_note
case_key: case-20260414-26cfc91d
dispatch_id: dispatch-case-20260414-26cfc91d-20260414T181516Z
analysis_date: 2026-04-14
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: inter-vs-cagliari-fixture-and-form
question: Will FC Internazionale Milano win on 2026-04-17?
driver: injuries-health
date_created: 2026-04-14
source_name: ESPN Italian Serie A scoreboard event page data
source_type: secondary-structured-data
source_url: https://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/scoreboard?dates=20260417
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers:
  - injuries-health
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260414-26cfc91d/researcher-analyses/2026-04-14/dispatch-case-20260414-26cfc91d-20260414T181516Z/personas/risk-manager.md
  - qualitative-db/40-research/cases/case-20260414-26cfc91d/researcher-analyses/2026-04-14/dispatch-case-20260414-26cfc91d-20260414T181516Z/evidence/risk-manager.md
tags: [sports, soccer, serie-a, inter, cagliari, fixture]
---

# Summary

ESPN's structured Serie A scoreboard data confirms the exact fixture covered by the market: Cagliari at Internazionale on 2026-04-17 at San Siro, scheduled for 18:45Z / 2:45 PM EDT. The same event payload also supplies current team records, recent form strings, venue, and sportsbook odds context.

## Key facts extracted

- Event listed: **Cagliari at Internazionale**.
- Date/time: **2026-04-17T18:45Z**.
- Venue: **San Siro, Milano**.
- Internazionale record shown as **24-3-5** with recent form **WWDDL**.
- Cagliari record shown as **8-9-15** with recent form **WLLLL**.
- Internazionale leading scorer in payload: **Lautaro Martínez (16 goals)**.
- Cagliari leading scorer in payload: **Sebastiano Esposito (6 goals)**.
- Embedded DraftKings odds in the same event payload show approximately **Inter -550 / Draw +500 / Cagliari +1100**.

## Evidence directly stated by source

- The match exists in the league fixture list on the contract date.
- Inter are the home side.
- Inter's season record and recent form are materially stronger than Cagliari's.
- Market/betting context outside Polymarket also prices Inter as a strong favorite.

## What is uncertain

- ESPN is not the governing settlement authority for Polymarket.
- The form string is only a compressed recent-results summary; it does not explain lineup strength, rotation, injuries, or motivational context.
- Sportsbook odds are informative but not a substitute for contract wording or final result reporting.

## Why this source may matter

It is the cleanest structured contextual source found in-tool for both fixture confirmation and broad team-strength context. It also provides an independent market-style cross-check that Inter are not merely a Polymarket favorite.

## Possible impact on the question

This source pushes probability upward for an Inter win because it confirms the fixture, home venue, and a large record/form gap. It also shows external pricing broadly consistent with a heavy favorite, which reduces the chance that Polymarket is an isolated mispricing. However, it does not eliminate draw risk or lineup/timing fragility.

## Reliability notes

Useful and recent, but still a secondary aggregator rather than the league's own official competition site. Best used alongside a more authoritative fixture/competition source.