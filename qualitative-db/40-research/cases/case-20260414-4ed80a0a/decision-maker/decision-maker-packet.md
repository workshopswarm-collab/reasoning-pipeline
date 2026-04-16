---
type: decision_packet
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
question: "Will Ethereum reach $2,400 April 13-19?"
market_id: 388995c3-1866-46a6-9793-69442db90054
external_market_id: 0x9a91f5fa90b334c224cb4e638248acc8907b44fa8ed56361b24573cd20491763
market_slug: will-ethereum-reach-2400-april-13-19
platform: polymarket
market_title: "Will Ethereum reach $2,400 April 13-19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-4ed80a0a/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-4ed80a0a/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.97
fair_value_high: 0.995
fair_value_mid: 0.9825
market_reference_price: 0.916
edge_mid_vs_market_pct_points: 6.7
independent_verification_quality: high
compressed_toward_market_applied: false
decision_confidence: high
valid_until: 2026-04-15T17:50:56.247681+00:00
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
- Primary crux: This contract appears effectively already satisfied because bundled Binance ETH/USDT data showed an in-window high of 2415.5 above the 2400 threshold, but the market's 0.916 price no longer offers a clean executable edge once the remaining uncertainty is mostly about settlement-surface parity and archival proof rather than ETH direction.
- One-sentence rationale: Ethereum very likely already satisfied this Binance-specific $2,400 touch contract because bundled evidence showed an in-window high above the threshold, but the residual uncertainty is narrow settlement-surface and archival-proof risk, so the disciplined output remains watch-only despite fair value above market.

## Why this is the right action / no-action call

This is a rare bounded case where own fair value exceeds market because the trigger appears already met in substance, yet execution remains non-authorized due to source-of-truth and settlement-path tail risk.

## Valuation

- Fair value low: 0.97
- Fair value high: 0.995
- Fair value midpoint: 0.9825
- Market reference price: 0.916
- Edge vs market (percentage points): 6.7
- Independent verification quality: `high`
- Compressed toward market applied: `false`
- Compression reason: Direct bundled Binance evidence shows an in-window high above 2400, leaving only modest settlement-surface and archival-proof tail risk rather than broad outcome uncertainty.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.88
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper prices would require a fresh settlement-surface verification.
- `scaled_enter`
  - `min_p:` 0.88
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0
  - `notes:` Potential value may exist below market, but this packet still withholds authorization because the remaining risk is operational rather than informational.
- `hold`
  - `min_p:` 0.94
  - `max_p:` 0.985
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with bounded fair value for an effectively already-satisfied Yes outcome.
- `trim`
  - `min_p:` 0.985
  - `max_p:` 0.997
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price reaches the upper end of justified fair value and operational tail dominates.
- `exit`
  - `min_p:` 0.997
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit or avoid at extreme prices because remaining uncertainty is almost entirely settlement-surface or administrative.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T17:50:56.247681+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `high`
- Portfolio constraints: Do not size aggressively despite apparent edge because the residual risk is concentrated in source-of-truth parity and settlement administration., Refresh only if a credible settlement-source dispute, data revision, or market-status correction emerges., Treat this as a near-settled Binance-threshold case rather than an ongoing ETH directional thesis.

## Invalidation

### Thesis breakers
- A direct Binance 1-minute source-of-truth audit shows no qualifying in-window high at or above 2400.
- A credible data correction or official settlement clarification rejects the observed 2415.5 print.
- A venue-specific dispute establishes that the archived API-derived evidence does not match the operational settlement surface.

### Market structure breakers
- A source-of-truth mismatch between Binance API data and the cited Binance chart becomes material.
- The displayed market price becomes stale relative to a new settlement-status update.

### Time breakers
- Formal settlement or official market correction should supersede this packet immediately.
- Any settlement delay shifts the relevant uncertainty from price path to administrative and source-parity risk.

### Reversal conditions
- Move to effectively closed confidence only after formal settlement or direct confirmation from the exact settlement surface.
- Move materially lower only on a fresh packet if a real parity dispute or data revision emerges.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the exact Binance chart or UI surface cited by the contract matches the archived API-derived qualifying print.
- Whether any late administrative clarification, correction, or dispute affects settlement.
- The exact first qualifying 1-minute candle was not archived in this bounded bundle.

### Reasons to pass / stay small
- Although fair value is above market, the remaining uncertainty is operational and auditability-driven rather than a robust forecasting edge.
- The market may already be in the process of catching up to an effectively satisfied condition, limiting executable value.

### What would change my mind
- Direct confirmation from the exact Binance 1-minute settlement surface would remove most residual doubt.
- A credible data revision below 2400 or a settlement clarification rejecting the observed print would lower fair value sharply.
- Official market settlement to Yes would collapse the remaining tail to zero.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a rare bounded case where own fair value exceeds market because the trigger appears already met in substance, yet execution remains non-authorized due to source-of-truth and settlement-path tail risk.

## Notes for downstream evaluator

This contract appears effectively already satisfied because bundled Binance ETH/USDT data showed an in-window high of 2415.5 above the 2400 threshold, but the market's 0.916 price no longer offers a clean executable edge once the remaining uncertainty is mostly about settlement-surface parity and archival proof rather than ETH direction.
