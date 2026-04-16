---
type: decision_packet
case_key: case-20260414-b6293fe0
dispatch_id: dispatch-case-20260414-b6293fe0-20260414T001837Z
question: "Will Bitcoin reach $74,000 April 13-19?"
market_id: case-20260414-b6293fe0
external_market_id: 0x7932ba47d328116e97bb3c037c2229aa61a00508a3b3be64fd3334050d085ff0
market_slug: will-bitcoin-reach-74k-april-13-19
platform: polymarket
market_title: "Will Bitcoin reach $74,000 April 13-19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-b6293fe0/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-b6293fe0/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.96
fair_value_high: 0.995
fair_value_mid: 0.98
market_reference_price: 0.89
edge_mid_vs_market_pct_points: 9.0
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
- Primary crux: This is overwhelmingly likely Yes because broad independent evidence indicates BTC traded above $74,000 during the relevant window and the contract only requires a qualifying Binance BTC/USDT 1-minute high, but without the archived exact Binance 1-minute candle in the bundle the residual uncertainty is operational rather than directional.
- One-sentence rationale: Bitcoin appears very likely to have already satisfied the $74,000 threshold under the contract's Binance 1-minute-high mechanics, so 0.89 looks below justified value, but because the reviewed bundle lacks the archived exact qualifying Binance candle the remaining risk is operational and the right posture is high-confidence but still audit-aware rather than pretending absolute certainty.

## Why this is the right action / no-action call

This packet is one of the rare cases where an extreme yes view is justified: the market, cross-venue evidence, and contract mechanics all point the same way, with the only meaningful residual tail coming from source-specific settlement proof rather than price-direction uncertainty.

## Valuation

- Fair value low: 0.96
- Fair value high: 0.995
- Fair value midpoint: 0.98
- Market reference price: 0.89
- Edge vs market (percentage points): 9.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Cross-venue and market-state evidence strongly support that the threshold was already hit in substance, but the lack of an archived direct qualifying Binance 1-minute candle keeps a small operational tail and prevents a full 0.99+ conviction estimate.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0.01
  - `notes:` Strong enter zone because the contract appears effectively already satisfied in substance and pricing would be far below justified value.
- `scaled_enter`
  - `min_p:` 0.86
  - `max_p:` 0.93
  - `target_exposure_fraction:` 0.006
  - `notes:` Still attractive if executable because the remaining risk is mostly settlement-source nuance.
- `hold`
  - `min_p:` 0.93
  - `max_p:` 0.975
  - `target_exposure_fraction:` 0.003
  - `notes:` Hold/add-light zone as price approaches high-confidence fair value.
- `trim`
  - `min_p:` 0.975
  - `max_p:` 0.992
  - `target_exposure_fraction:` 0.001
  - `notes:` Trim as residual operational tail dominates remaining upside.
- `exit`
  - `min_p:` 0.992
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because any remaining value is negligible relative to settlement-process tail risk.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.03
- Allow auto reversal: `false`
- Quote staleness seconds: 3600
- Valid until: 2026-04-16T23:59:00-04:00
- Time horizon: Apr 13-19 Binance BTC/USDT intrawindow high-touch resolution

## Risk controls

- Max position size (% bankroll): 0.01
- Max additional exposure (% bankroll): 0.003
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 40
- Liquidity minimum depth: 1500
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Fresh exposure is only appropriate if execution can still be obtained near the quoted market and no settlement dispute has emerged., Recheck the governing Binance 1-minute print or market status before sizing because residual risk is almost entirely operational., Do not rely on other venues or broader BTC/USD proxies if a source-specific settlement dispute appears.

## Invalidation

### Thesis breakers
- Direct Binance BTC/USDT 1-minute evidence shows no qualifying high at or above 74,000 in the relevant ET window.
- A legitimate Polymarket rules or settlement dispute establishes that broader venue prints do not map to a qualifying Binance print.
- An official market update or settlement notice contradicts the current high-confidence Yes interpretation.

### Market structure breakers
- The 0.89 quote is stale, crossed, or reflects a moment before the market incorporated the qualifying print.
- Execution venue status changes or liquidity disappears, eliminating practical ability to capture the edge.
- A rules-interpretation dispute emerges around ET windowing or qualifying candle methodology.

### Time breakers
- Once a direct Binance qualifying candle is archived or the market resolves, this packet should be replaced immediately.
- As the market reprices toward certainty, remaining value decays rapidly and operational tail dominates.

### Reversal conditions
- Move sharply lower only if direct Binance 1-minute evidence or official settlement guidance breaks against the current interpretation.
- Do not auto-reverse from this packet.
- Suspend fresh adds if a credible settlement-source dispute appears.

## Epistemic status

### Key uncertainties
- Whether the exact archived qualifying Binance BTC/USDT 1-minute candle can be produced from the reviewed bundle.
- Whether any edge-case settlement or source-of-truth dispute remains live despite broad evidence of a 74k+ print.
- Whether the 0.89 snapshot is temporally stale relative to the likely threshold hit.

### Reasons to pass / stay small
- Most remaining risk is operational rather than predictive, so execution quality depends on avoiding stale or already-collapsed prices.
- If the market has already functionally repriced to certainty elsewhere, the quoted edge may be less real than it appears.
- A missing direct archived Binance 1-minute artifact is a real auditability gap even when the substantive outcome looks decided.

### What would change my mind
- A direct archived Binance BTC/USDT 1-minute candle showing High >= 74000 would move confidence even closer to 0.995+ and reduce the remaining tail.
- Direct evidence that Binance never printed a qualifying 74000 high would cut fair value sharply.
- An official settlement clarification or dispute notice would materially change readiness and sizing.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet is one of the rare cases where an extreme yes view is justified: the market, cross-venue evidence, and contract mechanics all point the same way, with the only meaningful residual tail coming from source-specific settlement proof rather than price-direction uncertainty.

## Notes for downstream evaluator

This is overwhelmingly likely Yes because broad independent evidence indicates BTC traded above $74,000 during the relevant window and the contract only requires a qualifying Binance BTC/USDT 1-minute high, but without the archived exact Binance 1-minute candle in the bundle the residual uncertainty is operational rather than directional.
