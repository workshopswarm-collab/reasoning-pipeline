---
type: assumption_note
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
research_run_id: ad2bb4ac-0447-46ca-a5d6-744310cbccc2
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-18
question: "Will the price of Bitcoin be above $70,000 on April 18?"
driver: reliability
date_created: 2026-04-14
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-18 noon ET"
related_entities: ["bitcoin"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/base-rate.md"]
tags: ["assumption", "volatility", "threshold-market"]
---

# Assumption

Bitcoin remains in roughly the same broad trading regime through April 18 noon ET, without a new shock large enough to push BTC/USDT decisively back below 70,000 at the resolving minute.

## Why this assumption matters

The base-rate case for "Yes" relies on BTC already trading materially above 70k and on short-horizon continuation being more likely than a multi-thousand-dollar reversal within four days.

## What this assumption supports

- A probability estimate above 50%
- Treating current spot level as meaningful evidence rather than noise
- Leaning Yes while still discounting the market's extreme confidence

## Evidence or logic behind the assumption

Current Binance spot is around 74.2k, and recent daily closes show BTC spending a substantial share of recent time above 70k. That makes a stable-regime continuation view more natural than assuming an abrupt breakdown with no specific catalyst identified.

## What would falsify it

- A sharp macro or crypto-specific selloff before April 18
- BTC losing the low-70k area and failing to recover before the resolving minute
- New exchange, regulatory, or liquidation stress that changes the short-horizon regime

## Early warning signs

- Consecutive daily closes back below 70k
- Fast deterioration from mid-74k toward 71k or lower
- Large weekend volatility or liquidation cascades

## What changes if this assumption fails

The probability of Yes would fall quickly, because the contract is a single timestamp and does not reward earlier trading above the threshold.

## Notes that depend on this assumption

- Main base-rate finding for this run