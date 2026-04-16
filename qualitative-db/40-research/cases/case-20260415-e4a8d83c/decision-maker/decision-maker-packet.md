---
type: decision_packet
case_key: case-20260415-e4a8d83c
dispatch_id: refresh-case-20260415-e4a8d83c-20260416T002353Z
question: "Will the price of Bitcoin be above $74,000 on April 17?"
market_id: 367ed8d7-c08e-4588-a449-c83aead47ec3
external_market_id: 0x0457acf7468ed957f2422686cf5e63fb54d69fb116b67f74f6b64fd8e8b377dc
market_slug: bitcoin-above-74k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $74,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-e4a8d83c/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-e4a8d83c/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260415-e4a8d83c/decision-maker/refreshes/refresh-case-20260415-e4a8d83c-20260416T002353Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.65
fair_value_high: 0.69
fair_value_mid: 0.67
market_reference_price: 0.62
edge_mid_vs_market_pct_points: 5.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-17T00:24:50.101476+00:00
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
- Primary crux: The move from a prior fair-value center near 0.67 to a market price of 0.62 is best treated as repricing rather than a broken thesis: Bitcoin is still only modestly more likely than not to close above $74,000 on the April 17 noon ET Binance minute because spot remains above strike, and the market has now moved below bounded fair value enough to create a positive value gap, though exact-minute path fragility keeps authorization capped at watch-only.
- One-sentence rationale: BTC is still only modestly more likely than not to finish above $74,000 on the April 17 Binance noon minute, but with fair value near 0.67 and the market now down at 0.62, the valuation has improved enough to mark edge_present while keeping the disciplined output at watch-only because exact-minute downside fragility remains live.

## Why this is the right action / no-action call

This refresh is primarily a valuation improvement: same directional Yes, better price, but not enough cleanliness to authorize.

## Valuation

- Fair value low: 0.65
- Fair value high: 0.69
- Fair value midpoint: 0.67
- Market reference price: 0.62
- Edge vs market (percentage points): 5.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current Binance spot above strike supports a modest Yes lean and the market now sits below bounded fair value, but the exact-minute settlement structure and only medium verification quality still justify a conservative, non-authorized posture.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.55
  - `target_exposure_fraction:` 0.0
  - `notes:` Would be a clearly attractive price only with refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.55
  - `max_p:` 0.65
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone if BTC remains above 74k with a stable cushion.
- `hold`
  - `min_p:` 0.65
  - `max_p:` 0.69
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; current packet remains watch-only because exact-minute execution risk still dominates.
- `trim`
  - `min_p:` 0.69
  - `max_p:` 0.77
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a narrow one-minute crypto settlement with a modest spot cushion.
- `exit`
  - `min_p:` 0.77
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at rich prices because a routine intraday move can still decide the contract.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-17T00:24:50.101476+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure aggressively despite the improved valuation., Treat exact-minute Binance settlement risk as the dominant execution constraint., Prefer reassessment closer to settlement if the market remains cheap and BTC retains the cushion.

## Invalidation

### Thesis breakers
- BTC loses the 74k level on Binance and fails to reclaim it before the Apr 17 fixing window.
- A downside macro, crypto, or exchange-specific shock materially raises the probability of a sub-74k settlement minute.
- Binance-specific pricing, liquidity, operational, or display-surface issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding same-venue spot deterioration, changing the value comparison.
- Binance microstructure or settlement-surface behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 17 12:00 ET should supersede this packet before any action.
- The actual Apr 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if later pre-fix Binance checks show BTC still holding comfortably above 74k and the price remains meaningfully below fair value.
- Downgrade if BTC loses the strike area or if volatility expands.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability that the modest above-74k cushion survives the exact settlement minute over the remaining horizon.
- Whether an unobserved late catalyst emerges before the fixing window.
- How much residual discount exact-minute Binance UI-versus-API ambiguity deserves at a near-threshold strike.

### Reasons to pass / stay small
- This is still a one-minute single-venue settlement contract where path risk dominates because the cushion is small.
- Independent verification quality remains only medium.
- Even with a positive edge, the execution case is not clean enough to authorize.

### What would change my mind
- Later same-venue checks showing BTC still comfortably above 74k into the final hours would improve confidence in the current positive edge.
- A move back below 74k or into the low-73k area would reduce fair value materially.
- A rebound in market price back toward or above fair value would erase the current value case.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is primarily a valuation improvement: same directional Yes, better price, but not enough cleanliness to authorize.

## Notes for downstream evaluator

The move from a prior fair-value center near 0.67 to a market price of 0.62 is best treated as repricing rather than a broken thesis: Bitcoin is still only modestly more likely than not to close above $74,000 on the April 17 noon ET Binance minute because spot remains above strike, and the market has now moved below bounded fair value enough to create a positive value gap, though exact-minute path fragility keeps authorization capped at watch-only.
