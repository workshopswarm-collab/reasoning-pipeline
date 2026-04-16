---
type: evidence_map
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
research_run_id: fff189ab-e754-4a2c-b08d-e89b4163d7fa
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: ethereum
topic: will-the-binance-eth-usdt-1-minute-candle-for-12-00-pm-et-on-2026-04-17-close-above-2200
question: "Will the Binance ETH/USDT 1-minute candle for 12:00 PM ET on 2026-04-17 close above 2200?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/risk-manager.md"]
tags: ["evidence-map", "threshold-market", "intraday-risk", "binance"]
---

# Summary

The evidence still leans yes, but the key risk-manager adjustment is not directional ETH bearishness; it is discounting extreme confidence because this is a single-minute, exchange-specific, time-specific threshold contract.

## Question being evaluated

Will Binance ETH/USDT close above 2200 on the 12:00 PM ET 1-minute candle on April 17, 2026?

## Current lean

Lean yes, but less confidently than the 95% market price implies.

## Prior / starting view

Starting view: likely yes because current price is already above threshold and the horizon is short.

## Evidence supporting the claim

- Polymarket rules specify the exact source and condition; there is no hidden multi-source settlement ambiguity. Weight: high. Direct contract evidence.
- Same-session Binance public API context check shows ETHUSDT around 2356, leaving a cushion of about 156 points above 2200. Weight: high. Direct venue-matched contextual evidence.
- Time to resolution is short, reducing the number of distinct macro windows that can break the thesis. Weight: medium. Indirect contextual evidence.

## Evidence against the claim

- The contract resolves on one exact 1-minute close, not a daily average or broad directional move. That makes path and timing risk more important than the raw cushion alone suggests. Weight: high. Direct contract-interpretation risk.
- Extreme market pricing at 95% can overstate certainty when evidence independence is limited and when a single sharp crypto drawdown can traverse the threshold quickly. Weight: medium. Interpretive risk.
- Current contextual evidence comes primarily from Binance itself, so a venue-specific dislocation or data-surface issue is not independently stress-tested here. Weight: medium. Source-independence risk.

## Ambiguous or mixed evidence

- Current spot being well above threshold is supportive, but crypto can move several percent quickly; the same fact supports yes while also inviting complacency.
- Inability to fetch some third-party context pages due anti-bot protections did not negate the thesis, but it reduced independent confirmation quality.

## Conflict between inputs

No major factual conflict. The main conflict is between a straightforward high-probability directional read and a risk-manager insistence on haircutting confidence because the contract is narrow and exact.

## Key assumptions

- Noon ET is correctly interpreted as 16:00 UTC on April 17, 2026.
- Binance public API pricing is a reasonable context proxy for what the settlement source will show, even though the formal source of truth is the Binance trading interface/candle data at the exact time.
- No large adverse move or exchange-specific dislocation occurs before the resolving candle.

## Key uncertainties

- Overnight and morning crypto volatility.
- Whether exchange-specific data presentation or microstructure quirks matter at the exact resolving minute.
- Lack of stronger independent contextual confirmation from third-party market-data pages in this run.

## Disconfirming signals to watch

- ETH falls below 2300 well ahead of the resolution window.
- Elevated volatility into U.S. morning trading.
- Binance-specific irregularities or unusual divergence from other venues.

## What would increase confidence

- A fresh Binance check closer to resolution still showing a large cushion above 2200.
- Independent market-data confirmation from a third-party aggregator or exchange page showing broadly similar ETH levels.

## Net update logic

The evidence preserved the initial yes lean but reduced confidence below the market because the main hidden assumption is persistence through one exact minute close. The market seems to price the cushion, but maybe not enough of the narrow-window fragility.

## Suggested downstream use

Use as an orchestrator synthesis input and as a caution against treating a 95% market price as equivalent to near-certainty in a single-minute threshold contract.