---
type: decision_packet
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
question: "Will the price of Bitcoin be above $72,000 on April 15?"
market_id: case-20260413-395c5631
external_market_id: 0x7bdc81de7fa3bafa5ac9d027ff0a88d2b52e13a9b7b6872e2b49d4d281ae4f94
market_slug: bitcoin-above-72k-on-april-15
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 15?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-395c5631/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-395c5631/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: needs_more_research
fair_value_low: 0.68
fair_value_high: 0.76
fair_value_mid: 0.73
market_reference_price: 0.725
edge_mid_vs_market_pct_points: 0.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: low
valid_until: 2026-04-15T10:00:00-04:00
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
- Decision readiness: `needs_more_research`
- Primary crux: BTC is currently above the 72k strike and Yes is directionally favored, but the market already prices that at 72.5% and the contract resolves on a single Binance one-minute close at noon ET, so timing and exact-minute volatility risk leave too little edge for authorization without a fresher governing-venue check.
- One-sentence rationale: BTC above 72k remains slightly more likely than not by the Apr. 15 noon ET Binance minute, but because the market is already near fair value and the contract is mechanically fragile to exact-minute volatility, the disciplined output is watch-only and needs-more-research rather than an authorized trade.

## Why this is the right action / no-action call

This packet intentionally distinguishes directional lean from execution readiness: the bounded evidence supports a modest yes view, but not enough edge or freshness to justify action in a short-dated single-minute crypto market.

## Valuation

- Fair value low: 0.68
- Fair value high: 0.76
- Fair value midpoint: 0.73
- Market reference price: 0.725
- Edge vs market (percentage points): 0.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: The current above-strike cushion supports a modest yes lean, but exact-minute settlement fragility and lack of fresh governing-venue verification compress fair value toward the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.4
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the case is not ready and requires a fresh pre-settlement venue check.
- `scaled_enter`
  - `min_p:` 0.4
  - `max_p:` 0.62
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized until exact-minute settlement risk is refreshed close to resolution.
- `hold`
  - `min_p:` 0.62
  - `max_p:` 0.75
  - `target_exposure_fraction:` 0
  - `notes:` Hold/watch zone; yes is directionally favored but edge is too small and timing risk too important.
- `trim`
  - `min_p:` 0.75
  - `max_p:` 0.88
  - `target_exposure_fraction:` 0
  - `notes:` Avoid adding above fair value because single-minute volatility can still flip the contract.
- `exit`
  - `min_p:` 0.88
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at very high prices because exact-minute settlement risk is nontrivial even with spot above strike.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.08
- Allow auto reversal: `false`
- Quote staleness seconds: 3600
- Valid until: 2026-04-15T10:00:00-04:00
- Time horizon: Now through the Apr. 15 12:00 ET Binance settlement minute

## Risk controls

- Max position size (% bankroll): 0.005
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 50
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not initiate new exposure from this packet because the market is near bounded fair value and the case remains mechanically fragile., Reassess only after a fresh governing-venue Binance check close to settlement and a morning-of-resolution catalyst sweep., Treat exact-minute threshold markets as higher-risk than ordinary directional crypto views because path and timing matter as much as level.

## Invalidation

### Thesis breakers
- Fresh Binance price action loses 72k and fails to recover as settlement approaches.
- Morning-of-resolution macro or headline shocks trigger a broad risk-off move into the noon ET settlement minute.
- Clarification of resolution mechanics changes the effective settlement candle or venue interpretation.

### Market structure breakers
- The displayed market is already efficiently pricing the exact-minute volatility distribution, leaving no actionable edge.
- Venue-specific Binance microstructure or liquidation cascades distort the one-minute close relative to broader spot conditions.
- Adjacent strike pricing or updated market structure implies a materially different short-horizon distribution than currently assumed.

### Time breakers
- A fresh pre-settlement Binance check is mandatory because this packet will stale quickly on a sub-day horizon.
- The Apr. 15 morning U.S. data window and the final approach to noon ET can rapidly dominate all current reasoning.

### Reversal conditions
- Move toward authorized yes only if fresh Binance verification still shows a comfortable buffer above 72k with no major catalyst risk and market price remains favorable.
- Move toward no if BTC repeatedly trades below 72k or if volatility regime worsens materially before settlement.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Exact Binance BTC/USDT level and volatility profile closer to the settlement minute.
- Whether Apr. 15 morning macro or headline flow creates a short-lived downside move below strike.
- How much the current market already embeds exact-minute settlement fragility.

### Reasons to pass / stay small
- The package explicitly flags no fresh synthesis-time Binance verification.
- The market is effectively at bounded fair value, so there is minimal valuation cushion.
- Single-minute settlement contracts are unusually sensitive to path-dependent volatility and last-hour catalysts.

### What would change my mind
- A fresh Binance check near settlement showing BTC stably and comfortably above 72k would improve readiness for yes.
- Repeated trading below 72k or rising realized volatility into the settlement window would move me lower.
- A cleaner morning-of-resolution catalyst audit showing low shock risk would modestly improve the yes case.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet intentionally distinguishes directional lean from execution readiness: the bounded evidence supports a modest yes view, but not enough edge or freshness to justify action in a short-dated single-minute crypto market.

## Notes for downstream evaluator

BTC is currently above the 72k strike and Yes is directionally favored, but the market already prices that at 72.5% and the contract resolves on a single Binance one-minute close at noon ET, so timing and exact-minute volatility risk leave too little edge for authorization without a fresher governing-venue check.
