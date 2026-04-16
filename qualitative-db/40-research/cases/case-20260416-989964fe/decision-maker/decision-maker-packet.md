---
type: decision_packet
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
question: "Will the price of Ethereum be above $2,200 on April 17?"
market_id: 30172bb7-9f35-4ca6-93a4-adb8544ba07a
external_market_id: 0x99eb86c2cf41bbf90f3df2f839525c317790ad8b8024f55a80c997255e8787f7
market_slug: ethereum-above-2200-on-april-17
platform: polymarket
market_title: "Will the price of Ethereum be above $2,200 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260416-989964fe/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-989964fe/synthesizer-agent/syndicated-finding.md
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
valid_until: 2026-04-17T02:14:03.706142+00:00
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
- Primary crux: ETH above $2,200 on the April 17 noon ET Binance minute remains the strong base case because current spot is roughly 7% above strike and the contract mechanics are now clear, but a 0.955 market price still overstates confidence for a single-minute, single-venue crypto threshold contract with overnight and morning tail risk still live.
- One-sentence rationale: ETH above $2,200 on the April 17 Binance noon minute remains the strong base case, but with fair value around 0.925 and the market at 0.955, the disciplined output stays watch-only because near-certainty pricing still overstates confidence in a single-minute crypto settlement.

## Why this is the right action / no-action call

Compared with earlier packets, contract clarity improved, but the economic conclusion did not: strong directional Yes, poor execution price.

## Valuation

- Fair value low: 0.91
- Fair value high: 0.94
- Fair value midpoint: 0.925
- Market reference price: 0.955
- Edge vs market (percentage points): -3.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current Binance ETH/USDT context strongly supports Yes and contract ambiguity is no longer material, but bounded verification still does not justify paying a near-certainty price for a single-minute venue-specific settlement.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.84
  - `target_exposure_fraction:` 0
  - `notes:` Would require an unusually large dislocation versus this packet's high Yes base case.
- `scaled_enter`
  - `min_p:` 0.84
  - `max_p:` 0.91
  - `target_exposure_fraction:` 0
  - `notes:` Potential value zone if ETH remains comfortably above strike and no new settlement-surface issues appear.
- `hold`
  - `min_p:` 0.91
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.94
  - `max_p:` 0.97
  - `target_exposure_fraction:` 0
  - `notes:` Above fair value for a one-minute crypto settlement with residual path risk.
- `exit`
  - `min_p:` 0.97
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Avoid or exit at near-certainty pricing because even a brief downside move can flip the result.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-17T02:14:03.706142+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current market price., Treat exact-minute Binance settlement risk as the dominant execution constraint even with a strong directional Yes view., Reopen only if market cheapens materially or if a near-settlement Binance check preserves a large cushion above 2200.

## Invalidation

### Thesis breakers
- ETH/USDT moves materially closer to 2200 or below it before the Apr 17 fixing window.
- A bearish macro, crypto, or exchange-specific shock materially raises the probability of a sub-2200 settlement minute.
- Binance-specific pricing, liquidity, or operational issues emerge near resolution.

### Market structure breakers
- Market reprices materially after fresh spot or volatility changes, altering the value comparison.
- Unexpected Binance-specific minute-close behavior appears near the fixing window.

### Time breakers
- A fresh direct Binance observation on Apr 17 morning should supersede this packet before any action.
- The actual Apr 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if later pre-fix Binance checks still show a wide cushion above 2200 and the market price cheapens below fair value.
- Downgrade if ETH loses substantial cushion or volatility rises materially.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the current cushion above 2200 survives the exact settlement minute.
- Whether overnight or U.S.-morning shocks emerge before the fixing window.
- How much residual venue-specific tail risk should still be charged despite clear contract wording.

### Reasons to pass / stay small
- The market price is above bounded fair value.
- The contract resolves on one exact Binance minute rather than broad daily direction.
- The remaining edge is too small and too fragile to justify paying 0.955.

### What would change my mind
- A fresh near-settlement Binance check still showing ETH comfortably above 2200 with stable conditions would modestly improve confidence.
- A materially cheaper market price with unchanged cushion would improve the execution case.
- A fast move toward 2300 or below would reduce directional confidence materially.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: Compared with earlier packets, contract clarity improved, but the economic conclusion did not: strong directional Yes, poor execution price.

## Notes for downstream evaluator

ETH above $2,200 on the April 17 noon ET Binance minute remains the strong base case because current spot is roughly 7% above strike and the contract mechanics are now clear, but a 0.955 market price still overstates confidence for a single-minute, single-venue crypto threshold contract with overnight and morning tail risk still live.
