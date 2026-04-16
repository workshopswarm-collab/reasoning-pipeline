---
type: source_note
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
analysis_date: 2026-04-14
persona: base-rate
domain: sports
subdomain: soccer
entity:
topic: saudi-pro-league-match-context
question: Will Al Qadisiyah Saudi Club win on 2026-04-23?
driver:
date_created: 2026-04-14
source_name: Soccerway Saudi Professional League 2026 fixtures/results page
source_type: secondary-aggregator
source_url: https://www.soccerway.com/saudi-arabia/saudi-professional-league/
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [soccer, saudi-pro-league, fixtures, schedule-context, base-rate]
---

# Summary

This source note captures schedule and matchup context visible on Soccerway's Saudi Professional League 2026 page for the relevant match window.

## Key facts extracted

- Soccerway lists a Saudi Professional League 2026 fixture between **Al Qadsiah** and **Al Shabab** with encoded timestamp `1775930400`, which converts to **2026-04-11 18:00:00 UTC** in the page blob; the page clearly treats these clubs as current SPL participants and encodes a completed result for that head-to-head.
- The same page shows later fixtures for both clubs in **Round 29 / Round 30 / Round 31**, indicating both teams are active league participants late in the season rather than fringe or cup-only teams.
- Al Qadsiah appears in the schedule feed against clubs such as **Al Okhdood, Al Riyadh, Al Nassr, and Al Hazem**.
- Al Shabab appears in the same league feed against **Al Qadsiah, Al Riyadh, Al Fateh, and Al Taawon**.
- The encoded league feed suggests a prior **Al Qadsiah vs Al Shabab** meeting ended **2-2**, which matters as direct but limited contextual evidence against treating this as an overwhelmingly one-sided matchup.

## Evidence directly stated by source

- Saudi Professional League 2026 competition page exists and contains both clubs.
- Encoded fixture blob includes both teams and the matchup.
- Encoded score markers around the prior Al Qadsiah–Al Shabab entry indicate a 2-2 result.

## What is uncertain

- Soccerway is an aggregator, not the governing competition authority.
- The page content is heavily encoded, so table position and home/away strength are not legible without deeper scraping.
- The exact mapping between the market's 2026-04-23 date and Soccerway's schedule timestamping is not fully clean from this page alone.

## Why this source may matter

- It is a useful contextual source establishing that this is a normal late-season league fixture between two established SPL participants.
- The prior drawn head-to-head is modest disconfirming evidence against an extremely high home-win prior.

## Possible impact on the question

- The source supports an outside-view posture that a straight win market on Al Qadsiah should usually not clear very high probabilities unless there is clear table/form/team-news evidence overwhelming the generic league base rate.

## Reliability notes

- Medium reliability for schedule/context; weaker for authoritative settlement.
- Useful as contextual corroboration, not as sole source of truth for market resolution.
