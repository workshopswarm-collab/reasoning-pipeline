---
type: decision_packet
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
question: "Will the price of Bitcoin be above $70,000 on April 18?"
market_id: 0bf3deba-41d6-4ff1-abd8-0ffe3f4a6588
external_market_id: 0x55dfaab5bde3bdc44eac96354731aaee8e35ab1341f92cd7de8e50186fa24d1d
market_slug: bitcoin-above-70k-on-april-18
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 18?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-8a0619b6/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-8a0619b6/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.82
fair_value_high: 0.87
fair_value_mid: 0.845
market_reference_price: 0.89
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: low
valid_until: 2026-04-15T19:51:38.043878+00:00
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
- Primary crux: BTC is still more likely than not to finish above $70,000 on the April 18 noon ET Binance minute because spot was around 74.1k, but with only medium-quality verification, no strong independent four-day downside estimate, and a single-minute single-venue settlement, the bounded package is not strong enough to support acting against an 89% market.
- One-sentence rationale: Bitcoin is still the more likely side for the April 18 noon ET Binance close, but with no strong independent estimate of four-day downside risk and only medium verification on a single-minute single-venue market, the disciplined output is forbidden and needs-more-research rather than trading against an 89% market.

## Why this is the right action / no-action call

This is another case where directional belief and executable readiness diverge; the case is not ready for action even though Yes remains the base case.

## Valuation

- Fair value low: 0.82
- Fair value high: 0.87
- Fair value midpoint: 0.845
- Market reference price: 0.89
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current Binance BTC/USDT pricing above $70k supports a Yes lean, but exact-minute settlement mechanics, thin independent downside calibration, and residual implementation ambiguity keep fair value only modestly below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.76
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized from this packet because the case is not decision-ready.
- `scaled_enter`
  - `min_p:` 0.76
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0
  - `notes:` Even cheaper pricing would still require refreshed verification before action.
- `hold`
  - `min_p:` 0.82
  - `max_p:` 0.87
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair value zone, but not actionable under current evidence quality.
- `trim`
  - `min_p:` 0.87
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0
  - `notes:` Avoid increasing above fair value while downside distribution and settlement fragility remain insufficiently verified.
- `exit`
  - `min_p:` 0.94
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat or avoid at extreme prices because a single-minute crypto market still retains meaningful path risk.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T19:51:38.043878+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not enter from this packet; reopen only after a fresher settlement-proximate BTC check or stronger downside-risk calibration., Require better confirmation that the modest below-market view survives closer-to-settlement price action., Treat exact-minute Binance-close markets as operationally fragile when the edge is only modest.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below 71k-70k before the April 18 noon ET minute.
- A macro or crypto-specific downside catalyst materially raises short-horizon selloff risk.
- Evidence emerges that the operative Binance settlement minute or surface differs from the assumed mapping.

### Market structure breakers
- The current quote becomes stale relative to a materially changed Binance state.
- The assumed UI/API candle mapping proves wrong or disputed.

### Time breakers
- A fresh pre-settlement BTC check should supersede this packet before action.
- If no refreshed verification is available closer to settlement, this packet should not be used for trading.

### Reversal conditions
- Move from forbidden to watch-only or authorized only after stronger downside calibration or fresher price-state verification.
- Move lower if BTC compresses toward the threshold or settlement-surface ambiguity increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true four-day downside probability of BTC falling below $70k at the exact fixing minute.
- Whether any late macro or crypto catalyst emerges before settlement.
- Whether Binance UI-versus-API implementation details matter at the governing minute.

### Reasons to pass / stay small
- The edge versus market is modest and not strongly independently verified.
- Critical uncertainty is execution readiness, not directional belief.
- This is a single-minute single-venue crypto market where timing risk can dominate modest valuation gaps.

### What would change my mind
- A fresh same-venue check near settlement showing BTC still firmly above 74k would improve confidence and readiness.
- A stronger independent volatility or downside-tail estimate would make the market disagreement more actionable.
- A drop toward 71k-72k or any Binance-specific settlement ambiguity would lower fair value materially.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is another case where directional belief and executable readiness diverge; the case is not ready for action even though Yes remains the base case.

## Notes for downstream evaluator

BTC is still more likely than not to finish above $70,000 on the April 18 noon ET Binance minute because spot was around 74.1k, but with only medium-quality verification, no strong independent four-day downside estimate, and a single-minute single-venue settlement, the bounded package is not strong enough to support acting against an 89% market.
