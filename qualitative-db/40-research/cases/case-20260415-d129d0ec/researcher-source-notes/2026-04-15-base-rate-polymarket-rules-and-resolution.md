---
type: source_note
case_key: case-20260415-d129d0ec
dispatch_id: dispatch-case-20260415-d129d0ec-20260415T014044Z
analysis_date: 2026-04-15
persona: base-rate
domain: geopolitics
subdomain: russia-ukraine-war
entity: russia
topic: russia-military-action-against-kyiv-municipality-by-april-17
question: Will the Russian Armed Forces initiate a qualifying drone, missile, or air strike on Kyiv municipality by April 17 under this market's wording?
driver:
date_created: 2026-04-15
source_name: Polymarket market rules and resolution text
source_type: market-rule-primary
source_url: https://polymarket.com/event/russia-military-action-against-kyiv-municipality-by-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [russia, ukraine]
related_drivers: []
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [polymarket, resolution-criteria, kyiv, timing]
---

# Summary

This source defines what counts, what does not count, and which sources govern settlement. It is the key contract-interpretation source for the case.

## Key facts extracted

- Yes requires Russian Armed Forces to initiate a drone, missile, or air strike on Kyiv municipality between market creation and the specified date, using EET timing.
- Qualifying military action includes aerial bombs, drones, or missiles, including cruise or ballistic missiles, but excludes surface-to-air missiles.
- Any strike on terrestrial territory of Kyiv municipality counts.
- Intercepted missiles or drones can still count if they constitute a strike directed against Kyiv municipality during the timeframe, even if they do not land in the municipality or cause damage.
- Non-qualifying actions include artillery, small arms, SAMs, FPV or ATGM strikes, ground incursions, naval shelling, and cyberattacks.
- Primary resolution source is consensus of credible reporting from major international media and national broadcasters/newspapers; if ambiguous, official Ukrainian military and Kyiv/government authorities are the fallback.
- If the date/time cannot be confirmed by end of the third calendar date after the timeframe, the market resolves No even if later confirmed.

## Evidence directly stated by source

The rule text directly states both the inclusion/exclusion logic and the source-of-truth hierarchy.

## What is uncertain

- The fetched rules page does not itself confirm market creation time.
- The exact practical meaning of "between market creation and the specified date" depends on the platform countdown / date labeling, but the close time in assignment context is April 16 20:00 EDT and the rules say EET governs the strike window.
- "Clear evidence of a strike directed against Kyiv municipality" may leave room for interpretive disputes if only regional or oblast-level reporting appears.

## Why this source may matter

This is the authoritative contract source. For this market, contract wording is unusually important because intercepted projectiles can count and because date/time confirmation failure can force a No.

## Possible impact on the question

It raises the threshold for a confident Yes call unless there is clean reporting that the strike was directed at Kyiv municipality itself within the defined time window.

## Reliability notes

High reliability for settlement logic; not a factual source about whether any strike occurred.