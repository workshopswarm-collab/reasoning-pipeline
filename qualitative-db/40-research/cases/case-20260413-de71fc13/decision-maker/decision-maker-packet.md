---
type: decision_packet
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
question: "Will the price of Bitcoin be above $68,000 on April 13?"
market_id: case-20260413-de71fc13
external_market_id: 0x06111b1cdb7ec493e413a5691c410ce3423c86929d0b168f6078e341adbb6a46
market_slug: bitcoin-above-68k-on-april-13
platform: polymarket
market_title: "Will the price of Bitcoin be above $68,000 on April 13?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-de71fc13/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-de71fc13/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.93
fair_value_high: 0.965
fair_value_mid: 0.945
market_reference_price: 0.929
edge_mid_vs_market_pct_points: 1.6
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-13T15:50:00Z
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
- Primary crux: Fresh independent checks show BTC still around 71.2k, comfortably above 68,000, so Yes remains highly likely, but the market at 0.929 already captures most of that advantage for a contract settled on one still-future Binance minute close.
- One-sentence rationale: BTC remains comfortably above 68,000 across independent checks, so Yes is still likely, but the market already prices most of that advantage for a contract that settles on one still-future Binance minute close.

## Why this is the right action / no-action call

I treated synthesis as advisory, independently checked Binance spot, recent Binance 1-minute closes, and CoinGecko spot, and ended only modestly above market because the remaining uncertainty is entirely concentrated in the unformed noon-ET settlement minute.

## Valuation

- Fair value low: 0.93
- Fair value high: 0.965
- Fair value midpoint: 0.945
- Market reference price: 0.929
- Edge vs market (percentage points): 1.6
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: I keep fair value only modestly above the market because the decisive settlement candle is still in the future, single-minute single-venue risk remains live until noon ET, and independent verification cannot yet observe the exact governing close.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.84
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; a much cheaper market would require a fresh near-settlement decision.
- `scaled_enter`
  - `min_p:` 0.84
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry authorized because current bounded evidence supports only a modest edge over market.
- `hold`
  - `min_p:` 0.9
  - `max_p:` 0.945
  - `target_exposure_fraction:` 0
  - `notes:` Hold-only zone consistent with a strong Yes that is not cheap enough for fresh adds.
- `trim`
  - `min_p:` 0.945
  - `max_p:` 0.975
  - `target_exposure_fraction:` 0
  - `notes:` Trim/avoid increasing as price moves through the upper portion of fair value.
- `exit`
  - `min_p:` 0.975
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because the market would be overpaying for a still-future minute-specific settlement.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-13T15:50:00Z
- Time horizon: Same-day hours remaining into the noon ET / 16:00 UTC Binance settlement candle

## Risk controls

- Max position size (% bankroll): 0.015
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 30
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the estimated edge is modest relative to the event's exact-minute structure., Existing aligned exposure may be held, but avoid adding unless the market cheapens materially while BTC remains comfortably above 68,000 closer to settlement., Refresh live Binance data near settlement before any action because remaining uncertainty is concentrated in the final exact minute.

## Invalidation

### Thesis breakers
- BTCUSDT sells off sharply toward 68,000 before the operative settlement minute.
- Verified settlement mechanics differ materially from the assumed Binance 1-minute close interpretation used here.
- A venue-specific dislocation or broader market shock makes a sub-68,000 settlement close materially more likely than currently assumed.

### Market structure breakers
- Clarification of the operative Binance candle changes which minute or close governs settlement.
- Current executable market pricing diverges materially from the 0.929 reference, making this packet stale for action decisions.
- Exchange outage or data integrity issues make Binance spot or kline data unreliable near settlement.

### Time breakers
- This packet expires at valid_until unless refreshed with later pre-settlement data.
- Any new trading decision closer to settlement should rely on fresher data than this packet.

### Reversal conditions
- Reverse only on fresh late-window evidence that BTC has moved materially closer to 68,000 or below it with meaningful settlement risk.
- Do not auto-reverse from this packet; require a new packet with refreshed near-settlement verification.
- Suspend this packet if exchange-data or candle-interpretation assumptions break.

## Epistemic status

### Key uncertainties
- The exact governing Binance 12:00 ET candle close is still in the future, so path risk cannot be eliminated pre-resolution.
- Minor last-mile ambiguity remains between Binance API verification and the exact settlement-surface interpretation.
- Independent verification quality is medium because bounded checks confirm current cushion and cross-source consistency, not the future resolving minute itself.

### Reasons to pass / stay small
- At 0.929, the market already prices most of the obvious Yes advantage.
- Single-minute single-venue settlement makes a modest edge less attractive than it appears from spot cushion alone.
- A few-percent intraday move is not impossible in BTC, and one future minute alone decides the outcome.

### What would change my mind
- A sharp late-morning selloff toward 68,000 would lower fair value materially and could flip the side.
- A material market repricing lower without a corresponding BTC drop could create a better Yes entry and justify authorization.
- Direct confirmation from the exact settlement surface eliminating remaining minute-label ambiguity would slightly raise confidence but would not by itself create a large edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: I treated synthesis as advisory, independently checked Binance spot, recent Binance 1-minute closes, and CoinGecko spot, and ended only modestly above market because the remaining uncertainty is entirely concentrated in the unformed noon-ET settlement minute.

## Notes for downstream evaluator

Fresh independent checks show BTC still around 71.2k, comfortably above 68,000, so Yes remains highly likely, but the market at 0.929 already captures most of that advantage for a contract settled on one still-future Binance minute close.
