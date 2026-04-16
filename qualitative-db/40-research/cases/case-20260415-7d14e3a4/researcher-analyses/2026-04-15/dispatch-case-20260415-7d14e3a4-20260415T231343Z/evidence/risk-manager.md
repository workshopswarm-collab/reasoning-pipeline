---
type: evidence_map
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
research_run_id: a704258f-8c1e-4f6e-9857-8ac2f5424e69
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-for-2026-04-19-12-00-et-close-above-72000
question: "Will the Binance BTC/USDT 1-minute candle for 2026-04-19 12:00 ET close above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: final
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["personas/risk-manager.md"]
tags: ["evidence-map", "settlement-risk", "timing-risk", "bitcoin"]
---

# Summary

Evidence nets to a high-but-not-extreme Yes lean: current Binance pricing and recent closes support the threshold being cleared, but the contract's exact-minute settlement design creates underappreciated path risk.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle corresponding to 2026-04-19 12:00 ET have a final close strictly above 72,000?

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

Starting view was that an 86.5% market price might be too confident for a date-specific, one-minute-candle contract unless BTC had a very large cushion above 72,000.

## Evidence supporting the claim

- `researcher-source-notes/2026-04-15-risk-manager-binance-price-context.md`
  - Binance ticker showed BTCUSDT around 74,676.98 on 2026-04-15.
  - Causal relevance: gives a meaningful cushion above the threshold with only four days left.
  - Directness: direct for current price context, indirect for final settlement.
  - Weight: high.

- `researcher-source-notes/2026-04-15-risk-manager-binance-price-context.md`
  - Recent daily closes on Binance remained above 72,000 for several consecutive days.
  - Causal relevance: suggests threshold is not being held by a single transient spike.
  - Directness: indirect/contextual.
  - Weight: medium-high.

## Evidence against the claim

- `researcher-source-notes/2026-04-15-risk-manager-polymarket-rules.md`
  - Contract resolves on one exact 1-minute close at noon ET, not an average, daily close, or intraday high.
  - Causal relevance: increases vulnerability to exact timing and transient dips.
  - Directness: direct for contract interpretation.
  - Weight: high.

- `researcher-source-notes/2026-04-15-risk-manager-binance-price-context.md`
  - Cushion is only about 3.7% above the line, which is meaningful but not enormous for BTC over four days.
  - Causal relevance: a modest drawdown could flip outcome despite bullish broader trend.
  - Directness: indirect/contextual.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Market price near 86.5% is itself informative, but could partly reflect traders compressing path risk into a simple directional BTC view.
- Binance API verification strengthens timing interpretation, but does not eliminate operational ambiguity around final UI-visible candle sourcing at settlement.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: current price cushion supports Yes, while contract mechanics argue for discounting overconfidence.

## Key assumptions

- Recent above-threshold trading persists through the specific noon ET settlement minute.
- No exchange-specific anomaly or interpretation problem affects the relevant candle.
- Broad BTC weakness does not reappear before April 19.

## Key uncertainties

- Short-horizon BTC volatility over the remaining days.
- Exact path into the noon ET print.
- Residual operational ambiguity if Binance display/data behavior changes.

## Disconfirming signals to watch

- BTCUSDT falling back below 72,000 before April 19.
- Repeated rejection around 74k and loss of daily-close support.
- Any Binance data outage or candle-display inconsistency.

## What would increase confidence

- Another 24-48 hours of Binance spot holding clearly above 72,000.
- A widening cushion above 74,000.
- Additional confirmation that the exact noon ET 1-minute candle is straightforward to observe and stable on Binance.

## Net update logic

The evidence moved the starting view from skepticism about an extreme price to a still-skeptical but positive lean. What mattered most was the direct Binance price cushion and recent closes. What remained downweighted but still important was the one-minute exact-time settlement structure, which keeps this from being near-certain.

## Suggested downstream use

Use as orchestrator synthesis input and as a stress-test on any more bullish persona that treats this as almost a done deal.
