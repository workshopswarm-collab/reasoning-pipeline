---
type: decision_packet
case_key: case-20260414-e15c72fe
dispatch_id: refresh-case-20260414-e15c72fe-20260414T201353Z
question: "Will the price of Bitcoin be above $70,000 on April 20?"
market_id: 551a0230-0ffb-42cc-9103-4bea5dc0cb4e
external_market_id: 0x73f9d7c48acbeefbe93bdcdc747947e2e8573945f11720617290fe672bf997d2
market_slug: bitcoin-above-70k-on-april-20
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 20?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-e15c72fe/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-e15c72fe/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260414-e15c72fe/decision-maker/refreshes/refresh-case-20260414-e15c72fe-20260414T201353Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.78
fair_value_high: 0.83
fair_value_mid: 0.805
market_reference_price: 0.855
edge_mid_vs_market_pct_points: -5.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-15T20:14:50.237646+00:00
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
- Primary crux: The market move from 0.845 to 0.855 does not invalidate the prior crux; BTC is still more likely than not to settle above $70,000 on the April 20 noon ET Binance minute because same-venue spot remains materially above strike, but the single-minute Binance-only settlement keeps enough downside and operational fragility alive that the new price still looks somewhat rich.
- One-sentence rationale: Bitcoin is still likely to finish above $70,000 on the April 20 noon ET Binance minute because current same-venue pricing remains materially above the strike, but the move from 0.845 to 0.855 mainly compresses the prior edge rather than disproving it, and the market still looks somewhat too confident for a one-minute single-venue settlement with several days of downside path risk left.

## Why this is the right action / no-action call

This refresh is mainly a repricing update: same directional view, smaller edge, same watch-only posture.

## Valuation

- Fair value low: 0.78
- Fair value high: 0.83
- Fair value midpoint: 0.805
- Market reference price: 0.855
- Edge vs market (percentage points): -5.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: The refresh brief shows market repricing without new decisive evidence; current Binance BTC/USDT remaining well above $70k still supports a Yes lean, but exact-minute settlement mechanics and thin downside-tail calibration keep fair value below the updated market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh venue and path-risk check.
- `scaled_enter`
  - `min_p:` 0.72
  - `max_p:` 0.78
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current packet sees only a modest and now further-compressed below-market valuation gap.
- `hold`
  - `min_p:` 0.78
  - `max_p:` 0.83
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with bounded fair value for a favored Yes outcome.
- `trim`
  - `min_p:` 0.83
  - `max_p:` 0.92
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above fair value and exact-minute risk dominates.
- `exit`
  - `min_p:` 0.92
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit or avoid at very high prices because remaining uncertainty is almost entirely timing, path, and venue-specific.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T20:14:50.237646+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market has moved further above bounded fair value., Refresh if BTC weakens toward 71k-70k, or if macro or crypto-specific downside catalysts emerge before settlement., Treat this as an exact-minute Binance-close contract rather than a generic BTC trend view.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below 70k on Binance before the April 20 noon ET minute.
- A macro or crypto-specific shock materially raises downside risk before settlement.
- Evidence emerges of a Binance-specific print, timestamp, or operational anomaly affecting the governing minute.

### Market structure breakers
- The current quote becomes stale relative to a materially changed Binance state.
- The operative Binance settlement surface differs meaningfully from the assumed API-aligned verification path.

### Time breakers
- The exact April 20 12:00 ET Binance candle should supersede this packet once observed.
- Confidence should be reduced if the cushion compresses materially during the final pre-settlement window.

### Reversal conditions
- Move modestly higher only on a fresh packet if BTC remains firmly above 72k-74k into settlement while price remains favorable.
- Move materially lower on a fresh packet if BTC drifts toward the threshold or downside catalysts intensify.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true several-day downside distribution for BTC into the exact fixing minute.
- Whether any Binance-specific wick or microstructure event matters at settlement.
- How much of the remaining path fragility the repriced market is now correctly absorbing.

### Reasons to pass / stay small
- The market repriced upward without new decisive evidence, compressing an already modest valuation gap.
- The residual disagreement versus market remains driven mostly by settlement fragility rather than a strong factual misread.

### What would change my mind
- A fresh same-venue check closer to settlement showing BTC still comfortably above 72k-74k would move me somewhat toward the market.
- A drop toward 70k-71k or below would reduce fair value materially.
- Evidence of Binance-specific operational or settlement-surface anomalies would lower confidence despite current spot being above strike.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is mainly a repricing update: same directional view, smaller edge, same watch-only posture.

## Notes for downstream evaluator

The market move from 0.845 to 0.855 does not invalidate the prior crux; BTC is still more likely than not to settle above $70,000 on the April 20 noon ET Binance minute because same-venue spot remains materially above strike, but the single-minute Binance-only settlement keeps enough downside and operational fragility alive that the new price still looks somewhat rich.
