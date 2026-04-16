---
type: decision_packet
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
question: "Will the price of Bitcoin be above $72,000 on April 19?"
market_id: b8af2a6b-b2cc-4f28-9c10-9cc5807007e1
external_market_id: 0x96dd7e4c2eb7fda6bc3b2a593ac07eb1b1cc99c51ea086bd923208ee49cd1f98
market_slug: bitcoin-above-72k-on-april-19
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-7d14e3a4/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-7d14e3a4/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.77
fair_value_high: 0.82
fair_value_mid: 0.795
market_reference_price: 0.865
edge_mid_vs_market_pct_points: -7.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T23:23:51.325833+00:00
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
- Primary crux: Bitcoin is still more likely than not to close above $72,000 on the April 19 noon ET Binance minute because spot remains materially above strike, but the market at 0.865 is too rich relative to the bounded evidence and the remaining short-horizon downside distribution has not been independently verified strongly enough to support action on a single-minute settlement.
- One-sentence rationale: BTC is still more likely than not to finish above $72,000 on the April 19 Binance noon minute, but the market's 0.865 price leaves no sufficiently verified execution edge and the remaining exact-minute downside tail is too weakly modeled for action, so the correct packet is forbidden and needs_more_research rather than watch-only.

## Why this is the right action / no-action call

This case separates directional belief from execution readiness: plausible Yes thesis, but insufficiently verified basis for trading at a rich price.

## Valuation

- Fair value low: 0.77
- Fair value high: 0.82
- Fair value midpoint: 0.795
- Market reference price: 0.865
- Edge vs market (percentage points): -7.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current Binance spot above strike and recent regime context support a solid Yes baseline, but bounded evidence does not independently justify high-80s confidence for a one-minute settlement with several days of remaining volatility.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.7
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a far cheaper price and materially better downside-tail verification.
- `scaled_enter`
  - `min_p:` 0.7
  - `max_p:` 0.77
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only with stronger independent support and improved freshness.
- `hold`
  - `min_p:` 0.77
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone from current reasoning, but current packet remains non-actionable due readiness limits.
- `trim`
  - `min_p:` 0.82
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a multi-day exact-minute crypto threshold contract.
- `exit`
  - `min_p:` 0.9
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid entirely at near-certainty-like pricing while downside-tail verification remains insufficient.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T23:23:51.325833+00:00
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
- BTC loses substantial cushion and trades back toward 72k-73k on Binance before the Apr 19 fixing window.
- A downside macro, crypto, regulatory, or exchange-specific shock materially raises the probability of a sub-72k settlement minute.
- Binance-specific pricing, liquidity, or operational issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding new independent evidence, further worsening actionability.
- Binance settlement-surface or minute-mapping behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation and volatility check closer to Apr 19 12:00 ET should supersede this packet.
- The actual Apr 19 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade from forbidden only if fresher pre-settlement evidence materially improves downside-tail calibration or the market cheapens substantially.
- Downgrade directional confidence if BTC loses cushion or volatility rises materially.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a 3-4% downside move or wick landing on the exact settlement minute over the next several days.
- Whether weekend, macro, or crypto-specific news materially changes short-horizon volatility before settlement.
- How much residual discount exact-minute Binance UI-versus-API sensitivity deserves at current prices.

### Reasons to pass / stay small
- The current market price is well above bounded fair value.
- The bounded package itself flags blockers_require_new_research as yes.
- The remaining edge is not independently verified strongly enough to support action at an 86.5% price.

### What would change my mind
- A fresh near-settlement Binance and volatility check still showing a large cushion with calmer downside conditions would improve readiness.
- A materially cheaper market price with unchanged cushion would improve the execution case.
- A move back toward 72k-73k would reduce directional confidence materially.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This case separates directional belief from execution readiness: plausible Yes thesis, but insufficiently verified basis for trading at a rich price.

## Notes for downstream evaluator

Bitcoin is still more likely than not to close above $72,000 on the April 19 noon ET Binance minute because spot remains materially above strike, but the market at 0.865 is too rich relative to the bounded evidence and the remaining short-horizon downside distribution has not been independently verified strongly enough to support action on a single-minute settlement.
