---
type: source_note
case_key: case-20260414-d5888900
dispatch_id: dispatch-case-20260414-d5888900-20260414T143228Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-14 close above 70000?
driver: reliability
date_created: 2026-04-14
source_name: Binance spot API docs and live BTCUSDT price/klines
source_type: primary exchange docs plus exchange market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-d5888900/researcher-analyses/2026-04-14/dispatch-case-20260414-d5888900-20260414T143228Z/personas/variant-view.md]
tags: [source-note, binance, kline, market-data, verification]
---

# Summary

This source pair supports both the mechanics and the observed market state. Binance documentation states that klines are available via `/api/v3/klines`, are uniquely identified by open time, and contain a close-price field. A live read from Binance spot endpoints during this run showed BTCUSDT around 75.6k, materially above the 70k threshold.

## Key facts extracted

- Binance documents `GET /api/v3/klines` for candlestick data.
- Klines are "uniquely identified by their open time."
- The kline response explicitly includes a close-price field.
- Binance docs allow a `timeZone` parameter for interval interpretation, but note `startTime` and `endTime` remain interpreted in UTC.
- A runtime ET-to-UTC conversion check showed 2026-04-14 12:00:00 ET corresponds to 2026-04-14 16:00:00 UTC.
- A live Binance spot query during the run returned `{"symbol":"BTCUSDT","price":"75641.98000000"}`.
- A live Binance 1-minute kline query returned recent closes in the mid-75k range, all well above 70k.

## Evidence directly stated by source

From Binance docs:
- `GET /api/v3/klines`
- "Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time."
- Response includes `[open time, open, high, low, close, ...]` with close price in the fifth element.

From live Binance data captured during run:
- ticker price: `75641.98000000`
- recent 1m closes included `75957.98000000`, `75986.03000000`, `75935.90000000`, `75686.40000000`, `75641.98000000`

## What is uncertain

- The live query was not the exact final 12:00 ET candle close; it was an additional verification pass showing the market was trading far above the threshold near analysis time.
- Binance UI-vs-API reconciliation for final settlement is not fully specified by the contract beyond pointing to the chart page; a tiny residual operational ambiguity remains.

## Why this source may matter

This is the closest thing to a primary underlying source for the actual economic condition in the contract. It also materially reduces the plausibility of the main variant thesis (that an operational/settlement nuance matters) because the price level is not near the strike.

## Possible impact on the question

If BTCUSDT is trading ~75.6k close to the noon-ET resolution window, then a drop below 70k within the governing minute would require an extraordinary move. That makes the substantive economic path to No extremely remote, leaving only narrow exchange-data or settlement-interpretation edge cases as meaningful residual risks.

## Reliability notes

High value because one component is Binance's own API documentation and the other is live Binance market data. Independence versus Polymarket is moderate rather than high, because Polymarket rules explicitly key off Binance. Still, it is the correct underlying source family for this contract.