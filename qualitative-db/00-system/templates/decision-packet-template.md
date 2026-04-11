---
type: decision_packet
case_key:
dispatch_id:
question:
market_id:
market_title:
source_decision_handoff_path:
source_syndicated_finding_path:
recommended_side:
trade_authorization:
position_policy:
decision_readiness:
fair_value_low:
fair_value_high:
fair_value_mid:
market_reference_price:
edge_mid_vs_market_pct_points:
independent_verification_quality:
compressed_toward_market_applied:
decision_confidence:
valid_until:
tags: []
---

# Decision packet

Use this template for the Decision-Maker's final executable recommendation after reviewing synthesis.

Pipeline position:
- upstream = researcher swarm -> synthesis -> `decision-handoff.md`
- this artifact = Decision-Maker's final commitment object
- downstream = isolated execution, accounting, evaluator, retrospective review

Purpose:
- convert uncertain research into explicit action / no-action thresholds
- optimize for long-run prediction-market performance
- preserve risk discipline and auditability
- make PASS / WAIT / FLAT outputs just as valid as ACT when edge is weak or unverified

Canonical machine-readable contract:
- `decision-packet.schema.json`

Recommended usage:
- keep the JSON packet as the canonical machine-readable execution contract
- use this markdown file as the human-readable twin for operators, audits, and retrospectives

## Authoring rules

- Optimize for expected value, calibration, risk discipline, and auditability.
- Use the proposition's market-implied true-probability axis for all price bands, even when recommending `NO`.
- Define executable thresholds, not vague prose.
- Respect market baselines and base rates; large claimed edges need stronger proof.
- Do not manufacture activity just because the pipeline spent tokens or effort upstream.
- A correct packet may recommend `watch_only`, `risk_reduce_only`, `forbidden`, or `flat`.
- Every packet must expire with `valid_until` or an equivalent hard review trigger.
- If automated reversal from one side to the other is not explicitly allowed, require flattening first.

## Decision summary

- Side: `YES | NO | NONE`
- Trade authorization: `authorized | watch_only | risk_reduce_only | forbidden`
- Position policy: `enter_or_add | hold_only | reduce_only | exit_only | flat`
- Decision readiness: `ready | needs_more_research | needs_market_update`
- Primary crux:
- One-sentence rationale:

## Why this is the right action / no-action call

State clearly:
- why acting improves expected value, or
- why passing / waiting is the higher-EV choice right now

## Valuation

- Fair value low:
- Fair value high:
- Fair value midpoint:
- Market reference price:
- Edge vs market (percentage points):
- Independent verification quality: `low | medium | high`
- Compressed toward market applied: `true | false`
- Compression reason:

## Action bands

Define deterministic bands on the market-implied true-probability axis.
Bands should fully cover `[0,1]` with no gaps or overlaps.

Use the canonical band names below and map each one to a target fraction of `max_position_size_pct_bankroll`.

- `max_enter`
  - `min_p:`
  - `max_p:`
  - `target_exposure_fraction:`
  - `notes:`
- `scaled_enter`
  - `min_p:`
  - `max_p:`
  - `target_exposure_fraction:`
  - `notes:`
- `hold`
  - `min_p:`
  - `max_p:`
  - `target_exposure_fraction:`
  - `notes:`
- `trim`
  - `min_p:`
  - `max_p:`
  - `target_exposure_fraction:`
  - `notes:`
- `exit`
  - `min_p:`
  - `max_p:`
  - `target_exposure_fraction:`
  - `notes:`

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `effective_executable_quote | market_snapshot_quote`
- Rebalance threshold fraction:
- Allow auto reversal: `true | false`
- Quote staleness seconds:
- Valid until:
- Time horizon:

## Risk controls

- Max position size (% bankroll):
- Max additional exposure (% bankroll):
- Max single order (% bankroll):
- Slippage tolerance (bps):
- Liquidity minimum depth:
- Correlation bucket limit (% bankroll):
- Confidence level: `low | medium | high`
- Portfolio constraints:

## Invalidation

### Thesis breakers
- 

### Market structure breakers
- 

### Time breakers
- 

### Reversal conditions
- 

## Epistemic status

### Key uncertainties
- 

### Reasons to pass / stay small
- 

### What would change my mind
- 

### Decision quality
- `clean | good_not_clean | fragile | not_ready`

## Audit checks

- Market baseline respected: `true | false`
- Action bias check passed: `true | false`
- Self-preservation bias check passed: `true | false`
- Additional notes:

## Notes for downstream evaluator

State what should later be judged most harshly:
- Was the fair value estimate wrong?
- Was the edge real but too small to clear costs/risk?
- Was the sizing wrong?
- Was the invalidation logic too slow or too brittle?
- Was PASS the correct call even if the market later moved?
