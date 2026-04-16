---
type: source_note
case_key: case-20260413-2c39d778
dispatch_id: dispatch-case-20260413-2c39d778-20260413T215003Z
analysis_date: 2026-04-13
persona: market-implied
domain: prediction-markets
subdomain: market-structure
entity: polymarket
topic: Polymarket contract and current price
question: Will Vitality win IEM Rio 2026?
driver: reliability
date_created: 2026-04-13
source_name: Polymarket IEM Rio 2026 Winner market page
source_type: market-primary
source_url: https://polymarket.com/event/iem-rio-2026-winner
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [polymarket]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [market-implied finding, assumption note]
tags: [polymarket, contract, market-implied, source-note]
---

# Summary

The Polymarket contract states the market resolves to the winner of IEM Rio 2026, with ESL as the official resolution source and Liquipedia/credible reporting as fallback consensus reporting. The assignment states the current market price for Vitality is 0.705, implying a 70.5% win probability.

## Key facts extracted

- Current quoted price in assignment context: 0.705.
- Implied market probability: 70.5%.
- Primary resolution source: ESL official information.
- Fallback logic: consensus of credible reporting, example given as Liquipedia.
- If the tournament is postponed beyond 2026-04-30 23:59 ET, canceled, or no winner is declared by then, market resolves to Other.

## Evidence directly stated by source

- Resolution mechanics and governing source of truth are directly stated.
- This is the direct market contract surface for interpreting what counts.

## What is uncertain

- The market page excerpt available here does not expose full order-book logic or competing team prices.
- The quoted price may move materially during tournament play.

## Why this source may matter

This is the authoritative contract source for what the market is asking and what would settle it. It also makes clear that public structured reporting can matter as fallback, which reduces but does not eliminate settlement ambiguity.

## Possible impact on the question

Because the contract is winner-only and uses ESL as the primary source, the analysis should focus on whether 70.5% fairly represents Vitality's chance to emerge from the actual tournament field, not on vague brand strength or generalized team quality alone.

## Reliability notes

This is the primary source for contract mechanics and current price reference. It is not independent of the market-implied baseline because it is the market itself, so it should be paired with an external contextual source.
