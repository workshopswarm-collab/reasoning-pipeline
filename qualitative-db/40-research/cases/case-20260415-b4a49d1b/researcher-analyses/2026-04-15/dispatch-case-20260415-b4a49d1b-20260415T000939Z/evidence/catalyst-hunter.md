---
type: evidence_map
case_key: case-20260415-b4a49d1b
dispatch_id: dispatch-case-20260415-b4a49d1b-20260415T000939Z
research_run_id: 37811044-0361-41fb-a353-e9eb90ef1337
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-15
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance-btcusdt-market"]
proposed_drivers: ["scheduled-macro-catalyst-gap"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-b4a49d1b/researcher-analyses/2026-04-15/dispatch-case-20260415-b4a49d1b-20260415T000939Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "catalyst-timing", "resolution-logic"]
---

# Summary

The case is currently more about avoiding a downside catalyst than finding a bullish upside trigger. BTC is already above the threshold on the named venue.

## Question being evaluated

Will Binance BTC/USDT print a final 1-minute candle close above 70,000 at 12:00 ET on Apr 20, 2026?

## Current lean

Lean Yes.

## Prior / starting view

Starting point was that the market at 0.86 may be slightly too conservative if BTC is already trading well above 70k and no top-tier scheduled macro event remains before settlement.

## Evidence supporting the claim

- Binance direct price data shows BTC around 74.5k with ~6% cushion over the threshold.
  - direct evidence
  - high weight
  - matters because it uses the named exchange/source family from the contract
- Recent Binance daily closes show five consecutive closes above 70k in the captured sample.
  - direct-contextual hybrid
  - medium-high weight
  - matters because it suggests recent regime persistence above the threshold
- Official calendar check shows no FOMC decision or CPI release still ahead of Apr 20 noon ET.
  - contextual evidence
  - medium weight
  - matters because it reduces obvious scheduled downside repricing triggers

## Evidence against the claim

- The contract resolves on one exact minute, so a localized intraday dip below 70k at noon ET is enough for No even if BTC is broadly strong.
  - direct contract-interpretation risk
  - high weight
- BTC is volatile enough that a 6% move in five days is not remotely impossible.
  - contextual evidence
  - medium-high weight
- No obvious scheduled catalyst does not protect against unscheduled macro/geopolitical or exchange-specific shocks.
  - contextual evidence
  - medium weight

## Ambiguous or mixed evidence

- The same lack of scheduled catalysts that supports Yes also means the path may be dominated by noise and weekend liquidity, which can cut either way.
- Neighbor threshold pricing on Polymarket suggests the market distribution is coherent rather than obviously mispriced, limiting confidence in a large edge.

## Conflict between inputs

No major factual conflict. The tension is mostly weighting-based: how much confidence to place in current spot cushion versus the fragility of a single-minute settlement condition.

## Key assumptions

- No large unscheduled risk-off event occurs before Apr 20 noon ET.
- Binance remains the clean operative source and no operational anomalies distort the settlement minute.

## Key uncertainties

- Weekend crypto volatility between Apr 18-20.
- Whether any ETF-flow, geopolitical, or leverage unwind story emerges suddenly.
- How much noon ET timing specifically matters for intraday liquidity conditions.

## Disconfirming signals to watch

- BTC losing 72k on Binance with momentum.
- Escalating risk-off headlines or exchange instability.
- Sharp cross-asset selloff before the Apr 20 settlement window.

## What would increase confidence

- BTC still holding clearly above 72k into Apr 19-20.
- Quiet macro/news flow and no exchange disruptions.
- Stable Binance spot behavior around U.S. morning trading.

## Net update logic

Current spot distance to threshold and the absence of a major scheduled macro catalyst before resolution together outweigh the single-minute settlement fragility, but not by a huge margin. That pushes the view slightly above the market, not dramatically above it.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the catalyst-hunter lane was only modestly more bullish than the market.
