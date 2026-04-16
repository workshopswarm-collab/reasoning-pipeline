---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: reliability
date_created: 2026-04-16
source_name: Binance public price and kline API checks
source_type: exchange market data
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=30
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, price, kline, verification, base-rate]
---

# Summary

Direct Binance API checks show SOL/USDT already trading above the $80 threshold several days before resolution, with recent daily closes from April 7 through April 16 all above $80 and a live spot price around $85.25 at check time. This makes the outside-view base rate for staying above $80 over the next ~3.5 days fairly strong, though not certain because the contract is tied to one exact 12:00 ET minute close.

## Key facts extracted

- Binance spot ticker check returned SOLUSDT around 85.25 at the time of research.
- Recent daily closes from April 7 to April 16 were all above 80, approximately: 85.56, 82.57, 83.33, 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, 85.25.
- Recent 72-hour hourly range was roughly 81.54 to 87.67.
- Recent 1-minute klines also confirmed the exchange endpoint was returning current minute closes around 85.2 to 85.27.

## Evidence directly stated by source

- The exchange data itself directly states recent SOL/USDT prices and candle closes.
- The market is currently several dollars above the $80 threshold.

## What is uncertain

- Daily and hourly candles are contextual evidence, not the exact resolving candle.
- Crypto can move materially over multi-day windows, so current spot is not enough by itself.

## Why this source may matter

Because the market resolves from Binance data, Binance is both the key contextual source and the source-of-truth family. Recent prices above 80 establish the structural outside-view baseline: absent a material selloff, a final noon ET close above 80 is more likely than not.

## Possible impact on the question

This source supports a bullish base-rate view versus the binary threshold, but also shows why the remaining risk is mostly short-horizon volatility and single-minute timing risk rather than a deeper contract-interpretation problem.

## Reliability notes

High reliability for direct exchange price context and strong fit to the contract's designated source family. Independence versus the Polymarket page is medium rather than high because both ultimately reference the same underlying market state, but Binance is the more authoritative data surface.