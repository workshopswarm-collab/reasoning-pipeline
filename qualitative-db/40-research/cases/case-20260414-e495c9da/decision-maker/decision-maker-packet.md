---
type: decision_packet
case_key: case-20260414-e495c9da
dispatch_id: dispatch-case-20260414-e495c9da-20260414T191806Z
question: "Will the price of Bitcoin be above $70,000 on April 19?"
market_id: 00b2316a-1303-48a8-bfec-d7743c2a4264
external_market_id: 0x181bd38eac20ef70a12daab11f081f999991b044ad46c3d4ee468d97aee461a5
market_slug: bitcoin-above-70k-on-april-19
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-e495c9da/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-e495c9da/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.83
fair_value_high: 0.87
fair_value_mid: 0.85
market_reference_price: 0.895
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-15T19:28:36.355299+00:00
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
- Primary crux: BTC is more likely than not to be above $70,000 on the April 19 noon ET Binance minute because same-venue spot remains around 74k with recent 24h lows still above 72k, but the market's 89.5% price still looks somewhat too confident for a single exact-minute, single-venue weekend settlement.
- One-sentence rationale: Bitcoin is likely to finish above $70,000 on the April 19 noon ET Binance minute because current same-venue pricing remains materially above the strike, but the market's 89.5% price is still somewhat too confident for a one-minute single-venue weekend settlement with several days of downside path risk left.

## Why this is the right action / no-action call

This remains a Yes-leaning but non-executable case; the bounded evidence supports direction but not enough edge to authorize action.

## Valuation

- Fair value low: 0.83
- Fair value high: 0.87
- Fair value midpoint: 0.85
- Market reference price: 0.895
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current Binance BTC/USDT trading materially above $70k supports a strong Yes lean, but exact-minute weekend settlement mechanics and unresolved short-horizon downside-tail risk keep fair value below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.75
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh venue and path-risk check.
- `scaled_enter`
  - `min_p:` 0.75
  - `max_p:` 0.83
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current packet sees only a modest below-market valuation gap.
- `hold`
  - `min_p:` 0.83
  - `max_p:` 0.87
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with bounded fair value for a favored Yes outcome.
- `trim`
  - `min_p:` 0.87
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above fair value and exact-minute weekend risk dominates.
- `exit`
  - `min_p:` 0.94
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit or avoid at very high prices because remaining uncertainty is almost entirely timing, path, and venue-specific.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T19:28:36.355299+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market is already above bounded fair value., Refresh if BTC weakens toward 72k-70k, or if a weekend macro or crypto-specific shock emerges before settlement., Treat this as a weekend exact-minute Binance-close contract rather than a generic BTC bullishness view.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below 70k on Binance before the April 19 noon ET minute.
- A weekend macro or crypto-specific shock materially raises downside risk before settlement.
- Evidence emerges of a Binance-specific print, timestamp, or operational anomaly affecting the governing minute.

### Market structure breakers
- The current quote becomes stale relative to a materially changed Binance state.
- The operative Binance settlement surface differs meaningfully from the assumed API-aligned verification path.

### Time breakers
- The exact April 19 12:00 ET Binance candle should supersede this packet once observed.
- Confidence should be reduced if the cushion compresses materially during the final pre-settlement weekend window.

### Reversal conditions
- Move modestly higher only on a fresh packet if BTC remains firmly above 72k-74k into settlement while price remains favorable.
- Move materially lower on a fresh packet if BTC drifts toward the threshold or weekend downside catalysts intensify.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true weekend downside distribution for BTC into the exact fixing minute.
- Whether any Binance-specific wick or microstructure event matters at settlement.
- How much of the remaining weekend path fragility the market is already correctly pricing.

### Reasons to pass / stay small
- The market already prices a high Yes probability and leaves limited room for error.
- The residual disagreement versus market is modest and highly sensitive to late BTC volatility rather than a strong factual misread.

### What would change my mind
- A fresh same-venue check closer to settlement showing BTC still comfortably above 72k-74k would move me somewhat toward the market.
- A drop toward 70k-72k or below would reduce fair value materially.
- Evidence of Binance-specific operational or settlement-surface anomalies would lower confidence despite current spot being above strike.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This remains a Yes-leaning but non-executable case; the bounded evidence supports direction but not enough edge to authorize action.

## Notes for downstream evaluator

BTC is more likely than not to be above $70,000 on the April 19 noon ET Binance minute because same-venue spot remains around 74k with recent 24h lows still above 72k, but the market's 89.5% price still looks somewhat too confident for a single exact-minute, single-venue weekend settlement.
