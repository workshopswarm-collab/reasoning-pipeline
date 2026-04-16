---
type: source_note
case_key: case-20260414-fdb38a8b
dispatch_id: dispatch-case-20260414-fdb38a8b-20260414T180238Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract, resolution, binance]
---

# Summary

This source establishes the market-implied probability and the exact contract mechanics. It showed the 72,000 outcome trading around 81% Yes / 22% No at fetch time and states that resolution depends on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17.

## Key facts extracted

- The target line is 72,000 for April 17.
- The displayed market probability for the 72,000 threshold was about 81% Yes at fetch time.
- Resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 ET on the specified date.
- The decisive field is the candle's final Close price, which must be higher than 72,000 for Yes.
- This is exchange-specific: Binance BTC/USDT only, not broader BTC/USD composites.
- Price precision follows Binance source precision.

## Evidence directly stated by source

- The rules explicitly name Binance as the source of truth.
- The rules explicitly require the 12:00 ET one-minute candle close, not the intraday high, daily close, or another exchange print.
- The page displays current market pricing for each threshold, including 72,000.

## What is uncertain

- The fetched page is a web rendering rather than a signed API response, so displayed probabilities are useful but not perfect archival evidence.
- The page does not itself provide the future resolving candle, only the rules and current pricing.

## Why this source may matter

This source governs the contract. The timing and exchange specificity are material because BTC can trade above a threshold intraday while still failing the exact resolving minute close, and Binance-specific prints can differ modestly from other venues.

## Possible impact on the question

It raises the importance of short-horizon path dependence and exact timestamp risk. A broad bullish BTC view can still be overstated if traders implicitly think in terms of "BTC around that level by Friday" instead of "Binance BTC/USDT close at exactly 12:00 ET Friday above that level."

## Reliability notes

Useful as the governing market source, but the displayed price snapshot is secondary to the rule text. Best paired with direct Binance price data for actual probability work.