---
type: decision_packet
case_key: case-20260415-d129d0ec
dispatch_id: dispatch-case-20260415-d129d0ec-20260415T014044Z
question: "Russia military action against Kyiv municipality by April 17?"
market_id: a90c3ddd-b00b-4c10-84b2-f88f7e865efb
external_market_id: 0x6b09d2bd85728308faa51a74f78b1f27e798a4ff0751c70ac112d5dc11825832
market_slug: russia-military-action-against-kyiv-municipality-by-april-17
platform: polymarket
market_title: "Russia military action against Kyiv municipality by April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-d129d0ec/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-d129d0ec/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.6
fair_value_high: 0.67
fair_value_mid: 0.635
market_reference_price: 0.73
edge_mid_vs_market_pct_points: -9.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: low
valid_until: 2026-04-16T01:53:25.139435+00:00
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
- Primary crux: Russian strike tempo makes a Kyiv-municipality action by expiry more likely than not, but this contract is narrow on both geography and reporting standard, and the bounded package does not independently verify a clean Kyiv-municipality-specific qualifying signal strongly enough to support acting against a 0.73 market.
- One-sentence rationale: Russian military action against Kyiv municipality is still plausibly more likely than not before expiry given active strike tempo and contract rules that count intercepted Kyiv-directed attacks, but because the bounded package does not independently verify a clean Kyiv-municipality-specific signal and the geography or reporting-window ambiguity is material, the disciplined output is forbidden and needs-more-research rather than an anti-market trade.

## Why this is the right action / no-action call

This is a case where directional belief survives but execution readiness fails on source-of-truth precision.

## Valuation

- Fair value low: 0.6
- Fair value high: 0.67
- Fair value midpoint: 0.635
- Market reference price: 0.73
- Edge vs market (percentage points): -9.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Broad Russian aerial strike activity supports a meaningful Yes probability, but lack of strongly verified Kyiv-municipality-specific evidence and reporting-rule ambiguity keep fair value below the market while still not making the case execution-ready.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.5
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized from this packet because the case is not decision-ready.
- `scaled_enter`
  - `min_p:` 0.5
  - `max_p:` 0.6
  - `target_exposure_fraction:` 0
  - `notes:` Even cheaper pricing would still require cleaner Kyiv-municipality-specific evidence and source clarity.
- `hold`
  - `min_p:` 0.6
  - `max_p:` 0.67
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair value zone under current evidence, but not actionable under present ambiguity.
- `trim`
  - `min_p:` 0.67
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0
  - `notes:` Avoid increasing above fair value while municipality-specific targeting evidence remains insufficiently verified.
- `exit`
  - `min_p:` 0.8
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat or avoid at high prices because broad national strike tempo does not automatically settle this narrow Kyiv-municipality contract.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T01:53:25.139435+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not enter from this packet; reopen only after a fresher Kyiv-city-specific official or major-media signal is confirmed., Require clean interpretation of Kyiv municipality versus broader Kyiv-area reporting before treating any edge as tradable., Treat short-window war-event contracts as source-of-truth sensitive even when broad background tempo is elevated.

## Invalidation

### Thesis breakers
- Official Ukrainian Air Force, Kyiv city authority, or multiple major-media reports clearly confirm no Kyiv-municipality-directed action through expiry.
- A clarified settlement interpretation excludes reporting currently treated as potentially qualifying, such as intercepted but municipality-directed attacks.
- The next strike waves focus elsewhere without Kyiv-city-specific reporting while the window decays.

### Market structure breakers
- A settlement clarification changes how Kyiv municipality versus Kyiv region reporting is interpreted.
- The quote becomes stale relative to new Kyiv-specific reporting or source clarification.

### Time breakers
- The next overnight strike bulletin and any Kyiv city authority statement should supersede this packet quickly.
- If no fresh Kyiv-municipality-specific reporting is available closer to expiry, this packet should not be used for action.

### Reversal conditions
- Move from forbidden to watch-only or authorized only after clear Kyiv-municipality-specific evidence and settlement-source alignment emerge.
- Move materially higher if official or major-media confirmation clearly reports a qualifying Kyiv-directed action within the window.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether the next one to two Russian strike waves will include Kyiv municipality specifically rather than other regions.
- Whether qualifying Kyiv-directed intercepted attacks would be reported clearly enough for settlement.
- How the contract will treat city-versus-oblast reporting and exact reporting-window timing.

### Reasons to pass / stay small
- The edge versus market is not large enough to overcome the contract's location-specific and reporting-specific ambiguity.
- The most important missing information is municipality-specific source confirmation, not general war tempo.
- This is a short-window event contract where one ambiguous source distinction can dominate the trade outcome.

### What would change my mind
- A Kyiv city authority, Ukrainian Air Force, or multiple major-media reports clearly confirming a Kyiv-municipality-directed strike would raise confidence and readiness.
- A clean settlement clarification resolving city-versus-oblast ambiguity would materially improve readiness.
- Continued nationwide strikes without Kyiv-specific confirmation would push me lower as the window decays.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a case where directional belief survives but execution readiness fails on source-of-truth precision.

## Notes for downstream evaluator

Russian strike tempo makes a Kyiv-municipality action by expiry more likely than not, but this contract is narrow on both geography and reporting standard, and the bounded package does not independently verify a clean Kyiv-municipality-specific qualifying signal strongly enough to support acting against a 0.73 market.
