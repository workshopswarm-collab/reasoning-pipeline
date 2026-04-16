---
type: decision_packet
case_key: case-20260415-33c2f26e
dispatch_id: dispatch-case-20260415-33c2f26e-20260415T211658Z
question: "Will Al Nassr Saudi Club win on 2026-04-24?"
market_id: 582d73c0-f48c-4a83-ade9-60f2e5f69f6d
external_market_id: 0x3c868c63869036d68a224d1321dcfaec415c672bacee771e42113d3267b48e1a
market_slug: spl-nsr-ett-2026-04-24-nsr
platform: polymarket
market_title: "Will Al Nassr Saudi Club win on 2026-04-24?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-33c2f26e/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-33c2f26e/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.85
fair_value_high: 0.89
fair_value_mid: 0.87
market_reference_price: 0.915
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T21:50:27.943861+00:00
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
- Primary crux: Al Nassr is the deserved favorite on baseline strength, but a 0.915 regulation-win market is too extreme to trade against or with confidence without a clean bookmaker 1X2 consensus and fixture-specific lineup confirmation, especially because ordinary soccer draw risk alone keeps high-80s fair value plausible.
- One-sentence rationale: Al Nassr should be favored, but with fair value centered near 0.87 versus a 0.915 market and no fresh bookmaker or lineup validation, the correct packet is forbidden and needs_more_research rather than a trade on a regulation-only soccer favorite.

## Why this is the right action / no-action call

This case is a calibration-sensitive favorite-price question where missing late-market and lineup evidence is economically decisive.

## Valuation

- Fair value low: 0.85
- Fair value high: 0.89
- Fair value midpoint: 0.87
- Market reference price: 0.915
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Baseline team-strength evidence supports Al Nassr as a strong favorite, but no independent near-kickoff odds or lineup confirmation was secured to justify a stronger conclusion about whether 0.915 is too rich.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.78
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price plus fresh lineup and market validation.
- `scaled_enter`
  - `min_p:` 0.78
  - `max_p:` 0.85
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if late team news remains favorable and independent consensus supports Al Nassr strongly.
- `hold`
  - `min_p:` 0.85
  - `max_p:` 0.89
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone from current reasoning, but current packet remains non-actionable due freshness and validation gaps.
- `trim`
  - `min_p:` 0.89
  - `max_p:` 0.95
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a regulation-only soccer favorite with unresolved lineup and pricing validation.
- `exit`
  - `min_p:` 0.95
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid entirely at very rich prices unless late information becomes unusually favorable and independently confirmed.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T21:50:27.943861+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add exposure at the current price., Require a fresh bookmaker 1X2 consensus and lineup/injury confirmation before reconsidering action., Treat regulation-only draw variance as a binding constraint when pricing extreme soccer favorites.

## Invalidation

### Thesis breakers
- Confirmed adverse Al Nassr lineup, absences, or motivational weakness before kickoff.
- A strong independent bookmaker consensus materially above or below the current valuation range.
- Material pre-match news changing expected team strength or match context.

### Market structure breakers
- Market reprices materially after team news, changing the value comparison.
- Evidence emerges that the expected fixture or full-time settlement framing differs from the assumed standard regulation-only win market.

### Time breakers
- A fresh close-to-kickoff lineup and sharp-consensus check should supersede this packet before any action.
- The official full-time result of the scheduled match fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade from forbidden only if fresh lineup/injury and bookmaker-consensus checks materially improve confidence or the market cheapens enough to create a clear edge.
- Downgrade directional confidence if Al Nassr lineup strength or motivation is weaker than baseline.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Al Nassr's actual lineup strength and availability close to kickoff.
- Whether bookmaker or sharp consensus validates or contradicts a 91.5% regulation-win price.
- How much regulation-only draw risk should be charged in this exact fixture context.

### Reasons to pass / stay small
- The market is already above bounded fair value.
- No independently verified bookmaker 1X2 consensus near kickoff was obtained.
- No clean fixture-specific lineup/injury confirmation was obtained, and the edge is too fragile to survive ordinary soccer uncertainty.

### What would change my mind
- A verified strong Al Nassr lineup and consensus odds near the market would move me materially closer to market.
- A verified weakened lineup or materially lower bookmaker consensus would strengthen the below-market view.
- A materially cheaper market price with unchanged favorable team news would create a cleaner edge.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This case is a calibration-sensitive favorite-price question where missing late-market and lineup evidence is economically decisive.

## Notes for downstream evaluator

Al Nassr is the deserved favorite on baseline strength, but a 0.915 regulation-win market is too extreme to trade against or with confidence without a clean bookmaker 1X2 consensus and fixture-specific lineup confirmation, especially because ordinary soccer draw risk alone keeps high-80s fair value plausible.
