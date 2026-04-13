---
type: decision_packet
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
question: "Will the price of Bitcoin be above $70,000 on April 13?"
market_id: case-20260413-2d3a41aa
external_market_id: 0xbc820c185b6fe8a77c3ac68a54bdcd6ef28667b5f4ec5f09c0ea65002c6ee49e
market_slug: bitcoin-above-70k-on-april-13
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 13?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-2d3a41aa/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-2d3a41aa/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.77
fair_value_high: 0.87
fair_value_mid: 0.82
market_reference_price: 0.71
edge_mid_vs_market_pct_points: 11.0
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
- Primary crux: Fresh independent checks still show BTC around 71.6k, safely above 70,000, so Yes remains the likelier outcome, but the market snapshot is likely stale and the residual edge is too dependent on one future Binance minute close to justify fresh authorization.
- One-sentence rationale: BTC is still trading above 70,000, so Yes remains the better directional call, but because the provided 0.71 market baseline is likely stale and the contract settles on one future Binance minute, the disciplined output is watch-only rather than fresh entry.

## Why this is the right action / no-action call

I treated synthesis as advisory, independently verified Binance spot, recent Binance 1-minute closes, and CoinGecko spot, but declined authorization because independent live market-price refresh failed under bot detection and the bundle itself warns the assignment snapshot may be stale.

## Valuation

- Fair value low: 0.77
- Fair value high: 0.87
- Fair value midpoint: 0.82
- Market reference price: 0.71
- Edge vs market (percentage points): 11.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: I compressed only modestly from the fresh above-strike price signal, but I will not authorize action because the provided 0.71 market baseline is likely stale and I could not independently refresh the live market price within bounded verification after web_search failed with bot detection.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.62
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet because current uncertainty is about stale market reference, not just direction.
- `scaled_enter`
  - `min_p:` 0.62
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry authorized; even if the provided baseline looks cheap, it may no longer be current.
- `hold`
  - `min_p:` 0.72
  - `max_p:` 0.84
  - `target_exposure_fraction:` 0
  - `notes:` Hold-only zone reflecting a probable Yes without enough verified price edge for fresh adds.
- `trim`
  - `min_p:` 0.84
  - `max_p:` 0.92
  - `target_exposure_fraction:` 0
  - `notes:` Avoid increasing as price approaches upper fair-value estimates or if a refreshed market has already repriced.
- `exit`
  - `min_p:` 0.92
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at rich prices because the contract still settles on one future minute and edge disappears quickly.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-13T15:50:00Z
- Time horizon: Remainder of the morning into the Binance 12:00 ET / 16:00 UTC settlement candle

## Risk controls

- Max position size (% bankroll): 0.015
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 35
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the supplied market reference may be stale and residual value depends on exact live pricing., Existing aligned exposure may be held, but avoid adding unless a refreshed authoritative market quote still shows a meaningful discount while BTC remains above 70,000., Refresh both market price and live Binance data close to settlement before any new action.

## Invalidation

### Thesis breakers
- BTCUSDT falls sharply back toward or below 70,000 before the operative settlement minute.
- A refreshed authoritative market quote shows the apparent discount versus 0.71 has already disappeared.
- Verified settlement mechanics differ materially from the assumed Binance 1-minute close interpretation used here.

### Market structure breakers
- The supplied market reference is confirmed stale or mismatched to the current contract view, making this packet's edge estimate obsolete.
- Exchange outage or data integrity issues make Binance spot or kline data unreliable near settlement.
- A later authoritative market refresh materially contradicts the assumptions carried from the bounded bundle.

### Time breakers
- This packet expires at valid_until unless refreshed with later pre-settlement market and Binance data.
- Any new trading decision close to settlement should rely on fresher price data than this packet.

### Reversal conditions
- Reverse only on a new packet after refreshed live market pricing and near-settlement Binance verification.
- Do not auto-reverse from this packet.
- Suspend this packet if exchange-data or market-reference assumptions break.

## Epistemic status

### Key uncertainties
- The biggest live uncertainty is not current BTC direction but whether the provided 0.71 market baseline is still current enough to support an edge claim.
- The exact governing Binance 12:00 ET candle is still in the future, so same-morning path risk remains live.
- Independent verification quality is medium because bounded checks confirmed price cushion and cross-source consistency, but not a refreshed market quote after web_search failed.

### Reasons to pass / stay small
- If the market has already repriced upward from 0.71, the apparent edge may be gone or much smaller.
- Single-minute settlement means the trade can still lose on a brief late selloff even if current spot remains above 70,000.
- A stale baseline can create false confidence in EV, so restraint is higher EV than bluffing precision.

### What would change my mind
- A refreshed authoritative market quote still showing a substantial discount to fair value would justify authorization.
- A sharp BTC move down toward 70,000 would materially reduce fair value and could flip the side.
- Direct confirmation of the current market state from the resolution platform or a reliable market API would reduce the main execution blocker.

### Decision quality
- `fragile`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: I treated synthesis as advisory, independently verified Binance spot, recent Binance 1-minute closes, and CoinGecko spot, but declined authorization because independent live market-price refresh failed under bot detection and the bundle itself warns the assignment snapshot may be stale.

## Notes for downstream evaluator

Fresh independent checks still show BTC around 71.6k, safely above 70,000, so Yes remains the likelier outcome, but the market snapshot is likely stale and the residual edge is too dependent on one future Binance minute close to justify fresh authorization.
