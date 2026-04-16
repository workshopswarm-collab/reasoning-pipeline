---
type: source_note
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-20 above 68000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance API reference points
source_type: primary_market_rules_plus_primary_exchange_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, contract-interpretation, catalyst-calendar]
---

# Summary

The Polymarket market page provides the governing contract language and shows the current market-implied probability near 97% for the 68,000 threshold. Binance API checks confirm BTC/USDT is actively trading, that the market uses a 0.01 tick size, and that spot price on 2026-04-15 is around 74.9k, leaving a roughly 9.2% cushion above the threshold.

## Key facts extracted

- Polymarket rule text says the market resolves to Yes if the Binance BTC/USDT 1-minute candle for **12:00 PM ET** on **2026-04-20** has a final **Close** price **higher than 68,000**.
- Polymarket explicitly says the source is Binance BTC/USDT, not another venue or pair.
- The market page showed the 68,000 line trading around **97%** / **97.4¢ Yes** at fetch time.
- Binance API ticker check returned BTCUSDT spot around **74,895.57** during the run.
- Binance exchange info shows BTCUSDT spot is trading and the price tick size is **0.01**, which matters for exact settlement interpretation.
- Resolution-time conversion check: **2026-04-20 12:00 PM ET = 2026-04-20 16:00:00 UTC** because April is in daylight saving time.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected."
- "Price precision is determined by the number of decimal places in the source."

From Binance API outputs checked during the run:
- ticker price endpoint returned BTCUSDT price near 74,895.57
- exchangeInfo returned BTCUSDT status TRADING and price filter tickSize 0.01000000

## What is uncertain

- The public Binance trading page itself did not render cleanly through lightweight fetch, so the analysis relies on Binance public API endpoints plus Polymarket rule text rather than a scraped UI candle screenshot.
- The exact 12:00 PM ET candle close on April 20 is obviously still unknown at run time.

## Why this source may matter

This is the governing source-of-truth pair for the contract: Polymarket provides the actual market wording and Binance provides the underlying price source and precision framework. Without this pair, timing and threshold analysis could drift into wrong-exchange or wrong-timezone reasoning.

## Possible impact on the question

The most important direct implication is that the contract is not asking whether BTC touches or averages above 68k; it asks for the **final close** of one exact minute candle on Binance at a specific ET timestamp. Because BTC is currently around 74.9k, the key catalyst question is whether any event before noon ET on April 20 can cause a roughly 9% or larger selloff and still leave BTC below 68k exactly at the resolution minute.

## Reliability notes

- Polymarket is authoritative for the market rules.
- Binance public API is a strong direct source for current BTCUSDT trading state and price precision, though the exact settlement minute will still need the live exchange data at resolution.
- Evidence independence is moderate rather than high because the contract and exchange source are mechanically linked, not independent causal evidence.