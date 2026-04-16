---
type: evidence_map
case_key: case-20260416-e0b8c17c
dispatch_id: dispatch-case-20260416-e0b8c17c-20260416T050131Z
research_run_id: 6b2a6cd0-b0cf-4d63-b6bc-8692d1c88c99
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-20
question: "Will the price of Bitcoin be above $72,000 on April 20?"
driver: operational-risk
date_created: 2026-04-16
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-analyses/2026-04-16/dispatch-case-20260416-e0b8c17c-20260416T050131Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "path-risk", "settlement"]
---

# Summary

The evidence still leans Yes, but the main risk is that market confidence may be slightly overstating how much of that cushion survives a very narrow single-minute settlement mechanic.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle that closes at 12:00 ET on April 20, 2026 have a final Close price above 72,000?

## Current lean

Moderate Yes lean.

## Prior / starting view

Given the quoted market price of 0.835, the starting baseline was that the market already strongly expected a Yes outcome.

## Evidence supporting the claim

- Direct Binance spot context shows BTC/USDT currently around 75,000.
  - source: 2026-04-16-risk-manager-polymarket-rules-and-binance-source.md
  - causal relevance: provides current cushion of roughly 3,000 above threshold
  - evidence type: direct contextual market data
  - weight: high

- Recent Binance daily closes have mostly remained above 72,000.
  - source: direct Binance API check summarized in source note
  - causal relevance: indicates threshold is not currently an outlier level relative to recent trading
  - evidence type: direct contextual market data
  - weight: medium

- The contract uses Binance BTC/USDT specifically, and current Binance data are aligned with the thesis.
  - source: Polymarket rules plus direct Binance verification
  - causal relevance: removes cross-exchange mismatch risk from the main thesis
  - evidence type: direct / settlement-relevant
  - weight: medium

## Evidence against the claim

- Settlement depends on one exact 1-minute candle close at 12:00 ET, not a daily close or average.
  - source: Polymarket rules
  - causal relevance: creates substantial path and timestamp risk even if the broader trend stays constructive
  - evidence type: direct contract-interpretation evidence
  - weight: high

- Over the last 14 days, only about one-third of hourly closes were above 72,000.
  - source: direct Binance hourly sample summarized in source note
  - causal relevance: shows the threshold is comfortably below current spot, but not so low that temporary reversals are negligible
  - evidence type: direct contextual market data
  - weight: medium

- Crypto trades continuously through the weekend; a fast risk-off move or venue-specific wick near resolution could still defeat the thesis.
  - source: market structure plus contract mechanics
  - causal relevance: narrow-settlement markets are vulnerable to being directionally right but timestamp-wrong
  - evidence type: indirect but highly relevant
  - weight: medium

## Ambiguous or mixed evidence

- Current spot near 75,000 is supportive, but that same fact can foster overconfidence because traders may mentally substitute "currently above" for "will be above at the precise settlement minute."

## Conflict between inputs

There is little factual conflict between the inputs. The main issue is weighting: whether the current price cushion deserves more weight than the narrow timestamp-specific settlement risk.

## Key assumptions

- BTC remains materially above 72,000 into April 20 rather than mean-reverting toward the threshold.
- Binance’s settlement-relevant candle display tracks the broader direct market data without unusual anomalies.
- No abrupt weekend or macro shock meaningfully changes the price path before 16:00 UTC on April 20.

## Key uncertainties

- Short-horizon volatility between now and settlement.
- Whether 72,000 remains a comfortable buffer or becomes a contested level by April 19-20.
- Whether market participants are underpricing timestamp-specific fragility.

## Disconfirming signals to watch

- BTC/USDT losing 73,000 and spending sustained time near 72,000.
- Increasing downside volatility during U.S. hours.
- Binance-specific dislocation, unusual wick behavior, or display/API inconsistency near settlement.

## What would increase confidence

- BTC holding above 74,000 through April 18-19.
- A widening buffer above 72,000 ahead of the settlement window.
- Continued absence of venue-specific anomalies on Binance.

## Net update logic

The evidence keeps the thesis on the Yes side because current Binance prices are materially above the threshold and recent daily trading context is supportive. The risk-manager adjustment is mainly about confidence, not direction: a narrow single-minute settlement means the market should not be treated as equivalent to a broad "BTC will still be above 72k sometime around then" proposition.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- follow-up investigation near settlement if spot compresses toward the threshold