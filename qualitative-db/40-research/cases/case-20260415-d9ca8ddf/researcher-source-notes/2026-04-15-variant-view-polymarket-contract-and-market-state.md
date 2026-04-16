---
type: source_note
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET Apr 17 2026 1-minute candle close exceed 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for Bitcoin above 72,000 on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-implied-probability, binance]
---

# Summary

This source provides the live market-implied baseline and the governing contract language. For the 72,000 line, the market page showed roughly 93% Yes at fetch time, and the rules specify that settlement is based on the Binance BTC/USDT 1-minute candle at 12:00 ET on Apr 17, 2026, using the final Close price.

## Key facts extracted

- The relevant threshold market is the 72,000 outcome for Apr 17, 2026.
- The live displayed market probability on fetch was about 93% Yes for above 72,000.
- Settlement source is Binance, specifically BTC/USDT with 1m candles.
- The deciding datapoint is the final Close of the 12:00 ET candle on the specified date.
- The contract is not about other exchanges or other pairs.
- Precision is determined by Binance source decimals.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... '1m' and 'Candles' selected..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The page is a live UI and the displayed probability can move after the fetch.
- The page does not itself provide the future Apr 17 noon Binance candle value; it only defines how resolution will work.
- UI wording does not independently confirm whether any exchange outage, chart revision, or delayed display edge case would require fallback handling.

## Why this source may matter

This is the governing source-of-truth for how the market resolves and the benchmark for comparing a personal estimate against consensus pricing.

## Possible impact on the question

It makes timing and venue specificity central. Even if broader BTC spot remains strong, the market still depends on one exact Binance BTC/USDT 1-minute close at 12:00 ET on Apr 17.

## Reliability notes

Useful as the authoritative contract surface for this market, but not independent evidence on whether BTC will actually be above 72,000 at settlement. It is strongest on rules, not forecasting.