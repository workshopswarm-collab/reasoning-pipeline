---
type: decision_packet
case_key: case-20260415-f07c9e26
dispatch_id: refresh-case-20260415-f07c9e26-20260415T072338Z
question: "Will the price of Bitcoin be above $72,000 on April 16?"
market_id: 7da0bb87-594f-4bdb-a7ae-fddfc3f0f8bd
external_market_id: 0xee2d4eeeae30d06342d630e97c23ff423da2e542cbfb30a8ce252b9f47ccc9e3
market_slug: bitcoin-above-72k-on-april-16
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 16?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-f07c9e26/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-f07c9e26/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260415-f07c9e26/decision-maker/refreshes/refresh-case-20260415-f07c9e26-20260415T072338Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.86
fair_value_high: 0.89
fair_value_mid: 0.875
market_reference_price: 0.805
edge_mid_vs_market_pct_points: 7.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T07:24:41.392152+00:00
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
- Primary crux: The market move from 0.875 to 0.805 does not invalidate the prior directional crux; BTC is still more likely than not to be above $72,000 on the April 16 noon ET Binance minute because same-venue spot remained materially above strike, but the repricing has materially compressed and likely inverted the prior valuation gap, so the disciplined output remains non-authorized while waiting for fresher price-state confirmation.
- One-sentence rationale: Bitcoin is still more likely than not to finish above $72,000 on the April 16 noon ET Binance minute, but the drop from 0.875 to 0.805 likely compresses or reverses the prior below-market edge, so the disciplined output remains watch-only rather than treating the old thesis as unchanged alpha.

## Why this is the right action / no-action call

This refresh is mainly a valuation update: same directional lean, but prior anti-market skepticism is now much weaker and may no longer be positive EV without fresher spot confirmation.

## Valuation

- Fair value low: 0.86
- Fair value high: 0.89
- Fair value midpoint: 0.875
- Market reference price: 0.805
- Edge vs market (percentage points): 7.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: The refresh is a price move without a new bounded evidence bundle showing regime failure; prior synthesis still supports a high-probability Yes view, but the market has moved far enough toward that view that any previous below-market edge has been largely or fully erased.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.78
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh venue and path-risk check.
- `scaled_enter`
  - `min_p:` 0.78
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the prior edge has likely compressed away under the new market price.
- `hold`
  - `min_p:` 0.86
  - `max_p:` 0.89
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with bounded fair value for a high-probability Yes outcome.
- `trim`
  - `min_p:` 0.89
  - `max_p:` 0.96
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing if price returns above bounded fair value and exact-minute risk again dominates.
- `exit`
  - `min_p:` 0.96
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit or avoid at extreme prices because remaining uncertainty is almost entirely timing, path, and venue-specific.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T07:24:41.392152+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the repricing has likely erased the prior valuation edge., Refresh on a fresh same-venue BTC check before settlement if action is reconsidered., Treat this as an exact-minute Binance-close contract rather than a broad BTC directional view.

## Invalidation

### Thesis breakers
- BTC falls materially toward or below 72k on Binance before the April 16 noon ET minute.
- A macro, crypto-specific, or Binance-specific shock materially raises downside risk before settlement.
- Evidence emerges of a Binance-specific print, timestamp, or operational anomaly affecting the governing minute.

### Market structure breakers
- The current quote is stale relative to a materially changed Binance state.
- The operative Binance settlement surface differs meaningfully from the assumed one-minute close representation.

### Time breakers
- A fresh pre-settlement BTC check should supersede this packet before any action.
- The exact April 16 12:00 ET Binance candle should replace all prior reasoning once observed.

### Reversal conditions
- Move back toward below-market skepticism only on a fresh packet if the market re-expands without matching deterioration in spot state.
- Move materially lower on a fresh packet if BTC drifts toward the threshold or downside catalysts intensify.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the large market repricing reflects genuine spot deterioration not captured in the bounded refresh.
- The true short-horizon downside distribution for BTC into the exact fixing minute.
- Whether any Binance-specific wick or microstructure event matters at settlement.

### Reasons to pass / stay small
- The repricing has likely erased or inverted the prior valuation edge.
- This is still a one-minute single-venue crypto settlement with meaningful path risk.
- The bounded refresh does not provide enough fresh state evidence to upgrade from watch-only.

### What would change my mind
- A fresh same-venue check confirming BTC still comfortably above 74k into the final window would make the new lower market price look more attractive.
- A drop toward 72k-73k or below would validate the repricing and reduce fair value materially.
- Evidence of Binance-specific operational or settlement-surface anomalies would lower confidence even if spot remains above strike.

### Decision quality
- `fragile`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is mainly a valuation update: same directional lean, but prior anti-market skepticism is now much weaker and may no longer be positive EV without fresher spot confirmation.

## Notes for downstream evaluator

The market move from 0.875 to 0.805 does not invalidate the prior directional crux; BTC is still more likely than not to be above $72,000 on the April 16 noon ET Binance minute because same-venue spot remained materially above strike, but the repricing has materially compressed and likely inverted the prior valuation gap, so the disciplined output remains non-authorized while waiting for fresher price-state confirmation.
