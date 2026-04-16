---
type: decision_packet
case_key: case-20260415-65ec5d99
dispatch_id: dispatch-case-20260415-65ec5d99-20260415T210454Z
question: "Will Real Madrid CF win on 2026-04-21?"
market_id: 09869589-771a-4a3b-bbd2-2d4108886e72
external_market_id: 0x062918e2e53609c5eecbc396b65d714fe72dfff5e4829f5de83a71391e89c358
market_slug: lal-rea-ala-2026-04-21-rea
platform: polymarket
market_title: "Will Real Madrid CF win on 2026-04-21?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-65ec5d99/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-65ec5d99/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.74
fair_value_high: 0.78
fair_value_mid: 0.76
market_reference_price: 0.765
edge_mid_vs_market_pct_points: -0.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T21:15:01.355251+00:00
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
- Primary crux: Real Madrid should be favored to beat Alavés on baseline team quality, but the market at 0.765 is already near the middle of the bounded fair-value range and the remaining uncertainty is exactly the kind that matters most in soccer favorites—late lineup, rotation, motivation, and regulation-only draw risk—without an independently verified late-team-news or sharp-consensus check.
- One-sentence rationale: Real Madrid should be favored, but with fair value centered near 0.76 versus a 0.765 market and no fresh lineup or bookmaker-consensus validation, the correct packet is forbidden and needs_more_research rather than a marginal watch-only bet on a regulation-only soccer favorite.

## Why this is the right action / no-action call

This case is broadly market-consistent and too freshness-sensitive for action without late-team-news confirmation.

## Valuation

- Fair value low: 0.74
- Fair value high: 0.78
- Fair value midpoint: 0.76
- Market reference price: 0.765
- Edge vs market (percentage points): -0.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Baseline quality and home-field context support Real Madrid as deserved favorites, but no late lineup or bookmaker-consensus verification was obtained to justify a stronger move away from the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.68
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price plus fresh lineup and market validation.
- `scaled_enter`
  - `min_p:` 0.68
  - `max_p:` 0.74
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if late team news remains favorable and independent consensus supports Madrid.
- `hold`
  - `min_p:` 0.74
  - `max_p:` 0.78
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; current packet remains non-actionable due freshness and validation gaps.
- `trim`
  - `min_p:` 0.78
  - `max_p:` 0.85
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a regulation-only soccer favorite with unresolved lineup uncertainty.
- `exit`
  - `min_p:` 0.85
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid entirely at rich prices unless late information becomes unusually favorable and independently confirmed.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T21:15:01.355251+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add exposure at the current price., Require a fresh lineup/injury and bookmaker-consensus check before reconsidering action., Treat regulation-only draw variance as a binding constraint when pricing soccer favorites.

## Invalidation

### Thesis breakers
- Confirmed heavy Real Madrid rotation, key absences, or reduced league incentive before kickoff.
- A strong independent bookmaker consensus materially below the current market.
- Material pre-match news improving Alavés relative strength or reducing Real Madrid's win probability.

### Market structure breakers
- Market reprices materially after team news, changing the value comparison.
- Evidence emerges that the expected fixture context or settlement framing differs from the assumed standard full-time match result.

### Time breakers
- A fresh close-to-kickoff lineup and sharp-consensus check should supersede this packet before any action.
- The official full-time result of the scheduled match fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade from forbidden only if fresh lineup/injury and bookmaker-consensus checks materially improve confidence or the market cheapens enough to create a clear edge.
- Downgrade directional confidence if Real Madrid's lineup strength or motivation is weaker than baseline.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Real Madrid's actual lineup strength and rotation choice close to kickoff.
- Whether bookmaker or sharp consensus would validate or contradict the current market price.
- How much regulation-only draw risk should be charged in this exact match context.

### Reasons to pass / stay small
- The market is already near bounded fair value.
- No independently verified late lineup/injury picture was obtained.
- No independent sharp/bookmaker consensus check was obtained, and the edge is too small to survive ordinary soccer uncertainty.

### What would change my mind
- A verified strong Real Madrid lineup with normal motivation would move me toward market or slightly above it.
- A verified weakened lineup or rotation-heavy approach would move me below the current range.
- A materially cheaper market price with unchanged favorable team news would create a cleaner edge.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This case is broadly market-consistent and too freshness-sensitive for action without late-team-news confirmation.

## Notes for downstream evaluator

Real Madrid should be favored to beat Alavés on baseline team quality, but the market at 0.765 is already near the middle of the bounded fair-value range and the remaining uncertainty is exactly the kind that matters most in soccer favorites—late lineup, rotation, motivation, and regulation-only draw risk—without an independently verified late-team-news or sharp-consensus check.
