---
type: assumption_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: f0a4e7fb-4b0c-4950-b281-fe2a4d6335ef
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-market
entity: bitcoin
topic: "short-horizon stability assumption for BTC staying above 70,000 into the governing minute"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 20 close above 70,000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["binance", "bitcoin"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/base-rate.md"]
tags: ["assumption-note", "btc", "threshold-market", "short-horizon"]
---

# Assumption

BTC can absorb normal short-horizon volatility over the next five days without falling below 70,000 at the exact governing Binance noon ET minute on April 20.

## Why this assumption matters

The base-rate view is mostly a distance-to-threshold and short-horizon persistence judgment. If the current cushion is not durable, the Yes probability should fall materially.

## What this assumption supports

- A Yes probability above the raw market-neutral baseline.
- A view that current prices in the mid-74k area make 70k more likely than not to hold at the governing minute.
- A conclusion that the market is directionally right but slightly aggressive.

## Evidence or logic behind the assumption

- Current Binance spot is roughly 6.5% above the threshold.
- Independent spot checks from CoinGecko and Coinbase broadly agree with Binance on the current price region.
- For a five-day horizon, a several-thousand-dollar cushion is meaningful, though not overwhelming, for BTC.

## What would falsify it

- A sharp risk-off move that pushes BTC back near or below 70k before April 20.
- Exchange-specific dislocation on Binance BTC/USDT that is worse than broader market pricing.
- Evidence of regime instability that makes a 6.5% cushion much less protective than usual.

## Early warning signs

- Repeated closes back near 71k-72k.
- Binance underperforming Coinbase/aggregate USD venues.
- Major macro or crypto-specific shock before the event window.

## What changes if this assumption fails

The case shifts from “likely Yes with moderate cushion” to a much closer coin-flip or No-lean setup because the contract is about one exact minute close, not average price over the week.

## Notes that depend on this assumption

- The base-rate main finding for this dispatch.
- Any synthesis that treats current distance from threshold as the dominant structural input.