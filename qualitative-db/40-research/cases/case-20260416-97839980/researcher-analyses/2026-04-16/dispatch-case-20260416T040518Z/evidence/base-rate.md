---
type: evidence_map
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
research_run_id: 40e4111a-d59e-462d-bfc6-44a3522e83f5
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-price
entity: sol
topic: case-20260416-97839980 | base-rate
question: Will the price of Solana be above $80 on April 19?
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: [sol]
related_drivers: [reliability, operational-risk]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/base-rate.md]
tags: [evidence-map, short-horizon, binary-threshold]
---

# Summary

Short-horizon outside view favors Yes because SOL is already above the strike by a meaningful margin, but the remaining risk is concentrated in crypto downside volatility and minute-specific settlement mechanics.

## Question being evaluated

Whether Binance SOL/USDT will print a final 1-minute candle close above $80 at 12:00 ET on April 19, 2026.

## Current lean

Lean Yes.

## Prior / starting view

A token already trading clearly above a nearby threshold with only a few days left usually resolves Yes more often than not, unless the asset is highly volatile or there is known event risk.

## Evidence supporting the claim

- Binance spot snapshot around $85.32, directly above the threshold by about 6.6%.
  - direct
  - high weight
  - matters because distance to strike over a short remaining window is the main structural input
- Recent Binance 1-minute candles also clustered around the mid-$85 area.
  - direct
  - medium weight
  - matters because the contract settles on a 1-minute Binance close, so minute-level pricing context is relevant
- CoinGecko spot around $85.21, near Binance.
  - indirect/contextual
  - medium weight
  - matters as an independent anomaly check and extra verification pass

## Evidence against the claim

- SOL is a high-beta crypto asset, so a 6%-7% move over several days is not rare enough to dismiss.
  - contextual
  - high weight
- Settlement is on one specific Binance minute close, which introduces microstructure and venue-specific risk even if the broader market remains above $80 nearby.
  - direct to contract interpretation
  - medium weight

## Ambiguous or mixed evidence

- Market price at 92% may reflect informed confidence, but it could also slightly underprice short-horizon downside volatility because these ladder markets often cluster at extremes once spot is above the strike.

## Conflict between inputs

No meaningful factual conflict between the checked sources. The main issue is weighting current distance-to-strike versus crypto downside volatility.

## Key assumptions

- No major market selloff before resolution.
- Binance remains a fair reflection of broader SOL spot into the settlement minute.

## Key uncertainties

- Short-horizon realized volatility over the next three days.
- Any macro or crypto-specific catalyst before noon ET on April 19.

## Disconfirming signals to watch

- SOL loses $83 and fails to recover.
- Broad crypto market derisks sharply.
- Binance-specific anomaly near the relevant minute.

## What would increase confidence

- Continued SOL trading above $84-$85 into April 18-19.
- Confirmation of no obvious scheduled catalyst likely to cause a sharp drawdown.

## Net update logic

Starting from an outside view that nearby-above-strike assets usually finish above unless volatility overwhelms the cushion, the direct spot evidence supports Yes, but the extreme 92% market price looks a bit richer than a cautious base-rate read because the underlying remains a volatile crypto asset and the settlement is minute-specific.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- decision-maker review
