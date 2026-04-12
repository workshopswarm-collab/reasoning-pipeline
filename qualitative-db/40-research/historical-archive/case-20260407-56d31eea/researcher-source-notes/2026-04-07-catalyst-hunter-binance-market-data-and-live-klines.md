---
type: source_note
case_key: case-20260407-56d31eea
dispatch_id: dispatch-case-20260407-56d31eea-20260407T023203Z
analysis_date: 2026-04-07
persona: catalyst-hunter
domain: crypto
subdomain: exchanges
entity: binance
topic: case-20260407-56d31eea | catalyst-hunter
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-07 close above 66000?
driver: operational-risk
date_created: 2026-04-06T22:36:00-04:00
source_name: Binance Spot API market-data docs and live BTCUSDT 1m klines
source_type: primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [bitcoin, binance]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-56d31eea/researcher-analyses/2026-04-07/dispatch-case-20260407-56d31eea-20260407T023203Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, klines, settlement-source, 1m-candle]
---

# Summary

Binance's own market-data documentation defines the kline/candlestick endpoint and explicitly identifies the close price field for each 1-minute bar. A live pull of recent BTCUSDT 1-minute klines showed spot trading around 68.45k-68.59k at fetch time, comfortably above the 66k threshold.

## Key facts extracted

- Binance documents `GET /api/v3/klines` as the kline/candlestick endpoint for spot symbols.
- Klines are uniquely identified by open time.
- For each kline array, the fifth field is the close price.
- Binance supports 1-minute intervals (`1m`).
- A live Binance API pull of recent BTCUSDT 1-minute klines returned closes in the high 68k range, including values such as 68454.63, 68480.28, 68515.69, 68527.29, 68573.67, and 68592.59.

## Evidence directly stated by source

- Binance docs: `/api/v3/klines` returns candlestick bars, with the response array including `Close price` as the fifth field.
- Binance docs: `interval=1m` is a supported interval.
- Live Binance klines: recent BTCUSDT spot trading was materially above 66000 at the time checked.

## What is uncertain

- This note does not itself prove the exact 12:00 ET April 7 close because that timestamp had not yet occurred when checked.
- The market resolves on the final close of the specific 12:00 ET candle, so intraday price can still move materially before resolution.
- The Polymarket rule references the chart UI rather than the API, though the API definitions strongly clarify the same candle mechanics.

## Why this source may matter

This is the governing source family for settlement mechanics. It clarifies the exact data object that matters: the Binance BTC/USDT 1-minute candle close, not a multi-exchange average, not a futures contract, and not an approximate headline price.

## Possible impact on the question

The source materially supports a high probability of Yes because:
- the threshold is low relative to the observed live Binance spot level,
- the precise resolution object is clear,
- and the remaining path to No mainly requires a sub-66k move before the specified noon ET close.

## Reliability notes

High reliability for contract mechanics and current spot context because both the documentation and live data come from Binance directly. The main caveat is timing: only the exact noon ET candle close settles the market.