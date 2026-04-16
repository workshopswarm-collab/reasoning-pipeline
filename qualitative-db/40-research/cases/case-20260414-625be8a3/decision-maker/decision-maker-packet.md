---
type: decision_packet
case_key: case-20260414-625be8a3
dispatch_id: dispatch-case-20260414-625be8a3-20260414T002740Z
question: "Will the Virginia redistricting referendum pass?"
market_id: case-20260414-625be8a3
external_market_id: 0xc8e9ba9e25f5adcf7e159e62c24ca3bda9a5245a049acb94fdd534e67ed1969e
market_slug: will-the-virginia-redistricting-referendum-pass
platform: polymarket
market_title: "Will the Virginia redistricting referendum pass?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-625be8a3/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-625be8a3/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.74
fair_value_high: 0.82
fair_value_mid: 0.78
market_reference_price: 0.89
edge_mid_vs_market_pct_points: -11.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: low
valid_until: 2026-04-18T23:59:00-04:00
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
- Primary crux: Passage is more likely than not because the referendum appears officially scheduled and actively administered, but the market's 89% confidence is not supported by directly verified likely-voter polling or fully cleared legal/process risk, so the apparent anti-market edge is not execution-ready.
- One-sentence rationale: The referendum is probably more likely than not to pass because it appears officially scheduled and actively administered, but without directly verified voter-support evidence and fully cleared legal/process risk, the market's 89% confidence is too high to accept or fade aggressively, so the disciplined output is forbidden and needs-more-research.

## Why this is the right action / no-action call

This packet intentionally refuses action despite a meaningful below-market valuation because the missing evidence sits directly on the decisive crux: whether passage and occurrence are both as close to locked as the market implies.

## Valuation

- Fair value low: 0.74
- Fair value high: 0.82
- Fair value midpoint: 0.78
- Market reference price: 0.89
- Edge vs market (percentage points): -11.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Official scheduling and administration meaningfully support Yes, but absent directly verified polling and fully cleared legal/process risk, fair value should remain well below the market while avoiding an overly aggressive fade.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.25
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the case is not decision-ready.
- `scaled_enter`
  - `min_p:` 0.25
  - `max_p:` 0.55
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized until likely-voter support and legal/process stability are directly verified.
- `hold`
  - `min_p:` 0.55
  - `max_p:` 0.75
  - `target_exposure_fraction:` 0
  - `notes:` Flat while Yes remains plausible but insufficiently verified for execution.
- `trim`
  - `min_p:` 0.75
  - `max_p:` 0.9
  - `target_exposure_fraction:` 0
  - `notes:` Flat; apparent overpricing alone is not enough without cleaner referendum-specific evidence.
- `exit`
  - `min_p:` 0.9
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat/forbidden at extreme prices because residual legal/process and voter-support uncertainty still matter.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.12
- Allow auto reversal: `false`
- Quote staleness seconds: 21600
- Valid until: 2026-04-18T23:59:00-04:00
- Time horizon: Through referendum occurrence, late legal/process developments, and official statewide result reporting

## Risk controls

- Max position size (% bankroll): 0.0
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 1200
- Correlation bucket limit (% bankroll): 0.03
- Confidence level: `low`
- Portfolio constraints: No new exposure is authorized from this packet because the case remains research-incomplete on the decisive public-opinion and process-risk dimensions., Reopen only after direct likely-voter polling, stronger legal/docket verification, or late administrative confirmation materially improves evidence quality., Do not treat official ballot scheduling alone as enough to justify or fade an extreme price in a referendum contract.

## Invalidation

### Thesis breakers
- Credible independent polling or robust early-vote evidence shows the referendum is on track to pass by a wide margin.
- A fresh court or election-administration disruption materially increases non-occurrence or delayed-occurrence risk.
- Credible evidence shows statewide support is much weaker than implied by the market or that organized opposition is stronger than assumed.

### Market structure breakers
- The market is incorporating nonpublic polling or field data unavailable in the bounded package.
- Thin liquidity or narrative momentum is distorting the displayed 0.89 price.
- Official election-administration updates materially change the practical referendum path before election day.

### Time breakers
- Late legal or administrative changes before the vote can dominate all current reasoning.
- Official result reporting or referendum occurrence status should replace this packet immediately when available.

### Reversal conditions
- Move toward authorized Yes only after direct evidence of broad support and legal stability materially improves.
- Move lower if process risk increases or if credible polling shows a competitive or failing referendum.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether likely-voter support is actually strong enough to justify an 89% passage probability.
- How much the market price reflects hidden polling or campaign field data unavailable in the bundle.
- Whether residual legal/process challenges remain truly de minimis before the vote.

### Reasons to pass / stay small
- The bundle explicitly says blockers require new research, especially on polling and legal-process verification.
- The gap versus market is large enough that stronger confirmation is required before acting.
- The contract's occurrence/process component makes this more than a simple ballot-preference forecast.

### What would change my mind
- Direct credible likely-voter polling showing strong support for passage would move fair value higher and improve readiness.
- Clear primary-source legal/docket evidence that remaining challenges are weak or resolved would reduce process tail risk.
- Credible polling showing a competitive or losing referendum, or fresh legal disruption, would move fair value materially lower.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet intentionally refuses action despite a meaningful below-market valuation because the missing evidence sits directly on the decisive crux: whether passage and occurrence are both as close to locked as the market implies.

## Notes for downstream evaluator

Passage is more likely than not because the referendum appears officially scheduled and actively administered, but the market's 89% confidence is not supported by directly verified likely-voter polling or fully cleared legal/process risk, so the apparent anti-market edge is not execution-ready.
