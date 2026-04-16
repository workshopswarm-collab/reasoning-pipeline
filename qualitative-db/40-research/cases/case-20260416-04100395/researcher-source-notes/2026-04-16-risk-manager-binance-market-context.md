---
type: source_note
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: price-markets
entity: ethereum
topic: case-20260416-04100395 | risk-manager
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2300?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance ETHUSDT API + market rule reference
source_type: exchange_api_and_resolution_rule
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/risk-manager.md]
tags: [binance, resolution-source, ethusdt, 1m-candle]
---

# Summary

This source bundle establishes both the governing settlement mechanic and the closest direct market context available during the run. Polymarket’s rule text says resolution depends specifically on the Binance ETH/USDT 1-minute candle labeled 12:00 ET on 2026-04-17, with the final close price needing to be strictly higher than 2300. Binance spot data fetched during this run showed ETH/USDT around 2333.19, with the latest 1-minute candles clustering roughly 2333-2343.

## Key facts extracted

- Governing rule: resolve Yes only if the Binance ETH/USDT 1-minute candle for 12:00 ET on 2026-04-17 has a final close price higher than 2300.
- The contract is exchange-specific and pair-specific: Binance spot ETH/USDT, not other exchanges or ETH/USD proxies.
- Precision is whatever Binance displays in the source.
- Binance API at fetch time returned ETHUSDT price 2333.19000000.
- Recent Binance 1-minute candles fetched during the run showed closes of 2338.58, 2338.86, 2336.24, 2333.69, and 2335.17, indicating spot trading was modestly above the threshold at time of research.

## Evidence directly stated by source

- Polymarket rules directly define the winning condition and source of truth.
- Binance API directly reports current ETHUSDT spot price and recent 1-minute kline closes.

## What is uncertain

- These fetched Binance prices are from 2026-04-16, not the settlement minute on 2026-04-17 at 12:00 ET.
- API data here does not itself prove what the exact noon-ET candle tomorrow will be.
- It remains possible that market volatility or exchange-specific moves push the final settlement candle below 2300 even if ETH is above 2300 during this run.

## Why this source may matter

It anchors both the contract interpretation and the operational risk lens. Because resolution depends on one specific exchange’s one-minute close at one precise time, modest path volatility, minute-level timing, or exchange-specific prints can matter more than broad ETH directional sentiment.

## Possible impact on the question

This source supports a base case that Yes is currently favored because spot is already above 2300, but it also highlights why confidence should not be too high: the contract requires all of the following to hold simultaneously at resolution time — Binance spot ETH/USDT must remain above 2300, the relevant minute must be the 12:00 ET candle, and the final close must be strictly above the threshold.

## Reliability notes

- Polymarket rule text is the governing contract source for interpretation.
- Binance is the explicit source of truth for settlement, so exchange data quality is highly relevant.
- Independence is limited because the current-price evidence and settlement source come from the same exchange family; contextual cross-checks are still useful for broader market state.