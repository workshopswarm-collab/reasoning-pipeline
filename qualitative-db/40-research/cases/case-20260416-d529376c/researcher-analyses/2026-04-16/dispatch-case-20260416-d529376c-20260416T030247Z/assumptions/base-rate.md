---
type: assumption_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
research_run_id: 67ab0b3e-739e-41d0-a60a-16d6588377ff
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-19 12:00 ET"
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/base-rate.md"]
tags: ["threshold-market", "price-level", "assumption"]
---

# Assumption

The recent Binance SOL/USDT regime around the low-to-mid 80s remains broadly intact through the Apr 19 noon ET settlement window, without a sharp downside break below $80.

## Why this assumption matters

The base-rate case depends more on persistence of the recent price regime than on a new bullish catalyst. If the regime holds, a noon print above $80 is a modestly favorable default; if it breaks, the contract likely resolves No.

## What this assumption supports

- A probability estimate above 50% for Yes.
- Treating recent venue-specific price distribution as a meaningful outside-view prior.
- Interpreting the market’s 91.5% implied probability as too aggressive rather than directionally wrong.

## Evidence or logic behind the assumption

- Recent Binance daily closes were above $80 on most completed days in the April 1-15 sample.
- The spot level at retrieval was still in the mid-80s, leaving some cushion over the threshold.
- Short-horizon crypto prices often mean-revert within recent ranges absent a material new shock, but they can also gap suddenly.

## What would falsify it

- A sustained move back below $80 before Apr 19.
- A broader crypto risk-off shock that drags SOL decisively beneath the threshold.
- Venue-specific disruption on Binance that creates abnormal pricing or resolution friction around the settlement minute.

## Early warning signs

- SOL losing the low-80s support zone on Binance.
- BTC/ETH-wide risk-off move accompanied by SOL underperformance.
- Elevated exchange-specific volatility or execution issues near the settlement window.

## What changes if this assumption fails

The probability should move sharply toward No, because this contract is a single-minute threshold test rather than an average-price condition. Losing the price cushion matters disproportionately.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/base-rate.md