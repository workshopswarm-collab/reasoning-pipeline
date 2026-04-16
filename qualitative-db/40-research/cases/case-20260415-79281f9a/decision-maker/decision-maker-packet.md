---
type: decision_packet
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
question: "Will the price of Bitcoin be above $68,000 on April 20?"
market_id: c4503986-4093-47b0-953e-2a05b34dfdd7
external_market_id: 0xbb5b9915619f3ae3123468fadfd61e01690fdf5c0ee246e628e5af357662e88c
market_slug: bitcoin-above-68k-on-april-20
platform: polymarket
market_title: "Will the price of Bitcoin be above $68,000 on April 20?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-79281f9a/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-79281f9a/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.93
fair_value_high: 0.95
fair_value_mid: 0.94
market_reference_price: 0.9715
edge_mid_vs_market_pct_points: -3.2
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T20:37:38.183621+00:00
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
- Primary crux: Bitcoin is still very likely to close above $68,000 on the April 20 noon ET Binance minute because current same-venue pricing in the mid-74k range leaves a large cushion, but the market at 0.9715 is still too confident for a five-day, single-minute contract where a 9%+ drawdown or Binance-specific dislocation can still decide the outcome.
- One-sentence rationale: BTC is still very likely to finish above $68,000 on the April 20 Binance noon minute, but with fair value closer to 0.94 than the 0.9715 market and meaningful exact-minute five-day downside tail still live, the disciplined output remains watch-only rather than an authorized Yes trade.

## Why this is the right action / no-action call

This is a very high-probability but still overconfident crypto threshold market: strong directional Yes, weak execution value.

## Valuation

- Fair value low: 0.93
- Fair value high: 0.95
- Fair value midpoint: 0.94
- Market reference price: 0.9715
- Edge vs market (percentage points): -3.2
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Fresh Binance spot materially above strike and recent regime context support a high-probability Yes view, but bounded verification did not independently eliminate five-day downside-tail or exact-minute venue-specific risk enough to justify the 0.9715 market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.88
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price and refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.88
  - `max_p:` 0.93
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if BTC remains comfortably above 68k and no new downside catalyst appears.
- `hold`
  - `min_p:` 0.93
  - `max_p:` 0.95
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.95
  - `max_p:` 0.985
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a five-day one-minute crypto settlement with meaningful tail risk.
- `exit`
  - `min_p:` 0.985
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at extreme prices because exact-minute downside and venue-specific tail still matter.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T20:37:38.183621+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current price., Treat exact-minute Binance settlement risk as the dominant execution constraint., Reopen only if market cheapens materially or if a fresher near-settlement Binance check still shows a large cushion with reduced downside risk.

## Invalidation

### Thesis breakers
- BTC loses substantial cushion and trades back toward 69k-68k on Binance before the Apr 20 fixing window.
- A downside macro, crypto, regulatory, or exchange-specific shock materially raises the probability of a sub-68k settlement minute.
- Binance-specific pricing, liquidity, operational, or settlement-surface issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding same-venue spot deterioration, changing the value comparison.
- Binance microstructure or settlement-surface behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 20 12:00 ET should supersede this packet before any action.
- The actual Apr 20 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if later pre-fix Binance checks show the cushion still large with reduced downside risk.
- Downgrade if BTC loses cushion or if downside volatility, catalyst risk, or venue-specific weakness increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a 9%+ downside move or wick landing on the exact settlement minute over the next five days.
- Whether macro, liquidation, or weekend risk materially changes BTC volatility before settlement.
- How much additional discount exact-minute Binance operational fragility deserves at current prices.

### Reasons to pass / stay small
- The current market price is above bounded fair value.
- This is a one-minute single-venue settlement contract where tail risk matters more than broad BTC direction.
- The remaining edge is modest and not robust enough to justify authorization.

### What would change my mind
- Later same-venue checks showing BTC still comfortably above low-70k into the final day would move me somewhat closer to market.
- A move back toward 69k-70k would reduce fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a very high-probability but still overconfident crypto threshold market: strong directional Yes, weak execution value.

## Notes for downstream evaluator

Bitcoin is still very likely to close above $68,000 on the April 20 noon ET Binance minute because current same-venue pricing in the mid-74k range leaves a large cushion, but the market at 0.9715 is still too confident for a five-day, single-minute contract where a 9%+ drawdown or Binance-specific dislocation can still decide the outcome.
