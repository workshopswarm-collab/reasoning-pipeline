---
type: decision_packet
case_key: case-20260413-f68a8c5c
dispatch_id: dispatch-case-20260413-f68a8c5c-20260413T165914Z
question: "Will the price of Bitcoin be above $68,000 on April 14?"
market_id: case-20260413-f68a8c5c
external_market_id: 0x0047decf5a127be6ec0ba4eee78c9b224eb2d5445aff6241377272eacd42114f
market_slug: bitcoin-above-68k-on-april-14
platform: polymarket
market_title: "Will the price of Bitcoin be above $68,000 on April 14?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-f68a8c5c/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-f68a8c5c/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.94
fair_value_high: 0.975
fair_value_mid: 0.958
market_reference_price: 0.9595
edge_mid_vs_market_pct_points: -0.2
independent_verification_quality: medium
compressed_toward_market_applied: false
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
- Primary crux: Fresh independent checks still place BTC around 72.3k, roughly 6.3% above 68,000, so Yes remains overwhelmingly likely, but the market already prices near-certainty for a still-future one-minute Binance settlement event.
- One-sentence rationale: BTC remains far enough above 68,000 that Yes is still very likely, but with the market already near 96% and the contract settling on one future Binance minute, the disciplined output is watch-only rather than fresh entry.

## Why this is the right action / no-action call

I treated synthesis as advisory, independently verified Binance spot, recent 1-minute closes, and CoinGecko spot, and ended almost exactly on market because the current cushion is large while the only residual risk is narrow settlement mechanics.

## Valuation

- Fair value low: 0.94
- Fair value high: 0.975
- Fair value midpoint: 0.958
- Market reference price: 0.9595
- Edge vs market (percentage points): -0.2
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Fresh bounded verification broadly confirms the upstream range and does not justify either a large discount or a large premium versus the existing market; the remaining risk is mostly narrow settlement mechanics rather than uncertainty about current spot.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; any much cheaper price would require a fresh late-window decision.
- `scaled_enter`
  - `min_p:` 0.86
  - `max_p:` 0.92
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry authorized because current evidence does not support a robust edge above market.
- `hold`
  - `min_p:` 0.92
  - `max_p:` 0.965
  - `target_exposure_fraction:` 0
  - `notes:` Hold-only zone consistent with a very likely Yes outcome but insufficient valuation cushion for fresh adds.
- `trim`
  - `min_p:` 0.965
  - `max_p:` 0.985
  - `target_exposure_fraction:` 0
  - `notes:` Trim/avoid increasing as price moves into the upper end of fair value.
- `exit`
  - `min_p:` 0.985
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because minute-level settlement risk still prevents certainty.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 600
- Valid until: 2026-04-14T15:50:00Z
- Time horizon: Into the April 14 12:00 ET / 16:00 UTC settlement minute

## Risk controls

- Max position size (% bankroll): 0.015
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 30
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the estimated edge versus market is negligible., Existing aligned exposure may be held, but avoid adding unless the market cheapens materially while BTC remains comfortably above 68,000 closer to settlement., Refresh live Binance data near settlement before any action because all residual uncertainty is concentrated in the final exact minute.

## Invalidation

### Thesis breakers
- BTCUSDT sells off sharply toward 68,000 before the operative settlement minute.
- Verified settlement mechanics differ materially from the assumed Binance 1-minute close interpretation used here.
- A venue-specific dislocation or broader market shock makes a sub-68,000 settlement close materially more likely than currently assumed.

### Market structure breakers
- Clarification of the operative Binance candle changes which minute or close governs settlement.
- Current executable market pricing diverges materially from the 0.9595 reference, making this packet stale for action decisions.
- Exchange outage or data integrity issues make Binance spot or kline data unreliable near settlement.

### Time breakers
- This packet expires at valid_until unless refreshed with later market and Binance data.
- Any new trading decision close to settlement should rely on fresher data than this packet.

### Reversal conditions
- Reverse only on a new packet after refreshed near-settlement Binance verification shows materially higher downside risk.
- Do not auto-reverse from this packet.
- Suspend this packet if market-reference or exchange-data assumptions break.

## Epistemic status

### Key uncertainties
- The exact April 14 12:00 ET settlement candle is still in the future, so residual path risk cannot be eliminated.
- Minor UI/API exact-candle parity ambiguity remains if a discrepancy appears near settlement.
- Independent verification quality is medium because bounded checks confirm current cushion and cross-source alignment, not the future resolving minute itself.

### Reasons to pass / stay small
- At 95.95%, the market already prices almost all of the obvious Yes case.
- One-minute single-venue settlement means even a comfortably in-the-money threshold can still fail on a rare but real tail path.
- A tiny theoretical edge is not worth acting on when the market and fair value are already nearly identical.

### What would change my mind
- A sharp pre-settlement selloff toward 68,000 would lower fair value materially.
- A material market repricing lower without a corresponding BTC drop could create a genuine Yes edge and justify authorization.
- Direct confirmation eliminating settlement-surface ambiguity would slightly improve confidence but would not by itself create meaningful EV at current pricing.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: I treated synthesis as advisory, independently verified Binance spot, recent 1-minute closes, and CoinGecko spot, and ended almost exactly on market because the current cushion is large while the only residual risk is narrow settlement mechanics.

## Notes for downstream evaluator

Fresh independent checks still place BTC around 72.3k, roughly 6.3% above 68,000, so Yes remains overwhelmingly likely, but the market already prices near-certainty for a still-future one-minute Binance settlement event.
