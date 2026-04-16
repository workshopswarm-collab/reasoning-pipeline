---
type: evidence_map
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
research_run_id: 6756b604-71d6-404a-8f94-b896b4124a91
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: spot-price
entity: bitcoin
topic: bitcoin-above-70k-on-april-16
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 70000?"
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
downstream_uses: ["orchestrator synthesis", "decision-maker review"]
tags: ["evidence-map", "base-rate", "btc"]
---

# Summary

The evidence nets to Yes, but less confidently than the market's 98.5% implication. The base-rate case is that BTC currently has meaningful cushion over 70000, while the main reason not to mirror the market is that crypto can still move several thousand dollars inside one day and the contract resolves on one exact minute.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 70000?

## Current lean

Lean Yes.

## Prior / starting view

Before checking current data, the outside-view prior for a one-day threshold market with BTC already above the strike is Yes-leaning but not near-certain because crypto short-horizon volatility is nontrivial.

## Evidence supporting the claim

- Binance spot price during the run was around 73.6k-74.1k.
  - Source: 2026-04-15-base-rate-binance-market-data.md
  - Why it matters: the threshold is several thousand dollars lower than current spot.
  - Direct or indirect: direct contextual evidence from the governing exchange.
  - Weight: high.

- Recent daily closes mostly sat between 71k and 74k, above the 70k threshold.
  - Source: 2026-04-15-base-rate-binance-market-data.md
  - Why it matters: suggests the threshold is below the center of the recent regime rather than above it.
  - Direct or indirect: direct contextual evidence.
  - Weight: medium-high.

- Recent hourly candles stayed above 73.5k during the 24-hour window checked.
  - Source: Binance hourly klines captured during this run.
  - Why it matters: no immediate evidence of the market drifting toward the threshold.
  - Direct or indirect: direct contextual evidence.
  - Weight: medium.

## Evidence against the claim

- Recent daily lows reached about 70.5k, showing that a move of several thousand dollars inside a day is feasible.
  - Source: 2026-04-15-base-rate-binance-market-data.md
  - Why it matters: the downside tail is real and makes 98.5% look too high.
  - Direct or indirect: direct contextual evidence.
  - Weight: high.

- The contract resolves on one exact minute, not a daily close or average.
  - Source: 2026-04-15-base-rate-polymarket-rules.md
  - Why it matters: a brief intraday dip at the wrong moment is enough to flip the outcome.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.

## Ambiguous or mixed evidence

- The market itself prices Yes around 98.5%, which is informative but may partly reflect momentum-chasing or underweighting of one-minute timing risk.

## Conflict between inputs

There is no strong factual conflict. The tension is weighting-based: current price level strongly supports Yes, while volatility plus exact-minute settlement argues against extreme certainty.

## Key assumptions

- BTC remains in roughly the recent trading regime through tomorrow noon ET.
- Binance BTC/USDT remains representative and operationally normal at the settlement minute.

## Key uncertainties

- Short-horizon volatility overnight into the settlement minute
- Whether any fresh macro or crypto-specific shock emerges before noon ET
- Exact practical mapping of the ET-labeled noon minute to the observed Binance candle display, though the contract wording itself is fairly clear

## Disconfirming signals to watch

- Binance BTC/USDT falling toward 71k-72k before the morning of April 16
- A large risk-off move across crypto
- Exchange-specific operational issues on Binance

## What would increase confidence

- BTC holding above roughly 73k into the late morning of April 16
- Another verification pass close to the event showing Binance still comfortably above the threshold

## Net update logic

The main update versus a neutral prior is simple: current Binance spot is materially above 70000 and recent closes mostly support that regime. The main downward adjustment versus market price is that one-day BTC volatility is still large enough that a 98.5% estimate feels too aggressive for a one-minute threshold market.

## Suggested downstream use

Use as orchestrator synthesis input and as a check against overconfident market anchoring.