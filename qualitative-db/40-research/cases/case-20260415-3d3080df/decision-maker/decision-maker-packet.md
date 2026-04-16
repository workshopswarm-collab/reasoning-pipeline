---
type: decision_packet
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
question: "Will the price of Bitcoin be above $70,000 on April 20?"
market_id: 551a0230-0ffb-42cc-9103-4bea5dc0cb4e
external_market_id: 0x73f9d7c48acbeefbe93bdcdc747947e2e8573945f11720617290fe672bf997d2
market_slug: bitcoin-above-70k-on-april-20
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 20?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-3d3080df/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-3d3080df/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.81
fair_value_high: 0.85
fair_value_mid: 0.83
market_reference_price: 0.875
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T00:32:37.195346+00:00
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
- Primary crux: BTC above $70,000 on the April 20 noon ET Binance minute remains the base case because same-venue spot stayed around 74.5k and other venues corroborated the same regime, but the market's 87.5% price still looks somewhat too confident for a narrow single-minute, single-exchange settlement several days out.
- One-sentence rationale: Bitcoin is likely to finish above $70,000 on the April 20 noon ET Binance minute because current same-venue pricing remains materially above the strike and other venues corroborate the same regime, but the market's 87.5% price is still somewhat too confident for a one-minute single-venue settlement with meaningful multi-day downside path risk left.

## Why this is the right action / no-action call

This remains a Yes-leaning but non-executable case; the bounded evidence supports direction but not enough edge to justify fresh action.

## Valuation

- Fair value low: 0.81
- Fair value high: 0.85
- Fair value midpoint: 0.83
- Market reference price: 0.875
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current Binance BTC/USDT pricing materially above $70k and cross-venue corroboration support a strong Yes lean, but exact-minute settlement mechanics and only moderate verification of the correct path-risk discount keep fair value below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.75
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh venue and path-risk check.
- `scaled_enter`
  - `min_p:` 0.75
  - `max_p:` 0.81
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current packet sees only a modest below-market valuation gap.
- `hold`
  - `min_p:` 0.81
  - `max_p:` 0.85
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with bounded fair value for a favored Yes outcome.
- `trim`
  - `min_p:` 0.85
  - `max_p:` 0.93
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above fair value and exact-minute risk dominates.
- `exit`
  - `min_p:` 0.93
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit or avoid at extreme prices because remaining uncertainty is almost entirely timing, path, and venue-specific.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T00:32:37.195346+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market is already above bounded fair value., Refresh if BTC weakens toward 72k-70k across venues, or if unscheduled macro, geopolitical, or crypto-specific downside catalysts emerge before settlement., Treat this as an exact-minute Binance-close contract rather than a generic BTC trend view.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below 72k-70k before the April 20 noon ET minute.
- An unscheduled macro, geopolitical, or crypto-specific shock materially raises downside risk before settlement.
- Evidence emerges of a Binance-specific print, timestamp, or operational anomaly affecting the governing minute.

### Market structure breakers
- The current quote becomes stale relative to a materially changed Binance state.
- The operative Binance settlement surface differs meaningfully from the assumed one-minute close representation.

### Time breakers
- The exact April 20 12:00 ET Binance candle should supersede this packet once observed.
- Confidence should be reduced if the cushion compresses materially during the final 24-48 hours before settlement.

### Reversal conditions
- Move modestly higher only on a fresh packet if BTC remains firmly above 73k-74k into settlement while price remains favorable.
- Move materially lower on a fresh packet if BTC drifts toward the threshold or downside catalysts intensify.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true five-day downside distribution for BTC into the exact fixing minute.
- Whether any Binance-specific wick or microstructure event matters at settlement.
- How much of the remaining path fragility the market is already correctly pricing.

### Reasons to pass / stay small
- The market already prices a high Yes probability and leaves limited room for error.
- The residual disagreement versus market is modest and only moderately independently verified as a tradable edge.

### What would change my mind
- A fresh same-venue check closer to settlement showing BTC still comfortably above 73k-74k would move me somewhat toward the market.
- A drop toward 70k-72k or below would reduce fair value materially.
- Evidence of Binance-specific operational or settlement-surface anomalies would lower confidence despite current spot being above strike.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This remains a Yes-leaning but non-executable case; the bounded evidence supports direction but not enough edge to justify fresh action.

## Notes for downstream evaluator

BTC above $70,000 on the April 20 noon ET Binance minute remains the base case because same-venue spot stayed around 74.5k and other venues corroborated the same regime, but the market's 87.5% price still looks somewhat too confident for a narrow single-minute, single-exchange settlement several days out.
