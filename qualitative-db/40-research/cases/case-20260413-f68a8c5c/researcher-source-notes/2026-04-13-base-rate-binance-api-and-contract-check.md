---
type: source_note
case_key: case-20260413-f68a8c5c
dispatch_id: dispatch-case-20260413-f68a8c5c-20260413T165914Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-14
question: Will the Binance BTC/USDT 1-minute candle for 2026-04-14 12:00 ET close above 68000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance spot market API and Polymarket market rules page
source_type: primary_and_resolution_context
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, resolution-check, timezone-check]
---

# Summary

This note captures the direct contract-mechanics and current-price verification for the April 14 BTC above 68k market.

## Key facts extracted

- Polymarket rules state the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 14 has a final close strictly higher than 68,000.
- The governing source of truth is Binance BTC/USDT, not another exchange or pair.
- 2026-04-14 12:00 ET maps to 2026-04-14 16:00 UTC, so the relevant Binance 1-minute candle is the candle opening at 16:00:00 UTC.
- A direct Binance API check on 2026-04-13 around 13:00 ET showed BTC/USDT trading around 72.16k to 72.19k.
- Binance 24h ticker at the same check showed lastPrice about 72,187, weightedAvgPrice about 71,303, high about 72,464, low about 70,506, and 24h change about +1.75%.

## Evidence directly stated by source

- The Polymarket rules page directly states the settlement condition and source-of-truth surface.
- Binance API directly states current BTC/USDT prices and timestamps.

## What is uncertain

- The market does not settle from the API directly; it settles from the Binance trading interface candle currently available on the site, though this should correspond to the same underlying market data.
- A live exchange outage, interface discrepancy, or abnormal intraday move before 2026-04-14 12:00 ET could still change the result.

## Why this source may matter

This is the primary verification set for both the contract mechanics and the current distance from the 68,000 threshold.

## Possible impact on the question

Because BTC was already trading more than 6% above the threshold less than 24 hours before resolution, the direct-source setup strongly favors Yes absent a sharp selloff or settlement-surface problem.

## Reliability notes

- Binance API is a high-credibility direct market-data source for current BTC/USDT levels.
- Polymarket rules page is the relevant contextual source for what counts for resolution.
- Independence is only medium because both are tied to the same market ecosystem, but they answer different questions: settlement mechanics vs current price level.
