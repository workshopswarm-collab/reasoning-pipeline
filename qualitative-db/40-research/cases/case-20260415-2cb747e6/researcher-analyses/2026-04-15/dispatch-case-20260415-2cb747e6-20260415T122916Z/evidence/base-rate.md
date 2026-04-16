---
type: evidence_map
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
research_run_id: 7e669a3c-67a1-4abc-99d1-3fcecb033780
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: markets
entity: bitcoin
topic: bitcoin-above-72k-on-april-16
question: "Will the price of Bitcoin be above $72,000 on April 16?"
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
downstream_uses: ["base-rate finding", "orchestrator synthesis input"]
tags: ["evidence-map", "short-horizon", "threshold-market"]
---

# Summary

Net evidence favors Yes because BTC/USDT is already above the threshold on the correct venue, but the market’s near-90% pricing looks somewhat rich versus the remaining one-day downside risk for a single-minute settlement condition.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 16, 2026 close above 72,000?

## Current lean

Lean Yes, but with less confidence than the market implies.

## Prior / starting view

Before checking current price context, the outside-view prior for a one-day threshold market should center on current distance from strike versus usual 24-hour volatility, with a discount for single-minute timing risk.

## Evidence supporting the claim

- Binance direct price context shows BTC/USDT around 74.2k on April 15.
  - source: Binance public API source note
  - why it matters causally: the contract uses Binance BTC/USDT specifically, so current venue-matched level is the most relevant starting point
  - direct or indirect: direct
  - weight: high

- Recent daily closes have been above 72,000 on most of the last several days.
  - source: Binance public API source note
  - why it matters causally: demonstrates that 72,000 is already an in-range, recently sustained level rather than a distant upside target
  - direct or indirect: direct/contextual hybrid
  - weight: medium-high

- The threshold is only about 3% below checked spot, which usually favors persistence over a 24-hour horizon absent a new shock.
  - source: inferred from Binance direct data
  - why it matters causally: short-horizon threshold probability is largely a function of distance to strike relative to realized volatility
  - direct or indirect: contextual
  - weight: medium

## Evidence against the claim

- Recent daily ranges have often been large enough that a move back below 72,000 by the exact noon ET minute is plausible.
  - source: Binance public API source note
  - why it matters causally: this is a single-minute settlement market, so temporary downside excursions matter a lot
  - direct or indirect: direct/contextual hybrid
  - weight: high

- April 12 daily close was below 72,000 even though the asset had also recently traded above that level.
  - source: Binance public API source note
  - why it matters causally: shows the threshold is not securely locked and can be lost on routine volatility
  - direct or indirect: direct
  - weight: medium

- Market resolution depends on a strict greater-than test on one exact Binance minute candle.
  - source: Polymarket rules source note
  - why it matters causally: this creates timing/path dependence; being above 72,000 broadly is not enough if the exact reference minute prints lower
  - direct or indirect: direct
  - weight: high

## Ambiguous or mixed evidence

- The live market probability near 89.5%-90% may reflect informed order flow, but it may also underweight short-horizon realized volatility because traders anchor on the current spot level being above strike.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much to trust current spot persistence versus the risk of a one-day downside move into the exact settlement minute.

## Key assumptions

- Recent volatility regime remains a useful guide through settlement.
- Binance API price context is sufficiently aligned with the settlement-source candle.
- No major shock emerges before noon ET April 16.

## Key uncertainties

- Whether a macro or crypto-specific catalyst lands before settlement.
- Whether BTC can hold above 72,000 specifically at noon ET rather than just on average over the day.

## Disconfirming signals to watch

- BTC trades back toward 73,000 or below during the final hours before settlement.
- Volatility expands materially versus recent ranges.
- Binance reference pricing or UI interpretation becomes operationally ambiguous.

## What would increase confidence

- Additional venue-matched verification closer to settlement showing BTC still comfortably above 72,000.
- Evidence that realized hourly volatility is compressing rather than expanding.

## Net update logic

The base-rate prior started with a modest Yes lean because the asset is already above strike. Direct Binance data strengthened that lean, but not enough to justify the full market price, because the contract settles on a single exact minute and recent BTC volatility leaves room for a sub-72k print without requiring an extreme shock.

## Suggested downstream use

Use as an orchestrator synthesis input and as a caution against over-reading the current above-strike level as near-certainty.