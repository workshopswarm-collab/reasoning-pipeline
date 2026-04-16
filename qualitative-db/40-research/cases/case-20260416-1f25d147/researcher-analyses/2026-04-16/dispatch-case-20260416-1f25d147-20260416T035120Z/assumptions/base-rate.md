---
type: assumption_note
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
research_run_id: 5afb3e7a-47ad-4114-8b44-4ea2c2320c67
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: multi-day
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-analyses/2026-04-16/dispatch-case-20260416-1f25d147-20260416T035120Z/personas/base-rate.md"]
tags: ["assumption-note", "threshold", "volatility"]
---

# Assumption

The base-rate case assumes SOL remains in roughly the same trading regime over the next three days and does not suffer a sharp enough drawdown to print a noon-ET Binance 1-minute close below 80 on April 19.

## Why this assumption matters

The forecast is not about long-run value; it is about a narrow threshold over a short horizon. A small regime break or sudden volatility event would dominate the otherwise strong outside-view prior.

## What this assumption supports

- A high-probability Yes view.
- A modest discount versus the raw historical frequency because single-minute settlement introduces path sensitivity.
- Treating recent price persistence above 80 as informative rather than incidental.

## Evidence or logic behind the assumption

- Current Binance SOL/USDT price is about 85.23-85.24, leaving a cushion of roughly 6.5% above the threshold.
- Daily closes have been above 80 on 171 of the last 180 sessions and on all of the last 14 sessions in the retrieved sample.
- Conditional persistence has been strong: when SOL is already above 80, the next 3 days also stayed above 80 about 93% of the time in the sampled window.

## What would falsify it

- A broad crypto selloff or SOL-specific shock that pushes Binance SOL/USDT below 80 before settlement.
- A visible erosion of the price cushion into the low-80s, especially if accompanied by rising intraday volatility.
- Exchange-specific trading disruption or unusual price dislocation on Binance around the settlement window.

## Early warning signs

- SOL trading repeatedly below 82 before April 19.
- Bitcoin or large-cap crypto weakness severe enough to drag high-beta alts lower.
- Expanding intraday swings on Binance SOL/USDT.

## What changes if this assumption fails

The base-rate estimate should fall quickly because the contract is decided by one narrow minute. If SOL approaches 80 closely before settlement, the market should be treated less like a persistence question and more like a short-horizon volatility question.

## Notes that depend on this assumption

- Main base-rate finding for this dispatch.
