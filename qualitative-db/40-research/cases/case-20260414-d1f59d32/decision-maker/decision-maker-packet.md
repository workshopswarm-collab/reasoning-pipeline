---
type: decision_packet
case_key: case-20260414-d1f59d32
dispatch_id: dispatch-case-20260414-d1f59d32-20260414T144613Z
question: "Will the price of Bitcoin be above $74,000 on April 15?"
market_id: case-20260414-d1f59d32
external_market_id: 0xfb00ff35de120017fabe413f445c7260fcbbe3c17b11d69108f953ab573b7c92
market_slug: bitcoin-above-74k-on-april-15
platform: polymarket
market_title: "Will the price of Bitcoin be above $74,000 on April 15?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-d1f59d32/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-d1f59d32/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: needs_more_research
fair_value_low: 0.74
fair_value_high: 0.8
fair_value_mid: 0.77
market_reference_price: 0.815
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: low
valid_until: 2026-04-15T11:00:00-04:00
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
- Decision readiness: `needs_more_research`
- Primary crux: BTC is more likely than not to finish above $74,000 on the April 15 noon ET Binance minute because same-venue price was still materially above the strike, but the market's 81.5% price is somewhat rich for a one-minute settlement contract with a plausible sub-24-hour 1.8% downside path.
- One-sentence rationale: BTC is favored to finish above $74,000 on the April 15 noon ET Binance minute because same-venue pricing remained materially above the strike, but since the market's 81.5% price already leans hard into that view and the contract is a one-minute settle vulnerable to ordinary sub-day volatility, the disciplined output is watch-only and needs-more-research rather than an authorized trade.

## Why this is the right action / no-action call

This packet distinguishes a real directional Yes lean from execution readiness: the contract's exact-minute mechanics and the modest edge versus market make this a poor place to force action before a fresher pre-settlement check.

## Valuation

- Fair value low: 0.74
- Fair value high: 0.8
- Fair value midpoint: 0.77
- Market reference price: 0.815
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current same-venue Binance pricing above $74k supports a real Yes lean, but exact-candle settlement mechanics and unquantified final-hours downside volatility keep fair value modestly below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.58
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; much cheaper prices would require a fresh pre-settlement venue check.
- `scaled_enter`
  - `min_p:` 0.58
  - `max_p:` 0.7
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current packet sees only a modest and fragile edge.
- `hold`
  - `min_p:` 0.7
  - `max_p:` 0.79
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with a favored Yes outcome but insufficient valuation cushion for fresh adds.
- `trim`
  - `min_p:` 0.79
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above bounded fair value and exact-minute downside risk dominates.
- `exit`
  - `min_p:` 0.9
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at very high prices because one-minute settlement and plausible sub-day BTC volatility still matter.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.06
- Allow auto reversal: `false`
- Quote staleness seconds: 3600
- Valid until: 2026-04-15T11:00:00-04:00
- Time horizon: Through the April 15 12:00 ET Binance 1-minute settlement close

## Risk controls

- Max position size (% bankroll): 0.005
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 40
- Liquidity minimum depth: 1500
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not initiate new exposure from this packet because the market is already above bounded fair value and the edge is modest., Reassess close to settlement with a fresh same-venue Binance check before acting., Treat exact-minute crypto settle markets as path- and microstructure-sensitive even when spot is currently above strike.

## Invalidation

### Thesis breakers
- BTC trades back near or below $74,000 on Binance before the resolving minute.
- A fresh same-venue Binance check shows deteriorating price structure or repeated rejection through late morning ET on April 15.
- A verified final resolving candle above $74,000 would collapse the residual uncertainty and supersede this packet.

### Market structure breakers
- A Binance-specific microstructure, API/UI, or candle-mapping issue affects confidence in the governing close.
- The market reprices materially on new BTC path information before a fresh packet is produced.
- Late breaking macro or crypto-specific news materially changes intraday volatility expectations.

### Time breakers
- The final-hours path into the noon ET candle can dominate all current reasoning.
- A fresh same-venue pre-settlement check is required as the event approaches.

### Reversal conditions
- Move toward authorized yes only after a fresh packet if BTC remains comfortably above $74,000 closer to settlement while price remains favorable.
- Move materially lower if BTC weakens toward the strike or volatility rises sharply before the event.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- How much downside volatility BTC will realize before the April 15 noon ET minute.
- Whether any Binance-specific microstructure or candle-surface issue matters at settlement.
- How much the current market already incorporates near-term volatility and morning catalyst risk.

### Reasons to pass / stay small
- The edge versus market is modest and could disappear quickly if BTC firms further.
- The contract settles on one exact Binance minute close, so timing risk remains material.
- No robust independent quantification of final-hours downside risk was assembled in the bounded package.

### What would change my mind
- A fresh Binance check late on April 14 or early on April 15 showing BTC still comfortably above 75k would move fair value somewhat higher.
- A move back toward 74k or below would move fair value materially lower.
- Evidence of increased downside catalyst risk or Binance-specific settlement-surface issues would reduce confidence further.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet distinguishes a real directional Yes lean from execution readiness: the contract's exact-minute mechanics and the modest edge versus market make this a poor place to force action before a fresher pre-settlement check.

## Notes for downstream evaluator

BTC is more likely than not to finish above $74,000 on the April 15 noon ET Binance minute because same-venue price was still materially above the strike, but the market's 81.5% price is somewhat rich for a one-minute settlement contract with a plausible sub-24-hour 1.8% downside path.
