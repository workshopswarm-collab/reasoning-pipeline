---
type: evidence_map
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416-2ab48f50-20260416T002737Z
research_run_id: 62d0984e-d722-44a1-979f-0116662f6a84
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: spot-price
entity: bitcoin
topic: bitcoin-above-74000-on-april-17
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17 close above 74,000?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: "low-direct-conflict high-interpretive-fragility"
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416-2ab48f50-20260416T002737Z/personas/variant-view.md"]
tags: ["evidence-map", "threshold-market", "binance", "intraday"]
---

# Summary

Current Binance spot state points toward Yes, but the variant case is that the market may be overconfident because the contract is decided by one minute at noon ET and the current cushion over 74,000 is not wide.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 close strictly above 74,000?

## Current lean

Slight lean No versus market pricing, despite current spot being above threshold.

## Prior / starting view

Starting baseline was the market-implied 61% Yes, which assumes current above-threshold status deserves more than even odds into tomorrow noon.

## Evidence supporting the claim

- Binance spot data shows BTC currently above 74,000 on the governing venue/pair family.
  - Source: source note `2026-04-16-variant-view-binance-spot-context.md`
  - Why it matters causally: if the asset is already above threshold, the path to Yes is shorter than if it were below.
  - Direct or indirect: direct for current state, indirect for tomorrow noon outcome.
  - Weight: high.
- Recent sampled 1-minute closes were above 74,000 761 out of 1,000 minutes.
  - Source: same Binance note.
  - Why it matters causally: suggests the market spent most of the recent window above threshold.
  - Direct or indirect: indirect/time-transported.
  - Weight: medium.

## Evidence against the claim

- The contract settles on one exact one-minute close at noon ET rather than on broader daily direction.
  - Source: source note `2026-04-16-variant-view-polymarket-rules.md`
  - Why it matters causally: one-minute point estimates are more fragile than general "above threshold sometime / most of day" narratives.
  - Direct or indirect: direct for contract mechanics.
  - Weight: high.
- The latest cushion above 74,000 was only around 500-700 dollars depending on sample point, while recent 1,000-minute standard deviation was about 377 and the sampled range crossed below 74,000 repeatedly.
  - Source: Binance note.
  - Why it matters causally: ordinary volatility can erase that cushion without needing a major regime shift.
  - Direct or indirect: direct for fragility of threshold clearance.
  - Weight: high.
- Only 32.4% of sampled closes were above 74,500, implying the market has not established a deep buffer over the threshold.
  - Source: Binance note.
  - Why it matters causally: if the threshold is barely being cleared, exact-time contracts deserve caution.
  - Direct or indirect: indirect but highly relevant.
  - Weight: medium.

## Ambiguous or mixed evidence

- Current cross-venue contextual prices from CoinGecko and Yahoo roughly match Binance, which supports the general level but does not directly settle the noon ET candle.
- The market's own 61% price may reflect some traders already accounting for point-in-time fragility, so disagreement should remain modest rather than extreme.

## Conflict between inputs

There is little factual conflict. The main disagreement is interpretive and weighting-based: how much should current above-threshold status carry into a narrow point-in-time contract roughly 15.5 hours later?

## Key assumptions

- Threshold fragility matters more than current bullish spot narrative.
- Binance API current/recent candle data is representative enough of the venue state to evaluate cushion and volatility.
- No major news shock is needed for price to drift back below 74,000; ordinary variance could be enough.

## Key uncertainties

- Overnight macro or crypto-specific news flow.
- How sticky the current above-74,000 regime is into the U.S. noon window.
- Small operational ambiguity between Binance UI candle presentation and API-delivered kline values.

## Disconfirming signals to watch

- Sustained trading well above 74,500 or 75,000 into the settlement window.
- Realized volatility compressing while price remains above threshold.
- Clear evidence that noon ET tends to align with strong spot support rather than random point-in-time noise.

## What would increase confidence

- Another verification pass closer to settlement showing BTC still above threshold with a wider cushion.
- Confirmation from Binance UI/candle interface that the exact noon ET observation method matches the API reading cleanly.

## Net update logic

The evidence starts from a bullish fact pattern because BTC is already above 74,000 on Binance. The variant update is not that BTC is likely to crash, but that the market may be slightly overpaying for a threshold that is only modestly cleared and settled at a single exact minute. That narrows the fair edge and pushes the estimate down toward roughly even.

## Suggested downstream use

Use as orchestrator synthesis input and as a caution against treating this as a generic daily BTC-direction market rather than a narrow time-specific threshold contract.