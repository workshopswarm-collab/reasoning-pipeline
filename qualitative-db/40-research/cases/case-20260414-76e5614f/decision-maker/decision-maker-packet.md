---
type: decision_packet
case_key: case-20260414-76e5614f
dispatch_id: dispatch-case-20260414-76e5614f-20260414T182607Z
question: "Will the price of Bitcoin be above $72,000 on April 17?"
market_id: 34b19a2f-03db-4e0f-ba94-a0ddb3b0670c
external_market_id: 0x278e937ecb8ff1da49c4e04aba52d1922b3e0a7a15d09e621bbf33154c230287
market_slug: bitcoin-above-72k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-76e5614f/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-76e5614f/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.75
fair_value_high: 0.8
fair_value_mid: 0.775
market_reference_price: 0.83
edge_mid_vs_market_pct_points: -5.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-15T18:41:55.677845+00:00
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
- Primary crux: BTC is more likely than not to settle above $72,000 on the April 17 noon ET Binance minute because same-venue spot remains above strike, but with only a roughly 3-4% cushion and an exact-minute single-venue close rule, ordinary short-horizon volatility still makes the market's 0.83 price somewhat rich.
- One-sentence rationale: Bitcoin is likely to finish above $72,000 on the April 17 noon ET Binance minute because current same-venue pricing remains above the strike, but the market's 0.83 price is still somewhat too confident for a one-minute single-venue settlement with only a modest buffer and real short-horizon downside path risk left.

## Why this is the right action / no-action call

This remains a Yes-leaning but non-executable case; directional belief and trade authorization stay separated because the edge is modest and fragile.

## Valuation

- Fair value low: 0.75
- Fair value high: 0.8
- Fair value midpoint: 0.775
- Market reference price: 0.83
- Edge vs market (percentage points): -5.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current Binance BTC/USDT pricing above $72k supports a Yes lean, but exact-minute settlement mechanics, only medium-strength verification, and plausible 1-3 day downside path risk keep fair value below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.67
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh venue and path-risk check.
- `scaled_enter`
  - `min_p:` 0.67
  - `max_p:` 0.75
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current packet sees only a moderate and fragile below-market valuation gap.
- `hold`
  - `min_p:` 0.75
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with bounded fair value for a favored Yes outcome.
- `trim`
  - `min_p:` 0.8
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above fair value and exact-minute risk dominates.
- `exit`
  - `min_p:` 0.9
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit or avoid at very high prices because remaining uncertainty is almost entirely timing, path, and venue-specific.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T18:41:55.677845+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market remains above bounded fair value., Refresh if BTC weakens toward 73k or 72k, or if macro or crypto-specific downside catalysts emerge before settlement., Treat this as an exact-minute Binance-close contract rather than a generic BTC bullishness view.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below 72k on Binance before the April 17 noon ET minute.
- A macro or crypto-specific shock materially raises short-horizon downside risk before settlement.
- Evidence emerges of a Binance-specific print, timestamp, or operational anomaly affecting the governing minute.

### Market structure breakers
- The current quote becomes stale relative to a materially changed Binance state.
- The operative Binance settlement surface differs meaningfully from the API-based verification path.

### Time breakers
- The exact April 17 12:00 ET Binance candle should supersede this packet once observed.
- Confidence should be reduced if the cushion compresses materially during the final pre-settlement window.

### Reversal conditions
- Move modestly higher only on a fresh packet if BTC remains firmly above mid-74k into settlement while price remains favorable.
- Move materially lower on a fresh packet if BTC drifts toward the threshold or downside catalysts intensify.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true short-horizon downside distribution for BTC into the exact fixing minute.
- Whether any Binance-specific wick or microstructure event matters at settlement.
- How much of the remaining path fragility the market is already correctly pricing.

### Reasons to pass / stay small
- The market already prices a high Yes probability and leaves limited room for error.
- The residual disagreement versus market is moderate but still driven mostly by settlement fragility rather than a strong factual misread.

### What would change my mind
- A fresh same-venue check closer to settlement showing BTC still comfortably above mid-74k would move me somewhat toward the market.
- A drop toward 72k-73k or below would reduce fair value materially.
- Evidence of Binance-specific operational or settlement-surface anomalies would lower confidence despite current spot being above strike.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This remains a Yes-leaning but non-executable case; directional belief and trade authorization stay separated because the edge is modest and fragile.

## Notes for downstream evaluator

BTC is more likely than not to settle above $72,000 on the April 17 noon ET Binance minute because same-venue spot remains above strike, but with only a roughly 3-4% cushion and an exact-minute single-venue close rule, ordinary short-horizon volatility still makes the market's 0.83 price somewhat rich.
