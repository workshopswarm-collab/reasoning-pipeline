---
type: source_note
case_key: case-20260413-63496469
dispatch_id: dispatch-case-20260413-63496469-20260413T173535Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-66k-on-april-14
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 14, 2026 be above 66000?
driver: reliability
date_created: 2026-04-13
source_name: Binance spot BTC/USDT API endpoints (ticker price and 1m klines)
source_type: exchange market data / primary resolution-context source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-63496469/researcher-analyses/2026-04-13/dispatch-case-20260413-63496469-20260413T173535Z/personas/base-rate.md]
tags: [binance, btcusdt, source-note, primary-source]
---

# Summary

This source note captures direct Binance surfaces relevant to the contract: the live BTC/USDT spot ticker and 1-minute kline data accessible from Binance API endpoints. While the market formally resolves from the Binance UI candle, these API outputs are the closest direct machine-readable representation of the same underlying exchange feed and are useful both for current level-checking and for a recent same-time reference class.

## Key facts extracted

- Binance ticker price for BTCUSDT at research time returned `72426.03000000`.
- Binance 1-minute klines around the research timestamp showed closes around 72.4k.
- A rough same-time historical sample of the prior 14 days at 16:00 UTC (which corresponds to 12:00 ET during EDT) showed every sampled close above 66,000.
- The sampled closes from 2026-03-30 through 2026-04-12 ranged roughly from 66.8k to 72.9k.

## Evidence directly stated by source

- Current Binance BTCUSDT price is materially above the contract threshold.
- Recent same-time 1-minute closes from Binance have all cleared 66k in the sampled window.

## What is uncertain

- The contract settles on the Binance UI candle for 12:00 ET on 2026-04-14, not the API endpoints directly.
- A one-day-ahead crypto move can still be large enough to cross the threshold if there is a sharp selloff.
- The 14-day sample is a convenience reference class, not a full distributional study.

## Why this source may matter

It is the most direct available source for both current BTC/USDT level and the specific 1-minute-candle mechanics that govern resolution. It anchors the outside-view question: with BTC trading near 72.4k, how often does it fall more than ~8.9% within about 22.5 hours and land below 66k exactly at the settlement minute?

## Possible impact on the question

This source strongly supports a high Yes probability because the threshold is far below the current Binance spot level and recent same-time candle observations have been comfortably above 66k. It does not eliminate tail-risk from a sharp drawdown or exchange-specific operational issue.

## Reliability notes

- Primary and highly relevant because Binance is the named resolution source.
- The exact settlement surface is the Binance chart/UI candle, so there remains a small implementation ambiguity between public API outputs and the UI display.
- Independence is low because both current-level and historical checks come from the same underlying source family; this is why a secondary contextual source was also used in the main finding.
