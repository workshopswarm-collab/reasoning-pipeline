---
type: evidence_map
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: 26c93914-c5c6-45b7-bbb4-2001b4d5f8b5
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: ethereum-above-2100-on-april-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: operational-risk
date_created: 2026-04-09
agent: risk-manager
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/risk-manager.md"]
tags: ["evidence-map", "settlement-risk", "crypto"]
---

# Summary

The evidence nets to a Yes lean, but the risk-manager view is less bullish than the market because a one-minute noon snapshot creates path and timing risk that a 94% market may be underpricing.

## Question being evaluated

Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 10, 2026 have a final close above $2,100?

## Current lean

Lean Yes, but not as confidently as the market.

## Prior / starting view

Starting point was the market-implied 94% Yes probability from current_price 0.94.

## Evidence supporting the claim

- Current Polymarket board state shows the 2100 line trading around 97.4 cents Yes, implying strong crowd confidence that ETH will remain above the threshold into the relevant window.
  - directness: contextual / market-based
  - weight: medium
- Nearby ladder pricing is internally coherent: 2000 is near certainty, 2200 is around 60%, and 2300 is low, implying the market sees spot ETH materially above 2100 but not safely above 2200.
  - directness: contextual
  - weight: medium
- Binance sample 1-minute klines show ETH trading around 2211-2213 at the verification time, which is about $110 above the threshold and therefore gives some immediate buffer.
  - directness: direct exchange data, though not at resolution time
  - weight: high

## Evidence against the claim

- The market is not about daily close or broad exchange consensus; it is about a single Binance 1-minute candle at noon ET. That injects path dependence and minute-specific noise.
  - directness: direct rule-based
  - weight: high
- The governing evidence family is effectively single-source: Binance provides both the operative price surface and the timestamp conventions. That limits independence and leaves residual settlement-mechanics risk.
  - directness: direct
  - weight: medium-high
- If ETH is only modestly above 2100 by tomorrow, a brief intraminute downswing ending below the threshold at the final print could still resolve No even if the broader daily thesis stays bullish.
  - directness: inferential but mechanically central
  - weight: high

## Ambiguous or mixed evidence

- The Binance API clearly uses UTC timestamps, but Polymarket references the Binance UI chart. Those usually align, yet exact UI labeling was not independently captured here.
- High crowd confidence could reflect real information, but it can also overcompress uncertainty in mechanically narrow crypto intraday markets.

## Conflict between inputs

No major factual conflict found. The main issue is weighting-based: how much discount should be applied for single-minute timing risk and single-source settlement dependence.

## Key assumptions

- Noon ET maps to the Binance candle opening at 16:00:00 UTC on April 10.
- The API kline structure matches the practical chart-resolution surface closely enough for interpretation.
- ETH does not suffer a sharp price move that erases the current cushion before the relevant minute closes.

## Key uncertainties

- Exact ETH level relative to 2100 as the resolution minute approaches.
- Whether any UI/API labeling mismatch could matter in a close call.
- How much of the market’s confidence is justified versus simply momentum-following around current spot.

## Disconfirming signals to watch

- ETH trading back toward 2120 or below before noon ET April 10.
- Clarification that the relevant candle labeling differs from the assumed 16:00 UTC mapping.
- Short-term volatility spike that makes a one-minute close below 2100 plausible despite current cushion.

## What would increase confidence

- A fresh check closer to resolution still showing ETH comfortably above 2100.
- Independent confirmation from Binance chart docs or UI screenshot that the candle labeling convention matches the API interpretation.

## Net update logic

The biggest positive is simple: exchange-traded ETH is currently well above the threshold. The biggest negative is equally simple: the contract is resolved by a single minute on a single venue, so extreme certainty is harder to justify than for a broader daily-close question. That combination supports Yes but argues for trimming confidence versus market.

## Suggested downstream use

Use as an orchestrator synthesis input and as a caution against over-weighting the raw 94% market price without accounting for minute-level timing and operational interpretation risk.