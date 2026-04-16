---
type: source_note
case_key: case-20260415-e4a8d83c
dispatch_id: dispatch-case-20260415-e4a8d83c-20260415T230345Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: binance-btcusdt-resolution-mechanics-and-current-spot-context
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 74000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API docs plus live BTCUSDT API snapshot
source_type: primary_and_contextual_market_source
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-e4a8d83c/researcher-analyses/2026-04-15/dispatch-case-20260415-e4a8d83c-20260415T230345Z/personas/variant-view.md]
tags: [binance, resolution-source, candle-close, btcusdt, source-note]
---

# Summary

This source note captures the governing Binance market-data mechanics and a live BTC/USDT snapshot relevant to the April 17 noon ET resolution window.

## Key facts extracted

- Binance Spot API documentation says `GET /api/v3/klines` and `GET /api/v3/uiKlines` return 1-minute candlestick bars identified by their open time, with close price in field index 4.
- Binance documents a `timeZone` parameter for klines/uiKlines; interval interpretation can be shifted to a specified timezone, but `startTime` and `endTime` are still interpreted in UTC.
- Noon ET on 2026-04-17 converts to 2026-04-17 16:00:00 UTC, or `1776441600000` ms since epoch.
- A live Binance `ticker/price` snapshot on 2026-04-15 showed BTCUSDT around 74.8k.
- A live Binance `ticker/24hr` snapshot on 2026-04-15 showed: `lastPrice` 74807.29, 24h high 75425.00, 24h low 73514.00, and 24h weighted average 74263.73.
- A direct `uiKlines` query with `interval=1m` and `timeZone=-4` returned valid 1-minute bars, confirming an ET-aligned kline surface is available via Binance API even though the market says resolution is from the Binance chart UI.

## Evidence directly stated by source

- Binance docs explicitly state klines are uniquely identified by open time.
- Binance docs explicitly state the response includes open, high, low, close, volume, and close time.
- Binance docs explicitly state `timeZone` shifts interval interpretation away from UTC while `startTime`/`endTime` remain UTC.

## What is uncertain

- Polymarket says the settlement source is the Binance trading UI with 1m candles selected, not necessarily the REST API. The API is a strong verification/context surface, but there is still minor source-of-truth ambiguity if UI rendering and API outputs were ever to diverge.
- The final April 17 12:00 ET candle obviously cannot be checked yet; only the timing and mechanics can be verified now.

## Why this source may matter

The core market is narrower than a plain directional BTC call. It depends on one exchange, one pair, one minute candle, one timezone interpretation, and the close price for that minute. That creates a credible path-dependence / microstructure risk channel that can make the market slightly less certain than simple spot-vs-threshold thinking suggests.

## Possible impact on the question

Current spot being modestly above 74k supports Yes, but the 24h range already crossed both above and below 74k, showing the threshold is close enough that a single-minute close two days out is still materially uncertain. This tends to support a somewhat lower probability than a casual “spot is above 74k now” narrative would imply.

## Reliability notes

- Binance documentation is the strongest available primary source for how its API exposes 1-minute candles.
- Live API outputs are direct but only contextual for current spot; they do not settle the event yet.
- Evidence independence is limited because both the docs and live data come from Binance surfaces.
- For this case, that is acceptable because Binance is also the governing underlying exchange named in the contract.