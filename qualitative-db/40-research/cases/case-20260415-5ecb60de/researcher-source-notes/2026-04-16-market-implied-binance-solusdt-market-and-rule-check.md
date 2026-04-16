---
type: source_note
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: case-20260415-5ecb60de | market-implied
question: Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API and Polymarket rules page
source_type: primary-plus-resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: supports-yes
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/market-implied.md]
tags: [binance, polymarket-rules, solusdt, settlement-source]
---

# Summary

This note captures the source-of-truth surface for settlement and the current Binance spot context that the market is implicitly pricing.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance SOL/USDT 1-minute candle for 12:00 ET on April 19, using the final close of that candle.
- The title threshold is strictly above $80; exactly $80.00 would resolve No.
- A direct Binance ticker fetch returned SOLUSDT at 84.87 on 2026-04-15.
- Recent Binance 1-minute klines around the observation time were clustered near 84.87 to 84.93.
- Recent Binance daily klines show SOL closed above 80 on each of the last 10 daily candles returned, with closes including 80.03, 85.56, 82.57, 83.33, 84.83, 84.93, 81.53, 86.51, 83.72, and 84.85.

## Evidence directly stated by source

- Binance ticker endpoint reported `{ "symbol": "SOLUSDT", "price": "84.87000000" }`.
- Binance daily kline endpoint showed a 10-day range roughly from intraday lows of 78.38-83.80 and highs of 83.20-87.67, with most closes in the low-to-mid 80s.
- Polymarket rules explicitly define the governing source as Binance SOL/USDT with 1m candles and the noon ET candle close.

## What is uncertain

- The live ticker is not the settlement print; the contract depends on one exact minute-candle close at 12:00 ET on April 19.
- Daily closes above 80 do not guarantee the noon ET 1-minute close will also be above 80.
- Intraday crypto volatility over the next ~3.7 days could still move SOL below 80 by settlement.

## Why this source may matter

This is the most important direct evidence set because it both defines the contract mechanics and shows the current Binance price regime relative to the threshold.

## Possible impact on the question

The market's 90% Yes price appears grounded in the fact that Binance SOL/USDT is currently about 6% above the threshold and has been trading mostly above 80 recently. The same source also reveals the key failure mode: only one minute close matters, so a sharp selloff into noon ET on April 19 would be enough to flip the result.

## Reliability notes

- Binance is the authoritative settlement source named by contract.
- Polymarket's rules page is authoritative for interpretation of what counts.
- These sources are not independent of each other: one defines the rules, the other supplies the referenced data surface.