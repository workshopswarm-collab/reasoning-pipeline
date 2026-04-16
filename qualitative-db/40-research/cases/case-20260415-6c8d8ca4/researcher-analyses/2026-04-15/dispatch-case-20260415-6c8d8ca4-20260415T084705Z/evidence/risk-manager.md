---
type: evidence_map
case_key: case-20260415-6c8d8ca4
dispatch_id: dispatch-case-20260415-6c8d8ca4-20260415T084705Z
research_run_id: f8f73c4f-55be-4d85-9bb7-b2ca07acd76c
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle close on April 17 above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-6c8d8ca4/researcher-analyses/2026-04-15/dispatch-case-20260415T084705Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "settlement-risk", "timing-risk"]
---

# Summary

The evidence net is favorable to Yes because current Binance BTC/USDT is materially above the strike, but the contract is narrower than a generic bullish BTC call and therefore carries real timing/path fragility.

## Question being evaluated

Will the final close of the Binance BTC/USDT 1-minute candle at 12:00 ET on April 17 print above 72,000?

## Current lean

Lean Yes, but less confidently than the market price suggests.

## Prior / starting view

Starting view: likely Yes given the quoted 81% market price and the strike appearing below current BTC spot.

## Evidence supporting the claim

- Binance direct ticker and recent 1-minute klines put BTC/USDT around 74,037, roughly 2,037 points above the strike.
  - Source: Binance API source note
  - Why it matters causally: distance to strike is the most immediate predictor for a short-dated threshold contract
  - Direct or indirect: direct venue-context evidence
  - Weight: high

- Polymarket rules clearly define a single source of truth and a single relevant condition: Binance BTC/USDT 12:00 ET 1-minute close above 72,000.
  - Source: Polymarket rules source note
  - Why it matters causally: removes some contract ambiguity and lets the analysis focus on price path instead of interpretation disputes
  - Direct or indirect: direct contract evidence
  - Weight: high

## Evidence against the claim

- The contract is about one exact minute close, not the daily average or broad trading range.
  - Source: Polymarket rules source note
  - Why it matters causally: a short-lived drop into settlement can still resolve No even if the broader trend is bullish
  - Direct or indirect: direct contract evidence
  - Weight: high

- The observed cushion is only about 2.7% above the strike, which is not large for BTC over a two-day horizon.
  - Source: combined logic from Binance price snapshot and contract strike
  - Why it matters causally: a modest drawdown is sufficient to invalidate Yes
  - Direct or indirect: direct plus analytical
  - Weight: medium-high

## Ambiguous or mixed evidence

- Recent sampled minute candles were fairly calm, but the sample window was too short to say much about event-horizon volatility between now and settlement.
- Market price near 81% may reflect informed traders, but it may also encode overconfidence from current spot anchoring.

## Conflict between inputs

No major factual conflict. The main difference is weighting: current price buffer argues Yes, while contract narrowness argues for discounting confidence.

## Key assumptions

- Binance BTC/USDT remains above 72,000 through the specific settlement minute.
- No Binance-specific dislocation creates an idiosyncratic below-strike close.
- Short-horizon BTC volatility does not erase the current cushion before noon ET April 17.

## Key uncertainties

- How much realized volatility BTC will show over the next ~48 hours
- Whether macro/news shocks emerge before the settlement minute
- Whether the current market is underpricing one-minute path dependence

## Disconfirming signals to watch

- BTC/USDT trading back toward or below 73,000 ahead of settlement
- Rising intraday volatility or sharp crypto-wide liquidation
- Binance-specific spread/dislocation around noon ET settlement window

## What would increase confidence

- BTC/USDT holding well above 73,500 into April 17 morning ET
- Additional venue/context checks showing stable risk conditions without elevated downside volatility
- More time above the strike without meaningful deterioration in spot structure

## Net update logic

The direct venue data is enough to justify a Yes lean, but the risk-manager adjustment is to discount confidence because this is a narrow one-minute close contract with only a moderate cushion over the strike. The market looks directionally right but somewhat too confident.

## Suggested downstream use

Use as synthesis input emphasizing that the case is mostly about short-horizon path risk and contract narrowness, not long-run BTC thesis.