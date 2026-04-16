---
type: decision_packet
case_key: case-20260414-94e8aad1
dispatch_id: dispatch-case-20260414-94e8aad1-20260414T175223Z
question: "Will the price of Bitcoin be above $70,000 on April 16?"
market_id: b5021d2c-0b79-403b-a5df-3221dc962905
external_market_id: 0x24c9d39348a3ca9f3464ac85ac14826cd40c25fb2f4baf545602f1208baaf16c
market_slug: bitcoin-above-70k-on-april-16
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 16?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-94e8aad1/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-94e8aad1/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.92
fair_value_high: 0.95
fair_value_mid: 0.935
market_reference_price: 0.9595
edge_mid_vs_market_pct_points: -2.4
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-15T18:00:57.156794+00:00
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
- Primary crux: BTC is still very likely to finish above $70,000 on the April 16 noon ET Binance minute because same-venue spot remains around 74.7k with recent lows above 72k, but the market's 95.95% Yes price still looks slightly too aggressive for a single-minute, single-venue settlement with roughly 36-42 hours of crypto downside and wick risk left.
- One-sentence rationale: Bitcoin is likely to finish above $70,000 on the April 16 noon ET Binance minute because current same-venue pricing remains materially above the strike, but the market's 95.95% price is still slightly too confident for a one-minute single-venue settlement with meaningful short-horizon crypto tail risk left.

## Why this is the right action / no-action call

Directional belief remains Yes, but execution discipline still points to watch-only because the remaining edge versus market is modest and fragile.

## Valuation

- Fair value low: 0.92
- Fair value high: 0.95
- Fair value midpoint: 0.935
- Market reference price: 0.9595
- Edge vs market (percentage points): -2.4
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current Binance BTC/USDT trading materially above $70k supports a high-probability Yes view, but exact-minute settlement mechanics and plausible 1-2 day crypto downside tail keep fair value below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh venue and path-risk check.
- `scaled_enter`
  - `min_p:` 0.86
  - `max_p:` 0.92
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current packet sees only a modest below-market valuation gap.
- `hold`
  - `min_p:` 0.92
  - `max_p:` 0.95
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with bounded fair value for a high-probability Yes outcome.
- `trim`
  - `min_p:` 0.95
  - `max_p:` 0.985
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above fair value and exact-minute risk dominates.
- `exit`
  - `min_p:` 0.985
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit or avoid at extreme prices because remaining uncertainty is almost entirely timing, wick, and venue-specific.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T18:00:57.156794+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market is already above bounded fair value., Refresh if BTC weakens toward 72k or below, or if a macro or crypto-specific shock emerges before settlement., Treat this as an exact-minute Binance-close contract rather than a generic next-day BTC direction view.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below 72k on Binance before the April 16 noon ET minute.
- A macro or crypto-specific shock materially raises short-horizon downside risk before settlement.
- Evidence emerges of a Binance-specific print, timestamp, or operational anomaly affecting the governing minute.

### Market structure breakers
- The current quote becomes stale relative to a materially changed Binance state.
- The ET-labeled settlement minute fails to map cleanly to the operative Binance candle surface.

### Time breakers
- The exact April 16 12:00 ET Binance candle should supersede this packet once observed.
- Confidence should be reduced if the cushion compresses meaningfully during the final pre-settlement window.

### Reversal conditions
- Move modestly higher only on a fresh packet if BTC remains firmly above roughly 73k into final hours while price remains favorable.
- Move materially lower on a fresh packet if BTC drifts toward the threshold or Binance-specific anomalies appear.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true 36-42 hour downside tail for BTC into the exact fixing minute.
- Whether any Binance-specific wick or microstructure event matters at settlement.
- How much of the remaining minute-specific fragility the market is already pricing.

### Reasons to pass / stay small
- The market already prices a very high Yes probability and leaves limited room for error.
- The residual disagreement versus market is small and depends mostly on settlement fragility rather than a strong factual misread.

### What would change my mind
- A fresh same-venue check closer to settlement showing BTC still comfortably above 73k-74k would move me slightly toward the market.
- A drop toward 72k or below would reduce fair value materially.
- Evidence of Binance-specific operational or settlement-surface anomalies would lower confidence despite current spot being well above strike.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: Directional belief remains Yes, but execution discipline still points to watch-only because the remaining edge versus market is modest and fragile.

## Notes for downstream evaluator

BTC is still very likely to finish above $70,000 on the April 16 noon ET Binance minute because same-venue spot remains around 74.7k with recent lows above 72k, but the market's 95.95% Yes price still looks slightly too aggressive for a single-minute, single-venue settlement with roughly 36-42 hours of crypto downside and wick risk left.
