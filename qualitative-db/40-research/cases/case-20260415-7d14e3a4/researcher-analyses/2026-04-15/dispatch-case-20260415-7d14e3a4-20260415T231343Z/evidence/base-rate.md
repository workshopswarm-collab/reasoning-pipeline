---
type: evidence_map
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
research_run_id: ed48befe-3f2d-4329-bdfa-5c53846c308b
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-19
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 72000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "btc", "base-rate"]
---

# Summary

The evidence nets to a moderate Yes lean because BTC is currently comfortably above 72,000 on Binance and has recently spent most of its time above that line, but the contract resolves on a single future one-minute close, so short-horizon volatility still matters.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle corresponding to 12:00 ET on 2026-04-19 close above 72,000?

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

A generic short-horizon BTC threshold market a few days out should start with substantial uncertainty because Bitcoin can move several percent in either direction over a weekend. The prior should move toward Yes only if spot is already above the strike and the strike sits below the recent central trading range.

## Evidence supporting the claim

- Current Binance spot near 74.7k, around 3.8% above strike.
  - Source: 2026-04-15-base-rate-binance-btcusdt-price-context.md
  - Why it matters: distance-to-strike is the main structural edge in a short-dated threshold contract.
  - Direct or indirect: direct price context
  - Weight: high
- Recent Binance daily closes mostly above 72k, including 74.4k and 74.1k on Apr 13-14.
  - Source: 2026-04-15-base-rate-binance-btcusdt-price-context.md
  - Why it matters: suggests the threshold is below the recent central regime, not above it.
  - Direct or indirect: direct contextual market data
  - Weight: medium-high
- The contract settles on Binance BTC/USDT specifically, aligning the evidentiary venue with the observed data source.
  - Source: 2026-04-15-base-rate-polymarket-contract-rules.md plus Binance source note
  - Why it matters: lowers cross-venue basis risk for the main estimate.
  - Direct or indirect: direct contract interpretation
  - Weight: medium

## Evidence against the claim

- The market resolves on one exact future minute, not a daily close or average.
  - Source: 2026-04-15-base-rate-polymarket-contract-rules.md
  - Why it matters: a brief adverse move at the settlement minute can flip the market even if BTC spends most nearby time above 72k.
  - Direct or indirect: direct contract interpretation
  - Weight: high
- BTC has recently traded below 72k within the same week, including a 70.7k close on Apr 12 and lows near 70.5k.
  - Source: 2026-04-15-base-rate-binance-btcusdt-price-context.md
  - Why it matters: realized volatility is large enough that a 3-5% move lower by Sunday noon is plausible.
  - Direct or indirect: direct contextual market data
  - Weight: high
- Weekend / short-horizon crypto moves can be sharp and are hard to predict from simple trend persistence alone.
  - Source: inferred from the same recent Binance realized range
  - Why it matters: limits confidence in extrapolating current in-the-money status straight to the settlement minute.
  - Direct or indirect: contextual
  - Weight: medium

## Ambiguous or mixed evidence

- Polymarket pricing around 87% Yes may contain informed expectations, but it may also reflect trader extrapolation from current spot without enough discount for one-minute settlement risk.
- Recent price strength is supportive, but it may already be fully reflected in market price.

## Conflict between inputs

There is no major factual conflict between sources. The main tension is weighting-based: whether a spot price 3.8% above strike with a few days left deserves something near 87% or something closer to two-thirds.

## Key assumptions

- BTC stays in the current mid-70k regime through settlement.
- No material Binance-specific operational anomaly affects the settlement print.
- Noon-ET mapping to the Binance minute candle corresponds to 16:00 UTC during daylight time.

## Key uncertainties

- Short-horizon BTC volatility into a single minute.
- Whether weekend flow weakens BTC enough to revisit sub-72k levels.
- Whether the market has already correctly priced that volatility.

## Disconfirming signals to watch

- BTC losing 73k and then 72k before April 19.
- Repeated noon-ET weakness on Apr 16-18.
- Evidence of Binance-specific basis dislocation or data anomalies.

## What would increase confidence

- BTC remaining above roughly 74k through Apr 17-18.
- Additional independent chart/context source showing no hidden contract ambiguity.
- Continued Binance trading with lows staying meaningfully above 72k.

## Net update logic

The base-rate prior for a 4-day BTC threshold market should be uncertain, but the current distance above strike and recent realized distribution move the estimate above 50%. I do not go as high as the market because the contract is a narrow one-minute settlement and BTC has shown enough recent volatility that a sub-72k print on the relevant minute remains materially possible.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the base-rate lane is mildly contrarian versus the 87% market price.