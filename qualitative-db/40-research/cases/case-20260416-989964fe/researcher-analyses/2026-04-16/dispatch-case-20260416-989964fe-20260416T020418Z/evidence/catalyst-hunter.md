---
type: evidence_map
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
research_run_id: d3bad876-2b84-4db0-84c0-1cd8ee6aff39
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: "ETH above 2200 on April 17 catalyst netting"
question: "Will the Binance ETH/USDT 12:00 ET one-minute candle on April 17 close above 2200?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["macro-risk-event"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "catalyst-analysis", "binance", "ethusdt"]
---

# Summary

The net evidence favors Yes because ETH is already materially above the threshold and the contract settles on a single exchange-specific one-minute close tomorrow at noon ET. The main bearish path is a fresh downside catalyst large enough to force a >6% drop into that exact minute.

## Question being evaluated

Will Binance ETH/USDT close above 2200 on the 1-minute candle corresponding to Apr 17 2026 12:00 ET?

## Current lean

Lean Yes, high probability but below the market's 95% because single-minute crypto settlement still leaves room for shock or timing risk.

## Prior / starting view

A market priced at 95% Yes suggests the threshold is already well in the money or very close. The key question was whether the contract wording or timing mechanics created hidden fragility.

## Evidence supporting the claim

- Binance spot source note: ETHUSDT around 2353-2354 during verification.
  - Matters because the threshold is already about 153 points below spot.
  - Direct evidence.
  - High weight.
- Binance 24h stats: low of 2308.50 while still staying above 2200 in the observed 24h window.
  - Matters because recent realized range still leaves cushion above threshold.
  - Direct evidence.
  - Medium weight.
- Polymarket rules note: settlement depends on one exact Binance 1m close, not broader market narratives.
  - Matters because this limits interpretation error and defines what bearish move is needed.
  - Direct evidence on contract structure.
  - High weight.

## Evidence against the claim

- Single-minute settlement creates path fragility.
  - A sharp intraday selloff or exchange-specific dislocation at the resolution minute could still flip the outcome.
  - Directly relevant contract risk.
  - Medium-high weight.
- Crypto can move >6% quickly under risk-off shocks.
  - Matters because the current cushion is meaningful but not impossibly large for ETH.
  - Contextual evidence.
  - Medium weight.
- Extreme market pricing at 95% can hide complacency.
  - Matters because this case was explicitly flagged for extra verification under extreme probability.
  - Contextual/process evidence.
  - Medium weight.

## Ambiguous or mixed evidence

- No dominant scheduled catalyst was identified from collected sources.
  - This supports stability by default, but also means the analysis may miss an unscheduled shock.
- Recent price strength can either signal resilience or simply mean there is more room to mean-revert.

## Conflict between inputs

There is little factual conflict in the collected evidence. The disagreement is mainly weighting-based: whether a ~6.5% cushion over roughly one day deserves something closer to 90%, 93%, or 95%.

## Key assumptions

- No fresh major downside catalyst arrives before the settlement minute.
- Binance spot remains a reliable settlement source without operational distortion.
- The observed cushion above 2200 is large enough that ordinary noise is insufficient to break it.

## Key uncertainties

- Overnight macro or crypto-specific newsflow.
- Exchange-specific volatility around the exact settlement minute.
- Whether broader market sentiment is more fragile than current spot implies.

## Disconfirming signals to watch

- ETH breaking below 2300 with momentum.
- A broad crypto liquidation event.
- Any evidence that Binance spot is diverging abnormally from the broader market near settlement.

## What would increase confidence

- Continued ETH stability above 2300 into the U.S. morning on Apr 17.
- Absence of major macro or crypto headlines overnight.
- Additional confirmation from Binance spot around the hours immediately preceding settlement.

## Net update logic

The most important update was verifying that the actual settlement source, Binance ETHUSDT, is currently far enough above 2200 that the market only loses on a meaningful downside event. That pushes the analysis away from vague Ethereum sentiment and toward a narrower catalyst question: is there a realistic near-term shock capable of dragging ETH below 2200 exactly at noon ET tomorrow? Collected evidence says yes is still favored, but not so overwhelmingly that timing/path risk should be ignored.

## Suggested downstream use

Use as an orchestrator synthesis input and as a compact audit trail for why this persona stayed constructive while still haircutting the market slightly for timing fragility.