---
type: evidence_map
case_key: case-20260415-35855579
dispatch_id: dispatch-case-20260415-35855579-20260415T225312Z
research_run_id: 23536336-a499-49bc-976a-33c97c12c415
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-16
question: "Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-16 close above 72000?"
driver: operational-risk
date_created: 2026-04-15
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
tags: ["btc", "evidence-map", "threshold-market"]
---

# Summary

The net evidence supports a Yes lean because the underlying is already several percent above the strike with less than a day to go, and the contract mechanics are relatively clean once Binance BTC/USDT 1-minute close and ET noon timing are verified.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-16 have a final close above 72000?

## Current lean

Yes, with high but not near-certainty confidence.

## Prior / starting view

A generic outside-view prior for a short-horizon threshold market should heavily weight current distance from threshold, remaining time, and contract cleanliness rather than narrative crypto commentary.

## Evidence supporting the claim

- Live Binance BTCUSDT price during the run was about 75124.
  - source: case source note `2026-04-15-base-rate-binance-api-and-contract.md`
  - why it matters causally: current distance from the strike is the dominant short-horizon input
  - direct or indirect: direct
  - weight: high

- Binance 24hr low was about 73514, still above 72000.
  - source: same source note
  - why it matters causally: the threshold is below the full observed recent day range, suggesting some cushion
  - direct or indirect: direct
  - weight: medium-high

- Contract mechanics are explicit: Binance BTC/USDT, 1-minute candle, 12:00 ET, strict higher-than test.
  - source: Polymarket rules captured in same source note
  - why it matters causally: lowers rule ambiguity and supports cleaner estimation
  - direct or indirect: direct
  - weight: medium

## Evidence against the claim

- BTC is volatile enough that a 4%+ drop in under 24 hours is entirely possible.
  - source: general structural property of BTC plus observed intraday range data
  - why it matters causally: a single sharp selloff could invalidate the cushion
  - direct or indirect: indirect/contextual
  - weight: high

- The market resolves on one specific 1-minute close, not a daily close or average.
  - source: Polymarket rules
  - why it matters causally: a brief move at the wrong time can decide the market even if BTC spends most of the period above 72000
  - direct or indirect: direct
  - weight: medium

## Ambiguous or mixed evidence

- Current market pricing near 97.65% says traders see this as highly likely, but that may also reflect some crowd overconfidence in a one-minute threshold market.

## Conflict between inputs

There is little factual conflict. The key disagreement is weighting-based: how much one should discount the current cushion for BTC's ability to move several percent quickly.

## Key assumptions

- No major downside catalyst arrives before noon ET on 2026-04-16.
- Binance remains the operationally usable source of truth.
- Current observed BTCUSDT level is representative enough for a short-horizon base-rate estimate.

## Key uncertainties

- Overnight macro or crypto-specific news flow.
- Short-horizon realized volatility into the exact settlement minute.
- Possible exchange-specific disruptions or unusual wick behavior near noon ET.

## Disconfirming signals to watch

- BTCUSDT losing the recent 24hr low and moving toward 72k overnight.
- Material market stress or exchange issues before settlement.
- Elevated intraday volatility right before 12:00 ET.

## What would increase confidence

- BTC still trading comfortably above 73k to 74k closer to the settlement window.
- A calm overnight tape with no large downside catalyst.

## Net update logic

The base-rate starting point is that short-horizon threshold markets are mainly about current distance from strike plus remaining volatility. Since the asset is already roughly 4.2% above the threshold and even the recent 24hr low stayed above the threshold, the evidence supports Yes. The main reason this is not 99%+ is that BTC can move several percent quickly and the contract settles on a single 1-minute close rather than a broader average.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the base-rate lane stayed Yes but modestly less confident than the raw market price.
