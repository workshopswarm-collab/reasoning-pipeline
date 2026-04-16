---
type: evidence_map
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
research_run_id: 099e839f-c1b7-4b90-9771-cd9462c13fcd
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-at-12-00-pm-et-on-2026-04-17-close-above-70000
question: "Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 70000?"
driver: reliability
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["orchestrator synthesis input"]
tags: ["evidence-map", "market-implied", "btc"]
---

# Summary

Evidence nets to a high-probability Yes view with a small discount to the live market because current spot and neighboring strikes support the market's thesis, while short-horizon volatility and narrow settlement timing prevent treating 93% as fully locked.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 70,000?

## Current lean

Lean Yes, high probability but not near certainty.

## Prior / starting view

Start from the market's 92.5%-93% Yes prior because the market is liquid enough and the strike ladder contains useful distributional information.

## Evidence supporting the claim

- **Binance current spot around 74,293.57**
  - source: Binance ticker / source note
  - why it matters: direct governing-source evidence; current price sits ~6.1% above strike
  - direct or indirect: direct
  - weight: high

- **Recent Binance daily closes mostly above 70k with recent closes in low/mid 70k range**
  - source: Binance daily klines / source note
  - why it matters: shows 70k is below the recent center of mass rather than a knife-edge threshold
  - direct or indirect: direct
  - weight: high

- **Strike ladder centered above 70k (72k ~77%, 74k ~51%)**
  - source: Polymarket event page / source note
  - why it matters: crowd is implicitly pricing a distribution centered near 74k rather than just barely defending 70k
  - direct or indirect: direct for market beliefs, indirect for underlying outcome
  - weight: medium-high

## Evidence against the claim

- **Crypto can move >6% in three days**
  - source: inferred from recent Binance range and crypto volatility
  - why it matters: current cushion is meaningful but not insurmountable
  - direct or indirect: indirect/contextual
  - weight: medium

- **Settlement is a single exchange-specific 1-minute close at noon ET**
  - source: Polymarket rules / source note
  - why it matters: narrow timing and venue specificity create path dependence and small operational/timing risk
  - direct or indirect: direct contract mechanic
  - weight: medium

## Ambiguous or mixed evidence

- CoinGecko cross-check supports the general BTC pricing regime but adds little incremental value beyond confirming Binance is not obviously anomalous.

## Conflict between inputs

No major factual conflict. The only tension is weighting: market says ~93% while a cautious forecaster may trim slightly for volatility and narrow-resolution mechanics.

## Key assumptions

- BTC remains in roughly the recent 71k-76k regime into Apr 17.
- No exchange-specific distortion on Binance at the settlement minute.
- The market is using the strike ladder efficiently rather than overreacting to current spot.

## Key uncertainties

- Whether macro or crypto-specific news causes a sharp drawdown before settlement.
- Whether noon ET Friday price behavior differs materially from current observations.

## Disconfirming signals to watch

- BTC loses 72k decisively on Binance.
- Neighboring strike prices reprice materially lower, especially 72k and 74k.
- Any Binance-specific trading or data integrity issues near settlement.

## What would increase confidence

- Additional Binance price checks closer to Apr 17 showing BTC still comfortably above 72k.
- Stable ladder pricing with 70k remaining >90% while 72k/74k stay firm.

## Net update logic

The market prior already looked sensible. Direct Binance data confirms the strike is materially in the money right now, and the neighboring strikes suggest the market is not just extrapolating one print but embedding a broader distribution above 70k. The remaining haircut comes from ordinary crypto volatility plus a narrow single-minute settlement rule.

## Suggested downstream use

Use as an orchestrator synthesis input supporting a high-probability Yes view while preserving explicit caution on narrow settlement mechanics and downside volatility.
