---
type: decision_packet
case_key: case-20260415-75a50190
dispatch_id: refresh-case-20260415-75a50190-20260415T220500Z
question: "Will the price of Bitcoin be above $72,000 on April 21?"
market_id: 6c5bfff7-39b3-49d4-bb33-c8b7881a4e51
external_market_id: 0x98836967b3291ac597477867ab3e5d141ec344cac432df45f0aea9539fb5c4f2
market_slug: bitcoin-above-72k-on-april-21
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 21?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-75a50190/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-75a50190/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260415-75a50190/decision-maker/refreshes/refresh-case-20260415-75a50190-20260415T220500Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.72
fair_value_high: 0.78
fair_value_mid: 0.75
market_reference_price: 0.8
edge_mid_vs_market_pct_points: -5.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T22:05:57.552294+00:00
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
- Primary crux: The move from a prior fair-value center near 0.75 to a market price of 0.80 is best treated as repricing rather than a broken thesis: Bitcoin is still more likely than not to close above $72,000 on the April 21 noon ET Binance minute because same-venue spot around 74.8k leaves a real cushion, but the market now prices that cushion too richly for a six-day, single-minute settlement where a routine 4% drawdown or badly timed Binance dip can still decide the outcome.
- One-sentence rationale: BTC is still more likely than not to finish above $72,000 on the April 21 Binance noon minute, but the market's move to 0.80 pushes price above fair value centered near 0.75, so the disciplined output remains watch-only because meaningful exact-minute six-day downside tail is still live.

## Why this is the right action / no-action call

This refresh is primarily a valuation deterioration: same directional Yes, weaker execution case after repricing.

## Valuation

- Fair value low: 0.72
- Fair value high: 0.78
- Fair value midpoint: 0.75
- Market reference price: 0.8
- Edge vs market (percentage points): -5.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: No new bounded evidence justifies lifting fair value; the refresh added market repricing but not stronger independent verification that the remaining downside-path or exact-minute settlement risk has materially shrunk.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.65
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a materially cheaper price and refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.65
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if BTC remains comfortably above 72k and no new downside catalyst appears.
- `hold`
  - `min_p:` 0.72
  - `max_p:` 0.78
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.78
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a six-day one-minute crypto settlement with meaningful path dependence.
- `exit`
  - `min_p:` 0.86
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at rich prices because a routine downside move can still decide the contract.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T22:05:57.552294+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the updated market price., Treat exact-minute Binance settlement risk as the dominant execution constraint., Reopen only if market cheapens materially or if later same-venue checks show a larger sustained cushion above 72k with reduced volatility.

## Invalidation

### Thesis breakers
- BTC loses the 72k regime on Binance and fails to reclaim it before the Apr 21 fixing window.
- A downside macro, crypto, or exchange-specific shock materially raises the probability of a sub-72k settlement minute.
- Binance-specific pricing, liquidity, operational, or display-surface issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding same-venue spot deterioration, changing the value comparison.
- Binance microstructure or settlement-surface behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 21 12:00 ET should supersede this packet before any action.
- The actual Apr 21 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if later pre-fix Binance checks show BTC holding comfortably above 72k with a larger cushion.
- Downgrade if BTC compresses toward the threshold or if volatility expands.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a routine 4% downside move or wick landing on the exact settlement minute over the next six days.
- Whether an unscheduled macro or crypto-specific shock emerges before the fixing window.
- How much residual discount exact-minute Binance surface fragility deserves relative to a broader benchmark view.

### Reasons to pass / stay small
- The updated market price is above bounded fair value.
- This is a one-minute single-venue settlement contract where path risk matters more than broad BTC direction.
- The refresh added price movement, not new evidence supporting a higher probability.

### What would change my mind
- Later same-venue checks showing BTC still comfortably above 74k-75k into the final day would move me somewhat closer to market.
- A move back toward 72k-73k would reduce fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is primarily a valuation deterioration: same directional Yes, weaker execution case after repricing.

## Notes for downstream evaluator

The move from a prior fair-value center near 0.75 to a market price of 0.80 is best treated as repricing rather than a broken thesis: Bitcoin is still more likely than not to close above $72,000 on the April 21 noon ET Binance minute because same-venue spot around 74.8k leaves a real cushion, but the market now prices that cushion too richly for a six-day, single-minute settlement where a routine 4% drawdown or badly timed Binance dip can still decide the outcome.
