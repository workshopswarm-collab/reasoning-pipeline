---
type: decision_packet
case_key: case-20260415-c8d6e83e
dispatch_id: refresh-case-20260415-c8d6e83e-20260415T202231Z
question: "Will the price of Bitcoin be above $68,000 on April 20?"
market_id: c4503986-4093-47b0-953e-2a05b34dfdd7
external_market_id: 0xbb5b9915619f3ae3123468fadfd61e01690fdf5c0ee246e628e5af357662e88c
market_slug: bitcoin-above-68k-on-april-20
platform: polymarket
market_title: "Will the price of Bitcoin be above $68,000 on April 20?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-c8d6e83e/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-c8d6e83e/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260415-c8d6e83e/decision-maker/refreshes/refresh-case-20260415-c8d6e83e-20260415T202231Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.9
fair_value_high: 0.94
fair_value_mid: 0.92
market_reference_price: 0.9715
edge_mid_vs_market_pct_points: -5.1
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T20:23:32.524758+00:00
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
- Primary crux: Bitcoin is still highly likely to close above $68,000 on the April 20 noon ET Binance minute because current same-venue spot around 74.0k leaves a large cushion, but the market at 0.9715 is too rich relative to the bounded evidence and the remaining five-day, exact-minute downside tail has not been independently quantified strongly enough to support action.
- One-sentence rationale: BTC is still highly likely to finish above $68,000 on the April 20 Binance noon minute, but the market's move to 0.9715 leaves no credible execution edge and the remaining five-day exact-minute downside tail is too weakly verified for action, so the correct packet is forbidden and needs_more_research rather than watch-only.

## Why this is the right action / no-action call

This case separates directional belief from execution readiness: strong Yes view, but insufficiently verified basis for trading at near-certainty pricing.

## Valuation

- Fair value low: 0.9
- Fair value high: 0.94
- Fair value midpoint: 0.92
- Market reference price: 0.9715
- Edge vs market (percentage points): -5.1
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current Binance spot materially above strike supports a strong Yes baseline, but bounded evidence does not justify confidence near the repriced market because the remaining five-day downside-tail and exact-minute settlement risk have not been freshly or independently tightened.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.85
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a far cheaper price and fresher downside-tail verification.
- `scaled_enter`
  - `min_p:` 0.85
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only with stronger independent support and improved freshness.
- `hold`
  - `min_p:` 0.9
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone from prior reasoning, but current packet remains non-actionable due readiness limits.
- `trim`
  - `min_p:` 0.94
  - `max_p:` 0.98
  - `target_exposure_fraction:` 0.0
  - `notes:` Above bounded fair value for a five-day exact-minute crypto threshold contract.
- `exit`
  - `min_p:` 0.98
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid entirely at near-certainty pricing while downside-tail verification remains insufficient.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T20:23:32.524758+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add exposure at the current price., Require a fresher pre-settlement spot and volatility check before reconsidering action., Treat exact-minute Binance settlement risk as binding at current market levels.

## Invalidation

### Thesis breakers
- BTC loses substantial cushion and trades back toward 70k-68k on Binance before the Apr 20 fixing window.
- A downside macro, crypto, regulatory, or exchange-specific shock materially raises the probability of a sub-68k settlement minute.
- Binance-specific pricing, liquidity, or operational issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding new independent evidence, further worsening actionability.
- Binance settlement-surface or minute-mapping behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation and volatility check closer to Apr 20 12:00 ET should supersede this packet.
- The actual Apr 20 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade from forbidden only if fresher pre-settlement evidence materially improves downside-tail calibration or the market cheapens substantially.
- Downgrade directional confidence if BTC loses cushion or volatility rises materially.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of an 8%+ downside move or wick landing on the exact settlement minute over the next five days.
- Whether weekend or macro/crypto news materially changes short-horizon volatility before settlement.
- How much residual discount exact-minute Binance website-versus-API sensitivity deserves at current prices.

### Reasons to pass / stay small
- The current market price is well above bounded fair value.
- The bounded package itself flags blockers_require_new_research as yes.
- The remaining edge is not independently verified strongly enough to support action at a 97%+ price.

### What would change my mind
- A fresh near-settlement Binance and volatility check still showing a large cushion with calmer downside conditions would improve readiness.
- A materially cheaper market price with unchanged cushion would improve the execution case.
- A move back toward 70k-68k would reduce directional confidence materially.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This case separates directional belief from execution readiness: strong Yes view, but insufficiently verified basis for trading at near-certainty pricing.

## Notes for downstream evaluator

Bitcoin is still highly likely to close above $68,000 on the April 20 noon ET Binance minute because current same-venue spot around 74.0k leaves a large cushion, but the market at 0.9715 is too rich relative to the bounded evidence and the remaining five-day, exact-minute downside tail has not been independently quantified strongly enough to support action.
