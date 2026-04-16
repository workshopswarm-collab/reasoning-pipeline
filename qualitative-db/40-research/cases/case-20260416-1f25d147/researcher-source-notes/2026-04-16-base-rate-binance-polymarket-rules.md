---
type: source_note
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance SOL/USDT direct API checks and Polymarket rules page
source_type: primary_plus_market_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT ; https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=180 ; https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1m&limit=4320 ; https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-analyses/2026-04-16/dispatch-case-20260416-1f25d147-20260416T035120Z/personas/base-rate.md]
tags: [binance, polymarket, source-note, direct-source, timing-check]
---

# Summary

This source note captures the direct settlement mechanics and the most relevant current/base-rate price context for the April 19 SOL>$80 market.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance SOL/USDT **1 minute candle for 12:00 in ET timezone (noon)** on the specified date, using the candle's final **Close** price.
- The market is specifically about **Binance SOL/USDT**, not other exchanges or pairs.
- Direct Binance API spot check on 2026-04-15 late evening ET showed SOL/USDT around **85.23-85.24**.
- Direct Binance daily-klines sample for the last **180 days** showed SOL daily close above 80 on **171/180 days (96.7%)**.
- In recent windows, SOL daily closes were above 80 on:
  - **14/14 days (100%)** over the last 14 days
  - **29/30 days (96.7%)** over the last 30 days
  - **57/60 days (95.0%)** over the last 60 days
- Timing verification pass: Binance 1-minute klines map cleanly to ET timestamps. A check found the row corresponding to **2026-04-15 12:00:00 ET** with close **83.94**, confirming the practical mapping method for the settlement timestamp.
- Persistence check: conditional on a daily close already being above 80, the next 3 daily closes also stayed above 80 on **159/171 = 92.98%** of observed cases in the 180-day sample.

## Evidence directly stated by source

From Polymarket rules page:
- Yes resolves if the Binance 1-minute SOL/USDT candle for 12:00 ET on the target date has a final close higher than 80.
- Price precision is determined by the source.

From Binance API outputs observed during this run:
- Current ticker price: 85.23 / 85.24.
- Recent 1-minute closes near the observation time remained tightly clustered around 85.25-85.38.
- The noon-ET timestamp conversion is workable using Binance kline open time in UTC mapped into America/New_York.

## What is uncertain

- The contract settles on a **single one-minute close** at noon ET on April 19, not on the daily close or current spot price.
- A sharp market move between now and settlement could still push SOL below 80 at the decisive minute.
- The 180-day daily-close base rate is only a proxy for the narrower one-minute settlement condition.

## Why this source may matter

This is the governing direct-evidence bundle for the case: the rules define what counts, while Binance provides the actual source-of-truth market data and timing surface.

## Possible impact on the question

The direct data strongly support a high probability that the market resolves Yes, because SOL is already materially above 80 and has spent most of the last 2-6 months above that threshold. The main remaining risk is short-horizon crypto volatility causing a drop below 80 exactly at the relevant minute.

## Reliability notes

- Binance API is the most relevant direct data source because the contract explicitly settles from Binance SOL/USDT.
- Polymarket rules page is authoritative for contract mechanics but not for the final settlement price itself.
- Evidence independence is moderate rather than high because the rules and price source are mechanically linked to the same settlement framework, though they answer different questions (what counts vs current/base-rate state).
