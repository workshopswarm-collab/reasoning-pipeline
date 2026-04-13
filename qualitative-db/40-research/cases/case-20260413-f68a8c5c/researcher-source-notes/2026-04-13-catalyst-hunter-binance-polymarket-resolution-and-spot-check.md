---
type: source_note
case_key: case-20260413-f68a8c5c
dispatch_id: dispatch-case-20260413-f68a8c5c-20260413T165914Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-14
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-14 close above 68000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market page and Binance spot API docs/live endpoint check
source_type: primary-plus-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260413-f68a8c5c/researcher-analyses/2026-04-13/dispatch-case-20260413-f68a8c5c-20260413T165914Z/personas/catalyst-hunter.md
tags: [polymarket, binance, resolution-source, timing, candle-close]
---

# Summary

This note verifies the governing resolution mechanics and performs an additional direct spot check against Binance surfaces appropriate to this contract.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone, using the final Close price.
- The contract is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Binance spot API documentation confirms `/api/v3/klines` returns candlestick bars including open time and close price, and supports `interval=1m`.
- Binance documentation also notes `timeZone` can be provided for kline interpretation, while `startTime` and `endTime` are interpreted in UTC.
- A live direct API check on 2026-04-13 around 12:58-1:02 PM ET returned BTCUSDT 1-minute klines with closes around 72.15k-72.20k and ticker price 72,200, well above the 68,000 strike one day before resolution.
- Explicit timezone verification: 2026-04-14 12:00 ET = 2026-04-14 16:00 UTC.

## Evidence directly stated by source

- Polymarket rules: Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on April 14 has a final Close above 68,000.
- Binance docs: kline response includes close price and is uniquely identified by open time; 1m interval is supported.

## What is uncertain

- The exact realized 12:00 ET April 14 close is not yet known as of this note.
- Small contract-mechanics ambiguity remains around whether Polymarket operationally reads the website candle display versus backend API, though both should normally align if Binance data is stable.
- One-day-ahead crypto moves can still exceed 5-6% on adverse macro or idiosyncratic exchange/news catalysts.

## Why this source may matter

This is the core settlement path. For a narrow date-specific crypto threshold market, correctly identifying the exact exchange, pair, candle interval, timestamp, and close-field mechanics matters more than broad market commentary.

## Possible impact on the question

The spot check strongly supports a high Yes probability because BTC/USDT is currently about 6.2% above the strike with less than 24 hours remaining. The main remaining catalysts are adverse risk-off moves or Binance-specific market dislocations severe enough to push the noon ET close below 68,000.

## Reliability notes

- Polymarket market page is the direct contract/rules surface for this market.
- Binance API docs are authoritative for interpreting how kline fields and timezone handling work.
- Live Binance endpoint response is direct but only a spot check, not the settlement value itself.
- Evidence independence is medium rather than high because both contextual and direct verification still trace back to Binance as the governing source of truth.