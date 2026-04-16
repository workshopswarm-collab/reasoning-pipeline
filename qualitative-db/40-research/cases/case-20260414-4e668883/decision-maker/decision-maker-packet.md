---
type: decision_packet
case_key: case-20260414-4e668883
dispatch_id: dispatch-case-20260414-4e668883-20260414T133938Z
question: "Will Ethereum reach $2,400 April 13-19?"
market_id: case-20260414-4e668883
external_market_id: 0x9a91f5fa90b334c224cb4e638248acc8907b44fa8ed56361b24573cd20491763
market_slug: will-ethereum-reach-2400-april-13-19
platform: polymarket
market_title: "Will Ethereum reach $2,400 April 13-19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-4e668883/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-4e668883/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.84
fair_value_high: 0.9
fair_value_mid: 0.87
market_reference_price: 0.9235
edge_mid_vs_market_pct_points: -5.3
independent_verification_quality: medium
compressed_toward_market_applied: true
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
- Primary crux: ETH remains likely to print a qualifying Binance 1-minute high at or above $2,400 because it is trading within roughly half a percent of the threshold with several days left, but the market's 92.35% price still overstates certainty for a hit that had not yet been verified on the governing source during the reviewed checks.
- One-sentence rationale: ETH is still more likely than not to hit $2,400 during Apr 13-19 because a Binance touch-style trigger with spot already within about 0.5% of the threshold is favorable to Yes, but the market's 92.35% price remains too aggressive for a threshold that had not yet been verified as hit on the governing source during reviewed checks, so the disciplined posture is watch-only rather than chasing Yes.

## Why this is the right action / no-action call

This packet keeps the directional Yes stance while refusing to follow the market to near-certainty; the remaining disagreement is almost entirely about short-horizon path-failure risk, not the contract's basic mechanics.

## Valuation

- Fair value low: 0.84
- Fair value high: 0.9
- Fair value midpoint: 0.87
- Market reference price: 0.9235
- Edge vs market (percentage points): -5.3
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: ETH's proximity to the threshold and permissive touch mechanics support a high Yes probability, but fresh governing-source confirmation of an actual $2,400 print was still absent in the reviewed checks, so fair value remains modestly below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.68
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh path check.
- `scaled_enter`
  - `min_p:` 0.68
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the market is already richer than justified fair value.
- `hold`
  - `min_p:` 0.8
  - `max_p:` 0.88
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with a high-probability Yes outcome but not enough edge for fresh adds.
- `trim`
  - `min_p:` 0.88
  - `max_p:` 0.95
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above bounded fair value and residual path-failure risk dominates.
- `exit`
  - `min_p:` 0.95
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because even a sub-1% threshold touch can still fail over the remaining window.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.05
- Allow auto reversal: `false`
- Quote staleness seconds: 7200
- Valid until: 2026-04-18T23:59:00-04:00
- Time horizon: Apr 13-19 Binance ETH/USDT intrawindow high-touch resolution

## Risk controls

- Max position size (% bankroll): 0.0075
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 50
- Liquidity minimum depth: 1200
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market is already above bounded fair value., Existing aligned exposure may be held, but refresh on any verified Binance $2,400 print or sharp pullback away from the threshold before adjusting., Treat short-dated threshold-touch markets as path-dependent even when spot is only a few dollars below the trigger.

## Invalidation

### Thesis breakers
- A verified Binance ETH/USDT 1-minute high at or above $2,400 immediately resolves the market and supersedes this packet.
- ETH repeatedly rejects just below $2,400 and then sells off materially away from the threshold.
- Fresh evidence shows a broader crypto risk-off move or weakening momentum that materially lowers touch odds.

### Market structure breakers
- The market reprices sharply again on new ETH path information before a fresh packet is produced.
- Short-term volatility or exchange-specific liquidity conditions change enough to invalidate current near-touch calibration.
- A clearer authoritative rules capture reveals more restrictive mechanics than assumed.

### Time breakers
- A single fresh Binance wick to $2,400 can change the forecast immediately.
- As the remaining window shortens, stale path assumptions should be refreshed rather than extrapolated.

### Reversal conditions
- Move toward authorized yes only after a fresh packet if ETH continues pressing the threshold while price remains favorable.
- Move materially lower if ETH rejects again and pulls away from $2,400.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether a qualifying Binance $2,400 print has already occurred since the last reviewed checks.
- How much residual path-failure risk survives when ETH is trading within roughly half a percent of the trigger.
- Whether current price action reflects informed momentum continuation or simple threshold-chasing.

### Reasons to pass / stay small
- The market is already pricing a very high Yes probability, leaving little room for error.
- The checked sources still had ETH below the threshold on the governing metric at review time.
- Short-dated crypto threshold markets can remain path-sensitive even when the remaining move is small.

### What would change my mind
- A fresh verified Binance print at or above $2,400 would collapse the residual tail and move confidence toward resolution.
- Repeated renewed tests of $2,397-$2,399 without broader reversal would move fair value somewhat higher.
- A sharp move away from the threshold or fresh restrictive rule clarification would move fair value lower.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet keeps the directional Yes stance while refusing to follow the market to near-certainty; the remaining disagreement is almost entirely about short-horizon path-failure risk, not the contract's basic mechanics.

## Notes for downstream evaluator

ETH remains likely to print a qualifying Binance 1-minute high at or above $2,400 because it is trading within roughly half a percent of the threshold with several days left, but the market's 92.35% price still overstates certainty for a hit that had not yet been verified on the governing source during the reviewed checks.
