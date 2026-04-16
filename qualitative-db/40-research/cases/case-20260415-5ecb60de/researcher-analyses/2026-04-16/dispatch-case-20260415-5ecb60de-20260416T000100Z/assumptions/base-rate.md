---
type: assumption_note
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
research_run_id: db877a35-6693-42a2-b221-258519522004
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: will-the-binance-sol-usdt-1-minute-candle-close-at-12-00-et-on-2026-04-19-be-higher-than-80
question: "Will the Binance SOL/USDT 1-minute candle close at 12:00 ET on 2026-04-19 be higher than 80?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: medium
time_horizon: days
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/base-rate.md"]
tags: ["assumption", "binance", "threshold"]
---

# Assumption

The base-rate estimate assumes there is no new market-wide crypto shock or Binance-specific disruption large enough to push SOL/USDT below 80 by the April 19 noon ET settlement minute.

## Why this assumption matters

The current outside view is driven mainly by SOL already trading above the threshold and by recent frequency data showing closes usually remaining above 80. A large shock would break that outside-view anchor quickly.

## What this assumption supports

- A Yes-leaning probability estimate above 50%
- A view that the market is directionally right but somewhat overconfident at 90%
- A conclusion that ordinary volatility is less likely than not to be enough for a sub-80 noon print

## Evidence or logic behind the assumption

- Current Binance spot during the run was about 84.9.
- Recent daily closes were above 80 on 28 of the prior 29 completed days.
- The threshold is about 5.7% below current spot, which is reachable but not the modal short-horizon outcome given the recent sample.

## What would falsify it

- A broad crypto selloff that pushes SOL materially lower before April 19
- Binance-specific trading disruption, bad data, or venue-specific dislocation near the settlement minute
- A sustained move back into the high-70s before settlement

## Early warning signs

- SOL loses the 82-83 area and stays there
- BTC/ETH risk sentiment breaks sharply lower
- Binance order-book or candle integrity issues appear near noon ET windows

## What changes if this assumption fails

The probability should move down materially, and the market may deserve its current extreme confidence in No only if SOL is already trading near or below 80 close to settlement.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/base-rate.md