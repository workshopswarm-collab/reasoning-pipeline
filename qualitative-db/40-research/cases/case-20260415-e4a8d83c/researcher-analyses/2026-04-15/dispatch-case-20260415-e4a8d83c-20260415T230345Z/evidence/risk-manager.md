---
type: evidence_map
case_key: case-20260415-e4a8d83c
dispatch_id: dispatch-case-20260415-e4a8d83c-20260415T230345Z
research_run_id: 5bc669ee-e2c6-4a13-a147-74ec03127b0c
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: short-horizon-price-thresholds
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: operational-risk
date_created: 2026-04-15
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-e4a8d83c/researcher-analyses/2026-04-15/dispatch-case-20260415-e4a8d83c-20260415T230345Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "threshold-market", "timing-risk"]
---

# Summary

The evidence nets to a modest Yes lean, but the dominant risk is not broad BTC direction; it is path and settlement-window fragility around a narrow Binance 1-minute close.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on April 17, 2026 have a final Close price above 74,000?

## Current lean

Lean Yes, but only moderately. Current evidence supports a probability in the high-60s rather than a very high-confidence view.

## Prior / starting view

Starting baseline was the market-implied probability near 71.5%-72% Yes.

## Evidence supporting the claim

- **Direct Binance price is currently above threshold**  
  - Source: Binance API source note  
  - Why it matters: the market settles on Binance BTC/USDT, so being above 74,000 now is directly relevant  
  - Direct or indirect: direct  
  - Weight: high

- **Recent 1-minute Binance closes sampled above threshold**  
  - Source: Binance API source note  
  - Why it matters: confirms the threshold is not merely touched on a noisy print; recent minute closes themselves are above 74,000  
  - Direct or indirect: direct  
  - Weight: medium-high

- **Polymarket market pricing near 72% Yes**  
  - Source: Polymarket rules and market state note  
  - Why it matters: aggregate trader view is already leaning meaningfully Yes  
  - Direct or indirect: indirect/contextual  
  - Weight: medium

## Evidence against the claim

- **Settlement is one exact minute close, not broad spot strength**  
  - Source: Polymarket rules note  
  - Why it matters: narrow-window contracts can fail on timing even if the general thesis is right  
  - Direct or indirect: direct to contract interpretation  
  - Weight: high

- **Current cushion is not huge versus routine BTC volatility**  
  - Source: Binance API source note plus threshold arithmetic  
  - Why it matters: roughly 800 points of cushion can disappear quickly in BTC over a day and a half  
  - Direct or indirect: contextual but highly relevant  
  - Weight: high

- **Exchange-specific basis / microstructure risk remains**  
  - Source: contract rules plus Binance-specific settlement  
  - Why it matters: other venues being above 74k would not save a No if Binance prints lower at settlement minute  
  - Direct or indirect: direct to contract mechanics  
  - Weight: medium

## Ambiguous or mixed evidence

- Market price itself is mixed: it supports Yes directionally, but from a risk-manager lens it may also signal overconfidence in a path-dependent contract.

## Conflict between inputs

There is little factual conflict. The main issue is weighting conflict between current in-the-money status and the narrowness of the settlement condition.

## Key assumptions

- BTC/USDT remains above 74,000 through the exact settlement window.
- Binance minute-close mechanics remain straightforward and observable.
- No unusual exchange-specific distortion dominates the settlement minute.

## Key uncertainties

- Short-horizon BTC volatility over the next ~41 hours.
- Whether the market is underpricing timing risk embedded in a one-minute close.
- Whether the cushion above threshold remains large enough by settlement morning.

## Disconfirming signals to watch

- BTC/USDT loses the 74,000 level before April 17 morning.
- Settlement-morning Binance minute candles cluster near or below 74,000.
- Exchange-specific divergence emerges versus broader BTC pricing.

## What would increase confidence

- BTC holding materially above 74,000 into April 17 morning.
- Settlement-morning Binance minute closes staying comfortably above threshold.
- A larger cushion, ideally >1.5%-2%, reducing micro-timing fragility.

## Net update logic

The strongest update is that the actual settlement source is currently above the threshold, which justifies a Yes lean. But the lean is capped because this is a narrow, date-specific, minute-close market where modest adverse movement can flip the outcome. The risk-manager conclusion is therefore not that the market is wrong directionally, but that confidence should be slightly lower than the raw current in-the-money status might suggest.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with emphasis on contract-mechanics fragility and the need for any later synthesis to separate directional BTC view from settlement-window risk.