---
type: evidence_map
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
research_run_id: c2460820-4ec8-40ac-8c7e-7f89436a3201
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-15
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 15, 2026 close above 72000?"
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
downstream_uses: ["personas/risk-manager.md"]
tags: ["risk-manager", "evidence-map", "timing-risk"]
---

# Summary

The net evidence supports a Yes lean, but the main risk-manager objection is that this contract is resolved by one exact Binance minute nearly two days in the future, so timing/path risk deserves more weight than the simple spot-above-strike snapshot.

## Question being evaluated

Will Binance BTC/USDT close above 72,000 on the 12:00 ET 1-minute candle on April 15, 2026?

## Current lean

Moderate Yes lean.

## Prior / starting view

Starting baseline was the market itself at roughly 72.5% implied probability.

## Evidence supporting the claim

- Live Binance BTCUSDT was about 73,825.51 at review time.
  - source: 2026-04-13-risk-manager-binance-api-and-live-context.md
  - why it matters causally: the contract is already in the money by about 1.8k on the actual exchange named in the rules
  - direct or indirect: direct
  - weight: high

- Recent Binance 1-minute candles around review time were all above 73.4k.
  - source: 2026-04-13-risk-manager-binance-api-and-live-context.md
  - why it matters causally: shows immediate tape is comfortably above 72k rather than barely touching it
  - direct or indirect: direct
  - weight: medium

- Polymarket rules explicitly define a clean governing source of truth.
  - source: 2026-04-13-risk-manager-polymarket-rules-and-market-context.md
  - why it matters causally: reduces broad settlement ambiguity; the main uncertainty is price path, not rule confusion
  - direct or indirect: direct for settlement mechanics
  - weight: medium

## Evidence against the claim

- Settlement depends on one exact 12:00 ET minute, not daily close, not intraday high, and not any other exchange.
  - source: 2026-04-13-risk-manager-polymarket-rules-and-market-context.md
  - why it matters causally: converts a general bullish BTC view into a narrower timing-sensitive proposition
  - direct or indirect: direct
  - weight: high

- BTC can move more than the current 1.8k cushion in well under two days.
  - source: inference from exchange-native live trading range in the Binance note
  - why it matters causally: a moderate drawdown is enough to flip the answer despite current spot being above threshold
  - direct or indirect: contextual
  - weight: high

- The evidence set is thin on independent forward-looking catalysts or macro context.
  - source: run-level evidence gap
  - why it matters causally: market confidence could be too high if based mostly on spot anchoring rather than future distribution analysis
  - direct or indirect: contextual
  - weight: medium

## Ambiguous or mixed evidence

- Binance API documentation improves confidence in operational interpretation, but does not by itself say anything directional about where BTC will print at the deciding minute.
- Current spot being safely above 72k is supportive, but can also invite false confidence because the contract resolves on a future exact minute.

## Conflict between inputs

No major factual conflict. The main tension is weighting: current spot cushion supports Yes, while the risk-manager lens says exact-minute path dependence should stop this from being treated as nearly settled.

## Key assumptions

- The present cushion above 72k is enough to survive ordinary volatility.
- No exchange-specific disruption on Binance distorts the relevant candle.
- There is no large exogenous risk-off move before noon ET April 15.

## Key uncertainties

- Realized BTC volatility over the remaining ~42 hours
- Whether noon ET on April 15 coincides with a risk event or local drawdown
- How much the current market price already fully captures timing/path risk

## Disconfirming signals to watch

- Spot falls below 73k and trends lower
- Binance BTCUSDT revisits or breaks below 72k on April 14-15
- New exchange operational issues or sharp venue-specific dislocations

## What would increase confidence

- Continued trade above 73k into April 14-15
- Low realized volatility as the settlement window approaches
- Additional independent context showing no imminent macro/crypto event risk in the settlement window

## Net update logic

The base rate from the actual exchange print says Yes is more likely than not because BTC is already above the strike by a nontrivial amount. The risk-manager adjustment is to resist overconfidence: one exact-minute close and a still-meaningful time window leave enough room for a moderate downside move that the contract should not be treated as safe.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why this lane stayed only moderately above the market instead of issuing a high-conviction Yes.