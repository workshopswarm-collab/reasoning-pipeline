---
type: decision_packet
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
question: "Will the price of Bitcoin be above $70,000 on April 14?"
market_id: case-20260414-3ce42d6c
external_market_id: 0xb4edd1ceca7ae170d1ed632677a8671797b3d47374d38ffac7d410cfb9e9f5c7
market_slug: bitcoin-above-70k-on-april-14
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 14?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-3ce42d6c/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-3ce42d6c/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.989
fair_value_high: 0.995
fair_value_mid: 0.992
market_reference_price: 0.9995
edge_mid_vs_market_pct_points: -0.8
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-14T11:58:00-04:00
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
- Primary crux: BTC being above $70,000 at the April 14 noon ET Binance minute is overwhelmingly likely because the same-venue morning price sat far above the strike, but the market's 99.95% price already assumes away almost all of the exact-minute, single-venue settlement tail that still remains until the resolving candle is actually observed.
- One-sentence rationale: Bitcoin being above $70,000 at the April 14 noon ET Binance minute is overwhelmingly likely given the large same-venue pre-noon cushion, but because the market is already at 99.95% and the exact resolving candle was not directly observed, the disciplined posture is watch-only rather than chasing near-certainty.

## Why this is the right action / no-action call

This packet treats the case as directionally decided but not yet operationally closed; the only remaining uncertainty is narrow settlement-mechanics tail risk.

## Valuation

- Fair value low: 0.989
- Fair value high: 0.995
- Fair value midpoint: 0.992
- Market reference price: 0.9995
- Edge vs market (percentage points): -0.8
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: The bounded evidence supports an overwhelming Yes probability, but the unobserved final resolving candle and residual single-minute Binance tail keep fair value slightly below the market's near-certainty pricing.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh pre-noon venue check.
- `scaled_enter`
  - `min_p:` 0.94
  - `max_p:` 0.98
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the contract is already in tiny-tail operational-risk territory rather than directional-value territory.
- `hold`
  - `min_p:` 0.98
  - `max_p:` 0.994
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with overwhelming Yes probability but no fresh-add edge.
- `trim`
  - `min_p:` 0.994
  - `max_p:` 0.999
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price approaches the upper end of justified fair value.
- `exit`
  - `min_p:` 0.999
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because remaining value is dominated by exact-minute settlement and venue-specific anomaly risk.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.005
- Allow auto reversal: `false`
- Quote staleness seconds: 120
- Valid until: 2026-04-14T11:58:00-04:00
- Time horizon: Through the exact Binance 12:00 ET / 16:00 UTC settlement candle

## Risk controls

- Max position size (% bankroll): 0.001
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 10
- Liquidity minimum depth: 2500
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate new exposure from this packet because the market is already beyond bounded fair value., Existing aligned exposure may be held, but refresh on the exact resolving candle before any adjustment., Treat same-minute venue-specific settlement markets as operational-risk contracts once price is this extreme.

## Invalidation

### Thesis breakers
- A sharp late selloff materially compresses the cushion toward $70,000 before the noon ET minute.
- Direct observation of the resolving Binance candle closes at or below $70,000.
- Evidence emerges of a Binance-specific timestamp, print, or surface anomaly affecting the governing minute.

### Market structure breakers
- The current quote is stale relative to the latest pre-noon Binance state.
- UI-versus-API or surface-mapping differences prove material for the resolving candle.
- Liquidity collapses or market mechanics make the displayed quote non-executable.

### Time breakers
- The exact resolving candle should replace this packet immediately once observed.
- In the final minutes before noon ET, even small venue-specific changes can dominate all prior reasoning.

### Reversal conditions
- Move materially lower only on a fresh packet if BTC collapses sharply toward the threshold or a Binance-specific anomaly appears.
- Do not auto-reverse from this packet.
- Suspend action if the final candle source appears disputed.

## Epistemic status

### Key uncertainties
- The exact final Binance 12:00 ET candle close.
- Whether any Binance-specific operational, timestamp, or UI/API anomaly affects the governing minute.
- Residual intraday volatility over the final pre-noon window.

### Reasons to pass / stay small
- The market is already essentially pricing certainty, leaving no actionable edge.
- The missing exact resolving candle is now the only thing that matters economically.
- Single-minute, single-venue markets should not be treated as free money even with a very large pre-noon cushion.

### What would change my mind
- Direct observation of the final Binance candle closing above $70,000 would collapse the remaining tail.
- A sharp move toward the threshold before noon ET would lower fair value materially.
- Evidence of a Binance-specific settlement anomaly would reduce confidence despite the large cushion.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet treats the case as directionally decided but not yet operationally closed; the only remaining uncertainty is narrow settlement-mechanics tail risk.

## Notes for downstream evaluator

BTC being above $70,000 at the April 14 noon ET Binance minute is overwhelmingly likely because the same-venue morning price sat far above the strike, but the market's 99.95% price already assumes away almost all of the exact-minute, single-venue settlement tail that still remains until the resolving candle is actually observed.
