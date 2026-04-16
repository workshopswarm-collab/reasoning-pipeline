---
type: decision_packet
case_key: case-20260414-fdd1ff67
dispatch_id: dispatch-case-20260414-fdd1ff67-20260414T200433Z
question: "Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw?"
market_id: 769fb5f4-3c76-4e50-8737-abe3ba27f674
external_market_id: 0xd07a34813c5b79f87d6e233066840d185d370feeb69955839c23e3b852f57d26
market_slug: spl-qad-sha-2026-04-23-draw
platform: polymarket
market_title: "Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-fdd1ff67/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-fdd1ff67/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: NO
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.33
fair_value_high: 0.44
fair_value_mid: 0.385
market_reference_price: 0.76
edge_mid_vs_market_pct_points: -37.5
independent_verification_quality: low
compressed_toward_market_applied: false
decision_confidence: low
valid_until: 2026-04-15T20:13:45.014101+00:00
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
- Primary crux: A 76% draw price looks wildly above ordinary football base rates and above what the bounded bundle can justify, but because the package lacks a clean independent bookmaker screen for the exact fixture and still contains some contract-surface inconsistency, the disciplined output is no-side directionally but forbidden for execution.
- One-sentence rationale: The visible evidence makes a 76% regulation-time draw price look far too high for a standard football match, but because the bundle lacks a clean independent bookmaker consensus and still contains some contract-surface inconsistency, the disciplined output is directional no but forbidden and needs-more-research rather than a live anti-market trade.

## Why this is the right action / no-action call

This is a classic large-apparent-edge case where weak verification quality should dominate the execution decision.

## Valuation

- Fair value low: 0.33
- Fair value high: 0.44
- Fair value midpoint: 0.385
- Market reference price: 0.76
- Edge vs market (percentage points): -37.5
- Independent verification quality: `low`
- Compressed toward market applied: `false`
- Compression reason: Outside-view football base rates and bundle-level reasoning both point far below the market's draw price, but missing sportsbook consensus and residual contract-surface inconsistency prevent a tighter or executable estimate.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.25
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized from this packet because the case is not decision-ready despite the strong directional skepticism.
- `scaled_enter`
  - `min_p:` 0.25
  - `max_p:` 0.4
  - `target_exposure_fraction:` 0
  - `notes:` Even materially lower draw prices would still require cleaner fixture-specific odds and team-news verification.
- `hold`
  - `min_p:` 0.4
  - `max_p:` 0.5
  - `target_exposure_fraction:` 0
  - `notes:` Bounded fair value zone, but not actionable under current evidence quality.
- `trim`
  - `min_p:` 0.5
  - `max_p:` 0.7
  - `target_exposure_fraction:` 0
  - `notes:` Avoid increasing while contract-surface inconsistency and missing bookmaker consensus remain unresolved.
- `exit`
  - `min_p:` 0.7
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat or avoid at extreme prices because the observed market level is unsupported by the current auditable evidence.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-15T20:13:45.014101+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not enter from this packet; reopen only after a clean independent 1X2 bookmaker screen for the exact fixture is preserved., Require resolution of the residual market-surface inconsistency before acting on the apparent anti-market view., Treat late lineup and injury news as mandatory refresh inputs for a pre-kickoff football market.

## Invalidation

### Thesis breakers
- A clean independent bookmaker panel for the exact fixture shows draw pricing far higher than ordinary base rates imply.
- Verified team news or tactical context emerges that materially elevates draw likelihood.
- The market is clarified to use nonstandard settlement mechanics rather than a normal regulation-time draw.

### Market structure breakers
- The residual contract-surface inconsistency resolves in a way that changes the apparent market meaning.
- The current quote becomes stale relative to corrected market metadata or fixture confirmation.

### Time breakers
- Official starting lineups and late injury news should supersede this packet before kickoff.
- If no fresh odds and team-news verification is available near kickoff, this packet should not be used for action.

### Reversal conditions
- Move from forbidden to watch-only or authorized only after the exact fixture, market meaning, and independent odds consensus are all cleanly verified.
- Move materially toward market if a credible odds panel and team-news stack support an unusually high draw probability.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether independent mainstream sportsbook consensus for the exact fixture is anywhere near the current draw price.
- Whether the residual market-surface inconsistency reflects a metadata error or a real contract interpretation problem.
- How late lineup, injury, and tactical information will alter true draw probability closer to kickoff.

### Reasons to pass / stay small
- Independent verification quality is low despite the large apparent gap.
- A large edge claim needs stronger proof than the current package provides.
- Football draw markets are sensitive to late lineup and fixture-specific context that is not yet cleanly verified.

### What would change my mind
- A preserved bookmaker 1X2 screen showing unusually elevated draw prices would move me materially upward.
- A clean resolution of the contract-surface inconsistency would improve readiness.
- Verified team-news evidence indicating an unusually cagey or depleted matchup would raise draw probability.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a classic large-apparent-edge case where weak verification quality should dominate the execution decision.

## Notes for downstream evaluator

A 76% draw price looks wildly above ordinary football base rates and above what the bounded bundle can justify, but because the package lacks a clean independent bookmaker screen for the exact fixture and still contains some contract-surface inconsistency, the disciplined output is no-side directionally but forbidden for execution.
