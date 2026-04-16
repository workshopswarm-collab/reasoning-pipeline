---
type: decision_packet
case_key: case-20260416-d529376c
dispatch_id: refresh-case-20260416-d529376c-20260416T031241Z
question: "Will the price of Solana be above $80 on April 19?"
market_id: 139f80d9-bf3b-4b6b-9dea-031313b6ae5b
external_market_id: 0x00b28e37776a7f2f56ceec3bc4cf4f49d832b1c9db1ddd1cb597fb4438918f95
market_slug: solana-above-80-on-april-19
platform: polymarket
market_title: "Will the price of Solana be above $80 on April 19?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260416-d529376c/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-d529376c/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path: qualitative-db/40-research/cases/case-20260416-d529376c/decision-maker/refreshes/refresh-case-20260416-d529376c-20260416T031241Z/light-refresh-brief.json
refresh_mode: light
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.82
fair_value_high: 0.88
fair_value_mid: 0.85
market_reference_price: 0.92
edge_mid_vs_market_pct_points: -7.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-17T03:13:36.976332+00:00
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
- Trade authorization: `forbidden`
- Position policy: `flat`
- Decision readiness: `needs_more_research`
- Primary crux: The move from 0.915 to 0.92 is best treated as repricing rather than a broken thesis: SOL above $80 on the April 19 noon ET Binance minute remains the directional base case because spot is still in the mid-85s, but the bounded package still explicitly says blockers_require_new_research is yes, so the richer market only worsens execution economics rather than making the case more tradable.
- One-sentence rationale: SOL above $80 on April 19 remains the directional base case, but because this bounded package still explicitly requires more research on volatility calibration and near-settlement confirmation, the correct output remains forbidden and flat, and the move from 0.915 to 0.92 only worsens execution economics.

## Why this is the right action / no-action call

This refresh is repricing, not regime change: same strong Yes lean, same not-ready status, worse price.

## Valuation

- Fair value low: 0.82
- Fair value high: 0.88
- Fair value midpoint: 0.85
- Market reference price: 0.92
- Edge vs market (percentage points): -7.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Current SOL/USDT cushion supports a strong Yes lean, but fair value remains below market and is pulled toward it because downside-tail calibration and settlement-minute execution risk are only medium verified.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.76
  - `target_exposure_fraction:` 0
  - `notes:` Not actionable from this packet; would require materially stronger verification and a much cheaper price.
- `scaled_enter`
  - `min_p:` 0.76
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0
  - `notes:` Potential value zone only after new research resolves the stated blockers.
- `hold`
  - `min_p:` 0.82
  - `max_p:` 0.88
  - `target_exposure_fraction:` 0
  - `notes:` Current bounded fair-value zone, but action remains forbidden because package-level blockers require new research.
- `trim`
  - `min_p:` 0.88
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0
  - `notes:` Above fair value for a single-minute crypto settlement with unresolved downside-tail verification.
- `exit`
  - `min_p:` 0.94
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Avoid near-certainty pricing absent stronger proof that settlement-minute downside risk is negligible.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-17T03:13:36.976332+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate or add exposure from this packet., Require renewed research on downside-volatility calibration and a fresher near-settlement Binance check before reconsidering action., Treat exact-minute Binance path risk as the dominant execution constraint.

## Invalidation

### Thesis breakers
- SOL/USDT loses substantial cushion and trades back toward 80 before settlement.
- A broad crypto selloff, Solana-specific shock, or exchange-specific issue materially raises the probability of a sub-80 settlement minute.
- Binance-specific settlement-surface, pricing, or operational issues emerge near resolution.

### Market structure breakers
- Market reprices materially after fresh spot or volatility changes, altering the economic comparison.
- New evidence clarifies or worsens the Binance ET-noon minute mapping or settlement-surface behavior.

### Time breakers
- A fresh pre-settlement packet with improved volatility calibration and direct Binance verification should supersede this judgment.
- The actual April 19 12:00 ET Binance 1-minute close fully resolves and obsoletes this packet.

### Reversal conditions
- Move to ready/watch-only or better only if new research resolves the stated blockers on volatility calibration and near-settlement Binance confirmation.
- Downgrade directional confidence if SOL loses its current cushion materially.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- How much probability should be assigned to a roughly 6% downside move into one exact settlement minute over the remaining horizon.
- Whether a crypto-wide risk-off move emerges before April 19.
- Whether the residual Binance minute-mapping implementation risk is fully immaterial in practice.

### Reasons to pass / stay small
- The package explicitly says blockers_require_new_research is yes.
- The market repriced higher without adding stronger evidence.
- Low-90s pricing in a single-minute crypto threshold market still requires stronger proof than this bounded package provides.

### What would change my mind
- Independent evidence that downside volatility into the settlement minute is lower than currently assumed would improve actionability.
- A materially cheaper market price with unchanged cushion and better settlement-surface confidence would improve the trade case.
- A move down toward the low 80s would reduce even the directional Yes confidence.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This refresh is repricing, not regime change: same strong Yes lean, same not-ready status, worse price.

## Notes for downstream evaluator

The move from 0.915 to 0.92 is best treated as repricing rather than a broken thesis: SOL above $80 on the April 19 noon ET Binance minute remains the directional base case because spot is still in the mid-85s, but the bounded package still explicitly says blockers_require_new_research is yes, so the richer market only worsens execution economics rather than making the case more tradable.
