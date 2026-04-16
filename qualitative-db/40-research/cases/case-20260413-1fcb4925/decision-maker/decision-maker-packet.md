---
type: decision_packet
case_key: case-20260413-1fcb4925
dispatch_id: dispatch-case-20260413-1fcb4925-20260413T212655Z
question: "Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?"
market_id: case-20260413-1fcb4925
external_market_id: 0x0437f06a0b6a6d461042738182a8120ca0fa1edf534447df4cc7bac9833f838f
market_slug: will-progressive-bulgaria-pb-win-the-most-seats-in-the-2026-bulgarian-parliamentary-election
platform: polymarket
market_title: "Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-1fcb4925/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-1fcb4925/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.58
fair_value_high: 0.78
fair_value_mid: 0.68
market_reference_price: 0.9595
edge_mid_vs_market_pct_points: -27.9
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: low
valid_until: 2026-04-17T23:59:00-04:00
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
- Primary crux: PB may be the favorite to win the most seats, but the market's 95.95% price is far too confident relative to the bounded public evidence because there is no strong direct final-week polling or seat-model verification showing PB near-locked over GERB-SDS in a fragmented threshold-based election.
- One-sentence rationale: PB may be a real favorite, but because the 95.95% market price is unsupported by strong direct final-week polling or seat-model evidence and the election's fragmented seat-conversion dynamics leave GERB-SDS as a meaningful alternative, the disciplined output is forbidden and needs-more-research rather than an executable anti-market trade.

## Why this is the right action / no-action call

This packet intentionally separates directional skepticism of the extreme market price from trade authorization: the apparent mispricing is large, but the evidence gap sits exactly on the decisive crux and is too material to ignore.

## Valuation

- Fair value low: 0.58
- Fair value high: 0.78
- Fair value midpoint: 0.68
- Market reference price: 0.9595
- Edge vs market (percentage points): -27.9
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: The market may contain fresher local information than the bounded package, but the public evidence recovered here is far too thin to justify a 95%+ lock, so valuation is pulled well below market while remaining conservative versus the most bearish outside view.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.2
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the case is not decision-ready.
- `scaled_enter`
  - `min_p:` 0.2
  - `max_p:` 0.5
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized until direct late polling or seat-model evidence is verified.
- `hold`
  - `min_p:` 0.5
  - `max_p:` 0.75
  - `target_exposure_fraction:` 0
  - `notes:` Flat while PB remains plausible favorite but not sufficiently verified as a near-lock.
- `trim`
  - `min_p:` 0.75
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` Flat; avoid leaning on incomplete evidence in a fragmented seat-conversion environment.
- `exit`
  - `min_p:` 0.9
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat/forbidden at extreme prices because public evidence does not support near-certainty.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.15
- Allow auto reversal: `false`
- Quote staleness seconds: 14400
- Valid until: 2026-04-17T23:59:00-04:00
- Time horizon: Final-week polling through election-night seat projections and official CIK allocation

## Risk controls

- Max position size (% bankroll): 0.0
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.03
- Confidence level: `low`
- Portfolio constraints: No new exposure is authorized from this packet because the decisive late-polling and seat-model verification is missing., Reopen only after direct final-week polling, exit polling, early seat projections, or official CIK reporting materially improves evidence quality., Do not treat a very large gap versus market as sufficient when the market may embed local information and the contract is seat-based rather than vote-share based.

## Invalidation

### Thesis breakers
- Multiple independent final-week polls or seat models show PB clearly first with a dominant seat lead.
- Credible late polling or projections show GERB-SDS ahead or PB's lead too narrow to justify favoritism.
- Early official or consensus election-night seat reporting contradicts the current PB-favorite view.

### Market structure breakers
- The market is incorporating stronger local polling or elite information unavailable in the bounded package.
- Thin liquidity or headline-driven speculation is distorting the displayed 0.9595 quote.
- Seat-allocation dynamics or threshold effects materially change the relationship between topline vote share and most-seats probability.

### Time breakers
- Final-week polling, exit polls, and first credible seat projections can rapidly overwhelm current reasoning.
- Once election-night seat reporting or official CIK allocation becomes available, this packet should be replaced immediately.

### Reversal conditions
- Move toward authorized yes only after direct late polling or seat-model verification materially improves.
- Move toward no if credible evidence shows GERB-SDS or another bloc has the stronger most-seats path.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether high-quality final-week polling or seat models would validate PB as overwhelmingly likely to finish first in seats.
- How much the market price reflects local information unavailable in the bounded package.
- How seat conversion in a fragmented threshold-based system will translate from topline support to most-seats probability.

### Reasons to pass / stay small
- The package explicitly says blockers require new research and the key missing evidence is exactly what would justify an extreme price.
- A 95.95% market requires stronger proof than is present here.
- The strongest alternative winner, GERB-SDS, remains live enough that thin public evidence should not be stretched into near-certainty.

### What would change my mind
- Multiple independent final-week polls or seat models clearly showing PB first with a robust margin.
- Credible exit polls, early seat projections, or official CIK reporting indicating PB is decisively ahead in seats.
- Verified evidence that PB's support is softer, less seat-efficient, or behind GERB-SDS would move the estimate materially lower.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet intentionally separates directional skepticism of the extreme market price from trade authorization: the apparent mispricing is large, but the evidence gap sits exactly on the decisive crux and is too material to ignore.

## Notes for downstream evaluator

PB may be the favorite to win the most seats, but the market's 95.95% price is far too confident relative to the bounded public evidence because there is no strong direct final-week polling or seat-model verification showing PB near-locked over GERB-SDS in a fragmented threshold-based election.
