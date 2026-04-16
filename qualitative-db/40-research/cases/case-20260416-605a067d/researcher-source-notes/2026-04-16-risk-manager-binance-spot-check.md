---
type: source_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: daily-threshold-close
entity: ethereum
topic: Binance ETH/USDT spot and recent range ahead of April 17 noon ET close check
question: Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 close above 2200?
driver: reliability
date_created: 2026-04-16
source_name: Binance public market data API spot check
source_type: exchange market data / governing-source-adjacent
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/risk-manager.md
tags: [source-note, binance, ethusdt, market-data, verification]
---

# Summary

A direct Binance API spot check on April 16 showed ETH/USDT trading near **2298-2299**, with 24-hour high **2385.61** and low **2285.10**. That means the market is currently above the 2200 threshold by roughly 4.5%, but the contract still depends on the specific April 17 **12:00 ET** one-minute close, so an overnight drawdown remains the main path risk.

## Key facts extracted

- Binance ticker endpoint returned ETH/USDT spot around **2298.16-2298.49** at check time.
- Binance 24-hour stats showed:
  - **openPrice:** 2340.10
  - **lastPrice:** 2298.49
  - **highPrice:** 2385.61
  - **lowPrice:** 2285.10
- Recent 1-minute klines around the check showed ETH/USDT closing in the **2289-2299** range.
- A direct query for the future target timestamp corresponding to **2026-04-17 12:00 ET = 2026-04-17 16:00 UTC** returned an empty array, confirming the event had **not yet been verified** at the governing timestamp rather than already being observed negative.

## Evidence directly stated by source

Observed Binance API outputs at run time:
- `ticker/price`: `{"symbol":"ETHUSDT","price":"2298.16000000"}`
- `ticker/24hr`: included `"lastPrice":"2298.49000000"`, `"highPrice":"2385.61000000"`, `"lowPrice":"2285.10000000"`
- future-candle kline request for the exact target minute returned `[]`

## What is uncertain

- Spot and trailing 24-hour range do not guarantee the April 17 noon ET one-minute close.
- API endpoints are highly relevant but the rules cite the Binance chart interface; practical risk of mismatch is low but nonzero.
- Crypto remains volatile enough that a ~4.5% cushion one day ahead is helpful but not dispositive.

## Why this source may matter

This is the most relevant direct market-state evidence available before resolution because it comes from Binance ETH/USDT itself, the same exchange and pair named by the contract.

## Possible impact on the question

Current levels support a high Yes probability because ETH would need to fall materially below the current price and still be below 2200 specifically at noon ET tomorrow. The main downside scenario is not that ETH is currently weak; it is that crypto volatility plus timing-specific noon settlement can erase the cushion before the exact minute that counts.

## Reliability notes

- High recency and high exchange relevance.
- Medium certainty for final contract inference because this is pre-resolution evidence, not the actual target-minute close.
- Good independence from the Polymarket rules page on market-state facts, though still linked through the same underlying exchange.