---
type: decision_packet
case_key: case-20260413-9b3e550a
dispatch_id: dispatch-case-20260413-9b3e550a-20260413T191836Z
question: "Will We Continue the Change – Democratic Bulgaria (PP–DB) finish third in the 2026 Bulgarian parliamentary election?"
market_id: case-20260413-9b3e550a
external_market_id: 0x26eb9949eebf6ba37e8c3c97fd2b2dd4a88be9312bc02c82a765c29596a5a180
market_slug: will-we-continue-the-change-democratic-bulgaria-ppdb-finish-third-in-the-2026-bulgarian-parliamentary-election
platform: polymarket
market_title: "Will We Continue the Change – Democratic Bulgaria (PP–DB) finish third in the 2026 Bulgarian parliamentary election?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-9b3e550a/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-9b3e550a/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: NONE
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.6
fair_value_high: 0.69
fair_value_mid: 0.645
market_reference_price: 0.78
edge_mid_vs_market_pct_points: -13.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: low
valid_until: 2026-04-19T18:00:00+03:00
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

- Side: `NONE`
- Trade authorization: `forbidden`
- Position policy: `flat`
- Decision readiness: `needs_more_research`
- Primary crux: The bounded evidence supports PP–DB as a live third-place candidate, but not at anything close to 78% confidence because the exact-third race appears clustered and the decisive seat-order question was not independently verified with strong late polling or seat-model evidence.
- One-sentence rationale: Because PP–DB appears to be in a genuine but noisy third-place cluster and the bounded evidence lacks the strong late polling or seat-model verification needed for an exact-rank market, the disciplined output is to stay flat rather than trade against or with a 78% market.

## Why this is the right action / no-action call

I preserve the bounded provisional estimate around 0.645 only as a non-execution-ready expectation; the core blocker is insufficient exact-third seat-order evidence, not lack of directional intuition.

## Valuation

- Fair value low: 0.6
- Fair value high: 0.69
- Fair value midpoint: 0.645
- Market reference price: 0.78
- Edge vs market (percentage points): -13.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: No additional compression helps because the main blocker is missing exact-rank evidence on seats, not overprecision in the provisional midpoint.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.2
  - `target_exposure_fraction:` 0
  - `notes:` Zero-exposure band because this packet is not decision-ready.
- `scaled_enter`
  - `min_p:` 0.2
  - `max_p:` 0.4
  - `target_exposure_fraction:` 0
  - `notes:` Zero-exposure band because the exact-third race remains under-modeled in the bounded evidence.
- `hold`
  - `min_p:` 0.4
  - `max_p:` 0.6
  - `target_exposure_fraction:` 0
  - `notes:` Zero-exposure band; no autonomous hold/add decision is justified without stronger seat-order evidence.
- `trim`
  - `min_p:` 0.6
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0
  - `notes:` Zero-exposure band because the market may be reflecting local information not visible in this bounded package.
- `exit`
  - `min_p:` 0.8
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Zero-exposure band; remain flat until late polling or seat-order evidence materially improves.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 21600
- Valid until: 2026-04-19T18:00:00+03:00
- Time horizon: Late campaign through election-day seat-order reporting

## Risk controls

- Max position size (% bankroll): 0.0
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not trade from this packet because exact-third seat-order evidence is insufficiently verified., Require stronger late polling and/or credible seat-model evidence before authorizing any exposure., Keep target exposure at zero until the PP–DB vs DPS/Revival exact-third gap is better established.

## Invalidation

### Thesis breakers
- High-quality late polling or seat models show PP–DB clearly centered in third place.
- Fresh evidence shows PP–DB has a stronger path to second than third, undermining the third-place thesis further.
- Election-night or pre-election reporting clarifies seat-order dynamics in a way that materially changes the exact-third probability.

### Market structure breakers
- A clarified rule interpretation changes how coalition treatment or tie-breaks would rank PP–DB relative to rivals.
- The market reprices sharply on late local polling or election-day turnout signals, making this packet stale immediately.
- Official CIK or credible seat-order reporting resolves the race state more clearly than available here.

### Time breakers
- This packet should not be used after valid_until without refreshed late polling or election-day data.
- Because election ranking can shift rapidly late, stale pre-election packets should be replaced promptly as new local information appears.

### Reversal conditions
- No reversal logic applies because this packet authorizes no position.
- A new packet is required after stronger late polling, seat-model evidence, or election-night reporting.
- Do not auto-reverse from flat based on this packet.

## Epistemic status

### Key uncertainties
- The exact PP–DB vs DPS/Revival seat-order gap was not independently verified with strong late polling or seat models.
- Seat conversion may diverge from topline vote shares in ways that matter materially for exact third.
- Local late-cycle information may exist in the market that is not visible in the bounded public evidence.

### Reasons to pass / stay small
- An exact-third election market is fragile to small shifts and district-level seat conversion errors.
- The package itself says the most important evidence gap is unresolved and requires more research.
- A 78% market is too rich to fade confidently without stronger exact-rank evidence, but the current public case is also too weak to follow.

### What would change my mind
- A strong late polling batch or credible seat-model evidence centering PP–DB clearly in third would make the case more decision-ready.
- Evidence that PP–DB is actually more likely to finish second or fourth than currently implied would push the probability lower.
- Election-day early seat-order reporting or official CIK data would materially reduce uncertainty.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: I preserve the bounded provisional estimate around 0.645 only as a non-execution-ready expectation; the core blocker is insufficient exact-third seat-order evidence, not lack of directional intuition.

## Notes for downstream evaluator

The bounded evidence supports PP–DB as a live third-place candidate, but not at anything close to 78% confidence because the exact-third race appears clustered and the decisive seat-order question was not independently verified with strong late polling or seat-model evidence.
