---
type: decision_packet
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
question: "Will the price of Bitcoin be above $72,000 on April 16?"
market_id: 7da0bb87-594f-4bdb-a7ae-fddfc3f0f8bd
external_market_id: 0xee2d4eeeae30d06342d630e97c23ff423da2e542cbfb30a8ce252b9f47ccc9e3
market_slug: bitcoin-above-72k-on-april-16
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 16?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-9a9c8ea3/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-9a9c8ea3/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.91
fair_value_high: 0.94
fair_value_mid: 0.925
market_reference_price: 0.955
edge_mid_vs_market_pct_points: -3.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T19:30:11.894089+00:00
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
- Primary crux: Bitcoin is still very likely to close above $72,000 on the April 16 noon ET Binance minute because same-venue spot around 74.7k and a 24h low around 73.5k leave a meaningful cushion, but the market at 0.955 is still a bit too confident for a one-minute, single-venue settlement where a routine overnight selloff, a noon-time wick, or small UI/API parity risk can still decide the contract.
- One-sentence rationale: BTC is still very likely to finish above $72,000 on the April 16 Binance noon minute, but with fair value closer to 0.925 than the 0.955 market and meaningful exact-minute overnight downside tail still live, the disciplined output remains watch-only rather than an authorized Yes trade.

## Why this is the right action / no-action call

This is a high-probability but still overconfident crypto threshold market: directional Yes survives, execution value does not.

## Valuation

- Fair value low: 0.91
- Fair value high: 0.94
- Fair value midpoint: 0.925
- Market reference price: 0.955
- Edge vs market (percentage points): -3.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Fresh Binance spot materially above strike supports a strong Yes baseline, but bounded verification did not eliminate overnight downside-path or exact-minute settlement risk enough to justify the 0.955 market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a meaningfully cheaper price and refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.86
  - `max_p:` 0.91
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if BTC remains comfortably above 72k and no new downside catalyst appears.
- `hold`
  - `min_p:` 0.91
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.94
  - `max_p:` 0.98
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a narrow one-minute crypto settlement with meaningful overnight path dependence.
- `exit`
  - `min_p:` 0.98
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at extreme prices because exact-minute downside tail still matters.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T19:30:11.894089+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current price., Treat exact-minute Binance settlement risk as the dominant execution constraint., Reopen only if market cheapens materially or if a fresher near-settlement Binance check still shows a large cushion with no emerging volatility or source-surface concern.

## Invalidation

### Thesis breakers
- BTC loses cushion materially and trades back toward 72k-73k on Binance before the Apr 16 fixing window.
- A downside macro, crypto, or exchange-specific shock materially raises the probability of a sub-72k settlement minute.
- Binance-specific pricing, liquidity, operational, or UI/API display issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding same-venue spot deterioration, changing the value comparison.
- Binance microstructure or settlement-surface behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 16 12:00 ET should supersede this packet before any action.
- The actual Apr 16 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if later pre-fix Binance checks show the cushion still large with reduced downside risk.
- Downgrade if BTC loses cushion or if downside volatility, catalyst risk, or surface-parity concern increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a 3.5%+ downside move or wick landing on the exact settlement minute over the next ~21 hours.
- Whether overnight macro or crypto news materially changes short-horizon volatility before settlement.
- How much residual discount exact-minute Binance UI/API parity risk deserves at current prices.

### Reasons to pass / stay small
- The current market price is above bounded fair value.
- This is a one-minute single-venue settlement contract where path risk matters more than broad BTC direction.
- The remaining edge is small and not robust enough to justify authorization.

### What would change my mind
- Later same-venue checks showing BTC still comfortably above 73.5k-74k into the final hours would move me somewhat closer to market.
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

Bitcoin is still very likely to close above $72,000 on the April 16 noon ET Binance minute because same-venue spot around 74.7k and a 24h low around 73.5k leave a meaningful cushion, but the market at 0.955 is still a bit too confident for a one-minute, single-venue settlement where a routine overnight selloff, a noon-time wick, or small UI/API parity risk can still decide the contract.
