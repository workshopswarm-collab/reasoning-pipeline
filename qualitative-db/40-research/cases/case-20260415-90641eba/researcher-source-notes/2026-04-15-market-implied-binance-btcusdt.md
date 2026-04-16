---
type: source_note
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: binance-btcusdt-live-price-and-resolution-surface
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API BTCUSDT ticker and 1m klines
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/market-implied.md
tags: [binance, btcusdt, source-note, governing-source]
---

# Summary
Binance is the governing source of truth for this contract, so the most important direct evidence is the current BTC/USDT spot level and the exact 1-minute kline structure that will later determine settlement.

## Key facts extracted
- Binance spot API returned BTCUSDT price `74027.46000000` on 2026-04-15 during this run.
- Binance 1-minute klines showed recent closes of `73982.71000000`, `73994.61000000`, and `74027.45000000`.
- The latest returned kline opened at Unix ms `1776275220000` and closed at Unix ms `1776275279999`.
- The assigned contract resolves from the Binance BTC/USDT 12:00 ET candle's final `Close`, not high, low, or another exchange.

## Evidence directly stated by source
- Direct market price evidence from the governing exchange surface is currently about 5.7% above the 70000 threshold.
- Recent 1-minute candle closes are clustered around 73900-74000, showing the market is already comfortably above 70000 several days before resolution.

## What is uncertain
- This source does not say where BTC will trade at 12:00 ET on 2026-04-20.
- The contract depends on one specific future minute close, so current spot level is informative but not dispositive.

## Why this source may matter
This is the named resolution source. It anchors both the mechanics and the current state of the underlying.

## Possible impact on the question
If BTC remains materially above 70000 into Apr 20, the market's high Yes pricing is justified. A sharp drawdown below 70000 near the resolution minute is the main path to No.

## Reliability notes
- High reliability for current price and contract mechanics because Binance is the governing source.
- Moderate relevance for the final outcome because the decisive candle is still in the future.
