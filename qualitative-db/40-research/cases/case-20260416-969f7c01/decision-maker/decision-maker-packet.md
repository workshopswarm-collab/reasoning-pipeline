---
type: decision_packet
case_key: case-20260416-969f7c01
dispatch_id: refresh-case-20260416-969f7c01-20260416T020025Z
question: "Will the price of Ethereum be above $2,200 on April 17?"
market_id: 30172bb7-9f35-4ca6-93a4-adb8544ba07a
external_market_id: 0x99eb86c2cf41bbf90f3df2f839525c317790ad8b8024f55a80c997255e8787f7
market_slug: ethereum-above-2200-on-april-17
platform: polymarket
market_title: "Will the price of Ethereum be above $2,200 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260416-969f7c01/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-969f7c01/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260416-969f7c01/decision-maker/refreshes/refresh-case-20260416-969f7c01-20260416T020025Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.89
fair_value_high: 0.92
fair_value_mid: 0.905
market_reference_price: 0.955
edge_mid_vs_market_pct_points: -5.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-17T02:01:20.988427+00:00
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
- Primary crux: The move from 0.945 to 0.955 is best treated as repricing rather than a broken thesis: ETH above $2,200 on the April 17 noon ET Binance minute remains the clear base case, but the market is now even richer relative to bounded fair value for a venue-specific single-minute contract with overnight tail risk still live.
- One-sentence rationale: ETH above $2,200 on the April 17 Binance noon minute remains the clear base case, but with fair value still around 0.905 and the market now repriced to 0.955, the disciplined output remains watch-only because the richer price further overstates confidence in a single-minute crypto settlement.

## Why this is the right action / no-action call

This refresh is valuation deterioration, not regime change: same directional Yes, worse execution economics.

## Valuation

- Fair value low: 0.89
- Fair value high: 0.92
- Fair value midpoint: 0.905
- Market reference price: 0.955
- Edge vs market (percentage points): -5.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: The prior bounded synthesis already incorporated a strong above-strike ETH regime; the new market move adds price, not new evidence, so fair value stays unchanged while execution worsens.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0
  - `notes:` Would require an unusually large dislocation versus this packet's high Yes base case.
- `scaled_enter`
  - `min_p:` 0.82
  - `max_p:` 0.89
  - `target_exposure_fraction:` 0
  - `notes:` Potential value zone if ETH remains comfortably above strike and no new settlement-surface issues appear.
- `hold`
  - `min_p:` 0.89
  - `max_p:` 0.92
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.92
  - `max_p:` 0.96
  - `target_exposure_fraction:` 0
  - `notes:` Above fair value for a one-minute crypto settlement with residual path risk.
- `exit`
  - `min_p:` 0.96
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Avoid or exit at near-certainty pricing because even a brief downside move can flip the result.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-17T02:01:20.988427+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the updated market price., Treat exact-minute Binance settlement risk as the dominant execution constraint even with a strong directional Yes view., Reopen only if market cheapens materially or if a near-settlement Binance check preserves a large cushion above 2200.

## Invalidation

### Thesis breakers
- ETH/USDT moves materially closer to 2200 or below it before the Apr 17 fixing window.
- A bearish macro, crypto, or exchange-specific shock materially raises the probability of a sub-2200 settlement minute.
- Binance-specific pricing, liquidity, or display-surface issues emerge near resolution.

### Market structure breakers
- Market reprices materially after fresh spot or volatility changes, altering the value comparison.
- Binance settlement-surface or ET-to-UTC candle mapping behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation on Apr 17 morning should supersede this packet before any action.
- The actual Apr 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if later pre-fix Binance checks still show a wide cushion above 2200 and the market price cheapens below fair value.
- Downgrade if ETH loses substantial cushion or volatility rises materially.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the current cushion above 2200 survives the exact settlement minute.
- Whether overnight or U.S.-morning shocks emerge before the fixing window.
- How much residual discount exact-minute Binance UI-versus-API sensitivity deserves at this price level.

### Reasons to pass / stay small
- The updated market price is even further above bounded fair value.
- The refresh added repricing, not stronger evidence.
- The contract still resolves on one exact Binance minute rather than broad daily direction.

### What would change my mind
- A fresh near-settlement Binance check still showing ETH comfortably above 2200 with stable conditions would modestly improve confidence.
- A materially cheaper market price with unchanged cushion would improve the execution case.
- A fast move toward 2300 or below would reduce directional confidence materially.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is valuation deterioration, not regime change: same directional Yes, worse execution economics.

## Notes for downstream evaluator

The move from 0.945 to 0.955 is best treated as repricing rather than a broken thesis: ETH above $2,200 on the April 17 noon ET Binance minute remains the clear base case, but the market is now even richer relative to bounded fair value for a venue-specific single-minute contract with overnight tail risk still live.
