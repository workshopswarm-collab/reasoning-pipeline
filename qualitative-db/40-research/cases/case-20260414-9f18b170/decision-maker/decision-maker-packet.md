---
type: decision_packet
case_key: case-20260414-9f18b170
dispatch_id: refresh-case-20260414-9f18b170-20260414T144254Z
question: "Will Bitcoin reach $76,000 April 13-19?"
market_id: case-20260414-9f18b170
external_market_id: 0xf51551b39d50396009471492879718c582a9b1e7c8448793544f480991c1c019
market_slug: will-bitcoin-reach-76k-april-13-19
platform: polymarket
market_title: "Will Bitcoin reach $76,000 April 13-19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-9f18b170/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-9f18b170/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260414-9f18b170/decision-maker/refreshes/refresh-case-20260414-9f18b170-20260414T144254Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.85
fair_value_high: 0.91
fair_value_mid: 0.88
market_reference_price: 0.98
edge_mid_vs_market_pct_points: -10.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-18T23:59:00-04:00
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
- Primary crux: This now looks like a market repricing toward fair value rather than a factual regime change: BTC reaching $76,000 during Apr 13-19 remains likely because Binance is already trading just below the threshold and only a 1-minute high is needed, but 0.98 is clearly beyond what can be justified without a directly verified qualifying Binance print.
- One-sentence rationale: BTC is still likely to touch $76,000 during Apr 13-19 because Binance is already trading just below the threshold and the contract only needs one 1-minute high, but the jump to 0.98 now prices the event as too close to automatic without a directly verified qualifying Binance print, so the disciplined posture remains watch-only rather than chasing near-certainty.

## Why this is the right action / no-action call

This refresh is a valuation update, not a thesis change: the market has moved from near-fair toward clear overconfidence, while the underlying directional case remains the same.

## Valuation

- Fair value low: 0.85
- Fair value high: 0.91
- Fair value midpoint: 0.88
- Market reference price: 0.98
- Edge vs market (percentage points): -10.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: BTC's proximity to the threshold and touch mechanics justify a strong Yes probability, but absent a verified qualifying Binance 1-minute high there is no basis to follow the market up to near-certainty.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; much cheaper pricing would require a fresh live-path check.
- `scaled_enter`
  - `min_p:` 0.72
  - `max_p:` 0.84
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the market is already materially richer than justified fair value.
- `hold`
  - `min_p:` 0.84
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with a high-probability Yes outcome but no remaining valuation cushion.
- `trim`
  - `min_p:` 0.9
  - `max_p:` 0.97
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above fair value and residual venue-specific path risk dominates.
- `exit`
  - `min_p:` 0.97
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because no verified qualifying Binance print had yet been shown in the reviewed checks.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.03
- Allow auto reversal: `false`
- Quote staleness seconds: 7200
- Valid until: 2026-04-18T23:59:00-04:00
- Time horizon: Apr 13-19 Binance BTC/USDT intrawindow high-touch resolution

## Risk controls

- Max position size (% bankroll): 0.005
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 40
- Liquidity minimum depth: 1500
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market has repriced far above bounded fair value., Existing aligned exposure may be held, but refresh on any verified Binance print near or above $76,000 or a sharp pullback below $75,000 before adjusting., Treat venue-specific threshold-touch markets as execution-sensitive once pricing enters near-certainty territory.

## Invalidation

### Thesis breakers
- A verified Binance BTC/USDT 1-minute high at or above $76,000 immediately resolves the market and supersedes this packet.
- BTC fails repeated tests below $76,000 and then sells off materially away from the threshold.
- Fresh evidence shows the relevant Binance highs remain systematically weaker than implied by broader spot markets.

### Market structure breakers
- The market reprices sharply again on new Binance path information before a fresh packet is produced.
- Exchange-specific liquidity, wick behavior, or volatility conditions change enough to invalidate the current near-threshold calibration.
- A clearer rule-text capture reveals materially stricter settlement mechanics than assumed.

### Time breakers
- A single fresh Binance wick to $76,000 can change the forecast immediately.
- As the remaining window shortens, stale path assumptions should be refreshed rather than extrapolated.

### Reversal conditions
- Move toward authorized yes only after a fresh packet if a qualifying Binance print occurs while price remains favorable for residual execution.
- Move materially lower if BTC rejects and pulls away from the threshold.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether a qualifying Binance $76,000 print has already occurred since the last reviewed checks.
- How much residual path-failure risk survives when BTC is trading within roughly 0.2%-0.4% of the trigger.
- How much of the current 0.98 price reflects informed flow versus simple threshold-chasing or stale repricing.

### Reasons to pass / stay small
- The market has now repriced far beyond bounded fair value, leaving no realistic room for error.
- The compact package still does not show a direct verified qualifying Binance print.
- Short-dated touch markets can still fail on repeated near-misses, and those tails matter economically at 98%.

### What would change my mind
- A fresh verified Binance print at or above $76,000 would collapse the residual tail and move confidence toward resolution.
- A clear rejection followed by a move back below $75,000 would lower fair value materially.
- A cleaner rules capture removing residual source-specific uncertainty would slightly improve confidence but would not justify 0.98 without a qualifying print.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is a valuation update, not a thesis change: the market has moved from near-fair toward clear overconfidence, while the underlying directional case remains the same.

## Notes for downstream evaluator

This now looks like a market repricing toward fair value rather than a factual regime change: BTC reaching $76,000 during Apr 13-19 remains likely because Binance is already trading just below the threshold and only a 1-minute high is needed, but 0.98 is clearly beyond what can be justified without a directly verified qualifying Binance print.
