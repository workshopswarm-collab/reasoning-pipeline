---
type: decision_packet
case_key: case-20260415-540d9abf
dispatch_id: refresh-case-20260415-540d9abf-20260415T235725Z
question: "Will the price of Solana be above $80 on April 19?"
market_id: 139f80d9-bf3b-4b6b-9dea-031313b6ae5b
external_market_id: 0x00b28e37776a7f2f56ceec3bc4cf4f49d832b1c9db1ddd1cb597fb4438918f95
market_slug: solana-above-80-on-april-19
platform: polymarket
market_title: "Will the price of Solana be above $80 on April 19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-540d9abf/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-540d9abf/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260415-540d9abf/decision-maker/refreshes/refresh-case-20260415-540d9abf-20260415T235725Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.8
fair_value_high: 0.87
fair_value_mid: 0.835
market_reference_price: 0.9
edge_mid_vs_market_pct_points: -6.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T23:58:21.710801+00:00
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
- Primary crux: The move from a prior fair-value center near 0.835 to a market price of 0.90 is best treated as repricing rather than a broken thesis: Solana is still more likely than not to close above $80 on the April 19 noon ET Binance minute because current same-venue pricing around 84.9 leaves a meaningful cushion, but the market now prices that cushion too richly for a single-minute settlement where a normal crypto selloff or brief noon-minute dip can still decide the outcome.
- One-sentence rationale: SOL is still more likely than not to finish above $80 on the April 19 Binance noon minute, but the market's move to 0.90 pushes price above fair value centered near 0.835, so the disciplined output remains watch-only because meaningful exact-minute downside tail is still live.

## Why this is the right action / no-action call

This refresh is primarily a valuation deterioration: same directional Yes, weaker execution case after repricing.

## Valuation

- Fair value low: 0.8
- Fair value high: 0.87
- Fair value midpoint: 0.835
- Market reference price: 0.9
- Edge vs market (percentage points): -6.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: No new bounded evidence justifies lifting fair value; the refresh added market repricing but not stronger independent verification that the remaining downside-path or exact-minute settlement risk has materially shrunk.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price and refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.72
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if SOL remains comfortably above 80 and no new downside catalyst appears.
- `hold`
  - `min_p:` 0.8
  - `max_p:` 0.87
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.87
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a single-minute crypto threshold with meaningful multi-day path dependence.
- `exit`
  - `min_p:` 0.94
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at very rich prices because exact-minute downside tail still matters.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T23:58:21.710801+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the updated market price., Treat exact-minute Binance settlement risk as the dominant execution constraint., Reopen only if market cheapens materially or if later same-venue checks show SOL holding comfortably above 80 with reduced volatility.

## Invalidation

### Thesis breakers
- SOL loses the 80 level on Binance and fails to reclaim it before the Apr 19 fixing window.
- A downside crypto, SOL-specific, or exchange-specific shock materially raises the probability of a sub-80 settlement minute.
- Binance-specific pricing, liquidity, operational, or display-surface issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding same-venue spot deterioration, changing the value comparison.
- Binance microstructure or settlement-surface behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 19 12:00 ET should supersede this packet before any action.
- The actual Apr 19 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if later pre-fix Binance checks show SOL holding comfortably above 80 with reduced downside risk.
- Downgrade if SOL compresses toward the threshold or if volatility expands.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a ~5-6% downside move or wick landing on the exact settlement minute over the next several days.
- Whether a crypto-wide or SOL-specific shock emerges before the fixing window.
- How much residual discount exact-minute Binance UI-versus-API candle sensitivity deserves at current prices.

### Reasons to pass / stay small
- The updated market price is above bounded fair value.
- This is a one-minute single-venue settlement contract where path risk matters more than broad SOL direction.
- The refresh added price movement, not new evidence supporting a higher probability.

### What would change my mind
- Later same-venue checks showing SOL still comfortably above 82-84 into the final day would move me somewhat closer to market.
- A move back toward 80-81 would reduce fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is primarily a valuation deterioration: same directional Yes, weaker execution case after repricing.

## Notes for downstream evaluator

The move from a prior fair-value center near 0.835 to a market price of 0.90 is best treated as repricing rather than a broken thesis: Solana is still more likely than not to close above $80 on the April 19 noon ET Binance minute because current same-venue pricing around 84.9 leaves a meaningful cushion, but the market now prices that cushion too richly for a single-minute settlement where a normal crypto selloff or brief noon-minute dip can still decide the outcome.
