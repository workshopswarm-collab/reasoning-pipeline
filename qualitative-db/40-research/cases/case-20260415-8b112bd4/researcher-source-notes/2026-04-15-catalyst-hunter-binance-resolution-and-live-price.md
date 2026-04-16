---
type: source_note
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-8b112bd4 | catalyst-hunter
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API docs and live BTCUSDT endpoints
source_type: primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8b112bd4/researcher-analyses/2026-04-15/dispatch-case-20260415-8b112bd4-20260415T153012Z/personas/catalyst-hunter.md]
tags: [binance, resolution-source, live-price, candle]
---

# Summary

Binance is the governing source of truth for this market. Its spot API documentation confirms that 1-minute klines are uniquely identified by open time and that a `timeZone` parameter can interpret intervals in a specified timezone. A live Binance BTCUSDT ticker check at research time showed spot BTC/USDT around 73.7k, comfortably above the 70k threshold roughly 20.5 hours before the 12:00 ET Apr 16 resolution candle.

## Key facts extracted

- Binance docs define `GET /api/v3/klines` for candlestick bars and specify 1-minute interval support.
- Binance docs state a `timeZone` parameter can be used, with intervals interpreted in that timezone.
- Kline response includes explicit close price and open/close timestamps.
- Live Binance `ticker/price` returned BTCUSDT at `73664.58000000` on 2026-04-15 during this run.
- Recent 1-minute BTCUSDT klines fetched during this run showed closes around 73.65k-73.66k.

## Evidence directly stated by source

- Docs: klines are uniquely identified by open time and return open, high, low, close, volume, and close time.
- Docs: `timeZone` may be provided; intervals are interpreted in that timezone instead of UTC.
- Live ticker endpoint returned `{"symbol":"BTCUSDT","price":"73664.58000000"}`.

## What is uncertain

- The Polymarket contract references the Binance web chart with 1m candles at 12:00 ET, while my verification used Binance API endpoints and contract text rather than visually inspecting the web UI candle.
- Spot price can move materially in 20+ hours, so current level does not settle the market.

## Why this source may matter

This is the primary settlement source family. It anchors both contract interpretation and the live baseline level relative to 70k.

## Possible impact on the question

Because Binance spot BTC/USDT is already ~5.2% above the 70k line, the market only fails if BTC drops meaningfully before the specific Apr 16 12:00 ET 1-minute candle close. That makes the main near-term catalyst path one of downside shock or exchange-specific operational disturbance rather than gradual upside discovery.

## Reliability notes

Primary and highly relevant. Best source for settlement mechanics and live spot baseline. Main limitation is that the API docs explain endpoint behavior, not Polymarket adjudication edge cases beyond what the contract already says.