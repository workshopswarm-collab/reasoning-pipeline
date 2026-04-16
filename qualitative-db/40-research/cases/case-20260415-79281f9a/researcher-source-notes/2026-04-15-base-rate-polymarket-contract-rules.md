---
type: source_note
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: prediction-markets
entity:
topic: case-20260415-79281f9a | base-rate
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 68000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / contract description
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-79281f9a/researcher-analyses/2026-04-15/dispatch-case-20260415-79281f9a-20260415T202526Z/personas/base-rate.md]
tags: [source-note, polymarket, contract-rules, resolution, base-rate]
---

# Summary

This note captures the exact market wording and resolution mechanics from Polymarket.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 20, 2026 has a final close price higher than 68,000.
- Otherwise it resolves No.
- The named resolution source is Binance BTC/USDT with 1m candles selected.
- The contract is specifically about Binance BTC/USDT, not other exchanges or other trading pairs.
- Price precision is whatever decimal precision appears in the source.
- The displayed market-implied probability for the 68,000 line was about 97% during the research pull.

## Evidence directly stated by source

- Exact settlement timing, exchange, pair, candle interval, and threshold condition.
- The market price shown on the market page for the target line.

## What is uncertain

- The market page text does not itself resolve any ambiguity about rare exchange outages, data revisions, or UI/API differences around the final displayed candle.
- The page does not provide historical noon ET close distribution; it only defines the contract and current odds.

## Why this source may matter

This is the governing contract source. For a date-sensitive and multi-condition market, correct interpretation of the settlement mechanics matters as much as directional price analysis.

## Possible impact on the question

The source makes clear that all of the following must hold for Yes: the date must be April 20, the relevant candle must be the 12:00 ET 1-minute candle, the venue must be Binance, the pair must be BTC/USDT, and the final close must be strictly greater than 68,000.

## Reliability notes

High authority for contract interpretation. This should be paired with direct Binance pricing data and an independent contextual source because the market page is not independent evidence about where BTC is likely to trade.