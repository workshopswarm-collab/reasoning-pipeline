---
type: source_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
analysis_date: 2026-04-06
persona: risk-manager
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260406-574ca6af | risk-manager
question: Will Ethereum reach $2,200 March 30-April 5?
driver: price path within resolution window
date_created: 2026-04-06T01:36:30Z
source_name: Binance ETHUSDT 1m klines API
source_type: exchange market data
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum, binance]
related_drivers: [price path, threshold reach]
upstream_inputs: [polymarket contract]
downstream_uses: [risk-manager finding, evidence map]
tags: [binance, ethusdt, 1m, threshold-check, cex]
---

# Summary

Queried Binance 1-minute ETH/USDT kline data across the full market window. The observed maximum 1-minute candle high in the specified ET window was below the 2200 threshold.

## Key facts extracted

- Checked Binance ETH/USDT 1m klines from **2026-03-30 00:00 ET** through **2026-04-05 23:59:59 ET**.
- Maximum observed 1-minute candle high in that window: **2167.85**.
- Corresponding max candle open time: **1775062980000 ms** Unix epoch.
- Since **2167.85 < 2200**, the designated source appears not to have reached the threshold.

## Evidence directly stated by source

The Binance API directly returns 1-minute candles including open, high, low, close. The highest returned high over the queried window was 2167.85.

## What is uncertain

- This check relies on the public API matching the chart data used in the contract; usually that is a strong assumption but still an assumption.
- I did not independently reconcile the single max candle against the GUI chart screenshot-by-screenshot; this was an API-level verification pass.

## Why this source may matter

This is effectively the direct empirical check against the contract-defined settlement source.

## Possible impact on the question

If the API and contract-designated Binance 1m chart are consistent, then the market should resolve **No** because the threshold was not hit.

## Reliability notes

High relevance and high credibility as a direct Binance endpoint, though still slightly below the exact contractual surface because the contract references the Binance chart UI. Practical source-of-truth ambiguity remains low because the API and chart are normally derived from the same exchange data.