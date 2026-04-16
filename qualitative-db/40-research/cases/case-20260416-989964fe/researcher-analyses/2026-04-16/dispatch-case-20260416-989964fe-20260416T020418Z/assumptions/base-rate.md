---
type: assumption_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
research_run_id: 5cae2cce-4164-48b7-94a8-799a5e7e95b2
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-market
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-200-on-april-17
question: "Will the price of Ethereum be above $2,200 on April 17?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: short-term
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/base-rate.md"]
tags: ["assumption", "settlement-venue", "short-horizon"]
---

# Assumption

ETH/USDT on Binance will remain in roughly the recent trading regime through noon ET on April 17, without a shock large enough to push the final 12:00 PM ET one-minute close below 2200.

## Why this assumption matters

The high-Yes view is not based on a guarantee; it depends on short-horizon price continuity from a current level around the mid-2300s to the relevant settlement minute.

## What this assumption supports

- A probability estimate somewhat below but still close to the market's 95% implied level.
- The interpretation that the main risk is short-term volatility or venue-specific dislocation rather than a structural bearish base case.

## Evidence or logic behind the assumption

- Current Binance ETHUSDT spot and recent 1m prints are well above 2200.
- Nearby daily closes are mostly above 2200.
- For the market to fail from current levels, ETH would need a drop of roughly 6-7% by the settlement minute on the named venue.

## What would falsify it

- A sharp crypto-wide selloff before noon ET on April 17.
- Binance-specific price dislocation, outage, or bad print affecting the final settlement candle.
- Macro or crypto news that materially reprices ETH lower overnight or during the morning.

## Early warning signs

- ETHUSDT trading back toward the low-2200s or below on Binance before the settlement window.
- Rising realized intraday volatility with repeated tests of 2200.
- Exchange-specific operational issues or obvious divergence between Binance and other major venues.

## What changes if this assumption fails

The high-Yes probability would compress quickly, and the market could become close to a toss-up or even No-favored if ETH trades near the strike into the final hour.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/base-rate.md