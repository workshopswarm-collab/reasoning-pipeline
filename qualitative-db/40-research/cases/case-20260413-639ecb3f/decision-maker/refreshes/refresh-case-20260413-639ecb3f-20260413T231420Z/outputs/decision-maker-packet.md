---
type: decision_packet
case_key: case-20260413-639ecb3f
dispatch_id: refresh-case-20260413-639ecb3f-20260413T231420Z
question: "Will Ethereum reach $2,400 April 13-19?"
market_id: case-20260413-639ecb3f
external_market_id: 0x9a91f5fa90b334c224cb4e638248acc8907b44fa8ed56361b24573cd20491763
market_slug: will-ethereum-reach-2400-april-13-19
platform: polymarket
market_title: "Will Ethereum reach $2,400 April 13-19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-639ecb3f/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-639ecb3f/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260413-639ecb3f/decision-maker/refreshes/refresh-case-20260413-639ecb3f-20260413T231420Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.68
fair_value_high: 0.74
fair_value_mid: 0.71
market_reference_price: 0.79
edge_mid_vs_market_pct_points: -8.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T23:59:00-04:00
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
- Primary crux: This looks like a price-only repricing rather than a factual regime change: ETH still seems more likely than not to touch $2,400 during Apr 13-19, but the move from 0.76 to 0.79 now places the market clearly above the bounded evidence-supported range.
- One-sentence rationale: ETH reaching $2,400 during Apr 13-19 still looks more likely than not, but because the move to 0.79 is not matched by new independently verified evidence and the original proximity-versus-failed-breakout crux remains intact, the disciplined update is watch-only rather than chasing the repricing.

## Why this is the right action / no-action call

This refresh remains bounded and lightweight; no new first-hand rule-text or live-path evidence was added, so the update is about market repricing rather than a changed underlying thesis.

## Valuation

- Fair value low: 0.68
- Fair value high: 0.74
- Fair value midpoint: 0.71
- Market reference price: 0.79
- Edge vs market (percentage points): -8.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: The prior synthesis already incorporated touch mechanics and proximity, and no new first-hand rule-text or live-path evidence was added in this refresh to justify following the market higher.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.55
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; much cheaper pricing would require a refreshed rules and path check.
- `scaled_enter`
  - `min_p:` 0.55
  - `max_p:` 0.67
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current packet is hold/watch only and the market is already richer than justified fair value.
- `hold`
  - `min_p:` 0.67
  - `max_p:` 0.73
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with a moderate-high Yes probability but not enough edge for fresh adds.
- `trim`
  - `min_p:` 0.73
  - `max_p:` 0.85
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above bounded fair value and failed-breakout risk dominates.
- `exit`
  - `min_p:` 0.85
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because proximity does not guarantee the threshold prints on the governing venue.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.08
- Allow auto reversal: `false`
- Quote staleness seconds: 7200
- Valid until: 2026-04-16T23:59:00-04:00
- Time horizon: Apr 13-19 monitoring window through venue-specific threshold resolution

## Risk controls

- Max position size (% bankroll): 0.0075
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 60
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market has repriced above bounded fair value., Existing aligned exposure may be held, but refresh venue-specific rules and live ETH path before any adjustment., Treat short-dated crypto threshold markets as highly path-dependent even when spot is close to the level.

## Invalidation

### Thesis breakers
- ETH fails to retest the mid-2360s and instead reverses toward the low-2300s or below.
- Fresh restrictive rule text shows the contract is harder than a simple Binance 1-minute high touch interpretation.
- A sharp crypto-wide risk-off move materially reduces the chance of printing 2400 during the window.

### Market structure breakers
- The market reprices materially again on new crypto momentum or reversal information before a fresh packet is produced.
- Venue-specific settlement mechanics differ from the assumed Binance threshold-high interpretation.
- Short-term volatility regime changes make recent proximity-based calibration unreliable.

### Time breakers
- A single momentum extension or reversal over the next 24-48 hours can move probability materially.
- As the window shortens, stale path assumptions should be replaced rather than extrapolated.

### Reversal conditions
- Move toward authorization only after a fresh packet if ETH continues extending and rule mechanics are cleanly confirmed while price remains favorable.
- Move materially lower if ETH loses momentum, sells off away from 2400, or if rules prove more restrictive than assumed.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Exact first-hand authoritative rules text for the settlement feed and threshold mechanics.
- Whether current ETH momentum is durable enough to produce the final 1-2% move.
- How likely a short-horizon crypto-wide reversal is over the remaining window.

### Reasons to pass / stay small
- The apparent edge versus market has inverted more clearly after the repricing from 0.76 to 0.79.
- Independent verification of the exact authoritative settlement wording was not perfect in the synthesis pass.
- Short-dated crypto threshold markets can fail on the final increment even when spot is nearby.

### What would change my mind
- Clean direct rules text confirming the Binance 1-minute high interpretation would modestly improve confidence.
- A clean extension through the high-2300s would move fair value somewhat higher, though likely not enough to justify 0.79 without more support.
- A sharp selloff away from 2400 or evidence of more restrictive settlement mechanics would move fair value lower.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh remains bounded and lightweight; no new first-hand rule-text or live-path evidence was added, so the update is about market repricing rather than a changed underlying thesis.

## Notes for downstream evaluator

This looks like a price-only repricing rather than a factual regime change: ETH still seems more likely than not to touch $2,400 during Apr 13-19, but the move from 0.76 to 0.79 now places the market clearly above the bounded evidence-supported range.
