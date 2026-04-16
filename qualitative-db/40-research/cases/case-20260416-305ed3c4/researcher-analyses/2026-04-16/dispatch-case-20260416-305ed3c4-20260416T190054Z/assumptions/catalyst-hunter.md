---
type: assumption_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
research_run_id: 6623071e-5bcd-4364-8607-47e94578db40
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: exchange-market-data
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: "Will the price of Ethereum be above $2,200 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: catalyst-hunter
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: ["ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["catalyst-hunter.md"]
tags: ["assumption-note", "catalyst-timing", "binance"]
---

# Assumption

No scheduled or surprise catalyst before the Apr. 17 12:00 ET Binance close will produce a fast enough ETH selloff to push ETH/USDT from the current low-2300s down through 2200.

## Why this assumption matters

The thesis is not that ETH is structurally bullish in general; it is that the remaining time window is short and the market only needs ETH to stay above a relatively distant threshold at one exact minute.

## What this assumption supports

- A high-probability Yes view.
- A view that the current 97.5% market price is roughly fair to slightly conservative.
- A decision to stop research after rule verification plus direct Binance price verification rather than searching for lower-information narrative catalysts.

## Evidence or logic behind the assumption

- Direct Binance data shows ETH materially above 2200 with recent 1-minute closes around 2321-2344.
- The 24h Binance low was still above 2200.
- There is no identified scheduled event in the remaining window with obvious enough information value to explain an immediate >5% downside shock on its own.

## What would falsify it

- A sharp risk-off macro event, crypto-specific headline, exchange incident, or liquidation cascade that pushes Binance ETH/USDT below 2200 before the noon ET candle closes.
- Evidence that the relevant Binance candle/timezone mapping is different from the interpreted noon ET window.

## Early warning signs

- ETH breaks below the recent 24h low near 2285 on Binance.
- Broad crypto market liquidation accelerates overnight into U.S. morning trading.
- A Binance-specific outage, data issue, or market-structure disruption emerges near the resolution window.

## What changes if this assumption fails

The high-probability Yes view would need to be cut quickly, with contract-mechanics verification taking priority over broader narrative analysis.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/catalyst-hunter.md