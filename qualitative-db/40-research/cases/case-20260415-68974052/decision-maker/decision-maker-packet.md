---
type: decision_packet
case_key: case-20260415-68974052
dispatch_id: dispatch-case-20260415-68974052-20260415T183011Z
question: "Will the price of Bitcoin be above $72,000 on April 17?"
market_id: 34b19a2f-03db-4e0f-ba94-a0ddb3b0670c
external_market_id: 0x278e937ecb8ff1da49c4e04aba52d1922b3e0a7a15d09e621bbf33154c230287
market_slug: bitcoin-above-72k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-68974052/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-68974052/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.79
fair_value_high: 0.83
fair_value_mid: 0.81
market_reference_price: 0.85
edge_mid_vs_market_pct_points: -4.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T18:42:41.107058+00:00
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
- Primary crux: Bitcoin is still more likely than not to close above $72,000 on the April 17 noon ET Binance minute because current same-venue pricing around 74.2k leaves a real cushion, but 0.85 is still somewhat rich for a 42-hour, single-minute settlement where an ordinary sub-3% BTC drop can still flip the outcome.
- One-sentence rationale: BTC is still more likely than not to finish above $72,000 on the April 17 Binance noon minute, but with fair value centered near 0.81 rather than the 0.85 market and meaningful 42-hour exact-minute downside risk still live, the disciplined output remains watch-only.

## Why this is the right action / no-action call

This is a high-probability but still overconfident crypto threshold market: directional Yes survives, execution value does not.

## Valuation

- Fair value low: 0.79
- Fair value high: 0.83
- Fair value midpoint: 0.81
- Market reference price: 0.85
- Edge vs market (percentage points): -4.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current Binance spot materially above strike supports a strong Yes base case, but bounded verification did not independently tighten the remaining 24-48 hour downside-volatility risk enough to justify the market price.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.73
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price and still refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.73
  - `max_p:` 0.79
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if BTC remains comfortably above 72k and no new downside catalyst appears.
- `hold`
  - `min_p:` 0.79
  - `max_p:` 0.83
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.83
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a narrow one-minute crypto settlement with meaningful 42-hour path dependence.
- `exit`
  - `min_p:` 0.9
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at very rich prices because a normal BTC drawdown can still decide the contract.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T18:42:41.107058+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current price., Treat exact-minute Binance settlement risk as the dominant execution constraint., Reopen only if market cheapens materially or later same-venue checks show the cushion holding into the final hours.

## Invalidation

### Thesis breakers
- BTC loses cushion materially and trades back toward 72k-73k on Binance before the Apr 17 fixing window.
- A downside macro, crypto, or exchange-specific shock materially raises the probability of a sub-72k settlement minute.
- Binance-specific pricing, liquidity, or operational issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding same-venue spot deterioration, changing the value comparison.
- Binance microstructure or settlement-surface behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 17 12:00 ET should supersede this packet before any action.
- The actual Apr 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if later pre-fix Binance checks show the cushion still large with reduced downside risk.
- Downgrade if BTC loses cushion or if downside volatility or catalyst risk increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a roughly 3% downside move landing on the exact settlement minute over the next ~42 hours.
- Whether an unobserved near-term catalyst or volatility shock emerges before the fixing window.
- How much additional discount single-venue Binance settlement deserves versus a broader BTC directional market.

### Reasons to pass / stay small
- The current market price is above bounded fair value.
- This is a one-minute single-venue settlement contract where path risk matters more than broad BTC direction.
- The remaining edge is modest and not robust enough to justify authorization.

### What would change my mind
- Later same-venue checks showing BTC still comfortably above 73k-74k into the final hours would move me somewhat closer to market.
- A move back toward 72k-73k would reduce fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a high-probability but still overconfident crypto threshold market: directional Yes survives, execution value does not.

## Notes for downstream evaluator

Bitcoin is still more likely than not to close above $72,000 on the April 17 noon ET Binance minute because current same-venue pricing around 74.2k leaves a real cushion, but 0.85 is still somewhat rich for a 42-hour, single-minute settlement where an ordinary sub-3% BTC drop can still flip the outcome.
