---
type: evidence_map
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
research_run_id: 679c50d3-8adf-489f-92c0-cac9156ba686
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-200-on-april-17
question: "Will the price of Ethereum be above $2,200 on April 17?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["orchestrator synthesis input"]
tags: ["evidence-map", "eth", "binance", "daily-close"]
---

# Summary

The evidence nets to a strong Yes lean, but the most credible variant view is that a 95% market price may overstate certainty for a one-minute next-day settlement on a volatile crypto asset.

## Question being evaluated

Will the Binance ETH/USDT 1-minute candle labeled 12:00 ET on April 17 have a final Close strictly above 2200?

## Current lean

Yes, with probability below the market's 95% but still clearly high.

## Prior / starting view

Starting baseline was the market-implied ~95% Yes from Polymarket.

## Evidence supporting the claim

- Direct Binance spot check at 2352.52.
  - Source: 2026-04-16-variant-view-binance-spot-check.md
  - Why it matters causally: exchange-specific reference already sits well above strike.
  - Direct or indirect: direct for current state, indirect for settlement.
  - Weight: high.

- Contract wording requires only a final close above 2200, not a sustained average or cross-exchange confirmation.
  - Source: 2026-04-16-variant-view-polymarket-rules-and-market-state.md
  - Why it matters causally: narrow condition favors the side already in the money by a meaningful margin.
  - Direct or indirect: direct.
  - Weight: high.

- Secondary context checks around the low 2300s broadly match Binance directionally.
  - Source: 2026-04-16-variant-view-context-price-checks.md
  - Why it matters causally: reduces concern that the Binance primary spot read is a transient or isolated outlier.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- The contract settles on one exact future minute, not current spot.
  - Source: Polymarket rules note.
  - Why it matters causally: even a generally bullish price regime can still fail a narrow intraday timestamp condition.
  - Direct or indirect: direct.
  - Weight: high.

- ETH can move materially within 24 hours.
  - Source: general crypto market structure plus contextual price-source spread over capture times.
  - Why it matters causally: a ~6-7% cushion is strong but not invulnerable in crypto.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- Small discrepancies across captured spot/context values are expected because timestamps differ; they are not meaningful by themselves.
- No obvious exchange-specific outage or pricing anomaly was found, but that remains a background operational-risk channel until settlement occurs.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: whether a current cushion above 2200 justifies something as high as 95% on an exact-minute next-day contract.

## Key assumptions

- Current ETH cushion is large enough that residual risk is mainly exact-minute volatility rather than broad directional repricing.
- Binance remains a reliable and representative price source at settlement.

## Key uncertainties

- The actual 12:00 ET April 17 candle close is not yet observable.
- Near-term volatility regime between now and settlement could shift sharply.

## Disconfirming signals to watch

- ETH/USDT trades back toward or below 2200 before noon ET.
- Binance-specific price dislocation appears relative to broader ETH references.
- Sudden macro or crypto shock creates outsized intraday downside.

## What would increase confidence

- Another Binance check closer to settlement still showing a large cushion above 2200.
- Continued agreement between Binance and other ETH spot references.

## Net update logic

The direct exchange-specific spot evidence supports Yes strongly, but the contract's exact-minute structure is a real fragility that keeps the estimate below an unqualified market-level 95%. The variant view is not that No is likely; it is that extreme confidence may be slightly too high given the narrow settlement mechanics.

## Suggested downstream use

Use as orchestrator synthesis input for a modest downward adjustment versus the raw market-implied 95%, not for a directional flip.