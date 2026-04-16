---
type: evidence_map
case_key: case-20260415-1e5e80f9
dispatch_id: dispatch-case-20260415-1e5e80f9-20260415T080017Z
research_run_id: b7212269-8e66-47fc-b05d-6e587075e711
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-16
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 16 be above 72000?"
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-1e5e80f9/researcher-analyses/2026-04-15/dispatch-case-20260415-1e5e80f9-20260415T080017Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "binance", "timing-risk"]
---

# Summary

This evidence map nets a straightforward but timing-sensitive crypto contract: direct rule clarity plus an above-strike current price support Yes, while the main residual risk is a sharp move into one exact settlement minute.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for April 16 at 12:00 ET have a final close above 72,000?

## Current lean

Lean Yes, high but not extreme confidence.

## Prior / starting view

Starting baseline was the market-implied probability around 82.5% Yes.

## Evidence supporting the claim

- Polymarket rules clearly define settlement on Binance BTC/USDT 12:00 ET 1-minute close above 72,000.
  - direct
  - high weight
  - matters because it removes most wording ambiguity
- Binance public API check showed BTCUSDT around 73,722.51 on April 15.
  - direct contextual market evidence
  - high weight
  - matters because price was already materially above strike with some cushion
- Recent Binance 1-minute klines endpoint returned normal data.
  - direct contextual/operational evidence
  - medium weight
  - matters because it supports confidence in the relevant exchange data surface being live and standard

## Evidence against the claim

- The market settles on one exact minute close, not on average price, intraday high, or current pre-resolution spot.
  - direct contract-mechanics risk
  - high weight
  - matters because path dependence is the core failure mode
- BTC can move by more than the current cushion over a day, especially under macro or crypto-specific shock.
  - indirect contextual risk
  - medium weight
  - matters because the contract is short-dated and vulnerable to one sharp downside move
- Exchange-specific microstructure or timestamp interpretation issues can matter more than broader market direction in narrow-resolution contracts.
  - indirect but structurally relevant
  - low-to-medium weight
  - matters because Binance-specific close governs, not broader consensus price

## Ambiguous or mixed evidence

- Current spot being above strike is strongly supportive, but how supportive depends on expected near-term volatility and path risk, which were not deeply modeled in this run.
- Market price already embeds much of the obvious support, so the main question is whether confidence has become slightly too high for a one-candle contract.

## Conflict between inputs

No major factual conflict. The main issue is weighting: how much discount should be applied for single-candle timing risk versus the current above-strike cushion.

## Key assumptions

- The Binance API spot/context is representative enough to infer that Yes is favored, while recognizing it is not the settlement candle itself.
- No major new shock occurs before noon ET on April 16.
- The Polymarket rule text accurately captures the governing source and timing mechanics.

## Key uncertainties

- Exact BTC path into settlement minute.
- Whether volatility between now and settlement is ordinary or shock-driven.
- Any last-minute Binance-specific anomalies.

## Disconfirming signals to watch

- BTC loses most of its cushion and trades close to 72,000 before settlement.
- A broad risk-off move or crypto-specific liquidation event emerges.
- Evidence of ambiguity in how the noon ET candle is mapped or displayed.

## What would increase confidence

- BTC remains comfortably above 72,000 closer to settlement.
- Independent confirmation from a second Binance data surface or chart capture near resolution.
- Stable market action without major macro catalysts before noon ET.

## Net update logic

The evidence keeps the view in Yes territory because the contract wording is clear and current price sits above strike. The main downward adjustment from a near-certainty view comes from path dependence: one narrow resolution minute means a fast selloff could still flip the outcome.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why this risk-manager view is slightly more conservative than a purely spot-based read.