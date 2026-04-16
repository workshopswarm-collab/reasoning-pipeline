---
type: decision_packet
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416-2ab48f50-20260416T002737Z
question: "Will the price of Bitcoin be above $74,000 on April 17?"
market_id: 367ed8d7-c08e-4588-a449-c83aead47ec3
external_market_id: 0x0457acf7468ed957f2422686cf5e63fb54d69fb116b67f74f6b64fd8e8b377dc
market_slug: bitcoin-above-74k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $74,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260416-2ab48f50/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-2ab48f50/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.57
fair_value_high: 0.63
fair_value_mid: 0.6
market_reference_price: 0.62
edge_mid_vs_market_pct_points: -2.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-17T00:38:49.185562+00:00
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
- Trade authorization: `forbidden`
- Position policy: `flat`
- Decision readiness: `needs_more_research`
- Primary crux: Bitcoin is still slightly more likely than not to close above $74,000 on the April 17 noon ET Binance minute because spot remains above strike, but with the market already at 0.62 and the cushion under 1%, the remaining edge is too small and too dependent on exact-minute path behavior to support action without fresher pre-settlement validation.
- One-sentence rationale: BTC is still slightly more likely than not to finish above $74,000 on the April 17 Binance noon minute, but with fair value centered near 0.60, the market already near that level, and exact-minute path risk dominating because the spot cushion is under 1%, the correct packet is forbidden and needs_more_research rather than watch-only.

## Why this is the right action / no-action call

This case separates directional lean from actionability: plausible Yes thesis, but too close to the threshold and too freshness-sensitive for execution at current pricing.

## Valuation

- Fair value low: 0.57
- Fair value high: 0.63
- Fair value midpoint: 0.6
- Market reference price: 0.62
- Edge vs market (percentage points): -2.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current Binance spot above strike supports a slight Yes lean, but bounded verification did not independently rule out late-session catalyst risk or exact-minute path fragility strongly enough to justify action around a near-market price.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.48
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a far cheaper price and fresher pre-settlement confirmation.
- `scaled_enter`
  - `min_p:` 0.48
  - `max_p:` 0.57
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if BTC remains above 74k with improved freshness and calmer volatility.
- `hold`
  - `min_p:` 0.57
  - `max_p:` 0.63
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone from current reasoning, but current packet remains non-actionable due readiness limits.
- `trim`
  - `min_p:` 0.63
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a near-threshold one-minute crypto settlement.
- `exit`
  - `min_p:` 0.72
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid entirely at rich prices while exact-minute path risk dominates.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-17T00:38:49.185562+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add exposure at the current price., Require a fresh pre-settlement spot and volatility check before reconsidering action., Treat exact-minute Binance settlement risk as binding when the spot cushion is under 1%.

## Invalidation

### Thesis breakers
- BTC loses the 74k level on Binance and fails to reclaim it before the Apr 17 fixing window.
- A downside macro, crypto, or exchange-specific shock materially raises the probability of a sub-74k settlement minute.
- Binance-specific pricing, liquidity, or operational issues emerge near resolution.

### Market structure breakers
- Market reprices materially after fresh spot or volatility changes, altering the value comparison.
- Binance settlement-surface or ET-to-UTC minute mapping behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation and volatility check closer to Apr 17 12:00 ET should supersede this packet.
- The actual Apr 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade from forbidden only if fresher pre-settlement evidence materially improves confidence or the market cheapens enough to create a clearer edge.
- Downgrade directional confidence if BTC loses the strike area or volatility rises materially.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the tiny above-74k cushion survives the exact settlement minute.
- Whether U.S.-morning macro or crypto-specific shocks emerge before the fixing window.
- How much residual discount exact-minute Binance UI-versus-API sensitivity deserves when the strike is nearly at spot.

### Reasons to pass / stay small
- The current market is already near bounded fair value.
- The bounded package itself flags blockers_require_new_research as yes.
- The outcome is too path-dependent for the small apparent edge to survive ordinary uncertainty.

### What would change my mind
- A fresh near-settlement Binance check still showing BTC comfortably above 74k with calmer volatility would improve readiness.
- A materially cheaper market price with unchanged cushion would improve the execution case.
- A move back below 74k would reduce directional confidence materially.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This case separates directional lean from actionability: plausible Yes thesis, but too close to the threshold and too freshness-sensitive for execution at current pricing.

## Notes for downstream evaluator

Bitcoin is still slightly more likely than not to close above $74,000 on the April 17 noon ET Binance minute because spot remains above strike, but with the market already at 0.62 and the cushion under 1%, the remaining edge is too small and too dependent on exact-minute path behavior to support action without fresher pre-settlement validation.
