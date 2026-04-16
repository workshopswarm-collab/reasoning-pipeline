---
type: decision_packet
case_key: case-20260415-6580bcd8
dispatch_id: refresh-case-20260415-6580bcd8-20260415T083347Z
question: "Will the price of Bitcoin be above $72,000 on April 17?"
market_id: 34b19a2f-03db-4e0f-ba94-a0ddb3b0670c
external_market_id: 0x278e937ecb8ff1da49c4e04aba52d1922b3e0a7a15d09e621bbf33154c230287
market_slug: bitcoin-above-72k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-6580bcd8/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-6580bcd8/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260415-6580bcd8/decision-maker/refreshes/refresh-case-20260415-6580bcd8-20260415T083347Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.72
fair_value_high: 0.76
fair_value_mid: 0.74
market_reference_price: 0.79
edge_mid_vs_market_pct_points: -5.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T08:34:43.645775+00:00
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
- Primary crux: The move from 0.77 to 0.79 is best treated as repricing rather than a broken thesis: BTC is still more likely than not to close above $72,000 on the April 17 noon ET Binance minute, but the market is now further above bounded fair value and the exact-minute settlement discount remains the decisive issue.
- One-sentence rationale: BTC is still more likely than not to finish above $72,000 on the April 17 Binance noon minute, but the market's move up to 0.79 only makes the previous below-market valuation view worse, so the disciplined output remains watch-only with fair value anchored near 0.74 rather than chasing a richer price.

## Why this is the right action / no-action call

This refresh is a pure valuation update: same directional Yes, weaker execution case.

## Valuation

- Fair value low: 0.72
- Fair value high: 0.76
- Fair value midpoint: 0.74
- Market reference price: 0.79
- Edge vs market (percentage points): -5.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Prior synthesis was already compressed toward market because current same-venue state was supportive; the refresh adds price movement but no new evidence to justify lifting fair value.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.66
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price and still a fresh Binance check near settlement.
- `scaled_enter`
  - `min_p:` 0.66
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if same-venue cushion remains intact and pre-fix state still looks stable.
- `hold`
  - `min_p:` 0.72
  - `max_p:` 0.76
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.76
  - `max_p:` 0.84
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a single-minute settlement contract with material path dependence.
- `exit`
  - `min_p:` 0.84
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at rich prices because narrow-resolution downside tail dominates residual certainty.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T08:34:43.645775+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the updated market price., Treat exact-minute Binance settlement risk as the dominant execution constraint even when spot remains above strike., Reopen only if price cheapens materially or a fresher same-venue check near settlement materially improves the cushion.

## Invalidation

### Thesis breakers
- BTC falls back toward or below 72k on Binance before the Apr 17 fixing window.
- A concrete macro or crypto downside catalyst materially raises the probability of a sub-72k settlement minute.
- Binance-specific operational or candle-mapping issues emerge near settlement.

### Market structure breakers
- Market price moves materially again without corresponding same-venue spot support, changing the value comparison.
- Binance microstructure or liquidity behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 17 12:00 ET should supersede this packet before any action.
- The actual Apr 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if a fresh pre-fix Binance check shows a meaningfully larger cushion.
- Downgrade if BTC loses cushion or if downside volatility or catalyst risk increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a 2-3% downdraft landing exactly at the settlement minute.
- Whether the market already embeds fresher venue-specific information than the bounded package contains.
- How much residual operational ambiguity around the Binance noon bar matters in practice.

### Reasons to pass / stay small
- The updated market price is now above bounded fair value.
- This remains a one-minute single-venue settlement contract where ordinary BTC volatility matters disproportionately.
- The refresh added price movement, not new evidence supporting a higher probability.

### What would change my mind
- A fresh Binance check near settlement showing sustained trade well above 74k would move me somewhat closer to market.
- A move back toward 72k or evidence of elevated downside catalyst risk would lower fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is a pure valuation update: same directional Yes, weaker execution case.

## Notes for downstream evaluator

The move from 0.77 to 0.79 is best treated as repricing rather than a broken thesis: BTC is still more likely than not to close above $72,000 on the April 17 noon ET Binance minute, but the market is now further above bounded fair value and the exact-minute settlement discount remains the decisive issue.
