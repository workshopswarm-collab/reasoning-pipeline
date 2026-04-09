---
type: source_note
case_key: case-20260406-6e955d27
dispatch_id: dispatch-case-20260406-6e955d27-20260408T153555Z
analysis_date: 2026-04-08
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260406-6e955d27 | base-rate
question: Will the price of Bitcoin be above $66,000 on April 6?
driver: operational-risk
date_created: 2026-04-08
source_name: Binance BTCUSDT 1m kline endpoint and Polymarket market rules page
source_type: exchange_api_and_market_rules
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&startTime=1775491200000&endTime=1775491260000&limit=1
source_date: 2026-04-08
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, source-of-truth, settlement, btc]
---

# Summary

This source note combines the governing source-of-truth surface and the market-rule interpretation needed for settlement. Binance is the stated resolution source, and the exact 1-minute BTC/USDT candle corresponding to 2026-04-06 12:00 ET is directly queryable via Binance's kline endpoint.

## Key facts extracted

- The market rules state the market resolves to Yes if the Binance BTC/USDT 1 minute candle for 12:00 ET on April 6 has a final Close price above 66,000.
- 2026-04-06 12:00 ET converts to 2026-04-06 16:00:00 UTC.
- The Binance 1-minute kline for startTime 1775491200000 (2026-04-06 16:00:00 UTC) returned:
  - open: 69968.87000000
  - high: 69974.28000000
  - low: 69938.58000000
  - close: 69938.59000000
  - close time: 1775491259999
- 69938.59000000 is above 66000, so under the stated rules this market resolves Yes.
- Polymarket's event page also displayed Final outcome: Yes and No dispute at fetch time.

## Evidence directly stated by source

- Binance API directly states the exact 1-minute candle OHLC values for BTC/USDT at the relevant minute.
- Polymarket directly states the settlement rule text and displayed final outcome.

## What is uncertain

- The public web page wording says the source is the Binance trading UI with Candles selected; I verified the same minute through Binance API endpoints rather than the browser-rendered UI because the UI did not extract cleanly via tool fetch.
- I did not independently inspect Binance's rendered chart widget, but I did verify the exact minute through both `/api/v3/klines` and `/api/v3/uiKlines`, which returned the same candle payload.

## Why this source may matter

This is the decisive source set for the case. The market is a narrow, date-specific, source-defined settlement question, so correctly mapping ET noon to the exact Binance 1-minute candle is the main task.

## Possible impact on the question

This source effectively settles the market direction. If the queried minute and candle-close logic are correct, the answer is unambiguously Yes.

## Reliability notes

- Binance is the named governing source of truth, so source authority is high.
- The additional check against both `klines` and `uiKlines` reduces endpoint-format risk.
- Polymarket's displayed final outcome is useful corroboration but is not more authoritative than the named Binance source for the underlying price itself.