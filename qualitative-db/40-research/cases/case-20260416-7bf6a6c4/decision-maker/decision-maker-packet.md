---
type: decision_packet
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
question: "Will the price of Bitcoin be above $74,000 on April 17?"
market_id: 367ed8d7-c08e-4588-a449-c83aead47ec3
external_market_id: 0x0457acf7468ed957f2422686cf5e63fb54d69fb116b67f74f6b64fd8e8b377dc
market_slug: bitcoin-above-74k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $74,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260416-7bf6a6c4/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-7bf6a6c4/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.64
fair_value_high: 0.69
fair_value_mid: 0.665
market_reference_price: 0.71
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-17T03:01:13.598279+00:00
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
- Primary crux: BTC above $74,000 on the April 17 noon ET Binance minute is more likely than not because spot is already modestly above strike, but the market at 0.71 still looks somewhat too confident for an exact future one-minute close when the cushion is only around 1.2-1.3% and most evidence is current-price context rather than independently predictive proof.
- One-sentence rationale: BTC above $74,000 on the April 17 Binance noon minute is still more likely than not, but with fair value around 0.665 and the market at 0.71, the disciplined output remains watch-only because the exact-minute settlement structure makes a small current cushion too fragile to justify the quoted price.

## Why this is the right action / no-action call

The package's internal inconsistency supports caution: directional Yes survives, but the edge is not clean enough to authorize.

## Valuation

- Fair value low: 0.64
- Fair value high: 0.69
- Fair value midpoint: 0.665
- Market reference price: 0.71
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current BTC/USDT above-threshold persistence supports Yes, but bounded verification still does not justify paying a low-70s price for a single-minute close contract with a small cushion and material timing risk.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.56
  - `target_exposure_fraction:` 0
  - `notes:` Would require a materially cheaper price and refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.56
  - `max_p:` 0.64
  - `target_exposure_fraction:` 0
  - `notes:` Potential value zone only if BTC remains above 74k with improved cushion or calmer volatility.
- `hold`
  - `min_p:` 0.64
  - `max_p:` 0.69
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.69
  - `max_p:` 0.76
  - `target_exposure_fraction:` 0
  - `notes:` Above fair value for a near-threshold one-minute crypto settlement.
- `exit`
  - `min_p:` 0.76
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Avoid or exit at rich prices because exact-minute downside tail dominates when the cushion is small.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-17T03:01:13.598279+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current market price., Treat exact-minute Binance settlement risk as the dominant execution constraint., Reopen only if market cheapens materially or if later same-venue checks show BTC holding comfortably above 74k with a larger cushion.

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
- Whether overnight or U.S.-morning shocks emerge before the fixing window.
- How much residual venue-specific and minute-close risk should still be charged despite clear rules.

### Reasons to pass / stay small
- The market price is above bounded fair value.
- Most evidence is present-state context rather than independent predictive evidence.
- The contract resolves on one exact Binance minute rather than broad daily direction.

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
- Additional notes: The package's internal inconsistency supports caution: directional Yes survives, but the edge is not clean enough to authorize.

## Notes for downstream evaluator

BTC above $74,000 on the April 17 noon ET Binance minute is more likely than not because spot is already modestly above strike, but the market at 0.71 still looks somewhat too confident for an exact future one-minute close when the cushion is only around 1.2-1.3% and most evidence is current-price context rather than independently predictive proof.
