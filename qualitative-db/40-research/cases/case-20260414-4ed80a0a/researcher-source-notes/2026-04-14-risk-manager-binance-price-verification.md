---
type: source_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260414-4ed80a0a | risk-manager
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-14
source_name: Binance ETHUSDT market data verification
source_type: exchange market data / direct verification
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/risk-manager.md]
tags: [binance, verification, eth, market-data]
---

# Summary

Direct verification note using Binance ETH/USDT market data, the same venue Polymarket names in its rules.

## Key facts extracted

- Binance 24hr ticker at check time showed `highPrice: 2415.50000000` and `lastPrice: 2330.74000000`.
- Paginated Binance 1-minute klines from Apr 13 2026 00:00 ET through Apr 14 2026 ~13:42 ET returned 2,264 one-minute candles.
- The maximum observed 1-minute candle high in that checked window was `2415.5`.
- The maximum occurred in the candle opening at `2026-04-14T10:32:00-04:00` (New York time).
- Because `2415.5 >= 2400`, the market condition for `Yes` appears already satisfied under the stated Polymarket rule, subject only to normal data integrity / settlement mechanics.

## Evidence directly stated by source

- Direct market data from Binance API endpoints.
- The verified high exceeds the contract threshold by `15.5` dollars, so this is not a razor-thin edge near the trigger.

## What is uncertain

- API output is an access path to Binance data, not the exact chart UI named by Polymarket; however it is the same venue/pair and consistent with the contract logic.
- I did not independently archive a chart screenshot from the Binance UI itself.

## Why this source may matter

This is the decisive direct-evidence source for whether the trigger condition has already happened. It materially reduces the chance that the market is just overconfident without evidence.

## Possible impact on the question

If Binance market data is accepted as normal, this source effectively settles the directional question to near-certainty because a qualifying high has already printed within the qualifying date range.

## Reliability notes

High reliability as direct exchange data and strongly aligned with the contract’s named venue. The remaining residual risk is operational/settlement-path risk rather than directional price risk.