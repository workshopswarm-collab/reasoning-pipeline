---
type: evidence_map
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
research_run_id: 4a2cfafc-0fd1-4931-afed-b5796ce8fc7f
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-one-minute-candle-close-on-april-17-2026-be-above-70000
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle close on April 17, 2026 be above 70000?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-881aa4d0/researcher-analyses/2026-04-16/dispatch-case-20260416-881aa4d0-20260416T044756Z/personas/risk-manager.md"]
tags: ["evidence-map", "contract-interpretation", "downside-risk"]
---

# Summary

The net evidence still favors Yes strongly, but the residual risk is not literally zero because the contract is resolved by one exact Binance minute close at a future timestamp.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 have a final close above 70,000?

## Current lean

Lean Yes with only modest disagreement versus the market's near-certainty.

## Prior / starting view

Starting view was that a 99% market likely embeds too little path and venue-specific risk for a one-minute timestamped crypto contract.

## Evidence supporting the claim

- Binance direct spot check showed BTCUSDT at 74,911.37 during the run.
  - Direct or indirect: direct exchange data, but contextual rather than settlement-final.
  - Why it matters: leaves a large cushion above 70,000.
  - Weight: high.
- Polymarket contract wording only requires the single specified one-minute close to be above 70,000.
  - Direct or indirect: direct contract evidence.
  - Why it matters: does not require sustained trading above threshold throughout the day.
  - Weight: high.
- Market-implied baseline near 99.05% suggests consensus sees very low likelihood of a >7% downside move into the exact resolution minute.
  - Direct or indirect: market context.
  - Why it matters: useful as a confidence object, though not independent evidence.
  - Weight: medium.

## Evidence against the claim

- The contract is narrow and time-specific: only the final close of one exact minute counts.
  - Why it matters causally: a late sharp drop or exchange-specific dislocation can flip the outcome.
  - Weight: high.
- Crypto can move several percent quickly on macro or exchange-specific stress.
  - Why it matters causally: path risk is underappreciated when markets price near certainty.
  - Weight: medium.
- The authoritative settlement surface is Binance candles, not the generic spot API snapshot used for contextual verification.
  - Why it matters causally: source-surface mismatch leaves residual implementation risk.
  - Weight: medium.

## Ambiguous or mixed evidence

- The very high market price may reflect informed confidence, but it can also compress residual uncertainty too aggressively in low-time-to-resolution contracts.

## Conflict between inputs

No direct source conflict. The tension is mostly between high spot-price cushion and the narrowness of the settlement rule.

## Key assumptions

- Binance remains the operative source and functions normally.
- No material selloff pushes BTCUSDT below 70,000 into the observation minute.
- Exchange-specific prints do not diverge enough from broader market to create a surprise No.

## Key uncertainties

- Exact BTC path over the remaining hours.
- Whether April 17 US-morning volatility could compress the cushion materially.
- Whether Binance-specific candle formation introduces unexpected operational or microstructure risk.

## Disconfirming signals to watch

- BTCUSDT trading below ~72k ahead of the final window.
- Sudden exchange instability or abnormal Binance-only divergence.
- Major macro/news shock before noon ET on April 17.

## What would increase confidence

- A fresh Binance candle/spot check closer to the resolution window still showing a wide cushion.
- Confirmation that Binance trading and candle display remain normal through the morning.

## Net update logic

The direct Binance spot check kept the lean firmly on Yes, but contract interpretation prevents treating the remaining risk as negligible. The main update versus market is not a bearish BTC thesis; it is a discount for narrow timestamp risk, exchange-specific dependence, and one-minute-close fragility.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the residual probability was kept above zero despite extreme market pricing.