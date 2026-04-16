---
type: decision_packet
case_key: case-20260415-868fc947
dispatch_id: refresh-case-20260415-868fc947-20260415T115501Z
question: "Will the price of Bitcoin be above $72,000 on April 16?"
market_id: 7da0bb87-594f-4bdb-a7ae-fddfc3f0f8bd
external_market_id: 0xee2d4eeeae30d06342d630e97c23ff423da2e542cbfb30a8ce252b9f47ccc9e3
market_slug: bitcoin-above-72k-on-april-16
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 16?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-868fc947/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-868fc947/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260415-868fc947/decision-maker/refreshes/refresh-case-20260415-868fc947-20260415T115501Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.8
fair_value_high: 0.86
fair_value_mid: 0.83
market_reference_price: 0.885
edge_mid_vs_market_pct_points: -5.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T11:56:04.260405+00:00
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
- Primary crux: The move from a prior fair-value center near 0.83 to a market price of 0.885 is best treated as repricing rather than a broken thesis: BTC is still more likely than not to close above $72,000 on the April 16 noon ET Binance minute, but the market is now materially above bounded fair value for a one-minute settlement with unresolved wick and downside-path risk.
- One-sentence rationale: BTC is still more likely than not to finish above $72,000 on the April 16 Binance noon minute, but the market's move up to 0.885 only worsens the prior below-market valuation view, so the disciplined output remains watch-only with fair value anchored near 0.83 rather than chasing a richer price.

## Why this is the right action / no-action call

This refresh is a pure valuation update: same directional Yes, weaker execution case.

## Valuation

- Fair value low: 0.8
- Fair value high: 0.86
- Fair value midpoint: 0.83
- Market reference price: 0.885
- Edge vs market (percentage points): -5.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: No new bounded evidence justifies changing the prior probability range; the refresh adds price movement but not stronger verification of exact-minute stability or downside-tail suppression.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.74
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price and still a fresh Binance check near settlement.
- `scaled_enter`
  - `min_p:` 0.74
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if same-venue cushion remains intact and pre-fix volatility stays contained.
- `hold`
  - `min_p:` 0.8
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.86
  - `max_p:` 0.92
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a one-minute settlement contract with meaningful path dependence.
- `exit`
  - `min_p:` 0.92
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at very rich prices because exact-minute downside tail dominates residual uncertainty.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T11:56:04.260405+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the updated market price., Treat exact-minute Binance settlement risk as the dominant execution constraint even when spot remains above strike., Reopen only if price cheapens materially or a fresher pre-fix Binance check materially improves the cushion and path confidence.

## Invalidation

### Thesis breakers
- BTC loses cushion and trades materially back toward 72k-73k on Binance before the Apr 16 fixing window.
- A concrete downside catalyst or volatility shock materially raises the odds of a sub-72k settlement minute.
- Evidence appears that Binance's operative settlement surface differs materially from the assumed UI/API mapping.

### Market structure breakers
- Market price moves materially again without corresponding same-venue spot support, changing the value comparison.
- Binance operational or microstructure issues emerge near settlement.

### Time breakers
- A fresh direct Binance observation closer to Apr 16 12:00 ET should supersede this packet before any action.
- The actual Apr 16 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if a fresh pre-fix Binance check shows a meaningfully larger cushion.
- Downgrade if BTC loses cushion or if downside volatility or catalyst risk increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a meaningful downside move or wick landing exactly at the settlement minute.
- Whether the market embeds fresher venue-specific information than the bounded package contains.
- How much the mild UI-versus-API implementation ambiguity matters in practice.

### Reasons to pass / stay small
- The updated market price is now clearly above bounded fair value.
- This is a one-minute single-venue settlement contract where path risk matters more than broad BTC direction.
- The refresh added price movement, not new evidence supporting a higher probability.

### What would change my mind
- A fresh Binance check near settlement showing sustained trade well above 72k with subdued volatility would move me somewhat closer to market.
- A move back toward 73k or evidence of elevated downside catalyst risk would lower fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is a pure valuation update: same directional Yes, weaker execution case.

## Notes for downstream evaluator

The move from a prior fair-value center near 0.83 to a market price of 0.885 is best treated as repricing rather than a broken thesis: BTC is still more likely than not to close above $72,000 on the April 16 noon ET Binance minute, but the market is now materially above bounded fair value for a one-minute settlement with unresolved wick and downside-path risk.
