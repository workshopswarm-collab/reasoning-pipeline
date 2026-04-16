---
type: evidence_map
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
research_run_id: 85a9dae8-24de-4cae-8adb-7a1612e33454
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-16
question: "Will the price of Bitcoin be above $72,000 on April 16?"
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
downstream_uses: ["risk-manager-finding"]
tags: ["evidence-map", "binance", "timing-risk"]
---

# Summary

The evidence nets to a Yes lean, but the main underpriced risk is path dependence into one specific settlement minute rather than broad directional Bitcoin weakness.

## Question being evaluated

Will Binance BTC/USDT's 1-minute candle for 2026-04-16 12:00 ET have a final Close above 72,000?

## Current lean

Lean Yes, with moderate confidence and some discount to the market's implied confidence.

## Prior / starting view

Starting view was that a market trading near 0.895 deserved stress-testing because extreme probabilities on date-specific crypto contracts can underprice minute-level timing risk.

## Evidence supporting the claim

- Binance spot during the run was about 74.2k, leaving roughly a $2.2k cushion above the strike. Direct, high weight.
- Binance last-24h 1-minute range was roughly 73,514 to 74,786.72, meaning recent realized downside still stayed above 72k. Direct, high weight.
- Recent last-hour trading range was tight around 74.0k-74.3k, suggesting no immediate stress near the threshold. Direct, medium weight.
- Polymarket contract text is operationally clean on source-of-truth and measurement field, reducing interpretive ambiguity. Direct, medium weight.

## Evidence against the claim

- Resolution depends on one exact 1-minute close, so a transient drawdown at the wrong time is enough to lose. Direct contract/timing risk, high weight.
- BTC is volatile enough that a ~3% move over ~27.5 hours is plausible; the cushion is meaningful but not huge. Contextual market-structure risk, medium-high weight.
- The market's 89.5% implied probability may embed very high confidence relative to the thin evidence actually needed here. Interpretive disconfirmer, medium weight.

## Ambiguous or mixed evidence

- Tight recent trading can either indicate stability or just low realized volatility before a sudden move.
- The contract's reliance on Binance is clear, but exchange-specific prints can decouple from broader BTC references in stress conditions.

## Conflict between inputs

There is no major factual conflict between inputs. The main disagreement is weighting-based: how much confidence should be assigned to the current cushion versus the residual path risk of one precise settlement minute.

## Key assumptions

- Recent realized range is informative enough for the next ~27.5 hours.
- Binance will remain a reliable and representative pricing venue at settlement.
- No material macro or crypto-specific shock occurs before the resolution window.

## Key uncertainties

- Whether BTC can absorb a late selloff and still keep the settlement-minute close above 72k.
- Whether exchange-specific noise on Binance could matter disproportionately.
- Whether current market pricing is overconfident because the contract looks simple while the minute-level condition remains fragile.

## Disconfirming signals to watch

- BTC trading below 73k with momentum.
- Expanding realized volatility into the April 16 morning ET window.
- Binance-specific weakness or unusual spread/dislocation versus other BTC venues.

## What would increase confidence

- BTC remaining comfortably above 73.5k through the April 16 morning ET session.
- Another independent verification near settlement showing Binance still well above 72k.
- No notable exchange operational issues or market-wide risk-off catalyst.

## Net update logic

The direct exchange data supports Yes because current and recent prices are above the strike by a meaningful margin. The risk-manager discount comes from the contract's exact-minute dependence and the fact that a modest crypto drawdown can happen quickly. So the evidence does not flip the lean, but it does argue for slightly less confidence than the market.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review