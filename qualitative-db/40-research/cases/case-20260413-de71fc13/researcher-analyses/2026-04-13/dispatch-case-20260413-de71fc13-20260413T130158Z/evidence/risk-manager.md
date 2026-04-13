---
type: evidence_map
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
research_run_id: 7213894b-5e7f-408b-8df2-bb5d1cb8f592
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-68-000-on-april-13
question: "Will the price of Bitcoin be above $68,000 on April 13?"
driver: operational-risk
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-de71fc13/researcher-analyses/2026-04-13/dispatch-case-20260413-de71fc13-20260413T130158Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "intraday", "stress-test"]
---

# Summary

The case leans strongly Yes because the governing Binance price was already around 71.1k with under three hours remaining, but the risk-manager adjustment is that the market's near-certainty still embeds hidden assumptions about intraday stability and clean contract mechanics.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 13 close above 68,000?

## Current lean

Strong Yes lean, but not true certainty.

## Prior / starting view

Given the 92.9% market-implied probability and a same-day intraday threshold market, the starting view was that Yes was probably right directionally but needed stress-testing for timing and source-of-truth traps.

## Evidence supporting the claim

- Binance spot around 71.15k at ~9:03 AM ET.
  - source: 2026-04-13-risk-manager-price-checks.md
  - why it matters causally: direct governing venue level is well above the threshold.
  - direct or indirect: direct
  - weight: very high
- Binance recent 1-minute closes roughly 70.68k-71.21k across the prior four hours.
  - source: 2026-04-13-risk-manager-price-checks.md
  - why it matters causally: suggests no ongoing crash and provides a cushion context.
  - direct or indirect: direct
  - weight: high
- Coinbase and CoinGecko both near 71.1k.
  - source: 2026-04-13-risk-manager-price-checks.md
  - why it matters causally: reduces risk that Binance is showing an anomalous isolated print.
  - direct or indirect: indirect/contextual for settlement, direct for broader market context
  - weight: medium
- Polymarket rules cleanly identify Binance BTC/USDT 1m close at 12:00 ET.
  - source: 2026-04-13-risk-manager-polymarket-rules.md
  - why it matters causally: narrows the contract to a tractable, verifiable event.
  - direct or indirect: direct for mechanics
  - weight: high

## Evidence against the claim

- BTC can move several percent intraday, and the remaining buffer to 68k is only about 4.6%.
  - source or note reference: price-check source note; general crypto market behavior
  - why it matters causally: a fast selloff can still break an apparently safe morning cushion.
  - direct or indirect: indirect/contextual
  - weight: medium
- The market resolves on one exact Binance 1-minute close, not a daily average or multi-venue benchmark.
  - source or note reference: Polymarket rules note
  - why it matters causally: this creates timing and exchange-specific fragility that a generic BTC bullish view can underappreciate.
  - direct or indirect: direct for mechanics
  - weight: medium

## Ambiguous or mixed evidence

- Cross-venue alignment is supportive, but because settlement is Binance-specific it only partially reduces risk.
- Stable price action over the last few hours helps, but short-horizon crypto returns can regime-shift quickly.

## Conflict between inputs

No major factual conflict. The main difference is weighting: current price cushion points strongly to Yes, while the risk-manager lens discounts the market slightly for residual path and mechanics risk.

## Key assumptions

- Noon ET maps to the expected Binance candle time without hidden timezone issues.
- Binance spot remains reasonably aligned with the broader BTC market into resolution.
- No abrupt >4.5% downside shock occurs before noon ET.

## Key uncertainties

- Short-horizon BTC downside tail risk.
- Exact path into the noon ET candle.
- Small residual chance of exchange-specific or interpretation-related settlement friction.

## Disconfirming signals to watch

- BTC losing the 70k-70.5k area quickly on Binance.
- Venue-specific divergence on Binance versus Coinbase/other major spot sources.
- Any clarification suggesting the relevant candle time is being interpreted differently.

## What would increase confidence

- Another direct Binance check closer to noon ET still above 70k.
- Confirmation from the live Binance chart/UI that the 12:00 ET / 16:00 UTC mapping is exactly what traders expect.

## Net update logic

The evidence moved the view from generic high-probability Yes to specific high-probability-but-not-certain Yes. The direct Binance level and contract clarity matter most; the risk-manager discount comes from the market being priced close to certainty despite a single-minute, single-venue, still-future resolution point.

## Suggested downstream use

Use as orchestrator synthesis input and as a caution against treating extreme same-day threshold odds as certainty when one exact intraday print still governs settlement.