---
type: assumption_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: 0df82309-bacf-4ad5-81c2-4aabba0201f4
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: market-structure
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-100-on-april-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: reliability
date_created: 2026-04-09
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/base-rate.md"]
tags: ["assumption", "binance", "timing", "price-threshold"]
---

# Assumption

ETH will remain in the same broad price regime through the April 10 noon ET settlement minute, so a roughly $113 cushion over the $2,100 threshold is more likely than not to survive the next day.

## Why this assumption matters

The base-rate view is mostly an outside-view stability call rather than a catalyst-specific call. If regime stability fails, the current margin over the threshold may not matter.

## What this assumption supports

- A probability materially above 50% and above naive unconditional historical frequency.
- A view that the market's high Yes pricing is directionally justified, though perhaps a bit too confident.
- Reliance on recent spot level and short-horizon persistence as the main mechanism.

## Evidence or logic behind the assumption

- Current Binance ETHUSDT spot was about 2213, already well above 2100.
- Over the last 120 daily Binance candles fetched in-run, the next day also closed above 2100 in about 91.8% of cases when the prior day was already above 2100.
- The market resolves on a single minute close less than a day away, which reduces the window for structural regime change versus a longer-dated market.

## What would falsify it

- A sharp crypto selloff that pushes ETH below 2100 before the noon ET settlement minute.
- Material ETH-specific adverse news that breaks the recent price regime.
- Evidence that the relevant settlement minute or timezone interpretation differs from the assumed ET-to-UTC conversion.

## Early warning signs

- ETH losing the 2200 area and trading persistently near or below 2150 before settlement.
- Broad crypto weakness or risk-off move in BTC and majors during the overnight / morning window.
- Conflicting documentation showing the contract uses a different minute boundary than assumed.

## What changes if this assumption fails

The thesis would drop from a high-probability Yes view toward a more balanced or even No-leaning view depending on how far and how quickly ETH falls below the threshold.

## Notes that depend on this assumption

- Main finding at `qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/base-rate.md`.