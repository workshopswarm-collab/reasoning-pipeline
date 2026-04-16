---
type: source_note
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: solana
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?
driver: reliability
date_created: 2026-04-15
source_name: Binance SOLUSDT daily kline API context
source_type: exchange market data
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=10
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-analyses/2026-04-16/dispatch-case-20260416-1f25d147-20260416T035120Z/personas/catalyst-hunter.md]
tags: [binance, market-data, timing, context, catalyst-hunter]
---

# Summary

Binance daily klines show SOL has already been trading above the $80 threshold for multiple recent sessions leading into the April 19 resolution window. Recent daily closes and intraday highs indicate the threshold is currently in-the-money, but daily volatility remains large enough that a sub-$80 move by noon ET is still plausible in a crypto market.

## Key facts extracted

- Recent daily closes include approximately 85.56, 82.57, 83.33, 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, and partial current-day trading around 85.37.
- Recent daily lows stayed above 80 on several days, but at least one recent session traded down to roughly 78.38 and another to roughly 81.27 / 81.40.
- Recent realized range has been meaningful: several 3%–6% daily swings and a recent drop from 84.94 close/open area to 81.53 close.

## Evidence directly stated by source

- Binance market data directly confirms current and recent SOL/USDT trading levels.
- Recent price action places SOL only modestly above the strike rather than comfortably far above it.

## What is uncertain

- Daily candles are contextual, not settlement-direct, because the contract resolves on a one-minute noon-ET close.
- This source alone does not identify a discrete upcoming catalyst; it mainly characterizes path and volatility.

## Why this source may matter

This is the best direct exchange-side context available in-run. It shows the strike is presently favorable to Yes, while also showing that SOL can move several dollars in a short time, making timing and weekend risk still relevant.

## Possible impact on the question

The data supports a high Yes probability because the strike is below recent trading, but it tempers overconfidence because a moderate crypto drawdown before or into the noon ET window could still flip the outcome.

## Reliability notes

High reliability as direct Binance market data. Limited because interval is daily rather than the exact one-minute resolution candle.