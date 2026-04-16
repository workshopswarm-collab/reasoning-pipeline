---
type: decision_packet
case_key: case-20260414-8dcead65
dispatch_id: dispatch-case-20260414-8dcead65-20260414T160342Z
question: "Will the price of Bitcoin be above $70,000 on April 15?"
market_id: d57c986f-d265-4622-bad7-78ce1c10a3f2
external_market_id: 0x5687ed31630b7f74c281562c52cf56ea1385fd249688c71eba96b62a6e8a8c26
market_slug: bitcoin-above-70k-on-april-15
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 15?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-8dcead65/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-8dcead65/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.95
fair_value_high: 0.97
fair_value_mid: 0.96
market_reference_price: 0.979
edge_mid_vs_market_pct_points: -1.9
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-15T16:12:40.602708+00:00
tags: []
---

# Decision packet

Use this template for the Decision-Maker's final executable recommendation after reviewing synthesis.

Pipeline position:
- upstream = researcher swarm -> synthesis -> `decision-handoff.md`
- this artifact = Decision-Maker's final commitment object
- downstream = isolated execution, accounting, evaluator, retrospective review

Canonical machine-readable contract:
- `artifacts/decision-maker-packet.json`

## Decision summary

- Side: `YES`
- Trade authorization: `watch_only`
- Position policy: `hold_only`
- Decision readiness: `ready`
- Primary crux: BTC is still very likely to finish above $70,000 on the April 15 noon ET Binance minute because same-venue spot remains far above the strike and recent Binance lows are still above $70,000, but the market's 97.9% price is slightly too close to certainty for a future exact-minute, single-venue settlement.
- One-sentence rationale: Bitcoin being above $70,000 on the April 15 noon ET Binance minute is very likely given the large current cushion on the governing venue, but because the contract still depends on a future exact-minute single-venue close, the market's 97.9% price is slightly too close to certainty to justify fresh action.

## Why this is the right action / no-action call

Directional uncertainty is low; the remaining issue is narrow settlement-minute and venue-specific tail risk, so the disciplined posture is watch-only.

## Valuation

- Fair value low: 0.95
- Fair value high: 0.97
- Fair value midpoint: 0.96
- Market reference price: 0.979
- Edge vs market (percentage points): -1.9
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current Binance pricing well above $70k supports a very high Yes probability, but exact-minute Binance settlement mechanics and future-candle uncertainty keep fair value modestly below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` No fresh entry from this packet; materially cheaper prices would require a fresh pre-settlement venue check.
- `scaled_enter`
  - `min_p:` 0.9
  - `max_p:` 0.95
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the contract is already in small-tail operational-risk territory.
- `hold`
  - `min_p:` 0.95
  - `max_p:` 0.97
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with a very high-probability Yes outcome but no meaningful valuation cushion.
- `trim`
  - `min_p:` 0.97
  - `max_p:` 0.992
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above bounded fair value and exact-minute risk dominates.
- `exit`
  - `min_p:` 0.992
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because remaining uncertainty is almost entirely settlement-mechanics tail risk.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T16:12:40.602708+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market is already above bounded fair value., Refresh on any sharp move toward $72k or below, or on any Binance-specific anomaly, before acting., Treat this as a future exact-minute settlement contract, not a generic BTC direction bet.

## Invalidation

### Thesis breakers
- A sharp selloff materially compresses the cushion toward $70,000 before the noon ET minute.
- Evidence of a Binance-specific print, timestamp, or settlement-surface anomaly emerges.
- Direct observation of the resolving Binance candle closes at or below $70,000.

### Market structure breakers
- The current quote is stale relative to updated Binance state.
- Liquidity conditions or venue-specific issues make the displayed price non-executable.

### Time breakers
- The exact April 15 12:00 ET Binance candle should replace this packet immediately once observed.
- Overnight or same-morning macro/crypto shocks can still dominate current reasoning before settlement.

### Reversal conditions
- Move materially lower only on a fresh packet if BTC drops sharply toward the threshold or a Binance-specific anomaly appears.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The exact final Binance 12:00 ET April 15 candle close.
- Residual overnight and same-morning downside volatility.
- Whether any Binance-specific UI/API or candle-surface anomaly affects the governing minute.

### Reasons to pass / stay small
- The market is already near bounded fair value and leaves little room for error.
- The decisive future exact-minute candle has not occurred yet.

### What would change my mind
- A fresh same-venue check near settlement showing BTC still comfortably above $70k would modestly increase confidence.
- A rapid move toward $71k-$72k or below would reduce fair value materially.
- Direct evidence of a Binance-specific settlement anomaly would lower confidence despite the large cushion.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: Directional uncertainty is low; the remaining issue is narrow settlement-minute and venue-specific tail risk, so the disciplined posture is watch-only.

## Notes for downstream evaluator

BTC is still very likely to finish above $70,000 on the April 15 noon ET Binance minute because same-venue spot remains far above the strike and recent Binance lows are still above $70,000, but the market's 97.9% price is slightly too close to certainty for a future exact-minute, single-venue settlement.
