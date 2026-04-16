---
type: evidence_map
case_key: case-20260415-cd803ba3
dispatch_id: dispatch-case-20260415-cd803ba3-20260415T203927Z
research_run_id: 6f4d962f-f5d9-40ec-b349-be49bad71ac3
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-price
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-cd803ba3/researcher-analyses/2026-04-15/dispatch-case-20260415-cd803ba3-20260415T203927Z/personas/risk-manager.md"]
tags: ["risk-netting", "timing-risk", "binance"]
---

# Summary

The evidence leans Yes, but not as confidently as the market price suggests, because the market resolves on one exact Binance minute close and current price advantage over 74,000 is only modest.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for April 17, 2026 at 12:00 ET have a final close above 74,000?

## Current lean

Slight Yes lean, with path/timestamp fragility as the central risk.

## Prior / starting view

Starting view was that a 0.70 market price might be slightly aggressive for a narrow exact-minute crypto threshold market unless spot sat comfortably above strike.

## Evidence supporting the claim

- **Recent Binance BTC/USDT prices above 74,000**
  - source: Binance public ticker and recent 1-minute klines
  - causal relevance: the threshold is currently in-the-money
  - direct/indirect: direct contextual evidence tied to the named exchange/pair
  - weight: high

- **Strike is close to current spot rather than requiring a large move up**
  - source: Binance spot versus 74,000 strike
  - causal relevance: reduces the amount of bullish continuation needed
  - direct/indirect: direct contextual evidence
  - weight: medium

## Evidence against the claim

- **The contract resolves on one exact minute close**
  - source: Polymarket rules
  - causal relevance: adds timing/path dependence; current price level alone is insufficient
  - direct/indirect: direct contract evidence
  - weight: high

- **BTC short-horizon volatility is easily large enough to cross the threshold**
  - source: observed minute-to-minute Binance variation and general BTC market structure
  - causal relevance: a modest buffer above strike can vanish quickly
  - direct/indirect: partly direct, partly contextual
  - weight: high

## Ambiguous or mixed evidence

- Current spot being above 74,000 is supportive, but if the market already knows this and still prices only around 0.70, that may reflect correctly priced timestamp risk rather than mispricing.

## Conflict between inputs

There is little factual conflict. The main tension is weighting-based: how much confidence should be assigned to current above-threshold spot versus exact-time resolution fragility.

## Key assumptions

- Binance API pricing is a good practical proxy for the UI candle data named in the contract.
- No major venue-specific anomaly distorts the noon ET candle.
- BTC remains near current levels into April 17.

## Key uncertainties

- Short-horizon BTC volatility into the exact settlement minute.
- Whether April 17 U.S. session flow creates a risk-off move before noon ET.
- Exchange-specific microstructure around the relevant minute.

## Disconfirming signals to watch

- Sustained Binance BTC/USDT trade back below 74,000.
- Sharp risk-off move before April 17 noon ET.
- Exchange-specific odd candle behavior around settlement windows.

## What would increase confidence

- BTC holding comfortably above 74,500-75,000 on Binance into late April 16 / early April 17.
- Additional direct confirmation that Binance API and UI candle closes are matching cleanly.

## Net update logic

The direct exchange evidence pushes toward Yes because spot is currently above strike, but the exact-minute settlement design prevents a high-confidence conclusion. The market is directionally sensible, yet likely a bit too confident if it is implicitly treating 'currently above strike' as close to equivalent to 'above strike at the exact minute that matters.'

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review