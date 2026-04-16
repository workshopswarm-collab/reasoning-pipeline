---
type: decision_packet
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
question: "Will the price of Bitcoin be above $70,000 on April 19?"
market_id: 00b2316a-1303-48a8-bfec-d7743c2a4264
external_market_id: 0x181bd38eac20ef70a12daab11f081f999991b044ad46c3d4ee468d97aee461a5
market_slug: bitcoin-above-70k-on-april-19
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-91430615/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-91430615/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.82
fair_value_high: 0.86
fair_value_mid: 0.84
market_reference_price: 0.9
edge_mid_vs_market_pct_points: -6.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: low
valid_until: 2026-04-16T00:03:24.390405+00:00
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
- Trade authorization: `forbidden`
- Position policy: `flat`
- Decision readiness: `needs_more_research`
- Primary crux: BTC is still more likely than not to finish above $70,000 on the April 19 noon ET Binance minute because spot remained around 74.2k and the recent trading regime has mostly been above 70k, but the bounded package does not verify the exact settlement-minute downside distribution strongly enough to justify acting against a 90% market on what is still a modest edge.
- One-sentence rationale: Bitcoin is still the more likely side for the April 19 noon ET Binance close, but because the bounded package does not strongly verify the exact settlement-minute downside distribution and the edge versus the 90% market is only modest, the disciplined output is forbidden and needs-more-research rather than a live anti-market trade.

## Why this is the right action / no-action call

This is another case where directional belief and executable readiness diverge; the market may be somewhat too confident, but not by enough under current verification quality to justify action.

## Valuation

- Fair value low: 0.82
- Fair value high: 0.86
- Fair value midpoint: 0.84
- Market reference price: 0.9
- Edge vs market (percentage points): -6.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current Binance BTC/USDT pricing above $70k supports a Yes lean, but exact-minute settlement mechanics and only moderate verification of downside-tail risk keep fair value below market without creating a clean executable edge.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.76
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized from this packet because the case is not execution-ready.
- `scaled_enter`
  - `min_p:` 0.76
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0
  - `notes:` Even cheaper pricing would still require refreshed settlement-focused verification before action.
- `hold`
  - `min_p:` 0.82
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair value zone, but not actionable under current evidence quality.
- `trim`
  - `min_p:` 0.86
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0
  - `notes:` Avoid increasing above fair value while settlement-minute fragility remains insufficiently verified.
- `exit`
  - `min_p:` 0.94
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat or avoid at extreme prices because a single-minute crypto market retains meaningful path risk.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T00:03:24.390405+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not enter from this packet; reopen only after a fresher pre-settlement BTC check or stronger settlement-minute downside calibration., Require better confirmation that the modest below-market view survives closer-to-settlement price action., Treat weekend exact-minute Binance-close markets as operationally fragile when the edge is only modest.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below 72k-70k before the April 19 noon ET minute.
- A weekend macro or crypto-specific downside catalyst materially raises short-horizon selloff risk.
- Evidence emerges that the operative Binance settlement surface differs from the assumed minute-close mapping.

### Market structure breakers
- The current quote becomes stale relative to a materially changed Binance state.
- The assumed UI/API candle mapping proves wrong or disputed.

### Time breakers
- A fresh pre-settlement BTC check should supersede this packet before action.
- If no refreshed verification is available near settlement, this packet should not be used for trading.

### Reversal conditions
- Move from forbidden to watch-only or authorized only after stronger downside calibration or fresher price-state verification.
- Move lower if BTC compresses toward the threshold or settlement-surface ambiguity increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true four-to-five day downside probability of BTC falling below $70k at the exact fixing minute.
- Whether weekend volatility will be subdued enough to justify the market's 90% confidence.
- Whether Binance UI-versus-API implementation details matter at the governing minute.

### Reasons to pass / stay small
- The edge versus market is modest and only moderately independently verified.
- Critical uncertainty is execution readiness, not directional belief.
- This is a single-minute single-venue crypto market where timing risk can dominate modest valuation gaps.

### What would change my mind
- A fresh same-venue check near settlement showing BTC still firmly above 72k-73k would improve readiness and move me closer to market.
- A stronger independent volatility or downside-tail estimate would make the modest disagreement more actionable.
- A drop toward 70k-72k or any Binance-specific settlement ambiguity would lower fair value materially.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is another case where directional belief and executable readiness diverge; the market may be somewhat too confident, but not by enough under current verification quality to justify action.

## Notes for downstream evaluator

BTC is still more likely than not to finish above $70,000 on the April 19 noon ET Binance minute because spot remained around 74.2k and the recent trading regime has mostly been above 70k, but the bounded package does not verify the exact settlement-minute downside distribution strongly enough to justify acting against a 90% market on what is still a modest edge.
