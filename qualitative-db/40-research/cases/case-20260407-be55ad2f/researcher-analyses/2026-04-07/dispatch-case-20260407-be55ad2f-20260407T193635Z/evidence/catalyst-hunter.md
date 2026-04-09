---
type: evidence_map
case_key: case-20260407-be55ad2f
dispatch_id: dispatch-case-20260407-be55ad2f-20260407T193635Z
research_run_id: 7ea3a3e5-58b0-4c68-a256-d7a99c31967b
analysis_date: 2026-04-07
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-66k-on-april-8
question: "Will the price of Bitcoin be above $66,000 on April 8?"
driver: operational-risk
date_created: 2026-04-07T15:41:00-04:00
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-be55ad2f/researcher-analyses/2026-04-07/dispatch-case-20260407-be55ad2f-20260407T193635Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "bitcoin", "binance", "settlement"]
---

# Summary

The evidence nets to a high-probability Yes view, with the dominant remaining risk being short-horizon BTC downside into the exact April 8 12:00 ET Binance minute close rather than unclear contract mechanics.

## Question being evaluated

Will the Binance BTCUSDT 1-minute candle for 12:00 ET on April 8, 2026 have a final close price above 66,000?

## Current lean

Lean Yes, high probability but not near-certainty.

## Prior / starting view

Starting view from the market was already strongly Yes because the quoted market-implied probability was 0.896.

## Evidence supporting the claim

- Direct live Binance BTCUSDT spot during this run was about 68.47k, comfortably above the 66k threshold.
  - direct
  - high weight
  - matters because current cushion reduces the probability that ordinary noise alone pushes the final noon close below 66k
- Polymarket rules explicitly settle on Binance BTCUSDT 1m close at 12:00 ET, and Binance docs support timezone-specific kline interpretation.
  - direct on mechanics
  - high weight
  - matters because it reduces resolution ambiguity and lets the risk focus on price path
- Time to expiry is short enough that only a limited set of catalysts can still matter materially: macro shock, crypto-specific headline shock, or exchange-specific dislocation.
  - contextual
  - medium weight
  - matters because absent a shock, current cushion should usually survive to noon tomorrow

## Evidence against the claim

- BTC is volatile enough that a 3% to 4% downside move in less than a day is entirely plausible.
  - contextual
  - high weight
  - matters because the current cushion over 66k is meaningful but not enormous
- The market resolves on one exact one-minute Binance close, which creates path dependence and increases sensitivity to a brief sharp move or exchange-specific dislocation.
  - direct on mechanics
  - medium-high weight
  - matters because a tradeable intraminute selloff right at the resolving minute can decide the market even if broader BTC sentiment remains constructive

## Ambiguous or mixed evidence

- The extreme market structure across adjacent threshold markets suggests this market is mostly a localized threshold pricing problem rather than a broad directional disagreement about BTC itself.
- Polymarket page data visible through fetch showed the 66k line around 93.2%, slightly above the assignment snapshot price of 89.6%, implying either movement or scraping mismatch; this is not decision-critical but is a reminder to anchor on the assignment baseline for comparison.

## Conflict between inputs

There is no major factual conflict. The main uncertainty is weighting-based: how much to penalize the thesis for BTC's ability to move several percent in a short window.

## Key assumptions

- Binance web-chart and API timezone mechanics are aligned closely enough that the direct API verification is informative for settlement mechanics.
- No major overnight/morning catalyst forces a downside repricing larger than the current cushion.

## Key uncertainties

- Overnight macro tape and crypto-specific headline flow
- Exchange-specific wick or liquidity event at the resolving minute
- Whether BTC's current level is stable support or just a transient local high

## Disconfirming signals to watch

- BTCUSDT trading down toward 66.5k or lower before the US morning
- Visible Binance-specific price dislocation versus broader BTC spot
- Fresh risk-off macro impulse before noon ET

## What would increase confidence

- BTC holding above 67.5k into the US morning on April 8
- A pre-resolution verification pass confirming Binance still trades with a comfortable cushion above 66k
- A direct screenshot/manual chart check of the final resolving minute once available

## Net update logic

The evidence did not overturn the market's strong Yes lean. Instead it narrowed the mechanism: this is chiefly a volatility-and-timing problem around one exact minute. The direct-source mechanics check slightly increases confidence because it reduces the chance of a hidden settlement misunderstanding.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- pre-resolution verification reminder for the final Binance minute
