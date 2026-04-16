---
type: source_note
case_key: case-20260415-e4a8d83c
dispatch_id: dispatch-case-20260415-e4a8d83c-20260415T230345Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 above 74000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API docs and live BTCUSDT endpoints
source_type: primary_and_contextual_exchange_source
source_url: https://developers.binance.info/docs/binance-spot-api-docs/rest-api/market-data-endpoints
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
tags: [binance, btcusdt, resolution-source, source-note]
---

# Summary

Binance is both the governing source of truth for settlement mechanics and the most relevant contextual price source. Its docs confirm the `GET /api/v3/klines` endpoint returns 1-minute candlestick bars, that klines are uniquely identified by open time, and that a `timeZone` parameter can interpret kline intervals in a specified timezone while `startTime` and `endTime` remain UTC. Live Binance endpoints on 2026-04-15 around 19:04 ET showed BTC/USDT trading near 74.8k, with the 24-hour weighted average around 74.26k and the day high at 75.425k.

## Key facts extracted

- Binance spot API docs define `GET /api/v3/klines` for 1-minute candlestick bars and show the response field containing the candle close price.
- Docs state klines are uniquely identified by open time.
- Docs state `timeZone` can be supplied so kline intervals are interpreted in that timezone; accepted range includes offsets such as `-4:00` for EDT.
- Live Binance endpoint `ticker/price?symbol=BTCUSDT` returned about 74825.76 at research time.
- Recent 1-minute klines showed BTC/USDT trading in the upper 74k range around 23:00-23:04 UTC, which is 19:00-19:04 ET on 2026-04-15.
- Binance 24-hour ticker returned: last price about 74820.01, weighted average about 74263.61, high 75425.00, low 73514.00.

## Evidence directly stated by source

- Binance docs explicitly define the kline endpoint and candle-close field.
- Binance docs explicitly describe timezone handling for kline intervals.
- Live Binance endpoints directly report current BTC/USDT market levels and recent candle closes.

## What is uncertain

- The Polymarket rule text points traders to the Binance UI candle display, while my direct verification used Binance API docs and live API responses rather than the consumer web chart.
- The exact final settlement value on Apr 17 at 12:00 ET remains unknown and depends on future price action.
- API and UI should align, but any transient display or data-availability issue would be an operational-risk caveat rather than a pricing thesis.

## Why this source may matter

This is the nearest thing to an authoritative source because the market resolves specifically against Binance BTC/USDT 1-minute candle close data. It also anchors the current distance from the 74k threshold and confirms the timezone and candle mechanics that matter for resolution.

## Possible impact on the question

With BTC already trading modestly above 74k and recent 24-hour price action spanning both sides of 74k, the outside view is that a one-day-ahead noon print above 74k is plausible but far from locked in. The source supports a probability above 50% but not near certainty.

## Reliability notes

High relevance and high credibility because Binance is the named resolution source. Independence is limited because the same institution supplies both contract mechanics and contextual market levels, so a secondary source is still useful for contract wording and cross-checking interpretation.