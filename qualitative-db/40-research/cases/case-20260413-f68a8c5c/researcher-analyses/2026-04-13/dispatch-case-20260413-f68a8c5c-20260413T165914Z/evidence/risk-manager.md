---
type: evidence_map
case_key: case-20260413-f68a8c5c
dispatch_id: dispatch-case-20260413-f68a8c5c-20260413T165914Z
research_run_id: 292872c7-4988-489c-a076-60312ce49636
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: exchanges
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-68-000-on-april-14
question: "Will the price of Bitcoin be above $68,000 on April 14?"
driver: liquidity
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["liquidity", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-f68a8c5c/researcher-analyses/2026-04-13/dispatch-case-20260413-f68a8c5c-20260413T165914Z/personas/risk-manager.md"]
tags: ["evidence-map", "crypto", "timing-risk", "exchange-resolution"]
---

# Summary

Current evidence leans strongly toward Yes, but the residual risk is concentrated in one-minute timing and venue-specific execution rather than in broad daily BTC direction.

## Question being evaluated

Will Binance BTC/USDT record a 12:00 ET one-minute candle close on April 14 that is strictly above 68000?

## Current lean

Lean Yes with high probability, but lower confidence than the market price implies.

## Prior / starting view

Starting view from market price was 95.95% implied probability, signaling traders see the threshold as comfortably in-the-money.

## Evidence supporting the claim

- Polymarket rules define a straightforward threshold event tied to Binance BTC/USDT and a strict greater-than test.
  - source: source note on Polymarket rules
  - causal relevance: tells us exactly what needs to happen
  - direct vs indirect: direct contract evidence
  - weight: high

- Binance public API spot check showed BTCUSDT around 72200.91 on April 13, roughly 4200 above the threshold.
  - source: Binance API spot-check note
  - causal relevance: establishes a meaningful price cushion one day before settlement
  - direct vs indirect: direct contextual price evidence from governing venue family
  - weight: high

- Recent Binance 1-minute klines were also around 72.15k to 72.20k, showing the market was not currently hovering near 68k.
  - source: Binance API spot-check note
  - causal relevance: reduces immediate knife-edge concern
  - direct vs indirect: direct contextual evidence
  - weight: medium

- Binance.US and CoinGecko were directionally consistent near 72.2k.
  - source: Binance API spot-check note
  - causal relevance: lowers risk that the observed level was a one-off bad print or isolated parsing issue
  - direct vs indirect: indirect verification evidence
  - weight: low to medium

## Evidence against the claim

- The contract resolves on one exact one-minute close at noon ET, so a temporary selloff or wick at the wrong moment can flip the outcome even if BTC spends most of the day above 68k.
  - source: Polymarket rules note
  - causal relevance: main path-risk mechanism
  - direct vs indirect: direct contract evidence
  - weight: high

- Crypto can move several thousand dollars within 24 hours during risk-off episodes; the ~4.2k cushion is meaningful but not invulnerable.
  - source: market structure logic plus current cushion arithmetic
  - causal relevance: shows that current moneyness is not the same as certainty
  - direct vs indirect: indirect contextual reasoning
  - weight: medium

- The rule points to the Binance UI rather than explicitly to a stable archival API endpoint, leaving modest operational ambiguity for later settlement verification.
  - source: Polymarket rules note
  - causal relevance: operational rather than directional risk
  - direct vs indirect: direct contract-surface observation
  - weight: low to medium

## Ambiguous or mixed evidence

- Consistency between Binance API, Binance.US, and CoinGecko is reassuring, but these are all price-reporting surfaces around the same global BTC market and do not provide strong independence on tomorrow's noon close.

## Conflict between inputs

There is little direct factual conflict. The main disagreement is weighting-based: whether a ~4.2k cushion one day out justifies something near 96% or whether one-minute timing risk deserves more discount.

## Key assumptions

- Binance API spot checks are a good proxy for the settlement-relevant UI candle family.
- No major macro or crypto-specific shock hits before noon ET on April 14.
- Noon ET candle labeling is interpreted as expected relative to Binance's minute timestamps.

## Key uncertainties

- Exact path of BTC over the next ~19 hours.
- Whether volatility clusters around US trading hours or macro headlines before noon ET.
- Whether any exchange-specific display or timing issue complicates settlement interpretation.

## Disconfirming signals to watch

- BTCUSDT dropping below ~70k before the settlement window.
- Expanding intraday volatility or fast correlated risk-off move.
- Evidence of Binance-specific price dislocation or candle-timestamp ambiguity.

## What would increase confidence

- A fresh Binance check closer to settlement still showing >70k.
- Stable cross-venue pricing with no Binance-specific anomalies.
- Independent confirmation of exact ET-to-candle mapping on the Binance interface.

## Net update logic

The evidence keeps the base directional lean at Yes because the governing venue is currently well above the threshold. But the market's near-certainty appears to compress a real, if still minority, tail risk: this is a single-minute venue-specific event, not a broad end-of-day average. That timing concentration is the main reason to mark the estimate below the market.

## Suggested downstream use

Use as orchestrator synthesis input and as a reminder that extreme probabilities in narrow-resolution crypto contracts deserve a timing-risk haircut even when spot is comfortably through the line.