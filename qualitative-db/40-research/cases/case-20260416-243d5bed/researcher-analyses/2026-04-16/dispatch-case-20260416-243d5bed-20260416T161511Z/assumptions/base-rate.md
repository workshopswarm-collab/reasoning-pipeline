---
type: assumption_note
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
research_run_id: 5d168321-d89e-4b52-89c8-1535c009d575
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: "Threshold-hold assumption for ETH > 2300 at a single scheduled minute"
question: "Will the Binance ETH/USDT 12:00 ET one-minute candle on April 17 close above 2300?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/personas/base-rate.md"]
tags: ["assumption-note", "base-rate", "threshold-hold"]
---

# Assumption

ETH will remain in roughly its current trading regime through tomorrow noon ET, so a modest cushion above 2300 today is informative for the probability of tomorrow's exact one-minute close.

## Why this assumption matters

The base-rate view leans on the idea that a near-threshold market tends to behave more like a short-horizon hold/noise problem than a fresh repricing event. If that regime assumption fails, the outside-view anchor from current level and recent range becomes much less useful.

## What this assumption supports

- A probability above 50% for Yes.
- Treating current spot modestly above 2300 as meaningful evidence rather than noise.
- A conclusion that the market should not be priced near certainty because the contract is still a single-minute timestamp test.

## Evidence or logic behind the assumption

- Current Binance spot context is modestly above 2300.
- Recent ETH daily context shows several consecutive observations near or above the threshold rather than far below it.
- There is no identified scheduled binary catalyst in the gathered evidence that obviously dominates the next ~24 hours.

## What would falsify it

- A rapid risk-off move that pushes ETH materially below 2300 before the target window.
- A large crypto-specific headline or macro shock that changes the trading regime.
- Exchange-specific dislocation on Binance ETH/USDT relative to broader ETH spot markets.

## Early warning signs

- ETH losing the 2300 area decisively during the next several hours.
- Rising intraday volatility and repeated failure to reclaim 2300 after dips.
- Binance-specific spread or operational issues around the target window.

## What changes if this assumption fails

The probability of Yes should drop meaningfully, because this contract only needs one specific minute to miss the threshold. A broken regime assumption would shift the analysis away from base-rate hold behavior toward event-risk and intraday fragility.

## Notes that depend on this assumption

- Main finding at the assigned persona path.
- Binance mechanics source note.
- ETH price context source note.