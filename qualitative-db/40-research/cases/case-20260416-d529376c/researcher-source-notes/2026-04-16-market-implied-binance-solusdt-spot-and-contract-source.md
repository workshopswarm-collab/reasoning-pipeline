---
type: source_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: case-20260416-d529376c | market-implied
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close be above 80 on April 19, 2026?
driver: reliability
date_created: 2026-04-16
source_name: Binance SOL/USDT ticker and 1m klines; Polymarket market page / rules
source_type: exchange_api_and_market_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/market-implied.md]
tags: [source-note, crypto, polymarket, binance, sol]
---

# Summary

Primary source note for the case. The contract resolves off the Binance SOL/USDT 1-minute candle labeled 12:00 ET on April 19, 2026, and current direct Binance spot data shows SOL around 85.27 on April 16 03:04 UTC, which is already above the 80 threshold.

## Key facts extracted

- Binance ticker endpoint returned `SOLUSDT` price `85.27000000` at fetch time.
- Binance 1-minute klines for the most recent minutes around 2026-04-16 03:04 UTC showed closes of approximately 85.14, 85.23, 85.17, 85.21, and 85.26.
- Polymarket rules state the market resolves `Yes` if the Binance 1-minute candle for `SOL/USDT 12:00 in the ET timezone (noon)` on April 19 has a final close price strictly higher than 80.
- The contract is specifically about Binance SOL/USDT, not other exchanges or pairs.
- Price precision is determined by Binance source precision.

## Evidence directly stated by source

- Direct exchange data: current SOL/USDT spot level is above the contract strike by roughly $5.27 at observation time.
- Direct contract mechanics: all of the following must hold for `Yes`:
  1. Use Binance as source of truth.
  2. Use the SOL/USDT pair.
  3. Use the 1-minute candle corresponding to 12:00 ET on April 19, 2026.
  4. Use the final close of that candle.
  5. That close must be strictly greater than 80.00.

## What is uncertain

- The note does not itself prove where SOL will be at the relevant April 19 noon ET minute.
- There can still be material crypto volatility over ~3.5 days.
- The Polymarket page text is a public rendering of the rules, but final operational resolution still depends on Binance’s displayed/final candle data at the relevant minute.

## Why this source may matter

This is the governing source-of-truth surface plus direct current-price evidence. For a date-specific threshold market, the current distance from strike and exact resolution mechanics are the core inputs.

## Possible impact on the question

Because the source-of-truth exchange currently prices SOL materially above 80, it supports a high probability of `Yes`, though not certainty, over the remaining time window.

## Reliability notes

- Binance is the explicit authoritative resolution source, so source-of-truth ambiguity is low.
- Direct exchange API evidence is strong for current spot but not itself sufficient for future settlement; it must be paired with time-to-expiry and volatility judgment.
- Operationally, the main residual risk is timing/market volatility rather than source credibility.