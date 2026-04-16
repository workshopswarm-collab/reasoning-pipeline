---
type: decision_packet
case_key: case-20260413-64e915de
dispatch_id: refresh-case-20260413-64e915de-20260414T001639Z
question: "Will Ethereum reach $2,400 April 13-19?"
market_id: case-20260413-64e915de
external_market_id: 0x9a91f5fa90b334c224cb4e638248acc8907b44fa8ed56361b24573cd20491763
market_slug: will-ethereum-reach-2400-april-13-19
platform: polymarket
market_title: "Will Ethereum reach $2,400 April 13-19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-64e915de/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-64e915de/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260413-64e915de/decision-maker/refreshes/refresh-case-20260413-64e915de-20260414T001639Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.78
fair_value_high: 0.84
fair_value_mid: 0.81
market_reference_price: 0.88
edge_mid_vs_market_pct_points: -7.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-17T23:59:00-04:00
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
- Primary crux: This still looks like a price-only repricing rather than a factual regime change: ETH remains likely to hit $2,400 during Apr 13-19 because Binance touch mechanics and the near-miss around 2395 make Yes genuinely favored, but 0.88 still prices the final last-mile move too close to automatic.
- One-sentence rationale: ETH is still likely to hit $2,400 during Apr 13-19 because Binance touch mechanics and the near-miss around 2395 make Yes genuinely favored, but the move down to 0.88 mainly compresses the prior under rather than proving the final last-mile move is automatic, so the disciplined posture remains watch-only.

## Why this is the right action / no-action call

This refresh remains bounded and lightweight; no new first-hand Binance path evidence was added, so the update is about market repricing rather than a changed underlying thesis.

## Valuation

- Fair value low: 0.78
- Fair value high: 0.84
- Fair value midpoint: 0.81
- Market reference price: 0.88
- Edge vs market (percentage points): -7.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: No new first-hand Binance path evidence was added in this light refresh, so the correct update is to keep the prior low-80s range broadly intact rather than follow the market higher or treat the repricing as decisive.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.62
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; materially cheaper pricing would require a fresh path check.
- `scaled_enter`
  - `min_p:` 0.62
  - `max_p:` 0.74
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the market remains richer than justified fair value.
- `hold`
  - `min_p:` 0.74
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with a high-probability Yes outcome but not enough edge for fresh adds.
- `trim`
  - `min_p:` 0.82
  - `max_p:` 0.92
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price rises above bounded fair value and residual path-failure risk dominates.
- `exit`
  - `min_p:` 0.92
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because even a near-touch market can still fail over the remaining window.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.06
- Allow auto reversal: `false`
- Quote staleness seconds: 7200
- Valid until: 2026-04-17T23:59:00-04:00
- Time horizon: Apr 13-19 Binance ETH/USDT intrawindow high-touch resolution

## Risk controls

- Max position size (% bankroll): 0.01
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 50
- Liquidity minimum depth: 1200
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the market remains above bounded fair value., Existing aligned exposure may be held, but refresh on any renewed test of the 2390s or crypto-wide reversal before adjusting., Treat short-dated threshold-touch markets as highly path-dependent even when the level is only a few dollars away.

## Invalidation

### Thesis breakers
- ETH fails to revisit the high-2300s and instead reverses materially lower.
- A verified Binance ETH/USDT 1-minute high at or above $2,400 immediately resolves the market and supersedes this packet.
- Fresh evidence shows a stronger-than-assumed resistance regime or crypto-wide risk-off impulse that materially lowers touch odds.

### Market structure breakers
- The market reprices materially again on new ETH path information before a fresh packet is produced.
- Short-term volatility or exchange-specific liquidity conditions change enough to invalidate the current near-touch calibration.
- Any Binance-specific pricing irregularity emerges that changes confidence in expected wick behavior.

### Time breakers
- A renewed retest of the 2390s can change the probability materially within hours.
- As the remaining window shortens, stale path assumptions should be refreshed rather than extrapolated.

### Reversal conditions
- Move toward authorized yes only after a fresh packet if ETH continues retesting the threshold while price remains favorable.
- Move materially lower if ETH rejects again and sells off away from the threshold.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the initial near-touch impulse converts into a qualifying Binance wick before Apr 19.
- How much short-dated resistance around $2,400 will persist after the first near-miss.
- Whether broader crypto sentiment remains supportive over the remaining window.

### Reasons to pass / stay small
- The market drop from 0.905 to 0.88 compresses but does not eliminate the prior valuation gap.
- The strongest surviving No path is still live and still matters economically at this price.
- The bounded evidence supports a high Yes probability but not a near-automatic outcome.

### What would change my mind
- A clean Binance print above $2,400 would obviously resolve the market Yes.
- Repeated renewed tests of the high-2390s without broader reversal would move fair value somewhat higher and could narrow the under further.
- A sharp ETH selloff away from the threshold or evidence of deteriorating momentum would move fair value lower.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh remains bounded and lightweight; no new first-hand Binance path evidence was added, so the update is about market repricing rather than a changed underlying thesis.

## Notes for downstream evaluator

This still looks like a price-only repricing rather than a factual regime change: ETH remains likely to hit $2,400 during Apr 13-19 because Binance touch mechanics and the near-miss around 2395 make Yes genuinely favored, but 0.88 still prices the final last-mile move too close to automatic.
