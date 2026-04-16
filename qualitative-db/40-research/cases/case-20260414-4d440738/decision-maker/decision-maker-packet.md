---
type: decision_packet
case_key: case-20260414-4d440738
dispatch_id: refresh-case-20260414-4d440738-20260414T201459Z
question: "Will the price of Bitcoin be above $68,000 on April 20?"
market_id: c4503986-4093-47b0-953e-2a05b34dfdd7
external_market_id: 0xbb5b9915619f3ae3123468fadfd61e01690fdf5c0ee246e628e5af357662e88c
market_slug: bitcoin-above-68k-on-april-20
platform: polymarket
market_title: "Will the price of Bitcoin be above $68,000 on April 20?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-4d440738/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-4d440738/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260414-4d440738/decision-maker/refreshes/refresh-case-20260414-4d440738-20260414T201459Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.87
fair_value_high: 0.9
fair_value_mid: 0.885
market_reference_price: 0.935
edge_mid_vs_market_pct_points: -5.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-15T20:15:56.177855+00:00
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
- Primary crux: The market move does not invalidate the prior crux; BTC finishing above $68,000 on the April 20 noon ET Binance minute remains the clear base case because same-venue spot is still about 9% above strike, but a six-day crypto contract settled on one exact exchange-minute close still does not justify near-certainty as strongly as a 93.5% market implies.
- One-sentence rationale: Bitcoin is still likely to finish above $68,000 on the April 20 noon ET Binance minute because current same-venue pricing remains materially above the strike, but the repriced 93.5% market still looks somewhat too confident for a one-minute single-venue settlement with six days of downside path risk left.

## Why this is the right action / no-action call

This refresh is mainly a repricing update: same directional view, smaller edge, same watch-only posture.

## Valuation

- Fair value low: 0.87
- Fair value high: 0.9
- Fair value midpoint: 0.885
- Market reference price: 0.935
- Edge vs market (percentage points): -5.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: The refresh brief indicates a price move without new decisive evidence; current Binance BTC/USDT remaining well above $68k still supports a strong Yes lean, but exact-minute settlement mechanics and lack of a stronger downside-tail model keep fair value below the updated market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh venue and path-risk check.
- `scaled_enter`
  - `min_p:` 0.82
  - `max_p:` 0.87
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current packet sees only a modest and somewhat compressed below-market valuation gap.
- `hold`
  - `min_p:` 0.87
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with bounded fair value for a strong Yes outcome.
- `trim`
  - `min_p:` 0.9
  - `max_p:` 0.97
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above fair value and exact-minute risk dominates.
- `exit`
  - `min_p:` 0.97
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit or avoid at extreme prices because remaining uncertainty is almost entirely timing, path, and venue-specific.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T20:15:56.177855+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market remains above bounded fair value., Refresh if BTC weakens toward the low-70k region or if weekend or Monday-morning downside catalysts emerge before settlement., Treat this as an exact-minute Binance-close contract rather than a generic BTC regime call.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below the low-70k region before the April 20 noon ET minute.
- A weekend or Monday-morning macro or crypto-specific shock materially raises downside risk before settlement.
- Evidence emerges of a Binance-specific print, timestamp, or operational anomaly affecting the governing minute.

### Market structure breakers
- The current quote becomes stale relative to a materially changed Binance state.
- The operative Binance settlement surface differs meaningfully from the assumed minute-close mapping.

### Time breakers
- The exact April 20 12:00 ET Binance candle should supersede this packet once observed.
- Confidence should be reduced if the cushion compresses materially during the final weekend and Monday-morning window.

### Reversal conditions
- Move modestly higher only on a fresh packet if BTC remains firmly above 70k-72k into settlement while price remains favorable.
- Move materially lower on a fresh packet if BTC drifts toward the threshold or downside catalysts intensify.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true six-day downside distribution for BTC into the exact fixing minute.
- Whether any Binance-specific wick or microstructure event matters at settlement.
- How much of the remaining weekend and Monday-morning path fragility the repriced market is now absorbing.

### Reasons to pass / stay small
- The market already prices a very high Yes probability and leaves limited room for error.
- The residual disagreement versus market is moderate but remains mostly a confidence haircut rather than a strong factual misread.

### What would change my mind
- A fresh same-venue check closer to settlement showing BTC still comfortably above low-72k would move me somewhat toward the market.
- A drop back toward 68k-70k would reduce fair value materially.
- Evidence of Binance-specific operational or settlement-surface anomalies would lower confidence despite current spot being well above strike.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is mainly a repricing update: same directional view, smaller edge, same watch-only posture.

## Notes for downstream evaluator

The market move does not invalidate the prior crux; BTC finishing above $68,000 on the April 20 noon ET Binance minute remains the clear base case because same-venue spot is still about 9% above strike, but a six-day crypto contract settled on one exact exchange-minute close still does not justify near-certainty as strongly as a 93.5% market implies.
