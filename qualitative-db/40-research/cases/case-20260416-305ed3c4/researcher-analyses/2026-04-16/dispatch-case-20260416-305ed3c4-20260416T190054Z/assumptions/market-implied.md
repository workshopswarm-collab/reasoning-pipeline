---
type: assumption_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
research_run_id: 19e691be-89c6-4aca-a941-a51c15bcecb3
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: will-the-binance-eth-usdt-12-00-et-1-minute-candle-on-2026-04-17-close-above-2200
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2200?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance exchange"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/market-implied.md"]
tags: ["assumption-note", "ethusdt", "binance", "market-implied"]
---

# Assumption

ETH will not fall more than roughly 6% from the observed Binance spot level before the specific Apr 17 12:00 ET 1-minute close used for settlement.

## Why this assumption matters

The bullish case is not that ETH is barely above the strike now; it is that the current cushion above 2200 is large enough that only a meaningful short-horizon downside move would flip the outcome.

## What this assumption supports

- A probability estimate close to but below the market-implied 97.5%
- The interpretation that the market is mostly efficient rather than stale or overextended
- A view that contract timing and venue mechanics matter more than broad directional crypto thesis over this horizon

## Evidence or logic behind the assumption

- Binance spot was approximately 2343.56 at time of check, about 143.56 above the strike.
- Recent 1-minute closes were tightly clustered around 2343 rather than showing immediate disorder.
- The remaining time to settlement is less than one day, limiting the window for a large adverse move, though it does not remove that risk.

## What would falsify it

- A sharp overnight or morning selloff that takes Binance ETH/USDT below 2200 near the noon ET candle
- Exchange-specific disruption, unusual wick behavior, or venue divergence at the exact resolution minute
- New macro or crypto-specific shock causing a rapid multi-percent decline before settlement

## Early warning signs

- ETH losing the 2300 area quickly with momentum
- Elevated realized intraday volatility into the U.S. morning
- Abnormal Binance-specific prints or operational disruptions

## What changes if this assumption fails

The current pro-Yes view would compress fast because this is a single-minute threshold market; once the spot cushion materially erodes, the extreme confidence implied by the market would look less justified.

## Notes that depend on this assumption

- Main finding for market-implied persona
- Evidence map for this dispatch