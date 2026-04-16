---
type: source_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance SOLUSDT API snapshots and recent klines
source_type: exchange market data / primary contextual pricing source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: supports-yes
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/market-implied.md]
tags: [source-note, binance, solusdt, market-data]
---

# Summary

Primary contextual source for the actual exchange and pair named in the contract. A live API pull on 2026-04-16 00:07 EDT showed SOLUSDT at 85.32 on Binance, already above the 80 threshold by about 6.65%. Recent hourly and daily klines indicate SOL has been trading above 80 through the recent window sampled, which helps explain why the market is pricing the April 19 noon-close-above-80 contract at an extreme yes probability.

## Key facts extracted

- Binance ticker endpoint returned `{"symbol":"SOLUSDT","price":"85.32000000"}` on 2026-04-16 around 00:07 EDT.
- Recent 1-minute klines from Binance showed prints clustered around 85.15 to 85.32.
- Recent daily kline sample included a low of 78.38 on the oldest sampled day, but subsequent closes in the sample were above 80, with the latest sampled daily close at 85.38.
- Recent hourly sample over 48 hours showed SOL roughly in the mid-85 area, with the latest sampled hourly close at 85.38.

## Evidence directly stated by source

- Current Binance SOLUSDT spot price is above 80.
- Binance has enough observable recent trading history in the sampled window to show that 80 is not just barely in range; it is below current price by several dollars.

## What is uncertain

- This source does not by itself answer the exact settlement condition, which depends on the Binance 1-minute candle for 12:00 ET on 2026-04-19.
- Current price can still move materially over ~3.5 days in crypto.
- API sampling here is only a partial recent-history check, not a full volatility study.

## Why this source may matter

The contract explicitly settles using Binance SOL/USDT. Using Binance directly avoids exchange-mismatch errors and supports the market-implied logic: if SOL is already ~85.3, the burden for a no outcome is a drop below 80 by the precise settlement minute.

## Possible impact on the question

Supports a high yes probability because the underlying named source is already well above the line. It does not settle the contract today, but it makes the market's 0.92 pricing directionally understandable.

## Reliability notes

High credibility for current exchange price context because Binance is the governing venue named in the rules. Independence is limited because both the contract and this source rely on Binance, but that is appropriate here since source-of-truth alignment matters more than cross-source triangulation for the exact settlement mechanic.