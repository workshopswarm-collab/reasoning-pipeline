---
type: evidence_map
case_key: case-20260407-42a10bc6
dispatch_id: dispatch-case-20260407-42a10bc6-20260407T014927Z
research_run_id: 9f4e7feb-0fdd-44aa-83de-5ca4be3211af
analysis_date: 2026-04-07
persona: risk-manager
domain: crypto
subdomain: exchanges
entity: binance
topic: will-the-price-of-bitcoin-be-above-68-000-on-april-7
question: "Will the price of Bitcoin be above $68,000 on April 7?"
driver: operational-risk
date_created: 2026-04-07
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin", "binance"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-42a10bc6/researcher-analyses/2026-04-07/dispatch-case-20260407-42a10bc6-20260407T014927Z/personas/risk-manager.md"]
tags: ["btc", "binance", "evidence-map", "timing-risk"]
---

# Summary

The current lean is mildly Yes, but the main edge comes from spot already being above strike, while the main reason not to be too confident is that settlement is based on one exact minute close.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-07 close above 68,000?

## Current lean

Lean Yes, but with notable timing fragility.

## Prior / starting view

Starting view: market likely optimistic because current price and narrative can hide the risk of a single-minute settlement rule.

## Evidence supporting the claim

- Binance spot price at research time was above strike (`researcher-source-notes/2026-04-07-risk-manager-binance-btcusdt-market-and-rule-surface.md`).
  - Why it matters: direct settlement venue context.
  - Direct or indirect: direct venue context, though not final settling candle.
  - Weight: high.
- Binance order book top-of-book was also above strike.
  - Why it matters: supports that above-strike level was not just a stale last trade.
  - Direct or indirect: direct venue context.
  - Weight: medium.
- CoinGecko cross-check also showed BTC above strike.
  - Why it matters: reduces odds Binance was idiosyncratically rich.
  - Direct or indirect: indirect/contextual.
  - Weight: low to medium.

## Evidence against the claim

- The contract resolves on a **single exact one-minute close** at noon ET, not on whether BTC traded above 68,000 generally.
  - Why it matters: minute-level path risk is materially higher than day-level intuition suggests.
  - Direct or indirect: direct contract mechanic.
  - Weight: high.
- The assigned market metadata implied 84.5%, but the public event page around research time showed the 68,000 line near 70%.
  - Why it matters: this suggests either stale metadata or live uncertainty; either way confidence should be discounted.
  - Direct or indirect: contextual market-structure evidence.
  - Weight: medium.
- Binance 24h stats showed a low of 68,300, meaning price was not far above the strike and could slip below on modest weakness.
  - Why it matters: upside margin over strike is thin.
  - Direct or indirect: direct venue context.
  - Weight: high.

## Ambiguous or mixed evidence

- Broader BTC spot being above 68,000 is supportive directionally, but does not answer the exact minute-close question.
- Single-source settlement makes source-of-truth ambiguity low, but implementation/timestamp risk remains.

## Conflict between inputs

The main conflict is not factual but weighting-based: how much confidence should current above-strike spot create when the actual contract cares about one future minute close.

## Key assumptions

- Current above-strike pricing remains informative for the noon ET close.
- There is no large overnight or US-morning downside move.
- Binance chart/UI close and API-derived minute interpretation are aligned enough for practical forecasting.

## Key uncertainties

- Overnight BTC volatility before the noon ET resolution window.
- Whether the market-implied baseline in assignment metadata was stale.
- Whether late-session microstructure around noon ET creates a below-strike print.

## Disconfirming signals to watch

- BTC trading back below 68,000 and failing to reclaim.
- Weak US-morning price action into the resolution window.
- Any evidence that Binance-specific pricing is softer than broader spot.

## What would increase confidence

- Additional Binance checks closer to the resolution minute still showing BTC comfortably above 68,000.
- A wider cushion above strike, e.g. sustained trading above 68.5k-69k.

## Net update logic

Current spot above strike pushes the forecast toward Yes, but the contract's minute-close mechanic and thin cushion over strike justify discounting any near-certainty interpretation.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review