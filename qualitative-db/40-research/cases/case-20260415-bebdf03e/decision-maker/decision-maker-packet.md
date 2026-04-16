---
type: decision_packet
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
question: "Will the price of Bitcoin be above $72,000 on April 21?"
market_id: 6c5bfff7-39b3-49d4-bb33-c8b7881a4e51
external_market_id: 0x98836967b3291ac597477867ab3e5d141ec344cac432df45f0aea9539fb5c4f2
market_slug: bitcoin-above-72k-on-april-21
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 21?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-bebdf03e/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-bebdf03e/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.72
fair_value_high: 0.78
fair_value_mid: 0.75
market_reference_price: 0.815
edge_mid_vs_market_pct_points: -6.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T22:29:05.188045+00:00
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
- Primary crux: Bitcoin is still more likely than not to close above $72,000 on the April 21 noon ET Binance minute because current same-venue pricing around 75k and a 24h low above 72k leave a real cushion, but the market at 0.815 remains too confident for a six-day, single-minute settlement where a routine >4% drawdown or badly timed Binance dip can still decide the outcome.
- One-sentence rationale: BTC is still more likely than not to finish above $72,000 on the April 21 Binance noon minute, but with fair value closer to 0.75 than the 0.815 market and meaningful exact-minute six-day downside tail still live, the disciplined output remains watch-only rather than an authorized Yes trade.

## Why this is the right action / no-action call

This is a moderate-probability Yes with weak execution value: current cushion supports the thesis, but not the market's degree of confidence.

## Valuation

- Fair value low: 0.72
- Fair value high: 0.78
- Fair value midpoint: 0.75
- Market reference price: 0.815
- Edge vs market (percentage points): -6.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current Binance spot above strike and recent price context support a solid Yes baseline, but bounded verification did not independently establish a downside distribution tight enough to justify the market's 0.815 confidence.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.67
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a materially cheaper price and refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.67
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if BTC remains above 72k and no new downside catalyst appears.
- `hold`
  - `min_p:` 0.72
  - `max_p:` 0.78
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.78
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a six-day one-minute crypto settlement with meaningful path dependence.
- `exit`
  - `min_p:` 0.86
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at rich prices because a routine downside move can still decide the contract.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T22:29:05.188045+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current price., Treat exact-minute Binance settlement risk as the dominant execution constraint., Reopen only if market cheapens materially or if later same-venue checks show BTC holding comfortably above 72k with reduced volatility.

## Invalidation

### Thesis breakers
- BTC loses the 72k regime on Binance and fails to reclaim it before the Apr 21 fixing window.
- A downside macro, crypto, or exchange-specific shock materially raises the probability of a sub-72k settlement minute.
- Binance-specific pricing, liquidity, operational, or display-surface issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding same-venue spot deterioration, changing the value comparison.
- Binance microstructure or settlement-surface behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 21 12:00 ET should supersede this packet before any action.
- The actual Apr 21 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if later pre-fix Binance checks show BTC holding comfortably above 72k with a larger cushion.
- Downgrade if BTC compresses toward the threshold or if volatility expands.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a >4% downside move or wick landing on the exact settlement minute over the next six days.
- Whether an unscheduled macro or crypto-specific shock emerges before the fixing window.
- How much residual discount exact-minute Binance UI-versus-API sensitivity deserves relative to a broader benchmark view.

### Reasons to pass / stay small
- The current market price is above bounded fair value.
- This is a one-minute single-venue settlement contract where path risk matters more than broad BTC direction.
- The remaining edge is modest and not robust enough to justify authorization.

### What would change my mind
- Later same-venue checks showing BTC still comfortably above 74k-75k into the final day would move me somewhat closer to market.
- A move back toward 72k-73k would reduce fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a moderate-probability Yes with weak execution value: current cushion supports the thesis, but not the market's degree of confidence.

## Notes for downstream evaluator

Bitcoin is still more likely than not to close above $72,000 on the April 21 noon ET Binance minute because current same-venue pricing around 75k and a 24h low above 72k leave a real cushion, but the market at 0.815 remains too confident for a six-day, single-minute settlement where a routine >4% drawdown or badly timed Binance dip can still decide the outcome.
