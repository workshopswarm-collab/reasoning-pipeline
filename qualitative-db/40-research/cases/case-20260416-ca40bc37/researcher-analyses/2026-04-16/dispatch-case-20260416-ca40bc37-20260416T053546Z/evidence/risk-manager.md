---
type: evidence_map
case_key: case-20260416-ca40bc37
dispatch_id: dispatch-case-20260416-ca40bc37-20260416T053546Z
research_run_id: 1fc1ee5f-f4b7-4c12-b6f3-ed33622bfa41
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-20
question: "Will the price of Bitcoin be above $72,000 on April 20?"
driver: operational-risk
date_created: 2026-04-16
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
downstream_uses: []
tags: ["evidence-map", "bitcoin", "risk-manager", "timing-risk"]
---

# Summary

Evidence favors Yes because BTC is currently materially above 72,000 and the threshold ladder is internally coherent, but the contract remains fragile because one exact Binance minute close at noon ET decides resolution.

## Question being evaluated

Will Binance BTC/USDT close above 72,000 on the 12:00 ET one-minute candle on 2026-04-20?

## Current lean

Lean Yes, but with lower confidence than the market price implies.

## Prior / starting view

Starting view was that a market priced at 84.5% Yes probably reflected BTC already trading well above the threshold, but required stress-testing because date-specific minute-close contracts often hide path and timing risk.

## Evidence supporting the claim

- Live Binance BTCUSDT around 75.1k at capture time.
  - Source: Binance live ticker/source note.
  - Causal relevance: gives a current cushion of roughly 3k above the threshold.
  - Direct vs indirect: indirect for settlement, but directly from the designated exchange.
  - Weight: high.
- Polymarket threshold ladder is monotonic around the strike: 70k ~94%, 72k ~84-85%, 74k ~65-66%, 76k ~38-39%.
  - Source: Polymarket event page/source note.
  - Causal relevance: suggests the market is internally pricing the nearby threshold distribution in a sensible way rather than showing obvious mispricing.
  - Direct vs indirect: indirect contextual evidence.
  - Weight: medium.
- Only four days remain to resolution.
  - Source: assignment plus event page.
  - Causal relevance: limited time can favor the side already above strike if no major shock occurs.
  - Direct vs indirect: contextual.
  - Weight: medium.

## Evidence against the claim

- Binance 24-hour low was about 73.5k, which is not far above the 72k threshold in BTC terms.
  - Source: Binance 24-hour ticker/source note.
  - Causal relevance: shows the current cushion is real but not huge relative to plausible short-horizon volatility.
  - Direct vs indirect: indirect contextual evidence from designated exchange.
  - Weight: high.
- Contract resolves on one exact Binance one-minute close at 12:00 ET, not on sustained trading above the threshold.
  - Source: Polymarket rules plus Binance kline mechanics.
  - Causal relevance: timing/path dependence can create failure even if the broader bullish thesis is right.
  - Direct vs indirect: direct contract-interpretation evidence.
  - Weight: high.
- Binance UI rather than API is named in the rules.
  - Source: Polymarket rules.
  - Causal relevance: small but nonzero operational ambiguity if UI display or final published candle representation differs from API expectations.
  - Direct vs indirect: direct source-of-truth ambiguity.
  - Weight: low to medium.

## Ambiguous or mixed evidence

- BTC being above the strike today is supportive, but crypto can move several percent in a day, so present distance from strike is not decisive.
- The market price itself is informative, but for a risk-manager it may also signal excess confidence if traders are underweighting exact-minute resolution risk.

## Conflict between inputs

There is little direct source conflict. The main tension is between directional price cushion evidence and contract fragility/timing risk.

## Key assumptions

- BTC remains broadly above 72k into April 20.
- No sharp selloff or noon-specific dip hits the exact relevant minute.
- Binance's displayed final minute candle aligns with the expected interpretation from documented kline mechanics.

## Key uncertainties

- Short-horizon BTC volatility between now and April 20.
- Whether the 3k cushion is enough once exact-minute resolution risk is priced correctly.
- Small residual ambiguity from rules naming the Binance UI rather than a formal API endpoint.

## Disconfirming signals to watch

- BTC revisiting or breaking below 73k before April 20.
- Elevated macro or crypto event risk before the settlement window.
- Any sign of Binance data-display inconsistency around minute candles.

## What would increase confidence

- BTC holding comfortably above 74k-75k into April 19-20.
- Additional confirmation that the Binance UI candle and API kline remain aligned for minute-close interpretation.
- Lower realized volatility heading into the settlement window.

## Net update logic

The evidence supports a Yes lean because the market is not starting from the threshold; BTC already has meaningful cushion. But the risk-manager discount comes from how narrow the contract is. The market's ~84.5% probability looks somewhat rich relative to a contract that can fail on one bad minute, so the final estimate stays below market rather than matching it.

## Suggested downstream use

Use this as an orchestrator synthesis input and forecast update input, with emphasis on path dependence, exact-minute resolution mechanics, and the fact that uncertainty here is mostly timing/fragility rather than a broad directional anti-BTC thesis.
