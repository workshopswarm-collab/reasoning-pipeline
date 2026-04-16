---
type: decision_packet
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
question: "Will the price of Bitcoin be above $72,000 on April 17?"
market_id: 34b19a2f-03db-4e0f-ba94-a0ddb3b0670c
external_market_id: 0x278e937ecb8ff1da49c4e04aba52d1922b3e0a7a15d09e621bbf33154c230287
market_slug: bitcoin-above-72k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260416-b08a3934/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-b08a3934/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.87
fair_value_high: 0.9
fair_value_mid: 0.885
market_reference_price: 0.93
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-17T02:48:12.756854+00:00
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
- Primary crux: BTC above $72,000 on the April 17 noon ET Binance minute is the directional base case because spot and the recent 24h low both sit above strike, but the bounded package explicitly says blockers_require_new_research is yes, and that should dominate in an exact-minute, exchange-specific contract where the main remaining issue is the unverified pre-settlement morning path.
- One-sentence rationale: BTC above $72,000 on April 17 is still the directional base case, but because this bounded package explicitly requires new research on the final morning path and settlement-surface confidence, the correct output is forbidden and flat rather than trading a modest below-market view at 0.93.

## Why this is the right action / no-action call

This is another case where directional truth and execution readiness diverge: strong Yes lean, but not decision-ready.

## Valuation

- Fair value low: 0.87
- Fair value high: 0.9
- Fair value midpoint: 0.885
- Market reference price: 0.93
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Current BTC/USDT cushion strongly supports Yes, but the remaining exact-minute and settlement-surface risks are not sufficiently resolved for an executable valuation call.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.82
  - `target_exposure_fraction:` 0
  - `notes:` Not actionable from this packet; would require materially stronger verification and a much cheaper price.
- `scaled_enter`
  - `min_p:` 0.82
  - `max_p:` 0.87
  - `target_exposure_fraction:` 0
  - `notes:` Potential value zone only after new research resolves the stated blockers.
- `hold`
  - `min_p:` 0.87
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` Current bounded fair-value zone, but action remains forbidden because package-level blockers require new research.
- `trim`
  - `min_p:` 0.9
  - `max_p:` 0.95
  - `target_exposure_fraction:` 0
  - `notes:` Above fair value for a single-minute crypto settlement with unresolved final-morning verification risk.
- `exit`
  - `min_p:` 0.95
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Avoid near-certainty pricing absent stronger proof that exact-minute downside risk is negligible.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-17T02:48:12.756854+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate or add exposure from this packet., Require a fresh pre-settlement Binance check and clearer settlement-surface confidence before reconsidering action., Treat exact-minute Binance path risk as the dominant execution constraint.

## Invalidation

### Thesis breakers
- BTC/USDT loses substantial cushion and trades back toward 72,000 before settlement.
- A downside macro, crypto, or exchange-specific shock materially raises the probability of a sub-72,000 settlement minute.
- Binance-specific settlement-surface, pricing, or operational issues emerge near resolution.

### Market structure breakers
- Market reprices materially after fresh spot or volatility changes, altering the economic comparison.
- New evidence clarifies or worsens the Binance UI-versus-API settlement mapping.

### Time breakers
- A fresh pre-settlement packet with direct morning Binance verification should supersede this judgment.
- The actual April 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this packet.

### Reversal conditions
- Move to ready/watch-only or better only if new research resolves the stated blockers on final-morning verification and settlement-surface confidence.
- Downgrade directional confidence if BTC loses its current cushion materially.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- How much probability should be assigned to a 4%+ downside move into one exact settlement minute over the remaining horizon.
- Whether the final pre-settlement Binance morning path confirms the current cushion or erodes it materially.
- Whether the residual Binance UI-versus-API settlement-surface gap is fully immaterial in practice.

### Reasons to pass / stay small
- The package explicitly says blockers_require_new_research is yes.
- The valuation gap versus market is modest relative to unresolved exact-minute execution risk.
- Low-90s pricing in a single-minute crypto threshold market requires stronger proof than this bounded package provides.

### What would change my mind
- A direct near-settlement Binance check still showing BTC comfortably above 72,000 would improve actionability.
- A materially cheaper market price with unchanged cushion and better settlement-surface confidence would improve the trade case.
- A move back toward 72,000 would reduce even the directional Yes confidence.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is another case where directional truth and execution readiness diverge: strong Yes lean, but not decision-ready.

## Notes for downstream evaluator

BTC above $72,000 on the April 17 noon ET Binance minute is the directional base case because spot and the recent 24h low both sit above strike, but the bounded package explicitly says blockers_require_new_research is yes, and that should dominate in an exact-minute, exchange-specific contract where the main remaining issue is the unverified pre-settlement morning path.
