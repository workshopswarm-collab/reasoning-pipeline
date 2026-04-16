---
type: decision_packet
case_key: case-20260416-cd7fa6c7
dispatch_id: refresh-case-20260416-cd7fa6c7-20260416T024820Z
question: "Will the price of Bitcoin be above $74,000 on April 17?"
market_id: 367ed8d7-c08e-4588-a449-c83aead47ec3
external_market_id: 0x0457acf7468ed957f2422686cf5e63fb54d69fb116b67f74f6b64fd8e8b377dc
market_slug: bitcoin-above-74k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $74,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260416-cd7fa6c7/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-cd7fa6c7/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260416-cd7fa6c7/decision-maker/refreshes/refresh-case-20260416-cd7fa6c7-20260416T024820Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.58
fair_value_high: 0.62
fair_value_mid: 0.6
market_reference_price: 0.7
edge_mid_vs_market_pct_points: -10.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-17T02:49:21.795056+00:00
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
- Primary crux: The move to 0.70 is best treated as repricing rather than a broken thesis: BTC above $74,000 on the April 17 noon ET Binance minute is still only slightly more likely than not because spot remains modestly above strike, but the market has now moved materially above bounded fair value for a one-minute settlement where ordinary overnight or morning volatility can still flip the outcome.
- One-sentence rationale: BTC above $74,000 on the April 17 Binance noon minute remains only slightly more likely than not, but with fair value still around 0.60 and the market now repriced to 0.70, the disciplined output remains watch-only because the richer price further overstates confidence in a fragile single-minute crypto settlement.

## Why this is the right action / no-action call

This refresh is continued valuation deterioration, not regime change: same directional Yes, much worse execution economics after repricing.

## Valuation

- Fair value low: 0.58
- Fair value high: 0.62
- Fair value midpoint: 0.6
- Market reference price: 0.7
- Edge vs market (percentage points): -10.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Prior bounded synthesis already incorporated the above-strike BTC regime; the current move from earlier prices to 0.70 adds market optimism, not stronger evidence that the exact fixing minute will hold above 74,000.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.5
  - `target_exposure_fraction:` 0
  - `notes:` Would require a materially cheaper price and refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.5
  - `max_p:` 0.58
  - `target_exposure_fraction:` 0
  - `notes:` Potential value zone only if BTC remains above 74k with improved cushion or calmer volatility.
- `hold`
  - `min_p:` 0.58
  - `max_p:` 0.62
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.62
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0
  - `notes:` Above fair value for a near-threshold one-minute crypto settlement.
- `exit`
  - `min_p:` 0.72
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Avoid or exit at rich prices because the exact-minute downside tail dominates when the spot cushion is small.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-17T02:49:21.795056+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the updated market price., Treat exact-minute Binance settlement risk as the dominant execution constraint., Reopen only if market cheapens materially or if later same-venue checks show BTC holding comfortably above 74k with a larger cushion.

## Invalidation

### Thesis breakers
- BTC loses the 74k level on Binance and fails to reclaim it before the Apr 17 fixing window.
- A downside macro, crypto, or exchange-specific shock materially raises the probability of a sub-74k settlement minute.
- Binance-specific pricing, liquidity, operational, or display-surface issues emerge near resolution.

### Market structure breakers
- Market reprices materially after fresh spot or volatility changes, altering the value comparison.
- Binance settlement-surface or ET-to-UTC minute mapping behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 17 12:00 ET should supersede this packet before any action.
- The actual Apr 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if later pre-fix Binance checks show BTC holding comfortably above 74k with a larger cushion and the market price returns below fair value.
- Downgrade if BTC loses the strike area or volatility rises materially.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the modest above-74k cushion survives the exact settlement minute.
- Whether overnight or U.S.-morning macro or crypto-specific shocks emerge before the fixing window.
- How much residual discount exact-minute Binance UI-versus-API sensitivity deserves when the strike is nearly at spot.

### Reasons to pass / stay small
- The updated market price is far above bounded fair value.
- The refresh added repricing, not stronger evidence.
- The contract still resolves on one exact Binance minute rather than broad daily direction.

### What would change my mind
- A fresh near-settlement Binance check still showing BTC comfortably above 74k with calmer volatility would improve confidence modestly.
- A materially cheaper market price with unchanged cushion would improve the execution case.
- A move back below 74k would reduce directional confidence materially.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is continued valuation deterioration, not regime change: same directional Yes, much worse execution economics after repricing.

## Notes for downstream evaluator

The move to 0.70 is best treated as repricing rather than a broken thesis: BTC above $74,000 on the April 17 noon ET Binance minute is still only slightly more likely than not because spot remains modestly above strike, but the market has now moved materially above bounded fair value for a one-minute settlement where ordinary overnight or morning volatility can still flip the outcome.
