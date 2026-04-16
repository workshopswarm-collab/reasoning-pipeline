---
type: decision_packet
case_key: case-20260415-6c8d8ca4
dispatch_id: refresh-case-20260415-6c8d8ca4-20260415T125510Z
question: "Will the price of Bitcoin be above $72,000 on April 17?"
market_id: 34b19a2f-03db-4e0f-ba94-a0ddb3b0670c
external_market_id: 0x278e937ecb8ff1da49c4e04aba52d1922b3e0a7a15d09e621bbf33154c230287
market_slug: bitcoin-above-72k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-6c8d8ca4/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-6c8d8ca4/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260415-6c8d8ca4/decision-maker/refreshes/refresh-case-20260415-6c8d8ca4-20260415T125510Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.76
fair_value_high: 0.82
fair_value_mid: 0.79
market_reference_price: 0.84
edge_mid_vs_market_pct_points: -5.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T12:56:15.196283+00:00
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
- Primary crux: The move from a prior fair-value center near 0.79 to a market price of 0.84 is best treated as repricing rather than a broken thesis: BTC is still more likely than not to close above $72,000 on the April 17 noon ET Binance minute, but the market is now above bounded fair value for a single-minute settlement with still-meaningful 2-3% downside-path risk.
- One-sentence rationale: BTC is still more likely than not to finish above $72,000 on the April 17 Binance noon minute, but the market's move to 0.84 pushes price above bounded fair value centered near 0.79, so the disciplined output remains watch-only because exact-minute downside-path risk still consumes the edge.

## Why this is the right action / no-action call

This refresh is mostly a valuation update: same directional Yes, weaker execution case after repricing.

## Valuation

- Fair value low: 0.76
- Fair value high: 0.82
- Fair value midpoint: 0.79
- Market reference price: 0.84
- Edge vs market (percentage points): -5.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Fresh same-venue spot verification preserved the Yes case and reduced room for a large bearish fade, but did not justify lifting fair value enough to match the repriced market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.7
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price and still a fresh Binance check near settlement.
- `scaled_enter`
  - `min_p:` 0.7
  - `max_p:` 0.76
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if same-venue state remains strong and exact-minute risk is not worsening.
- `hold`
  - `min_p:` 0.76
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.82
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a one-minute settlement contract with meaningful path dependence.
- `exit`
  - `min_p:` 0.9
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at rich prices because exact-minute downside tail dominates residual uncertainty.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T12:56:15.196283+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the updated market price., Treat exact-minute Binance settlement risk as the dominant execution constraint., Reopen only if price cheapens materially or a fresher near-settlement Binance check materially improves confidence in the cushion.

## Invalidation

### Thesis breakers
- BTC falls materially back toward 72k-73k on Binance before the Apr 17 fixing window.
- A fresh downside catalyst or volatility shock materially raises the odds of a sub-72k settlement minute.
- Binance begins underperforming broader spot materially ahead of settlement.

### Market structure breakers
- Market price moves materially again without corresponding same-venue spot support, changing the value comparison.
- Binance operational or microstructure issues emerge near settlement.

### Time breakers
- A fresh direct Binance observation closer to Apr 17 12:00 ET should supersede this packet before any action.
- The actual Apr 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if a fresh pre-fix Binance check shows a meaningfully larger cushion.
- Downgrade if BTC loses cushion or if downside volatility or catalyst risk increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a 2-3% downside move landing exactly at the settlement minute.
- Whether the market already embeds fresher venue-specific information than the bounded package contains.
- How realized volatility will evolve in the final pre-settlement window.

### Reasons to pass / stay small
- The current market price is above bounded fair value.
- This is a one-minute single-venue settlement contract where path risk matters more than broad BTC direction.
- Any edge is too small and fragile to justify authorization.

### What would change my mind
- A fresh Binance check near settlement showing sustained trade well above 74k would move me somewhat closer to market.
- A move toward 72k-73k or evidence of elevated downside catalyst risk would lower fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is mostly a valuation update: same directional Yes, weaker execution case after repricing.

## Notes for downstream evaluator

The move from a prior fair-value center near 0.79 to a market price of 0.84 is best treated as repricing rather than a broken thesis: BTC is still more likely than not to close above $72,000 on the April 17 noon ET Binance minute, but the market is now above bounded fair value for a single-minute settlement with still-meaningful 2-3% downside-path risk.
