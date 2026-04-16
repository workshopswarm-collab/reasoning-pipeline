---
type: decision_packet
case_key: case-20260413-e2ee488e
dispatch_id: dispatch-case-20260413-e2ee488e-20260413T222544Z
question: "Will the price of Bitcoin be above $70,000 on April 15?"
market_id: case-20260413-e2ee488e
external_market_id: 0x5687ed31630b7f74c281562c52cf56ea1385fd249688c71eba96b62a6e8a8c26
market_slug: bitcoin-above-70k-on-april-15
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 15?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-e2ee488e/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-e2ee488e/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.9
fair_value_high: 0.94
fair_value_mid: 0.92
market_reference_price: 0.945
edge_mid_vs_market_pct_points: -2.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-15T10:30:00-04:00
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
- Primary crux: BTC is materially above the 70k strike and the main remaining path to No is a short-horizon one-minute settlement tail, so Yes remains the correct directional call, but the market's 94.5% price is already slightly richer than the bounded evidence justifies.
- One-sentence rationale: BTC remains likely to settle above 70k on the Apr. 15 noon ET Binance minute because spot is materially above strike, but the market's 94.5% price already slightly overstates what the bounded evidence supports, so the disciplined posture is watch-only rather than chasing Yes.

## Why this is the right action / no-action call

This packet is decision-ready in the sense that the directional call is clear and the main blocker is pricing rather than missing core facts, but execution remains sensitive to fresh pre-settlement venue verification.

## Valuation

- Fair value low: 0.9
- Fair value high: 0.94
- Fair value midpoint: 0.92
- Market reference price: 0.945
- Edge vs market (percentage points): -2.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: The bounded evidence already supports a very high Yes probability, but one-minute settlement fragility and residual downside-tail risk keep fair value modestly below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.7
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; a much cheaper price would require a fresh venue check.
- `scaled_enter`
  - `min_p:` 0.7
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the current bounded packet is a hold/watch posture, not a fresh-add authorization.
- `hold`
  - `min_p:` 0.86
  - `max_p:` 0.93
  - `target_exposure_fraction:` 0
  - `notes:` Hold zone consistent with a high-probability Yes outcome but limited remaining edge.
- `trim`
  - `min_p:` 0.93
  - `max_p:` 0.97
  - `target_exposure_fraction:` 0
  - `notes:` Trim or avoid increasing as price moves above the upper end of justified fair value.
- `exit`
  - `min_p:` 0.97
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because exact-minute settlement tail risk still exists.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.05
- Allow auto reversal: `false`
- Quote staleness seconds: 3600
- Valid until: 2026-04-15T10:30:00-04:00
- Time horizon: Now through the Apr. 15 12:00 ET Binance settlement minute

## Risk controls

- Max position size (% bankroll): 0.01
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 40
- Liquidity minimum depth: 1500
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate new exposure from this packet because the market is already at or above bounded fair value., Existing aligned exposure may be held, but refresh Binance spot and resolution mechanics close to settlement before any adjustment., Treat single-minute venue-specific crypto settlement markets as timing-sensitive even when spot is comfortably above strike.

## Invalidation

### Thesis breakers
- Fresh Binance price action breaks below 70k or erodes most of the current cushion before settlement.
- A macro or crypto-specific shock meaningfully raises short-horizon downside volatility into the noon ET minute.
- A Binance-specific pricing or operational irregularity makes venue-specific settlement risk more important than currently assumed.

### Market structure breakers
- The market reprices materially on new information before a fresh venue check can be performed.
- Adjacent strike or related market pricing implies a different short-horizon distribution than currently assumed.
- Clarification of Binance chart/UI versus API settlement behavior reveals a meaningful mechanical discrepancy.

### Time breakers
- A fresh pre-settlement Binance verification becomes mandatory as the contract approaches the final settlement window.
- Apr. 15 morning data or headline flow can change the probability materially within hours.

### Reversal conditions
- Move toward authorization only on a fresh packet after renewed Binance verification still shows a comfortable buffer and favorable pricing.
- Move materially lower if BTC trades repeatedly near 70k or the downside volatility regime worsens.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Exact Binance price path and realized volatility into the settlement minute.
- Residual macro or crypto-specific shock risk before Apr. 15 noon ET.
- Whether Binance-specific chart/UI behavior at settlement introduces any small operational discrepancy versus broader market prints.

### Reasons to pass / stay small
- The market is already slightly above bounded fair value, so there is little or no remaining edge.
- Single-minute settlement contracts retain meaningful tail risk even with current spot above strike.
- A fresher pre-settlement venue check would matter before any live execution decision.

### What would change my mind
- A fresh Binance check close to settlement showing BTC still comfortably above 70k with stable volatility would increase confidence but not necessarily create edge at the current price.
- A sharp move down toward 71k-72k or rising downside volatility would lower fair value materially.
- Any meaningful Binance-specific settlement irregularity would reduce confidence in the current high-Yes estimate.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet is decision-ready in the sense that the directional call is clear and the main blocker is pricing rather than missing core facts, but execution remains sensitive to fresh pre-settlement venue verification.

## Notes for downstream evaluator

BTC is materially above the 70k strike and the main remaining path to No is a short-horizon one-minute settlement tail, so Yes remains the correct directional call, but the market's 94.5% price is already slightly richer than the bounded evidence justifies.
