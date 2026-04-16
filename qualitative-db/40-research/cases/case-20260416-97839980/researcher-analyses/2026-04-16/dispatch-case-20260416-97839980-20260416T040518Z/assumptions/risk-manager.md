---
type: assumption_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
research_run_id: 3a7e2827-18f7-4f75-9a5f-9b536335e7b1
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-price-resolution
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?"
driver: operational-risk
date_created: 2026-04-16
agent: risk-manager
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-19 noon ET"
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/risk-manager.md", "qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/evidence/risk-manager.md"]
tags: ["assumption", "timing-risk", "spot-price"]
---

# Assumption

SOL can remain above the $80 strike on Binance spot through the specific settlement minute on April 19 rather than merely trading above it days earlier.

## Why this assumption matters

The bullish directional case is already mostly in the price: SOL is above 80 now. The remaining uncertainty is not whether SOL can ever print above 80, but whether it stays above 80 at the exact one-minute close that resolves the contract.

## What this assumption supports

- A Yes probability materially above 50%
- A view that current spot cushion is meaningful rather than illusory
- A judgment that market confidence near 92% is slightly too high but directionally sensible

## Evidence or logic behind the assumption

- Binance spot currently shows SOL at 85.39, about $5.39 above strike.
- Recent Binance daily closes and hourly candles show repeated acceptance above 80 rather than a single transient spike.
- Because the market only needs a close above 80, not above a higher threshold, current state gives some buffer against ordinary noise.

## What would falsify it

- A broad crypto selloff that pushes Binance SOL/USDT back under 80 before or at settlement.
- A SOL-specific negative catalyst, exchange-specific dislocation, or liquidity shock that causes the 12:00 ET minute close to print 80.00 or lower.
- Evidence that Binance spot begins trading materially weaker than other major venues heading into settlement.

## Early warning signs

- SOL loses the low-80s support area and starts closing hourly candles below 83, then below 80.
- BTC/ETH risk-off move drags majors lower into the weekend.
- Increased intraday wickiness near 80 on Binance spot specifically.

## What changes if this assumption fails

If this assumption weakens, the main thesis shifts from "Yes with moderate cushion" to "the contract is a pure timing coin flip with elevated path risk," and the fair probability would move sharply down toward market-neutral or below.

## Notes that depend on this assumption

- Main finding: risk-manager.md
- Evidence map: evidence/risk-manager.md