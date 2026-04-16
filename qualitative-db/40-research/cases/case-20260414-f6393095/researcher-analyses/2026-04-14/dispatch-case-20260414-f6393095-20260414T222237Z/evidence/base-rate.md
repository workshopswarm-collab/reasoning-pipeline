---
type: evidence_map
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
research_run_id: e8efd8ac-ffdc-46b6-9bb9-5573d72e6844
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-17
question: "Will the price of Bitcoin be above $70,000 on April 17?"
driver: reliability
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["synthesis"]
tags: ["evidence-map", "bitcoin", "threshold-market"]
---

# Summary

The outside-view lean is Yes, but with a modest discount to the market because date-specific one-minute threshold contracts remain fragile to short, sharp BTC swings.

## Question being evaluated

Will Binance BTC/USDT print a final 12:00 ET one-minute candle close above $70,000 on Apr. 17, 2026?

## Current lean

Yes, with high but not extreme confidence.

## Prior / starting view

Given current spot already materially above threshold and only ~2.5 days to settlement, the generic base-rate prior should be strongly positive unless BTC is sitting right on the line or a known catalyst threatens a sharp drawdown.

## Evidence supporting the claim

- Binance daily kline history shows eight consecutive daily closes above $70,000 from Apr. 7 to Apr. 14.
  - Source: case source note on Binance price history
  - Why it matters causally: same venue and pair as settlement source; indicates current regime persistence
  - Direct or indirect: direct contextual evidence, though not exact interval
  - Weight: high
- Current market state on Polymarket prices the $70k line around 93.9% Yes.
  - Source: case source note on Polymarket contract and market state
  - Why it matters causally: aggregated trader view plus current spot context
  - Direct or indirect: indirect/contextual evidence
  - Weight: medium
- Recent daily lows on Binance remained above $70,000 despite volatility.
  - Source: Binance daily kline note
  - Why it matters causally: threshold cushion has persisted through ordinary swings
  - Direct or indirect: direct contextual evidence
  - Weight: medium-high

## Evidence against the claim

- Contract resolves on a single one-minute close at noon ET, not a daily close.
  - Source: Polymarket rules
  - Why it matters causally: one bad short-term move can flip the outcome
  - Direct or indirect: direct contract interpretation
  - Weight: high
- BTC can move several percent in under three days, so a drop from ~74k to below 70k is not a tail impossibility.
  - Source: general BTC volatility plus recent wide daily ranges in Binance data
  - Why it matters causally: threshold cushion is meaningful but not enormous
  - Direct or indirect: contextual evidence
  - Weight: medium-high

## Ambiguous or mixed evidence

- The market’s extreme 93%+ pricing could be justified by current regime, but it may also underweight short-horizon one-minute fragility.

## Conflict between inputs

No major factual conflict. The main issue is weighting: how much to discount same-venue spot strength for exact-minute settlement risk.

## Key assumptions

- The recent Binance BTC/USDT regime persists through Apr. 17 noon ET.
- No exchange-specific anomaly causes a one-minute undercut below 70,000.

## Key uncertainties

- Short-horizon BTC volatility over the next ~60 hours
- Potential macro/crypto news shocks before settlement
- Whether intraday downside tests intensify on Apr. 16-17

## Disconfirming signals to watch

- Binance BTC/USDT trades back toward 71k or lower before settlement
- Repeated intraday failures above 72k followed by accelerating downside
- Market repricing of the 70k line out of the 90s

## What would increase confidence

- Another day of Binance trading with lows safely above 70k
- No adverse macro headlines into Apr. 17
- Continued threshold ladder shape with 70k well separated from the 74k line

## Net update logic

The key update is not a story about new bullish catalysts. It is that same-venue Binance pricing already sits comfortably above the contract threshold and has stayed there for over a week. That pushes the base rate strongly toward Yes. The main discount comes from contract design: one exact minute still leaves room for a volatility-driven miss, so a modest haircut from the market is warranted.

## Suggested downstream use

- Orchestrator synthesis input
- Forecast update
- Decision-maker review
