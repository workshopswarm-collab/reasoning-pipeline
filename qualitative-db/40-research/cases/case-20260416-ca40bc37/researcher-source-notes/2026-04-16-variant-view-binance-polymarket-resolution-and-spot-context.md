---
type: source_note
case_key: case-20260416-ca40bc37
dispatch_id: dispatch-case-20260416-ca40bc37-20260416T053546Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance Spot API docs + Binance BTCUSDT live endpoints + Polymarket market rules
source_type: mixed_primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-16
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
downstream_uses: [variant-view finding]
tags: [binance, polymarket, resolution, btc]
---

# Summary

This source bundle establishes the settlement mechanics and current spot context for the case. The market resolves off Binance BTC/USDT 1-minute candle close at 12:00 PM America/New_York on April 20, 2026, not on a daily close and not on a multi-exchange index.

## Key facts extracted

- Polymarket rules say the market resolves "Yes" only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20 has a final close strictly higher than 72,000.
- Binance API docs confirm `/api/v3/klines` returns candlestick bars identified by open time, with close price as the fifth field in the response array.
- Binance docs also confirm a `timeZone` parameter exists for kline interval interpretation, but `startTime` and `endTime` remain UTC-interpreted.
- Current Binance BTC/USDT spot price on 2026-04-16 around 05:37 UTC was about 75.1k.
- Recent daily BTCUSDT candles show BTC has been trading materially above 72k for several consecutive days, with recent closes roughly 74.4k, 74.1k, 74.8k, and 75.1k.
- 24h Binance ticker data at capture showed last price about 75,088, 24h low about 73,514, and 24h high about 75,425.

## Evidence directly stated by source

- Polymarket directly states the governing source is Binance BTC/USDT 1-minute candle close at 12:00 ET.
- Binance docs directly state kline close price location and time-handling rules.
- Binance live endpoints directly state the current spot price and recent candle values.

## What is uncertain

- The ultimate April 20 noon close is still four days away, so this bundle does not settle the market.
- Spot can gap meaningfully over four days, especially around macro headlines or crypto-specific liquidations.
- The Polymarket web page is not itself an exchange record; Binance is the governing settlement source.

## Why this source may matter

This is the core contract-interpretation source set. It narrows the question from a vague BTC price forecast to a concrete operational event: whether Binance prints a one-minute close above 72,000 exactly at noon ET on April 20.

## Possible impact on the question

Because BTC is currently around 75k and recent daily/24h ranges remain above 72k, the market's high yes probability is understandable. The variant angle is not that the contract is misread, but that a four-day horizon plus a single-minute exchange-specific close can still embed more path and venue risk than a casual "BTC is already above 72k" framing suggests.

## Reliability notes

- Primary source quality is high for settlement mechanics because Polymarket states the rule and Binance defines the underlying candle structure.
- Evidence independence is medium: Polymarket rules and Binance docs are distinct, but both point to the same exchange-specific truth source.
- Binance live endpoint data is authoritative for current Binance prices but only contextual for the future settlement event.
