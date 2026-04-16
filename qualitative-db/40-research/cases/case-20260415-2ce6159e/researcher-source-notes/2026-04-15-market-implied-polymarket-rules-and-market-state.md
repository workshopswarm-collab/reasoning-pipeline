---
type: source_note
case_key: case-20260415-2ce6159e
dispatch_id: dispatch-case-20260415-2ce6159e-20260415T142913Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-2ce6159e | market-implied
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for Bitcoin above 72000 on April 16
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2ce6159e/researcher-analyses/2026-04-15/dispatch-case-20260415-2ce6159e-20260415T142913Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-implied, bitcoin]
---

# Summary

This source establishes both the live market-implied probability and the exact contract mechanics that matter for resolution.

## Key facts extracted

- The 72,000 line was trading around 93% Yes on the fetched page.
- The event is part of a ladder market for April 16 daily noon ET thresholds.
- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final Close above 72,000.
- The resolution source is Binance BTC/USDT with 1m candles selected.
- The contract is specifically about Binance BTC/USDT, not other exchanges or trading pairs.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Contract wording and source of truth are explicit on-page.
- The live crowd-implied probability for the 72,000 threshold was about 93% at fetch time.

## What is uncertain

- The Polymarket page is not itself the authoritative resolution source; it only defines the contract and shows current pricing.
- The fetched page snapshot is a moment in time and can move materially before resolution.

## Why this source may matter

It governs what conditions must all hold for a Yes resolution and provides the market prior that the market-implied persona is tasked to decode.

## Possible impact on the question

This source strongly frames the problem as mostly about whether BTC/USDT on Binance can remain above 72,000 through the specific noon ET close print on April 16, not whether Bitcoin is broadly strong on other venues.

## Reliability notes

Useful and necessary for contract interpretation, but not sufficient alone for the factual price outlook because Polymarket is not the source-of-truth venue for settlement.