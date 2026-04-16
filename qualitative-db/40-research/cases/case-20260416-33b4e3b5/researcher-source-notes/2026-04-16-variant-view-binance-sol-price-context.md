---
type: source_note
case_key: case-20260416-33b4e3b5
dispatch_id: dispatch-case-20260416-33b4e3b5-20260416T021538Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: tokens
entity: sol
topic: sol price context into Apr 19 noon ET threshold market
question: Will Binance SOL/USDT 1-minute candle close above 80 at 12:00 ET on April 19, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Binance SOLUSDT spot API (ticker, daily klines, monthly klines, recent 1m klines)
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-33b4e3b5/researcher-analyses/2026-04-16/dispatch-case-20260416-33b4e3b5-20260416T021538Z/personas/variant-view.md]
tags: [binance, market-data, source-note, sol]
---

# Summary

Direct Binance market data shows SOL/USDT trading around 84.91 on 2026-04-15 22:16-22:17 ET, modestly above the 80 threshold, with recent daily closes mostly in the low-to-mid 80s and April monthly trading so far between roughly 76.70 and 87.67. This makes the contract largely a short-horizon path question around whether SOL can avoid a sub-80 dip specifically into the April 19 12:00 ET one-minute close.

## Key facts extracted

- Binance ticker price at fetch time: `84.91000000`.
- Binance server time fetch returned `1776305837053`, corresponding to about 2026-04-15 22:17:17 ET / 2026-04-16 02:17:17 UTC.
- April 2026 monthly kline so far: open about 83.19, high 87.67, low 76.70, latest close 84.79.
- Recent daily closes from Binance over the prior several days included 86.51, 83.72, 84.90, and 84.79, indicating repeated trading above 80 but not by a huge margin.
- Recent 1-minute candles near fetch time clustered tightly around 84.76-84.99, showing no immediate approach to the threshold.
- The contract-relevant timestamp of April 19, 2026 12:00 ET converts to 2026-04-19 16:00:00 UTC.

## Evidence directly stated by source

- Binance spot API directly reported the current price and historical kline OHLC values.
- The one-minute kline endpoint demonstrates the contract can in principle be checked directly against Binance minute-close data.

## What is uncertain

- This source does not predict where SOL will trade on April 19 at noon ET.
- Exchange spot data alone does not explain what catalysts or market-wide shocks could move SOL below 80 before settlement.
- We do not yet have the actual April 19 12:00 ET candle because the market has not resolved.

## Why this source may matter

This is the governing exchange data environment for the contract. Because the market resolves specifically on a Binance 1-minute close, direct Binance price context is more important than broader crypto commentary.

## Possible impact on the question

The data supports a base case that Yes is favored because current trading is about 6% above the threshold and recent price action has often held above 80. But the relatively narrow buffer versus recent intramonth low 76.70 means a sharp weekend drawdown remains the main realistic path to No.

## Reliability notes

Binance is both the named resolution source and a direct market-data source, so relevance is very high. Independence is limited because both current context and final settlement depend on the same venue, but for this contract that is appropriate rather than a flaw.