---
type: assumption_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
research_run_id: 27948bd5-60af-48f1-a914-06657c345a9c
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-market-microstructure
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: "Will the price of Ethereum be above $2,200 on April 17?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
status: active
certainty: medium-high
importance: high
time_horizon: "<24h"
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["market-implied-finding", "evidence-map"]
tags: ["assumption", "market-anchor", "short-horizon"]
---

# Assumption

The market's ~94.5% Yes price is mainly assuming that ETH can absorb ordinary overnight volatility and still print a Binance ETH/USDT 12:00 ET one-minute close above 2200 on April 17.

## Why this assumption matters

The gap between current Binance spot (~2353) and the threshold (2200) is large enough that the question is mostly about tail-risk over the next roughly 14.5 hours, not about fine valuation.

## What this assumption supports

- A high-Yes base case.
- A view that the market is broadly efficient rather than stale.
- A conclusion that only a relatively sharp downside move or exchange-specific anomaly is likely to flip the result.

## Evidence or logic behind the assumption

- Direct Binance price checks place ETH more than 6% above the threshold.
- The fetched Binance 24h low was still above 2200.
- The neighboring Polymarket strike ladder (2200 ~95%, 2300 ~71%, 2400 ~30%) looks internally coherent with spot in the low-to-mid 2300s.

## What would falsify it

- ETH trades down through 2200 before noon ET and remains there into the settlement minute.
- Binance-specific dislocation causes ETH/USDT on Binance to underperform broader ETH references.
- Contract interpretation around the exact 12:00 ET candle differs from the assumed minute-close mechanics.

## Early warning signs

- Rapid overnight crypto selloff of several percentage points.
- Binance ETH/USDT diverging negatively from other major ETH spot references.
- Unusual exchange operational issues near settlement.

## What changes if this assumption fails

The market would look materially overconfident, and the correct posture would shift from 'roughly agree with a slight underweight' to a more skeptical view of crowd pricing and venue-specific execution risk.

## Notes that depend on this assumption

- Main finding at the assigned persona path.
- Evidence map for market-vs-tail-risk netting.