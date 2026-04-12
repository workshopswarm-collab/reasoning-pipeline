---
type: source_note
case_key: case-20260407-be55ad2f
dispatch_id: dispatch-case-20260407-be55ad2f-20260407T193635Z
analysis_date: 2026-04-07
persona: variant-view
domain: crypto
subdomain: market-structure
entity: btc
topic: case-20260407-be55ad2f | variant-view
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-08 close above 66000?
driver: operational-risk
date_created: 2026-04-07
source_name: Polymarket rules page plus Binance Spot API docs and live Binance API context
source_type: primary-plus-contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-8
source_date: 2026-04-07
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
downstream_uses: [qualitative-db/40-research/cases/case-20260407-be55ad2f/researcher-analyses/2026-04-07/dispatch-case-20260407-be55ad2f-20260407T193635Z/personas/variant-view.md]
tags: [binance, polymarket, btcusdt, resolution-mechanics, timezone, candle-definition]
---

# Summary

This note captures the governing market rules and the most relevant direct verification surfaces for the April 8 BTC > 66,000 market.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle for **12:00 ET (noon)** on the date in the title.
- Resolution depends on the candle's final **Close** price, not VWAP, last traded price at another venue, or broad spot consensus.
- Price precision is determined by the number of decimals in the Binance source.
- Binance Spot API docs state klines are **uniquely identified by their open time**.
- Binance Spot API docs state `startTime` and `endTime` are interpreted in **UTC** even when a `timeZone` parameter is supplied.
- Binance kline response format explicitly includes open time, close price, and close time.
- A conversion check shows **2026-04-08 12:00:00 ET = 2026-04-08 16:00:00 UTC = 1775664000000 ms**.
- Live Binance context on 2026-04-07 showed BTC/USDT around **68,513.55**, roughly 2.5k above the 66k threshold.
- Binance 24h stats showed an intraday low near **67,732.01**, still above 66k at the time checked.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- "Price precision is determined by the number of decimal places in the source."

From Binance Spot API docs:
- "Klines are uniquely identified by their open time."
- `timeZone` changes interval interpretation, but `startTime` and `endTime` remain UTC.
- Response fields include open time and close time, so the 12:00 ET candle is the candle that opens at 12:00 ET, not the one that ends at 12:00 ET.

From live Binance API context:
- `/api/v3/ticker/price?symbol=BTCUSDT` returned about 68513.55 at check time.
- `/api/v3/ticker/24hr?symbol=BTCUSDT` returned a 24h low around 67732.01 and last price around 68513.55.

## What is uncertain

- The eventual April 8 12:00 ET candle close is still unresolved at research time.
- Binance front-end chart rendering could differ cosmetically from raw API output in edge presentation cases, though the docs and API structure strongly suggest the same underlying kline semantics.
- Short-horizon crypto volatility could still push BTC below 66k before the specific settlement minute.

## Why this source may matter

This is the core source set for the case because the contract is rule-sensitive and depends on exact exchange, exact pair, exact time zone, and exact candle definition.

## Possible impact on the question

The rules and Binance docs together reduce one major failure mode: misreading which candle counts. The live Binance price context makes the market's high implied probability directionally understandable, but not risk-free.

## Reliability notes

- Polymarket rules page is the governing contract surface for what counts.
- Binance Spot API docs are the strongest contextual source for interpreting candle timestamps and timezone handling.
- Live Binance API endpoints are direct venue data and useful for an additional verification pass.
- Evidence independence is medium: Polymarket and Binance docs are distinct surfaces, but both ultimately point to the same exchange data source for settlement.