---
type: source_note
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: prediction-markets
entity: btc
topic: bitcoin-above-72k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page
source_type: market contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, resolution, source-note]
---

# Summary

The Polymarket contract page directly states that the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 19, 2026, using the final close price and Binance as the source of truth.

## Key facts extracted

- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on the specified date has a final close above 72,000.
- Otherwise the market resolves No.
- The governing source is Binance, specifically the BTC/USDT chart with 1-minute candles selected.
- The contract is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Price precision follows the source.
- The current Polymarket price for the 72,000 line was shown at roughly 87% Yes / 14% No on collection.

## Evidence directly stated by source

- Exact resolution wording.
- Official source-of-truth venue.
- Current market-implied probability shown on the market page.

## What is uncertain

- The page does not independently verify how Binance handles edge cases if a UI display and API print diverge, though both are likely aligned in normal circumstances.
- The visible odds are a snapshot and can move before the final write-up.

## Why this source may matter

This source governs what conditions must all be true for a Yes resolution: the correct venue, the correct pair, the correct timezone framing, the correct minute candle, and a final close strictly above 72,000.

## Possible impact on the question

This source does not push the probability up or down by itself, but it sharply narrows the relevant evidence. General BTC sentiment, other exchanges, or end-of-day closes matter only indirectly unless they help estimate the Binance noon-ET one-minute close on April 19.

## Reliability notes

- Authoritative for contract interpretation.
- Essential for avoiding category error on date/time/source.
- Independence versus Binance price data is high enough for audit purposes because it defines the contract rather than describing the underlying price path.