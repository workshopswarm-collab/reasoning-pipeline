---
type: source_note
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-structure
entity:
topic: Binance ETH/USDT resolution mechanics and current spot level
question: Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-17 close above 2300?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance Spot API and market page description
source_type: primary
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=20
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cc34f737/researcher-analyses/2026-04-16/dispatch-case-20260416-cc34f737-20260416T162722Z/personas/catalyst-hunter.md]
tags: [binance, ethusdt, resolution-source, one-minute-candle]
---

# Summary

Binance is the governing source of truth for this contract, and Binance Spot API output confirms ETHUSDT is actively trading with 1-minute klines and a price filter tick size of 0.01. The most recent sampled 1-minute candles on 2026-04-16 around 16:22-16:31 UTC closed between 2332.08 and 2337.20, meaning ETH/USDT was already modestly above the 2300 threshold roughly 19.5 hours before the noon ET resolution print.

## Key facts extracted

- `exchangeInfo` for `ETHUSDT` shows symbol status `TRADING` on Binance spot.
- Binance spot API provides `1m` kline data for `ETHUSDT`, matching the contract’s stated resolution surface.
- Current sampled closes near research time were all above 2300: e.g. 2337.20, 2334.68, 2334.71, 2336.04, 2334.20, 2334.91, 2335.02, 2332.08, 2333.35, 2332.73.
- Tick size in exchange metadata is `0.01000000`, so a close above 2300.00 resolves Yes; 2300.00 or below does not.
- The Polymarket market page metadata showed next update/resolution time `2026-04-17T16:00:00.000Z`, which matches 12:00 ET.

## Evidence directly stated by source

- Binance API directly states the symbol exists and is trading.
- Binance API directly states minute-by-minute open/high/low/close values.
- Exchange metadata directly states the quote precision / tick size used by the market source.

## What is uncertain

- This source does not tell us where ETH/USDT will trade at the actual resolving minute on 2026-04-17.
- It does not independently confirm whether Binance’s website UI and API could diverge at settlement, though the API strongly suggests the same underlying market data.

## Why this source may matter

This is the primary resolution-relevant source. It anchors both the contract interpretation and the immediate starting level relative to 2300.

## Possible impact on the question

Because ETH/USDT is already above 2300 with a buffer of roughly $32-$37, the market only needs ETH to avoid a moderate downward move by noon ET tomorrow. The key remaining risk is not source ambiguity but short-horizon price volatility or an exchange-specific dislocation.

## Reliability notes

High reliability for contract mechanics and current traded level. Independence is limited because the market explicitly settles to Binance, but that is appropriate rather than problematic here.