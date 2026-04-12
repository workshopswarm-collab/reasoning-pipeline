---
type: source_note
case_key: case-20260407-be55ad2f
dispatch_id: dispatch-case-20260407-be55ad2f-20260407T193635Z
analysis_date: 2026-04-07
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-66k-on-april-8
question: Will the price of Bitcoin be above $66,000 on April 8?
driver: operational-risk
date_created: 2026-04-07T15:41:00-04:00
source_name: Binance Spot API market data docs + live BTCUSDT API checks
source_type: primary_and_direct
source_url: https://developers.binance.info/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [bitcoin, btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-be55ad2f/researcher-analyses/2026-04-07/dispatch-case-20260407-be55ad2f-20260407T193635Z/personas/catalyst-hunter.md]
tags: [binance, resolution-mechanics, timezone, candles, source-note]
---

# Summary

This source note verifies the governing source of truth and the operational mechanics that matter for settlement: Binance BTCUSDT 1-minute candles, ET/noon alignment, candle close definition, precision, and API rate-limit considerations.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone, using the final `Close` price, and that price precision is determined by the source.
- Binance Spot API docs for `GET /api/v3/klines` and `GET /api/v3/uiKlines` say:
  - klines are uniquely identified by their open time
  - `timeZone` can be passed, with default UTC
  - if `timeZone` is provided, kline intervals are interpreted in that timezone rather than UTC
  - `startTime` and `endTime` are still interpreted in UTC regardless of `timeZone`
- Live API check on 2026-04-07 showed `uiKlines?symbol=BTCUSDT&interval=1m&timeZone=-4` returning 1-minute candles with open times mapping cleanly to current ET minutes during daylight time.
- Example: returned kline open time `1775590800000` converts to `2026-04-07T19:40:00Z`, which is exactly `2026-04-07 15:40 ET`, confirming that `timeZone=-4` maps minute buckets to ET during current DST.
- Live BTCUSDT spot ticker checks during this run were around 68.47k, materially above the 66k threshold.
- Live responses exposed `x-mbx-used-weight-1m` values of 9 and 11 after these queries, which indicates the low-weight endpoints used here are lightweight enough for manual verification if kept sparse.

## Evidence directly stated by source

- Binance docs directly state that kline intervals are interpreted in the provided timezone.
- Binance docs directly state that klines are identified by open time.
- Binance docs directly show the close price field position in the returned kline array.
- Polymarket directly states Binance BTCUSDT 1m candle close is the settlement source.

## What is uncertain

- This check verifies the ET alignment mechanics using the API, but the actual resolving candle is tomorrow's 12:00 ET candle, not yet available.
- Polymarket rules reference the Binance web chart surface specifically; while the API mechanics appear consistent with that chart, final settlement still depends on the chart/source as interpreted by the market operator.
- DST/ET handling on April 8, 2026 should still be EDT (-4), but this remains an operational assumption rather than a settled outcome until the actual resolving minute is observed.

## Why this source may matter

This is the key source for avoiding false confidence from generic BTC prices. The market does not resolve on a multi-exchange spot print or daily close; it resolves on a very specific Binance BTCUSDT 1-minute ET bucket and that makes timezone/candle mechanics genuinely material.

## Possible impact on the question

Because live Binance BTCUSDT is already comfortably above 66k and the settlement mechanics appear operationally straightforward, the main remaining risk is intraday downside into the specific April 8 12:00 ET minute rather than ambiguity about what data series counts.

## Reliability notes

- Primary reliability is high because the source is the exchange's own market-data documentation plus live direct exchange API outputs.
- Independence is limited because both the docs and API originate from Binance, but for source-of-truth mechanics that is acceptable and expected.
- Rate-limit risk was handled by using only a few low-weight requests rather than repeated polling.
