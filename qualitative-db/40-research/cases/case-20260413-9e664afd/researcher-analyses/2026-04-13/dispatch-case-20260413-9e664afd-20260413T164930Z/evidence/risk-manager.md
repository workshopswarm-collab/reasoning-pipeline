---
type: evidence_map
case_key: case-20260413-9e664afd
dispatch_id: dispatch-case-20260413-9e664afd-20260413T164930Z
research_run_id: d9a2a364-1821-4857-ac23-b84546a89590
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-1-minute-candle-on-2026-04-14-close-above-70000
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-14 close above 70000?"
driver: operational-risk
date_created: 2026-04-13T12:52:00-04:00
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-9e664afd/researcher-analyses/2026-04-13/dispatch-case-20260413T164930Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "binance", "timing"]
---

# Summary

This case is mostly about contract mechanics plus short-horizon volatility. The strongest support is that Binance BTC/USDT is already above 72k, giving a >2k cushion. The strongest risk is that only one venue and one exact minute close count, so path risk is underpriced if traders overgeneralize from current spot.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-14 have a final close above 70,000?

## Current lean

Lean Yes, but with more fragility than a simple current-spot comparison suggests.

## Prior / starting view

Starting baseline was the market price of 0.845, implying 84.5% for Yes.

## Evidence supporting the claim

- Binance direct price data shows BTC/USDT around 72.3k during research.
  - direct
  - high weight
  - matters because the market only needs a close above 70k, not a move to a new level
- The threshold is only about 3.2% below observed spot.
  - indirect calculation from direct price data
  - medium-high weight
  - matters because a modest cushion exists entering the final 24 hours
- Polymarket rules are clear that the relevant timestamp is noon ET on Apr 14.
  - direct contract interpretation
  - medium weight
  - matters because there is little ambiguity about what counts for settlement

## Evidence against the claim

- The contract is narrow: only the Binance BTC/USDT 12:00 ET one-minute close matters.
  - direct from Polymarket rules
  - high weight
  - this makes temporary downside at the wrong moment sufficient for No
- BTC can move more than 3% within a day, especially around macro or sentiment shocks.
  - contextual / market-structure knowledge
  - medium weight
  - the current cushion is meaningful but not overwhelming
- Venue-specific prints can diverge from broader market impressions.
  - contextual
  - medium weight
  - matters because other exchanges being above 70k would not save a No on Binance

## Ambiguous or mixed evidence

- High market confidence may reflect reasonable base rates, but it may also compress uncertainty too much for a one-minute close contract.

## Conflict between inputs

There is no strong factual conflict in the collected evidence. The main disagreement is weighting-based: whether an ~84.5% implied probability is too confident given the narrow settlement mechanics.

## Key assumptions

- BTC remains above 70k on Binance through noon ET tomorrow.
- No Binance-specific pricing anomaly materially distorts the relevant one-minute close.

## Key uncertainties

- Short-horizon BTC volatility into the Apr 14 noon ET window.
- Any exogenous catalyst before settlement.

## Disconfirming signals to watch

- BTC losing 71k and approaching 70k before the final morning.
- Binance-specific price weakness relative to other venues.
- Elevated volatility around the noon ET window.

## What would increase confidence

- BTC holding comfortably above 71k into the U.S. morning on Apr 14.
- Cross-venue stability with no Binance-specific dislocation.

## Net update logic

Direct exchange data and clear rules support Yes, but the risk-manager adjustment is to discount some market confidence because the contract resolves on a single exact minute close. That makes timing and venue-specific fragility more important than in a generic daily close intuition.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- retrospective evaluation