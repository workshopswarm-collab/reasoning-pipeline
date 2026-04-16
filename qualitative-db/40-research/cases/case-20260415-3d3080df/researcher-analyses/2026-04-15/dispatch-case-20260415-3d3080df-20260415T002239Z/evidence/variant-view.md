---
type: evidence_map
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
research_run_id: 29a9b491-26db-4f17-b52e-080c411c745c
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: markets
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 be above 70000?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/variant-view.md"]
tags: ["evidence-map", "binance", "threshold", "noon-close"]
---

# Summary

Net lean is Yes, but with a weaker edge than the market price implies because the contract is a narrow timestamped threshold event rather than a broad weekly directional thesis.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle closing at 12:00 ET on April 20, 2026 print above 70,000?

## Current lean

Lean Yes, but only moderately; the market appears somewhat overconfident.

## Prior / starting view

Starting view was that a price already around 74.5k with only four days left should justify a strong Yes lean.

## Evidence supporting the claim

- Binance ticker and recent 1-minute klines show BTC/USDT around 74.5k, roughly 6.5% above threshold. Direct evidence. High weight.
- Polymarket rules confirm the threshold is strict but straightforward and tied to the same exchange pair currently above 70k. Direct contract evidence. High weight.
- The short time horizon limits the number of major macro cycles left before resolution. Indirect but relevant. Medium weight.

## Evidence against the claim

- The contract only cares about a single minute at noon ET, so path dependence is high; BTC can be above 70k generally yet still fail at the required timestamp. Direct contract-structure argument. Medium-high weight.
- A 4.5k cushion is meaningful but not enormous for BTC over four days; crypto can move >5% quickly. Indirect contextual evidence. Medium weight.
- Resolution is exchange-specific to Binance BTC/USDT, so exchange-specific dislocations or relative basis versus other venues can matter. Direct rule implication. Medium weight.

## Ambiguous or mixed evidence

- Market pricing near 85% may reflect informed consensus, but it may also reflect lazy anchoring to spot >70k rather than to the exact noon-minute contract mechanics.

## Conflict between inputs

There is little factual conflict. The disagreement is mainly weighting-based: how much confidence current spot >70k deserves once the narrow noon ET contract condition is respected.

## Key assumptions

- Current Binance pricing is representative enough to use as the base anchor.
- No large exogenous shock hits before April 20 noon ET.
- Binance remains a usable and credible source for the target minute candle.

## Key uncertainties

- Short-horizon BTC volatility over the next four days.
- Whether noon ET trading on April 20 coincides with elevated U.S. risk-session volatility.
- Whether Binance-specific noise matters at the exact minute.

## Disconfirming signals to watch

- BTC/USDT falling toward or below 72k before April 20.
- Sharp risk-off macro headlines.
- Evidence that Binance noon ET candles are unusually noisy versus broader spot.

## What would increase confidence

- BTC holding comfortably above 73k-74k into April 19-20.
- Additional venue/context evidence showing volatility compression rather than expansion.
- Confirmation that noon ET on recent days did not exhibit unusual exchange-specific dislocations.

## Net update logic

The direct Binance anchor keeps the answer on Yes, but reading the exact rules knocks confidence down from the market's mid-80s level because this is not simply "BTC currently above 70k"; it is a timestamped, single-venue, one-minute-close contract.

## Suggested downstream use

Use as synthesis input: the variant view is not a reversal to No, but a warning that the market may be modestly overpaying for a seemingly easy Yes due to narrow contract mechanics.