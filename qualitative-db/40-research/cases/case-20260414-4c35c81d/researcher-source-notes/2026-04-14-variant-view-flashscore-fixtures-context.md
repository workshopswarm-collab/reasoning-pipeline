---
type: source_note
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
analysis_date: 2026-04-14
persona: variant-view
domain: sports
subdomain: soccer
entity:
topic: saudi-pro-league-fixtures-context
question: Will Al Qadisiyah Saudi Club win on 2026-04-23?
driver:
date_created: 2026-04-14
source_name: Flashscore Saudi Professional League fixtures page
source_type: secondary-fixtures-context
source_url: https://www.flashscore.com/football/saudi-arabia/saudi-professional-league/fixtures/
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4c35c81d/researcher-analyses/2026-04-14/dispatch-case-20260414-4c35c81d-20260414T204205Z/personas/variant-view.md]
tags: [fixtures, contextual-source, verification]
---

# Summary

This source was used as a contextual verification pass on the Saudi Professional League schedule and nearby fixtures around the target match date.

## Key facts extracted

- Flashscore lists Saudi Professional League fixtures around the target date.
- The extracted page clearly shows several league matches scheduled on 23 April and 24 April 2026.
- The extracted page does not clearly display the Al Qadisiyah vs Al Shabab match in the returned readable snippet, so it is only partial contextual support rather than direct confirmation of the specific fixture.

## Evidence directly stated by source

The source directly states that it provides Saudi Professional League fixtures and shows a dated fixture list around 23 April 2026.

## What is uncertain

- The readable extract is incomplete and does not surface the target fixture directly.
- The source does not provide standings, xG, injuries, or lineup certainty in the returned extract.
- Because the snippet is partial, this is not sufficient as a sole source for exact match-specific assessment.

## Why this source may matter

It serves as an additional, meaningfully separate verification pass from the market page. Even though it is imperfect, it helps establish that the league calendar is live and that the match belongs to a routine league-fixture context rather than a clearly misdated or canceled event.

## Possible impact on the question

Limited direct impact. The main contribution is negative: there is no strong independent contextual signal here justifying an 83% home-win price on its own. The source therefore reinforces caution about overconfidence when hard match-specific evidence is sparse.

## Reliability notes

Useful as a broad secondary fixtures source, but the readable extraction quality for this run was limited. Reliability for exact match-level detail in this artifact is only medium-low.