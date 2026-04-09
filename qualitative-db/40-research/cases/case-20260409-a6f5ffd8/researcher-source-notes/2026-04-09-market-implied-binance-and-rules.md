---
type: source_note
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260409-a6f5ffd8 | market-implied
question: Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-09 close above 70000?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance BTCUSDT klines API docs plus Polymarket market rules page
source_type: primary_and_contextual
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data ; https://polymarket.com/event/bitcoin-above-on-april-9
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/market-implied.md]
tags: [binance, polymarket, resolution-rules, timestamp]
---

# Summary

This source note captures the governing resolution mechanics and the key timing interpretation needed for the April 9 BTC > 70k market.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle for `12:00 in the ET timezone (noon)` on the specified date, using the final `Close` price.
- The source-of-truth surface named by the market is Binance BTC/USDT with `1m` and `Candles` selected on the exchange interface.
- Binance spot API documentation says `Klines are uniquely identified by their open time`.
- Noon ET on 2026-04-09 is 16:00:00 UTC because New York is on EDT (UTC-4) on that date.
- Therefore the relevant 1-minute candle is the candle whose open time is 2026-04-09 16:00:00 UTC and whose close time is 16:00:59.999 UTC.
- Direct API retrieval for that future timestamp currently returns no rows because the market is still unresolved at analysis time; this is expected and not contradictory.
- A verification pass on current Binance API endpoints showed a small live discrepancy across endpoints (`api.binance.com` vs `api1` / `api-gcp`) for a recent candle, suggesting care is warranted when using non-governing mirrors before settlement.

## Evidence directly stated by source

- Polymarket explicitly names Binance BTC/USDT 1m candle close as the resolution source.
- Binance docs explicitly state klines are identified by open time.

## What is uncertain

- Whether the Binance web UI and public API will display perfectly identical values in real time for the settlement candle at the exact moment of resolution.
- Whether Polymarket operators treat the noon ET candle as the candle opened at 12:00:00 ET or any differently labeled visual bucket in the UI; the docs strongly imply open-time identification, but the UI wording alone is less explicit than the API docs.

## Why this source may matter

This is the main source-of-truth and rule-interpretation layer. The market is mostly about timestamp mechanics, not macro BTC direction.

## Possible impact on the question

Because BTC was already trading above 70k well before the target window, the rules/timing interpretation is the main reason the market is not literally 100%. If the candle mapping is standard open-time mapping, the price only needs to remain above 70k through the close of the 16:00 UTC / 12:00 ET minute.

## Reliability notes

- Primary source quality is high for Binance API docs and high for Polymarket’s own market page because they directly describe the governing source and contract wording.
- Evidence independence is limited because both sources concern the same settlement mechanic rather than independent market fundamentals.
- Small discrepancies across Binance public API hosts for a live recent candle suggest mild operational-risk around mirror consistency, but not enough to undermine the main timing interpretation.