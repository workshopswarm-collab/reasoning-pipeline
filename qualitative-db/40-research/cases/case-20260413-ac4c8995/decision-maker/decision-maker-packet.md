---
type: decision_packet
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
question: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
market_id: case-20260413-ac4c8995
external_market_id: 0x18a6cd68c80f4838ed7916ef826f5cab501aba0c30588cf06c9a44fac018e84d
market_slug: will-united-left-bsp-win-at-least-one-seat-in-the-2026-bulgarian-parliamentary-election
platform: polymarket
market_title: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-ac4c8995/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-ac4c8995/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: needs_more_research
fair_value_low: 0.64
fair_value_high: 0.74
fair_value_mid: 0.69
market_reference_price: 0.735
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: low
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
- Decision readiness: `needs_more_research`
- Primary crux: United Left (BSP) is still more likely than not to win at least one seat because it is described as an existing parliamentary bloc that previously cleared the 4% threshold, but the unresolved CIK entity-mapping issue and lack of fresh threshold-sensitive polling make the case too fragile and too close to market for authorization.
- One-sentence rationale: United Left (BSP) is probably more likely than not to win at least one seat, but because the case sits close to market and remains highly sensitive to unresolved CIK entity mapping and late threshold evidence, the disciplined output is watch-only and needs-more-research rather than an authorized trade.

## Why this is the right action / no-action call

This packet intentionally separates directional judgment from execution readiness: the bounded evidence supports a modest yes lean, but not a clean, auditable, threshold-safe authorization.

## Valuation

- Fair value low: 0.64
- Fair value high: 0.74
- Fair value midpoint: 0.69
- Market reference price: 0.735
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: The bounded evidence already clusters close to the market, and the dominant problem is unresolved verification on threshold survival and entity mapping rather than a large valuation disagreement.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.2
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the case is not decision-ready despite a directional yes lean.
- `scaled_enter`
  - `min_p:` 0.2
  - `max_p:` 0.5
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized until entity mapping and threshold verification improve.
- `hold`
  - `min_p:` 0.5
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0
  - `notes:` Hold/watch zone; directionally yes but not clean enough for fresh adds.
- `trim`
  - `min_p:` 0.72
  - `max_p:` 0.85
  - `target_exposure_fraction:` 0
  - `notes:` Avoid adding above roughly fair value given threshold fragility and unresolved mapping risk.
- `exit`
  - `min_p:` 0.85
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at expensive prices because small late moves can still produce a zero-seat outcome.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.12
- Allow auto reversal: `false`
- Quote staleness seconds: 21600
- Valid until: 2026-04-16T23:59:00-04:00
- Time horizon: Through election day and official seat allocation

## Risk controls

- Max position size (% bankroll): 0.005
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 800
- Correlation bucket limit (% bankroll): 0.03
- Confidence level: `low`
- Portfolio constraints: Do not initiate new exposure from this packet because the case remains threshold-fragile and research-incomplete., Only reassess after direct CIK entity/ballot mapping confirmation and fresher polling or reporting around the 4% threshold., Treat naming or coalition-registration ambiguity as a hard blocker because a mapping mistake can invalidate the contract interpretation.

## Invalidation

### Thesis breakers
- Credible fresh polling shows the market-relevant BSP/United Left entity below or clearly near-below the 4% threshold.
- Direct CIK registration or ballot materials show the market-relevant entity is not the expected BSP–United Left formation.
- Evidence of coalition fracture, de-registration, or naming mismatch materially weakens seat eligibility.

### Market structure breakers
- The market is incorporating fresher local threshold polling unavailable in the bounded package.
- Thin liquidity or naming confusion is distorting the displayed 0.735 quote.
- Official reporting on ballot registration or seat eligibility changes the executable interpretation of the contract.

### Time breakers
- Late threshold polling before 19 April can move this probability materially.
- Election-night counts and official allocation will quickly dominate current pre-election reasoning.

### Reversal conditions
- Move toward authorized yes only after direct CIK mapping and stronger threshold evidence are verified.
- Shift toward no if credible sub-threshold polling or official mapping problems appear.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Direct official CIK confirmation that the market-relevant entity is the expected BSP/United Left formation.
- Fresh independent evidence on current vote share relative to the 4% threshold.
- How much late-cycle threshold risk is already embedded in the market price.

### Reasons to pass / stay small
- The case is threshold-fragile, so small factual errors have discontinuous consequences.
- The market is near the bounded fair-value range, so there is little valuation cushion to compensate for verification gaps.
- The bundle explicitly says blockers require new research, especially on CIK mapping and fresh polling.

### What would change my mind
- Direct CIK ballot or registration confirmation cleanly matching the contract subject to BSP–United Left.
- Fresh polling or credible reporting showing the bloc safely above 4%, which would strengthen the yes case and possibly improve readiness.
- Fresh polling or official evidence showing sub-threshold risk or naming problems, which would move the estimate materially lower.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet intentionally separates directional judgment from execution readiness: the bounded evidence supports a modest yes lean, but not a clean, auditable, threshold-safe authorization.

## Notes for downstream evaluator

United Left (BSP) is still more likely than not to win at least one seat because it is described as an existing parliamentary bloc that previously cleared the 4% threshold, but the unresolved CIK entity-mapping issue and lack of fresh threshold-sensitive polling make the case too fragile and too close to market for authorization.
