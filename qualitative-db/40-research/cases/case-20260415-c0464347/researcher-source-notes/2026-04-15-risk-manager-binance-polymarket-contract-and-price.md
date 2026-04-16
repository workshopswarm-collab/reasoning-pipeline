---
type: source_note
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API docs plus live BTCUSDT price/klines; Polymarket market rules
source_type: primary_and_contextual_mix
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data ; https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, btc, contract-check, timing-check]
---

# Summary

This source bundle establishes the contract mechanics and current state for the case. Polymarket states the market resolves on the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-20, using the final candle close and Binance as source of truth. Binance API docs confirm `/api/v3/klines` exposes 1-minute candles, the `close` field, and a `timeZone` parameter that changes interval interpretation while `startTime`/`endTime` remain UTC. Live Binance price and kline endpoints show BTC/USDT trading materially above 70000 at run time.

## Key facts extracted

- Polymarket rule: market resolves Yes if the Binance BTC/USDT 12:00 ET one-minute candle on Apr 20 has a final close above 70000.
- Binance docs: `/api/v3/klines` returns 1-minute candles and the fifth price field is close.
- Binance docs: `timeZone` parameter changes how candle intervals are interpreted; accepted range includes `-4`, which matches ET daylight time at the scheduled resolution date.
- Live Binance ticker price during this run was about 74632-74643.
- Binance 24hr ticker during this run showed high 76038, low 73795, last 74632, so spot remained well above 70000 even on the day range low.

## Evidence directly stated by source

- Polymarket explicitly names Binance BTC/USDT close price as the resolution source.
- Binance docs explicitly define kline response structure and timezone handling.
- Binance live endpoints directly report current BTCUSDT price and recent one-minute closes.

## What is uncertain

- This bundle does not prove what the Apr 20 noon ET candle will be; it only confirms current distance above threshold and the exact settlement mechanics.
- Polymarket references the Binance trading UI rather than API docs, so there is a small operational interpretation risk if UI and API presentation ever diverge, though both appear to rely on the same candle construct.

## Why this source may matter

The case is narrow, date-sensitive, and rule-sensitive. These sources jointly cover the two core requirements: what must happen for resolution and whether BTC currently has enough cushion above 70000 to justify a high probability.

## Possible impact on the question

Strongly supports a high Yes probability because the contract threshold is simple and current spot is roughly 6.6% above the line with five days remaining. It also highlights the main risk-manager caveat: this is still path-sensitive and a single one-minute close below 70000 at the specified timestamp is enough to lose.

## Reliability notes

- Binance API docs are high-credibility for contract interpretation of candle mechanics.
- Binance live market-data endpoints are direct but still only contextual for the future event.
- Polymarket rules are authoritative for how the prediction contract will be adjudicated.
