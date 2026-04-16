---
type: source_note
case_key: case-20260416-33b4e3b5
dispatch_id: dispatch-case-20260416-33b4e3b5-20260416T021538Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: case-20260416-33b4e3b5 | market-implied
question: Will the price of Solana be above $80 on April 19?
driver: reliability
date_created: 2026-04-15
source_name: Binance SOLUSDT spot endpoints and market page rules
source_type: exchange API plus market rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-33b4e3b5/researcher-analyses/2026-04-16/dispatch-case-20260416-33b4e3b5-20260416T021538Z/personas/market-implied.md]
tags: [binance, solusdt, market-state, resolution-source]
---

# Summary

This source note captures the direct exchange data and contract mechanics most relevant to the April 19 SOL>$80 market.

## Key facts extracted

- Binance spot ticker returned `{"symbol":"SOLUSDT","price":"84.80000000"}` during this run.
- Binance daily klines for the prior two weeks show SOL/USDT has recently closed above $80 on most days, with closes including 80.40, 80.83, 81.89, 85.56, 82.57, 83.33, 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, and partial current-day trade around 84.80.
- The recent 1-hour klines near the time of research show SOL/USDT trading mostly between about 84.0 and 85.5 rather than hovering near the $80 threshold.
- Binance exchange info for SOLUSDT shows `PRICE_FILTER` tick size `0.01000000`, implying the operative price precision on the source surface is two decimals.
- Polymarket rules say the market resolves from the Binance SOL/USDT 1-minute candle for `12:00` ET on April 19 using the final `Close` price, and the outcome is Yes only if that close is higher than 80.

## Evidence directly stated by source

- Binance direct spot and kline endpoints state current and recent traded prices for SOL/USDT.
- Binance symbol metadata states the trading increment / price filter.
- Polymarket directly states the governing resolution rule and the exchange/pair/timeframe used for settlement.

## What is uncertain

- The settlement depends on one exact 1-minute close at noon ET on April 19, not on current spot or daily closes.
- Short-horizon crypto volatility can still move SOL from the mid-80s to below 80 by settlement.
- Exchange API checks here verify the direct source surfaces and price context, but not the exact future settlement candle.

## Why this source may matter

This is the core direct-evidence package for both market state and contract interpretation: it identifies the precise source of truth and shows that the market is currently pricing from a level materially above the threshold.

## Possible impact on the question

The evidence supports why the market is heavily tilted Yes: SOL is currently around 84.8 and has spent much of the recent period above 80, so an 80 threshold three days out does not require a new rally. But because settlement keys off one exact 12:00 ET 1-minute close, the margin above threshold matters more than broad trend alone.

## Reliability notes

- Binance is the authoritative source of truth for settlement under the posted market rules.
- This is high-credibility direct evidence for current price state and contract mechanics.
- It is not fully outcome-determinative because the market has not yet reached the settlement timestamp.