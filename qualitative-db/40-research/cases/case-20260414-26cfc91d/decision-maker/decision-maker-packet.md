---
type: decision_packet
case_key: case-20260414-26cfc91d
dispatch_id: dispatch-case-20260414-26cfc91d-20260414T181516Z
question: "Will FC Internazionale Milano win on 2026-04-17?"
market_id: e4997a9f-4abd-47ad-aafd-ff8249c228ec
external_market_id: 0xbae558b7842eea7e1897618ca33da728dbae0415880a4593bd13a712f45b1d9f
market_slug: sea-int-cag-2026-04-17-int
platform: polymarket
market_title: "Will FC Internazionale Milano win on 2026-04-17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-26cfc91d/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-26cfc91d/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.77
fair_value_high: 0.8
fair_value_mid: 0.785
market_reference_price: 0.815
edge_mid_vs_market_pct_points: -3.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: low
valid_until: 2026-04-15T18:24:04.383257+00:00
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
- Primary crux: Inter are still the deserved favorite, but in a regulation-only match where draw is a full loss and late lineup news can move true win probability materially, the bounded package is not strong enough to justify acting against an 81.5% market without a preserved bookmaker screen and final team-news confirmation.
- One-sentence rationale: Inter are likely the better side and probable winner, but without preserved late lineup confirmation and a broad bookmaker screen, the disciplined output is forbidden and needs-more-research rather than acting against an 81.5% regulation-win market.

## Why this is the right action / no-action call

This is a classic case where directional opinion exists but execution readiness does not; the missing late-match inputs matter more than the modest valuation gap.

## Valuation

- Fair value low: 0.77
- Fair value high: 0.8
- Fair value midpoint: 0.785
- Market reference price: 0.815
- Edge vs market (percentage points): -3.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Team-strength context supports Inter as a strong favorite, but absent a broad bookmaker screen and late lineup verification, fair value should stay only modestly below the market rather than implying an actionable anti-market edge.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.7
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized from this packet because the case is not decision-ready.
- `scaled_enter`
  - `min_p:` 0.7
  - `max_p:` 0.77
  - `target_exposure_fraction:` 0
  - `notes:` Even cheaper prices would still require refreshed lineup and odds verification.
- `hold`
  - `min_p:` 0.77
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair value zone, but not actionable under current evidence quality.
- `trim`
  - `min_p:` 0.8
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` Avoid increasing above fair value while draw risk and lineup uncertainty remain unresolved.
- `exit`
  - `min_p:` 0.9
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat/avoid at extreme prices because a regulation-only football market always retains real draw risk.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T18:24:04.383257+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not enter from this packet; reopen only after lineup and late availability news are confirmed closer to kickoff., Require an independently preserved broad bookmaker screen before treating a modest below-market view as tradable., Treat regulation-time draw risk as the main No path, not a minor tail.

## Invalidation

### Thesis breakers
- Confirmed Inter absences or rotation materially reduce attacking quality before kickoff.
- A preserved broad bookmaker screen shows consensus meaningfully higher than the current bounded fair value range.
- New opponent or fixture-status information changes match context or settlement interpretation.

### Market structure breakers
- Settlement wording is clarified in a way that differs from the assumed 90-minute-only mechanics.
- The current quote becomes stale relative to late bookmaker or lineup information.

### Time breakers
- Official starting lineups and late team-news should supersede this packet before kickoff.
- If no fresh verification is available near kickoff, this packet should not be used for action.

### Reversal conditions
- Move from forbidden to watch-only or authorized only after fresh lineup confirmation and a preserved odds screen support the same view.
- Move lower if key Inter attackers are unavailable or the market drifts against Inter on new information.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Final Inter lineup and key-attacker availability.
- True draw probability in this specific matchup relative to the market's implied view.
- Whether late bookmaker consensus would confirm or contradict the slight below-market assessment.

### Reasons to pass / stay small
- The bounded edge versus market is modest and could disappear on ordinary lineup updates.
- Critical late information was not independently preserved in the synthesis package.
- This is a regulation-only football market where draw risk is economically important.

### What would change my mind
- A clean late bookmaker screen and full-strength Inter lineup would move me closer to market and could upgrade readiness.
- Credible reports of rotation or absences would move fair value lower.
- Clarified settlement wording from the operator would reduce residual interpretation risk.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a classic case where directional opinion exists but execution readiness does not; the missing late-match inputs matter more than the modest valuation gap.

## Notes for downstream evaluator

Inter are still the deserved favorite, but in a regulation-only match where draw is a full loss and late lineup news can move true win probability materially, the bounded package is not strong enough to justify acting against an 81.5% market without a preserved bookmaker screen and final team-news confirmation.
