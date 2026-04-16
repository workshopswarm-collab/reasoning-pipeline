---
type: evidence_map
case_key: case-20260415-04e7318a
dispatch_id: dispatch-case-20260415-04e7318a-20260415T145259Z
research_run_id: 411c3203-cc4f-4309-85ba-2d8277e2de0e
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 PM ET one-minute candle close on 2026-04-20 be above 70000?"
driver: operational-risk
date_created: 2026-04-15
agent: variant-view
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-04e7318a/researcher-analyses/2026-04-15/dispatch-case-20260415-04e7318a-20260415T145259Z/personas/variant-view.md"]
tags: ["evidence-map", "bitcoin", "binance", "threshold-market"]
---

# Summary

This evidence map nets out a high-probability Yes view with a modest variant discount versus market confidence, driven mainly by contract path dependence rather than by a bearish BTC thesis.

## Question being evaluated

Will the Binance BTC/USDT 12:00 PM ET one-minute candle close on April 20, 2026 above 70,000?

## Current lean

Lean Yes, but slightly less confidently than the market.

## Prior / starting view

Starting view was that a market trading around 87% likely already embeds the obvious fact that BTC is above 70k today, so the only useful contribution would come from checking whether the contract mechanics create hidden fragility.

## Evidence supporting the claim

- **Current Binance spot materially above threshold**
  - Source: Binance API price and recent 1m klines captured in source note.
  - Why it matters causally: starting level near 74.15k leaves about a 4.15k cushion above 70k.
  - Direct or indirect: direct contextual evidence.
  - Weight: high.

- **Independent major-exchange check broadly matches Binance level**
  - Source: Kraken public ticker around 74.16k.
  - Why it matters causally: reduces concern that Binance spot is idiosyncratically elevated versus broader market.
  - Direct or indirect: indirect/contextual verification.
  - Weight: medium.

- **Contract threshold is not especially close to current price**
  - Source: implied from Binance spot vs 70k threshold.
  - Why it matters causally: BTC can decline several percent and still resolve Yes.
  - Direct or indirect: derived from direct price evidence.
  - Weight: medium-high.

## Evidence against the claim

- **Single-minute close risk is more fragile than a broad daily-price question**
  - Source: Polymarket rules structure.
  - Why it matters causally: even a temporary dip at the exact reference minute can flip resolution.
  - Direct or indirect: direct contract-mechanics evidence.
  - Weight: high.

- **Exchange-specific resolution introduces operational and microstructure risk**
  - Source: Polymarket reliance on Binance BTC/USDT specifically.
  - Why it matters causally: wick, local dislocation, or UI/API interpretation issues matter more than cross-market averages.
  - Direct or indirect: direct contract-mechanics evidence.
  - Weight: medium.

- **BTC can move more than 5% in short windows**
  - Source: general market behavior; not tied here to a specific catalyst in sourced evidence.
  - Why it matters causally: the current cushion is meaningful but not enormous for BTC.
  - Direct or indirect: contextual inference.
  - Weight: medium-low.

## Ambiguous or mixed evidence

- CME crypto page confirms institutional trading infrastructure exists, but it does not directly settle short-horizon BTC direction for this market.
- Lack of strong catalyst evidence cuts both ways: it argues against a sharp drop, but also means the bullish case is mostly level-based rather than catalyst-backed.

## Conflict between inputs

There is little factual conflict. The tension is interpretive:
- market participants appear to emphasize current price cushion and likely persistence above 70k
- the variant view emphasizes that the contract is narrower than that narrative because it settles on one Binance minute close at noon ET

This is mostly a weighting-based and contract-interpretation-based disagreement.

## Key assumptions

- BTC remains broadly above 70k into April 20.
- Binance noon ET candle maps cleanly to the expected reference minute without material ambiguity.
- No major downside catalyst or venue-specific disruption appears before resolution.

## Key uncertainties

- Exact volatility path into the specific settlement minute.
- Whether any weekend/liquidity event creates a temporary dip despite otherwise bullish price action.
- Residual operational ambiguity between Binance UI candle display and API timestamp conventions.

## Disconfirming signals to watch

- BTC losing 72k with momentum.
- Binance trading materially below peer venues.
- Clarification that the practical settlement implementation differs from the straightforward ET-noon to UTC mapping.

## What would increase confidence

- Continued multi-venue spot stability above 72k through April 19-20.
- A direct check of Binance UI candle handling closer to resolution.
- Evidence of benign macro calendar / no obvious downside event risk before noon ET April 20.

## Net update logic

The evidence leaves the natural answer as Yes, but the variant update is to trim confidence below the market's 87% because the contract is about a single exchange-specific minute close, not the general proposition that BTC is currently trading comfortably above 70k. What mattered most was the combination of a healthy current cushion and a mechanically narrow settlement rule.

## Suggested downstream use

Use this as forecast update input and orchestrator synthesis input, especially for distinguishing level-based confidence from contract-mechanics fragility.