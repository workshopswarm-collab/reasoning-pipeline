---
type: evidence_map
case_key: case-20260415-6580bcd8
dispatch_id: dispatch-case-20260415-6580bcd8-20260415T081158Z
research_run_id: b8437e64-00fb-4b1c-ab80-575f352bfec2
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-at-12-00-et-on-april-17-2026-close-above-72000
question: "Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 17, 2026 close above 72000?"
driver: operational-risk
date_created: 2026-04-15
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-6580bcd8/researcher-analyses/2026-04-15/dispatch-case-20260415-6580bcd8-20260415T081158Z/personas/risk-manager.md"]
tags: ["evidence-map", "volatility", "contract-interpretation"]
---

# Summary

The evidence nets to a Yes lean because current Binance BTCUSDT spot is already safely above 72k and the contract mechanics are clear, but the risk concentration is unusually high because settlement depends on one exact 1-minute close on one exchange two days ahead.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 17, 2026 close above 72,000?

## Current lean

Moderate Yes lean, but with nontrivial fragility from short-horizon volatility and exact-timestamp concentration.

## Prior / starting view

Starting view from market price: roughly 77% Yes, implying the market sees BTC's current cushion above 72k as meaningful.

## Evidence supporting the claim

- Binance spot price around 73,830 on 2026-04-15.
  - source: 2026-04-15-risk-manager-binance-btcusdt-market-and-api.md
  - why it matters causally: threshold is already exceeded by roughly 1.8k.
  - direct or indirect: direct for current state, indirect for future resolution.
  - weight: high

- Binance 24h low around 73,514, still above 72k.
  - source: 2026-04-15-risk-manager-binance-btcusdt-market-and-api.md
  - why it matters causally: even a fairly weak intraday point in the checked window remained above threshold.
  - direct or indirect: direct for recent realized volatility context.
  - weight: medium

- Polymarket contract mechanics are explicit and unambiguous about source, pair, interval, timezone, and threshold direction.
  - source: 2026-04-15-risk-manager-binance-btcusdt-market-and-api.md
  - why it matters causally: reduces interpretive settlement risk and lets the analysis focus on actual price-path risk.
  - direct or indirect: direct for contract interpretation.
  - weight: medium

## Evidence against the claim

- The market resolves on one exact minute, not on average daily level or broad exchange consensus.
  - source: Polymarket rule text and same source note
  - why it matters causally: a brief downside move near noon ET can flip the result even if BTC spends most of the period above 72k.
  - direct or indirect: direct for settlement fragility.
  - weight: high

- Current cushion above threshold is only about 2.5%.
  - source: Binance spot versus threshold
  - why it matters causally: BTC can move more than that over two days without requiring an extreme regime shift.
  - direct or indirect: indirect for future resolution risk.
  - weight: high

- Single-venue dependence creates exchange-specific wick or microstructure risk.
  - source: contract rules specifying Binance only
  - why it matters causally: cross-exchange strength does not save the trade if Binance alone prints below 72k at the relevant minute.
  - direct or indirect: direct for operational settlement risk.
  - weight: medium

## Ambiguous or mixed evidence

- Market pricing around 77% is informative, but it may partly reflect traders extrapolating current spot rather than fully pricing timestamp-specific fragility.
- Same-day realized range looked supportive, but one day of range context does not tightly bound the next two days of BTC volatility.

## Conflict between inputs

No material factual conflict in the checked inputs. The main disagreement is weighting-based: how much probability mass to assign to short-horizon downside and venue-specific print risk.

## Key assumptions

- Current cushion above 72k is large enough to survive ordinary BTC volatility into the settlement minute.
- Binance spot prints will remain broadly representative of the broader BTC market rather than showing an isolated dislocation at the key minute.

## Key uncertainties

- Whether BTC enters April 17 with ample cushion or trades close to the line.
- Whether macro or crypto-specific headlines induce a fast downside move around the resolution window.
- Whether Binance-specific wick behavior matters at the one-minute-close level.

## Disconfirming signals to watch

- BTCUSDT spending sustained time below 72k before April 17 noon ET.
- Rising downside volatility with repeated tests of 72k.
- Binance-specific anomalies versus broader spot markets near the resolution window.

## What would increase confidence

- Another verification pass closer to the event showing BTC still materially above 72k.
- Evidence that recent realized volatility remains low enough that the 1.8k cushion is robust.
- Confirmation of clean Binance market functioning near the event.

## Net update logic

The direct source-of-truth and current spot level are enough to support a Yes lean, but the risk lens pushes against treating 77% as obviously cheap. The main net is: favorable current distance from threshold, offset by concentrated timestamp/venue risk and a cushion that is meaningful but not huge.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- decision-maker review
