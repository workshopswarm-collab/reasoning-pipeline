---
type: decision_packet
case_key: case-20260413-9e664afd
dispatch_id: dispatch-case-20260413-9e664afd-20260413T164930Z
question: "Will the price of Bitcoin be above $70,000 on April 14?"
market_id: case-20260413-9e664afd
external_market_id: 0xb4edd1ceca7ae170d1ed632677a8671797b3d47374d38ffac7d410cfb9e9f5c7
market_slug: bitcoin-above-70k-on-april-14
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 14?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-9e664afd/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-9e664afd/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.84
fair_value_high: 0.9
fair_value_mid: 0.87
market_reference_price: 0.845
edge_mid_vs_market_pct_points: 2.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-14T15:50:00Z
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
- Primary crux: Fresh independent checks still place BTC around 72.15k, comfortably above 70,000, so Yes remains the base case, but the market pricing is internally inconsistent across sources and the contract still turns on one future Binance minute close, which makes the true edge too uncertain for fresh authorization.
- One-sentence rationale: BTC is still clearly above 70,000, so Yes remains the better directional call, but because the bounded inputs contain inconsistent market pricing and the contract settles on one future Binance minute, the disciplined output is watch-only rather than fresh entry.

## Why this is the right action / no-action call

I treated synthesis as advisory, independently verified Binance spot, recent 1-minute closes, and CoinGecko spot, and kept fair value in the high-Yes range while refusing authorization because the sign of the edge depends too much on which cited market price is actually live.

## Valuation

- Fair value low: 0.84
- Fair value high: 0.9
- Fair value midpoint: 0.87
- Market reference price: 0.845
- Edge vs market (percentage points): 2.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: I keep fair value in the high-Yes range given current BTC distance above 70k, but I compress toward market because the true live market baseline is internally inconsistent inside the bounded package and the final result still depends on one future Binance minute close.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; such a cheap market would require a fresh packet with reconciled market pricing.
- `scaled_enter`
  - `min_p:` 0.72
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry authorized because current evidence does not robustly establish edge against a reliable live market baseline.
- `hold`
  - `min_p:` 0.82
  - `max_p:` 0.88
  - `target_exposure_fraction:` 0
  - `notes:` Hold-only zone consistent with a strong Yes base case but insufficiently verified pricing edge.
- `trim`
  - `min_p:` 0.88
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0
  - `notes:` Avoid increasing as price reaches the upper portion of fair value or matches the higher live-page baseline cited in the bundle.
- `exit`
  - `min_p:` 0.94
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at rich prices because exact-minute path dependence leaves no justified edge there.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 600
- Valid until: 2026-04-14T15:50:00Z
- Time horizon: Final day into the Apr 14 noon ET / 16:00 UTC settlement minute

## Risk controls

- Max position size (% bankroll): 0.015
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 35
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because market-pricing inconsistency plus exact-minute path risk makes the edge insufficiently robust., Existing aligned exposure may be held, but avoid adding unless a refreshed authoritative market quote still shows meaningful discount while BTC remains comfortably above 70,000., Refresh both market price and live Binance data near settlement before any action.

## Invalidation

### Thesis breakers
- BTCUSDT falls sharply back toward or below 70,000 before the operative settlement minute.
- A refreshed authoritative market quote confirms the live market is already near the higher ~93% level, removing any residual value case.
- Verified settlement mechanics differ materially from the assumed Binance 1-minute close interpretation used here.

### Market structure breakers
- The discrepancy between the dispatch baseline and the fetched live page is resolved in a way that materially changes the edge calculation.
- Exchange outage or data integrity issues make Binance spot or kline data unreliable near settlement.
- A clarified rule interpretation elevates UI-versus-API settlement-surface differences from minor to material.

### Time breakers
- This packet expires at valid_until unless refreshed with later market and Binance data.
- Any new trading decision close to settlement should rely on fresher data than this packet.

### Reversal conditions
- Reverse only on a new packet after refreshed authoritative market pricing and near-settlement Binance verification.
- Do not auto-reverse from this packet.
- Suspend this packet if market-reference or exchange-data assumptions break.

## Epistemic status

### Key uncertainties
- The largest uncertainty is whether the true live market baseline is closer to 84.5% or the higher ~93% cited from the fetched page in the bundle.
- The contract still settles on one future Binance minute close, so path risk remains live despite current cushion.
- Minor UI-versus-API source-of-truth ambiguity remains if any discrepancy appears near settlement.

### Reasons to pass / stay small
- If the real live market is already near 93%, the apparent edge versus 84.5% is illusory.
- A one-minute single-venue crypto settlement can lose on a brief late selloff even when current spot looks favorable.
- A modest edge is not worth trading when the market baseline itself is not cleanly verified.

### What would change my mind
- A refreshed authoritative market quote still materially below my fair value would justify authorization.
- A sharp BTC move back toward 70,000 would lower fair value materially and could flip the side.
- Direct confirmation that the settlement surface aligns cleanly with the API-equivalent minute data would modestly improve confidence.

### Decision quality
- `fragile`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: I treated synthesis as advisory, independently verified Binance spot, recent 1-minute closes, and CoinGecko spot, and kept fair value in the high-Yes range while refusing authorization because the sign of the edge depends too much on which cited market price is actually live.

## Notes for downstream evaluator

Fresh independent checks still place BTC around 72.15k, comfortably above 70,000, so Yes remains the base case, but the market pricing is internally inconsistent across sources and the contract still turns on one future Binance minute close, which makes the true edge too uncertain for fresh authorization.
