---
type: decision_packet
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
question: "Will Al Qadisiyah Saudi Club win on 2026-04-23?"
market_id: bfdb337e-2542-4e6d-905c-a36b8a776ffb
external_market_id: 0xa7ab3287ef5d0d78754479fff50e028c0e97c9d42de0b37334038f1dbcd2d9b0
market_slug: spl-qad-sha-2026-04-23-qad
platform: polymarket
market_title: "Will Al Qadisiyah Saudi Club win on 2026-04-23?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-4c35c81d/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-4c35c81d/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: NO
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.03
fair_value_high: 0.12
fair_value_mid: 0.075
market_reference_price: 0.83
edge_mid_vs_market_pct_points: -75.5
independent_verification_quality: high
compressed_toward_market_applied: false
decision_confidence: low
valid_until: 2026-04-15T20:52:19.026648+00:00
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

- Side: `NO`
- Trade authorization: `forbidden`
- Position policy: `flat`
- Decision readiness: `needs_more_research`
- Primary crux: If the governing fixture is the independently verified Al Qadsiah vs Al Shabab match that already finished 2-2 on 2026-04-14, then this should resolve No because a draw is not a win; but because the assignment date conflicts with that evidence and explicit official settlement-source confirmation is still missing, the disciplined output is no-side directionally but forbidden for execution.
- One-sentence rationale: The visible evidence strongly suggests this market should resolve No because the referenced Al Qadsiyah vs Al Shabab match already ended 2-2, but since the assignment date conflicts with that evidence and explicit official settlement-source confirmation is still missing, the disciplined output is forbidden and needs-more-research rather than trading the apparent edge.

## Why this is the right action / no-action call

This is a high-conviction direction with low execution readiness due to contract identity ambiguity; source mismatch dominates valuation.

## Valuation

- Fair value low: 0.03
- Fair value high: 0.12
- Fair value midpoint: 0.075
- Market reference price: 0.83
- Edge vs market (percentage points): -75.5
- Independent verification quality: `high`
- Compressed toward market applied: `false`
- Compression reason: If the verified 2026-04-14 2-2 match is the governing fixture, No should be near-certain; the only reason fair value is not driven even lower is residual uncertainty about whether the contract instead references a different future fixture.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.02
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized from this packet because the case is not decision-ready despite the strong directional no view if the verified 2-2 result governs.
- `scaled_enter`
  - `min_p:` 0.02
  - `max_p:` 0.08
  - `target_exposure_fraction:` 0
  - `notes:` Even much lower prices would still require clean fixture-identity confirmation before action.
- `hold`
  - `min_p:` 0.08
  - `max_p:` 0.15
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair value zone under the already-played-match interpretation, but not actionable while contract identity remains unresolved.
- `trim`
  - `min_p:` 0.15
  - `max_p:` 0.4
  - `target_exposure_fraction:` 0
  - `notes:` Avoid increasing while settlement-source ambiguity remains unresolved.
- `exit`
  - `min_p:` 0.4
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat or avoid at elevated prices because the market may be tied to a mismapped or stale fixture record.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T20:52:19.026648+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not enter from this packet; reopen only after explicit official settlement-source confirmation ties the contract to the correct fixture., Require resolution of the date and fixture-identity conflict before treating the apparent edge as tradable., Treat matchup/date mismatches as hard blockers even when one side appears overwhelmingly favored by the evidence.

## Invalidation

### Thesis breakers
- An official league or market settlement source shows the governing fixture is actually on 2026-04-23 and unplayed.
- A clarified contract source ties the market to a different Al Qadsiyah fixture than the verified 2026-04-14 draw.
- The independently verified 2-2 result is shown to be unrelated to the market's intended matchup.

### Market structure breakers
- The market metadata or slug is corrected in a way that changes the referenced fixture.
- A stale or inconsistent assignment date is resolved and contradicts the already-played-fixture interpretation.

### Time breakers
- Any explicit settlement clarification should supersede this packet immediately.
- If no clean fixture-identity confirmation is obtained, this packet should not be used for trading.

### Reversal conditions
- Move from forbidden to watch-only or authorized only after official confirmation of the exact governing fixture and settlement source.
- Move sharply upward if the contract is confirmed to reference a future unplayed match.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the contract truly references the verified 2026-04-14 2-2 match or a different future fixture.
- Which official source the market operator will actually use for settlement.
- Whether the 2026-04-23 date in the assignment is stale metadata or the intended contract identity.

### Reasons to pass / stay small
- The apparent edge is huge but entirely hostage to contract-identity resolution.
- Fixture/date mismatch is a hard blocker even when one interpretation looks overwhelming.
- This is a source-of-truth problem, not a standard pre-match pricing problem.

### What would change my mind
- Explicit official settlement documentation tying the market to the already-played 2-2 match would collapse residual uncertainty and strengthen No further.
- Official confirmation that the intended fixture is instead on 2026-04-23 and unplayed would move the estimate sharply upward.
- A corrected market metadata record resolving the fixture-date mismatch would materially improve readiness.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a high-conviction direction with low execution readiness due to contract identity ambiguity; source mismatch dominates valuation.

## Notes for downstream evaluator

If the governing fixture is the independently verified Al Qadsiah vs Al Shabab match that already finished 2-2 on 2026-04-14, then this should resolve No because a draw is not a win; but because the assignment date conflicts with that evidence and explicit official settlement-source confirmation is still missing, the disciplined output is no-side directionally but forbidden for execution.
