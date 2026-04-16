---
type: decision_packet
case_key: case-20260416-5baa54ee
dispatch_id: dispatch-case-20260416-5baa54ee-20260416T032738Z
question: "Will the price of Bitcoin be above $70,000 on April 20?"
market_id: 551a0230-0ffb-42cc-9103-4bea5dc0cb4e
external_market_id: 0x73f9d7c48acbeefbe93bdcdc747947e2e8573945f11720617290fe672bf997d2
market_slug: bitcoin-above-70k-on-april-20
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 20?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260416-5baa54ee/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-5baa54ee/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.89
fair_value_high: 0.93
fair_value_mid: 0.91
market_reference_price: 0.94
edge_mid_vs_market_pct_points: -3.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-17T03:36:29.635428+00:00
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
- Primary crux: BTC above $70,000 on the April 20 noon ET Binance minute remains the clear base case because spot is around 75k and recent sampled Binance closes have remained well above strike, but a 0.94 market price still looks slightly too rich for a single-minute, single-venue crypto settlement with four days of path risk and small residual Binance settlement-surface ambiguity.
- One-sentence rationale: BTC above $70,000 on the April 20 Binance noon minute remains the clear base case, but with fair value around 0.91 and the market at 0.94, the disciplined output stays watch-only because near-certainty pricing still overstates confidence in a single-minute crypto settlement with several days of residual tail risk.

## Why this is the right action / no-action call

Strong directional Yes does not imply executable value here; the limiting factor is rich pricing, not weak thesis.

## Valuation

- Fair value low: 0.89
- Fair value high: 0.93
- Fair value midpoint: 0.91
- Market reference price: 0.94
- Edge vs market (percentage points): -3.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current BTC/USDT cushion strongly supports Yes, but bounded verification does not justify paying 0.94 for a single-minute venue-specific settlement with several days of residual path risk.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.84
  - `target_exposure_fraction:` 0
  - `notes:` Would require an unusually large dislocation versus this packet's high Yes base case.
- `scaled_enter`
  - `min_p:` 0.84
  - `max_p:` 0.89
  - `target_exposure_fraction:` 0
  - `notes:` Potential value zone if BTC remains comfortably above strike and no new settlement-surface issues appear.
- `hold`
  - `min_p:` 0.89
  - `max_p:` 0.93
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.93
  - `max_p:` 0.97
  - `target_exposure_fraction:` 0
  - `notes:` Above fair value for a one-minute crypto settlement with residual path risk.
- `exit`
  - `min_p:` 0.97
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Avoid or exit at near-certainty pricing because even a brief downside move can flip the result.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-17T03:36:29.635428+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current market price., Treat exact-minute Binance settlement risk as the dominant execution constraint even with a strong directional Yes view., Reopen only if market cheapens materially or if a near-settlement Binance check preserves a large cushion above 70k.

## Invalidation

### Thesis breakers
- BTC/USDT moves materially closer to 70k or below it before the Apr 20 fixing window.
- A bearish macro, crypto, or exchange-specific shock materially raises the probability of a sub-70k settlement minute.
- Binance-specific pricing, liquidity, or display-surface issues emerge near resolution.

### Market structure breakers
- Market reprices materially after fresh spot or volatility changes, altering the value comparison.
- Binance settlement-surface or ET-to-UTC candle mapping behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation on Apr 20 morning should supersede this packet before any action.
- The actual Apr 20 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if later pre-fix Binance checks still show a wide cushion above 70k and the market price cheapens below fair value.
- Downgrade if BTC loses substantial cushion or volatility rises materially.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the current cushion above 70k survives the exact settlement minute.
- Whether weekend or macro shocks emerge before the fixing window.
- How much residual discount exact-minute Binance UI-versus-API sensitivity deserves at this price level.

### Reasons to pass / stay small
- The market price is above bounded fair value.
- The contract resolves on one exact Binance minute rather than broad daily direction.
- The remaining edge is modest and not robust enough to justify paying 0.94.

### What would change my mind
- A fresh near-settlement Binance check still showing BTC comfortably above 70k with stable conditions would modestly improve confidence.
- A materially cheaper market price with unchanged cushion would improve the execution case.
- A fast move toward 70k would reduce directional confidence materially.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: Strong directional Yes does not imply executable value here; the limiting factor is rich pricing, not weak thesis.

## Notes for downstream evaluator

BTC above $70,000 on the April 20 noon ET Binance minute remains the clear base case because spot is around 75k and recent sampled Binance closes have remained well above strike, but a 0.94 market price still looks slightly too rich for a single-minute, single-venue crypto settlement with four days of path risk and small residual Binance settlement-surface ambiguity.
