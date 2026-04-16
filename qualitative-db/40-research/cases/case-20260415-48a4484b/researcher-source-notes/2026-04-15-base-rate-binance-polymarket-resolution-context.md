---
type: source_note
case_key: case-20260415-48a4484b
dispatch_id: dispatch-case-20260415-48a4484b-20260415T180644Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules plus Binance BTCUSDT API checks
source_type: primary market rules plus exchange data
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, resolution-source, btc, daily-close]
---

# Summary

The Polymarket contract specifies that resolution depends on the Binance BTC/USDT 1-minute candle for **12:00 ET on April 16** and specifically the candle's final **Close** price. Current Binance spot data on April 15 around 14:08 ET showed BTC/USDT near 74.2k, materially above the 72k threshold.

## Key facts extracted

- The governing market rule is: resolve Yes if the Binance BTC/USDT 1-minute candle for **12:00 in ET timezone (noon)** on April 16 has a final **Close** price higher than 72,000.
- The rule is exchange-specific: Binance BTC/USDT, not other exchanges or pairs.
- Current spot/ticker check from Binance API returned BTCUSDT around **74,199.45**.
- Recent 1-minute Binance klines around 18:04-18:08 UTC (14:04-14:08 ET) closed between about **74,214.96 and 74,279.12**.
- A 60-minute Binance sample ending 18:08 UTC showed closes ranging from about **73,931.47 to 74,279.12**, so the market was not merely one tick above 72k; it had a buffer of roughly 1.9k-2.3k over the threshold during the observed hour.

## Evidence directly stated by source

- Polymarket rules directly state the resolution mechanics and source of truth.
- Binance API directly states current BTCUSDT ticker price and minute-candle OHLC values.

## What is uncertain

- The outcome depends on the single 12:00 ET minute close on April 16, not the current price on April 15.
- The rule wording leaves some operational ambiguity about whether ET is implemented via UI/local timezone conversion versus a canonical UTC timestamp, though noon ET on April 16 should map cleanly to 16:00 UTC if DST remains in effect.
- Exchange outages, sharp overnight selloffs, or unusual volatility could still move price below 72k by resolution.

## Why this source may matter

This is the key source set for both contract interpretation and current state. It establishes exactly what must happen for Yes and shows that the market starts from a price level already materially above the threshold.

## Possible impact on the question

This source set pushes toward Yes because BTC is currently comfortably above 72k and because the source-of-truth mechanics are clear enough to know the event is a straightforward single-minute threshold check rather than a broader daily average or cross-exchange measure.

## Reliability notes

- Polymarket rules are the primary source for settlement logic.
- Binance is the explicit resolution source, so its data is authoritative for price measurement.
- Evidence independence is moderate rather than high because both rule interpretation and final settlement hinge on the same market/exchange ecosystem.
- Operational risk still matters: exchange display/API specifics and timezone mapping should be checked explicitly in the final memo.