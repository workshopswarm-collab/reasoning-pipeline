---
type: source_note
case_key: case-20260415-35855579
dispatch_id: dispatch-case-20260415-35855579-20260415T225312Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API docs + live BTCUSDT market endpoints + Polymarket market rules
source_type: primary_and_contextual
source_url: https://developers.binance.info/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, source-of-truth, resolution, btc]
---

# Summary

This source note captures the governing contract mechanics from the Polymarket market page and verifies that Binance exposes live BTCUSDT pricing and 1-minute kline endpoints capable of supplying the settlement candle. It also records the current live BTCUSDT level as of the research run.

## Key facts extracted

- Polymarket says the market resolves Yes if the Binance BTC/USDT 1-minute candle for `12:00` in ET on 2026-04-16 has a final close price strictly higher than `72000`.
- The market is specifically about Binance BTC/USDT, not another exchange or pair.
- Binance spot API documentation shows `GET /api/v3/klines` supports `interval=1m` and returns kline rows including open time, close price, and close time.
- Binance docs note `startTime` and `endTime` are interpreted in UTC even when a `timeZone` parameter is provided.
- 2026-04-16 12:00 ET corresponds to 2026-04-16 16:00 UTC.
- Live Binance spot endpoint during the run returned BTCUSDT around `75119.53` to `75124.27`.
- Binance 24hr endpoint during the run returned: lastPrice `75124.26`, openPrice `74070.74`, highPrice `75425.00`, lowPrice `73514.00`.
- Recent 1-minute klines near the run time showed closes around `75124.27` at 18:54 ET on 2026-04-15.

## Evidence directly stated by source

- Polymarket rules explicitly define the source of truth and the all-conditions-needed contract logic.
- Binance API docs explicitly define the kline endpoint and its returned close-price field.
- Binance live endpoints directly state current BTCUSDT market price and recent kline closes.

## What is uncertain

- The exact BTCUSDT close at 2026-04-16 12:00 ET is not yet known because the market has not resolved.
- Accessing the Binance website chart UI directly from this environment triggered a WAF challenge, so verification relies on Binance's official API/docs rather than the web chart surface.
- Short-horizon BTC volatility remains the main unresolved determinant.

## Why this source may matter

This is the core source-of-truth stack for the case. The contract is narrow and date-specific, so correct interpretation depends on the exact exchange, pair, timeframe, timezone, and strict `higher than` condition.

## Possible impact on the question

Because live Binance pricing during the run is already about 4.3% above the 72000 threshold with less than a day remaining, the base-rate implication is that Yes should remain the favored outcome absent a substantial downside move before noon ET on 2026-04-16.

## Reliability notes

- Polymarket market page is authoritative for contract wording.
- Binance API documentation is authoritative for how the underlying 1-minute kline data is exposed.
- Binance live API endpoints are direct primary data for current BTCUSDT pricing.
- Independence between Polymarket and Binance is medium rather than high because the contract explicitly references Binance, but for source-of-truth purposes this is appropriate rather than problematic.
