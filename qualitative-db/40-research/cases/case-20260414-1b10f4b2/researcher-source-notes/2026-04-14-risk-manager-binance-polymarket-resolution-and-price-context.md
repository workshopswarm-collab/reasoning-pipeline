---
type: source_note
case_key: case-20260414-1b10f4b2
dispatch_id: dispatch-case-20260414-1b10f4b2-20260414T201759Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the price of Bitcoin be above $68,000 on April 20?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market rules + Binance spot API/docs
source_type: primary_and_contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium-high
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
tags: [polymarket, binance, resolution, source-note, btc]
---

# Summary

This source note combines the market's governing resolution language from Polymarket with Binance spot market documentation and live BTCUSDT price context. The key risk point is that this market is not about generic Bitcoin price on April 20; it is about one exact Binance BTC/USDT 1-minute candle close at 12:00 PM ET (16:00 UTC) on April 20, 2026.

## Key facts extracted

- Polymarket rule: resolves Yes if the Binance 1 minute candle for BTC/USDT at 12:00 ET on April 20 has a final Close price strictly higher than 68,000.
- Resolution source is explicitly Binance BTC/USDT, not other exchanges or pairs.
- Binance docs for `GET /api/v3/klines` state klines are uniquely identified by open time and return open, high, low, close, volume, and close time.
- Assignment timestamp is 2026-04-14 16:19 ET; April 20 12:00 ET maps to 2026-04-20 16:00:00 UTC.
- A direct API query for that future 1-minute kline currently returns an empty array, which is expected and confirms the lookup method to use later.
- Live Binance context at assignment time showed BTCUSDT around 74.3k, well above 68k, with 24h high around 76.0k and low around 73.0k.

## Evidence directly stated by source

- Polymarket directly states the exact rule and source of truth.
- Binance docs directly state that kline close price is an available field and that the endpoint can be queried by symbol, interval, startTime, endTime, and optional timezone.
- Binance live ticker directly states current BTCUSDT last price, 24h high/low, and average price.

## What is uncertain

- The Binance website UI wording in the Polymarket rules points users to the chart UI, while Binance API docs describe the same underlying kline structure; that is strong but not an explicit Polymarket statement that API and UI settlement values are identical.
- The exact April 20 noon ET candle does not exist yet, so this note cannot directly settle the market.
- BTC can move materially over six days; current spot level is only contextual, not determinative.

## Why this source may matter

The market is date-sensitive, source-specific, and extreme-priced. Correct interpretation depends more on exact contract mechanics and exchange-specific settlement than on broad BTC narrative alone.

## Possible impact on the question

This source set supports a high-probability Yes baseline because current Binance BTCUSDT is already roughly 6.3k above the threshold. But it also sharpens the main risk-manager objection: a high price today does not remove path risk, exchange-specific wick risk, or timing risk at one exact minute.

## Reliability notes

- Polymarket is the governing contract source, so it is the authoritative source for what counts.
- Binance API docs are high-credibility contextual documentation for how to retrieve the relevant candle data.
- Live Binance API price data are direct but only contemporaneous context, not a forward-looking guarantee.
- Evidence independence is moderate rather than high because both settlement mechanics and price context ultimately depend on Binance.
