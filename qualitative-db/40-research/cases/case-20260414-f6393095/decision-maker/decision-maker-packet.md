---
type: decision_packet
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
question: "Will the price of Bitcoin be above $70,000 on April 17?"
market_id: 02f818d5-3451-482c-ba4b-0a663270e680
external_market_id: 0x80281108ecd458d73c9e0eafe0946a91645d98771f1326e565657b6f8dcc00e6
market_slug: bitcoin-above-70k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-f6393095/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-f6393095/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.9
fair_value_high: 0.93
fair_value_mid: 0.915
market_reference_price: 0.935
edge_mid_vs_market_pct_points: -2.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-15T22:31:32.449821+00:00
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
- Primary crux: BTC is still very likely to finish above $70,000 on the April 17 noon ET Binance minute because same-venue spot remained around 73.9k-74.1k and the recent 24h low stayed above 70k, but the market's 93.5% price is only slightly rich rather than clearly wrong because the remaining disagreement is mostly about exact-minute settlement fragility.
- One-sentence rationale: Bitcoin is likely to finish above $70,000 on the April 17 noon ET Binance minute because current same-venue pricing remains materially above the strike and recent lows stayed above it, but the market's 93.5% price is only slightly too confident for a one-minute single-venue settlement, so the disciplined posture remains watch-only.

## Why this is the right action / no-action call

This is a high-probability Yes with only a marginal valuation discount versus market, not a compelling execution opportunity.

## Valuation

- Fair value low: 0.9
- Fair value high: 0.93
- Fair value midpoint: 0.915
- Market reference price: 0.935
- Edge vs market (percentage points): -2.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current Binance BTC/USDT pricing comfortably above $70k with limited time remaining supports a high-probability Yes view, but exact-minute settlement mechanics and lack of a stronger short-horizon volatility model keep fair value a bit below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh venue and path-risk check.
- `scaled_enter`
  - `min_p:` 0.86
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current packet sees only a very modest below-market valuation gap.
- `hold`
  - `min_p:` 0.9
  - `max_p:` 0.93
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with bounded fair value for a high-probability Yes outcome.
- `trim`
  - `min_p:` 0.93
  - `max_p:` 0.98
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above fair value and exact-minute risk dominates.
- `exit`
  - `min_p:` 0.98
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit or avoid at extreme prices because remaining uncertainty is almost entirely timing, path, and venue-specific.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T22:31:32.449821+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market is already at or above bounded fair value., Refresh if BTC weakens toward 72k or below, or if Binance-specific stress emerges before settlement., Treat this as an exact-minute Binance-close contract rather than a broad BTC directional bet.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below 72k on Binance before the April 17 noon ET minute.
- A macro or crypto-specific shock materially raises downside risk before settlement.
- Evidence emerges of a Binance-specific print, timestamp, or operational anomaly affecting the governing minute.

### Market structure breakers
- The current quote becomes stale relative to a materially changed Binance state.
- The operative Binance settlement surface differs meaningfully from the assumed one-minute close representation.

### Time breakers
- The exact April 17 12:00 ET Binance candle should supersede this packet once observed.
- Confidence should be reduced if the cushion compresses materially during the final pre-settlement window.

### Reversal conditions
- Move modestly higher only on a fresh packet if BTC remains firmly above mid-73k into settlement while price remains favorable.
- Move materially lower on a fresh packet if BTC drifts toward the threshold or Binance-specific stress intensifies.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true short-horizon downside distribution for BTC into the exact fixing minute.
- Whether any Binance-specific wick or microstructure event matters at settlement.
- How much of the remaining one-minute path fragility the market is already pricing.

### Reasons to pass / stay small
- The market already prices a very high Yes probability and leaves little room for error.
- The residual disagreement versus market is small and not strongly independently verified as a tradable edge.

### What would change my mind
- A fresh same-venue check closer to settlement showing BTC still comfortably above 73k-74k would move me slightly toward the market.
- A drop toward 71k-72k or below would reduce fair value materially.
- Evidence of Binance-specific operational or settlement-surface anomalies would lower confidence despite current spot being above strike.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a high-probability Yes with only a marginal valuation discount versus market, not a compelling execution opportunity.

## Notes for downstream evaluator

BTC is still very likely to finish above $70,000 on the April 17 noon ET Binance minute because same-venue spot remained around 73.9k-74.1k and the recent 24h low stayed above 70k, but the market's 93.5% price is only slightly rich rather than clearly wrong because the remaining disagreement is mostly about exact-minute settlement fragility.
