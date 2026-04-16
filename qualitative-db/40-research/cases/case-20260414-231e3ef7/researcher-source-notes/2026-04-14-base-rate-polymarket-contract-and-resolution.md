---
type: source_note
case_key: case-20260414-231e3ef7
dispatch_id: dispatch-case-20260414-231e3ef7-20260414T140546Z
analysis_date: 2026-04-14
persona: base-rate
domain: markets
subdomain: prediction-markets
entity:
topic: Polymarket contract language for 2026 FIDE Candidates Tournament winner market
question: Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market description
source_type: market_contract
source_url: https://polymarket.com/event/2026-fide-candidates-tournament-winner
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-231e3ef7/researcher-analyses/2026-04-14/dispatch-case-20260414-231e3ef7-20260414T140546Z/personas/base-rate.md]
tags: [polymarket, resolution, contract, source-note]
---

# Summary

This source is the governing contract text for market interpretation and resolution logic.

## Key facts extracted

- The market resolves to the player that wins the 2026 FIDE Candidates Tournament scheduled for March 29 - April 16, 2026.
- If a listed player becomes impossible to win under FIDE rules, that player's market resolves No.
- If the tournament is cancelled, postponed after April 30, 2026, or no winner is declared within that timeframe, the market resolves Other.
- The primary resolution source is official information from FIDE, though a consensus of credible reporting may also be used.

## Evidence directly stated by source

- Official FIDE information is the named primary source of truth.
- Consensus reporting is a fallback, not the first resort.
- The contract cares about actual tournament winner status, not merely interim leader status.

## What is uncertain

- The description does not specify which exact FIDE page or document will be used.
- It does not specify how quickly Polymarket will settle after official confirmation.
- It does not define edge-case handling beyond the stated fallback to credible consensus reporting.

## Why this source may matter

In a market trading near certainty, the main remaining risk is often not the board position alone but resolution mechanics and whether the event has actually been officially won.

## Possible impact on the question

This source caps confidence below 100% unless the tournament has already been officially completed and attributed to Sindarov by FIDE.

## Reliability notes

This is the authoritative contract language for market interpretation, but not the underlying factual scoreboard. It must be paired with official or strong contextual evidence about the tournament state.