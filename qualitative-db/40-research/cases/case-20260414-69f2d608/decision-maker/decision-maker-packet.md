---
type: decision_packet
case_key: case-20260414-69f2d608
dispatch_id: dispatch-case-20260414-69f2d608-20260414T020911Z
question: "Will the US x Iran ceasefire be extended by April 21, 2026?"
market_id: case-20260414-69f2d608
external_market_id: 0xc0be7b1f19f9b658778c2be7e6bc67596a00f347ab64392d0f5d387534c7c3b4
market_slug: will-the-us-x-iran-ceasefire-be-extended-by-april-21-2026
platform: polymarket
market_title: "Will the US x Iran ceasefire be extended by April 21, 2026?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-69f2d608/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-69f2d608/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.54
fair_value_high: 0.61
fair_value_mid: 0.575
market_reference_price: 0.705
edge_mid_vs_market_pct_points: -13.0
independent_verification_quality: medium
compressed_toward_market_applied: false
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
- Primary crux: An extension is still somewhat more likely than not because the ceasefire remains intact and mediators are active, but the market's 70.5% confidence is too high relative to the strict no-gap official-confirmation mechanics and the absence of any actual bilateral extension announcement.
- One-sentence rationale: An extension remains somewhat more likely than not because the ceasefire is still holding and diplomacy is active, but with no official bilateral extension confirmation and a contract that is strict about no-gap mechanics, the market's 70.5% confidence is too high to trust or fade aggressively, so the disciplined output is forbidden and needs-more-research.

## Why this is the right action / no-action call

This packet intentionally distinguishes a broad geopolitical Yes lean from contract-level execution readiness: the unresolved issue is not whether diplomacy exists, but whether it converts into a qualifying public extension on time.

## Valuation

- Fair value low: 0.54
- Fair value high: 0.61
- Fair value midpoint: 0.575
- Market reference price: 0.705
- Edge vs market (percentage points): -13.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: The ceasefire still holding and mediator activity justify a Yes-leaning range, but the lack of official bilateral confirmation and the strict mechanics keep fair value well below the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.2
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the case is not decision-ready.
- `scaled_enter`
  - `min_p:` 0.2
  - `max_p:` 0.45
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized until extension mechanics and talks timing are directly verified.
- `hold`
  - `min_p:` 0.45
  - `max_p:` 0.6
  - `target_exposure_fraction:` 0
  - `notes:` Flat while a modest Yes lean exists but remains too mechanics-sensitive for execution.
- `trim`
  - `min_p:` 0.6
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0
  - `notes:` Flat; the market appears rich relative to current evidence, but the edge is not clean enough to authorize action.
- `exit`
  - `min_p:` 0.8
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat/forbidden at high prices because the current public evidence does not support near-lock extension odds.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.12
- Allow auto reversal: `false`
- Quote staleness seconds: 21600
- Valid until: 2026-04-18T23:59:00-04:00
- Time horizon: Through any no-gap extension announcement or expiry-window diplomacy before April 21

## Risk controls

- Max position size (% bankroll): 0.0
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 1200
- Correlation bucket limit (% bankroll): 0.03
- Confidence level: `low`
- Portfolio constraints: No new exposure is authorized from this packet because the decisive extension-mechanics evidence is missing., Reopen only after direct official U.S./Iran statements, confirmed second-round talks, or top-tier consensus reporting on a no-gap extension deal., Do not trade this as a generic de-escalation view; the contract requires specific extension mechanics and public confirmation.

## Invalidation

### Thesis breakers
- Parallel official U.S. and Iranian confirmation of a no-gap extension or replacement agreement.
- Renewed hostilities, explicit rejection of extension, or failed follow-on talks materially reduce extension odds.
- Top-tier credible-media consensus reports a finalized official extension consistent with the contract mechanics.

### Market structure breakers
- The market is incorporating real backchannel knowledge of a nearly completed extension not visible in the bounded package.
- Thin liquidity or geopolitical headline momentum is temporarily distorting the displayed 0.705 quote.
- Deadline/operational-close interpretation changes the practical settlement path.

### Time breakers
- A confirmed second round of talks or official bilateral statement could quickly dominate all current reasoning.
- As the ceasefire expiry window approaches, stale assumptions about timing and no-gap mechanics should be replaced rather than extrapolated.

### Reversal conditions
- Move toward authorized Yes only after a fresh packet if official confirmation or overwhelming credible-media consensus of an extension appears.
- Move materially lower if talks fail again, the ceasefire breaks, or either side rejects extension publicly.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether a second round of talks actually occurs before the relevant expiry window.
- Whether any deal would be framed publicly as a qualifying no-gap extension or replacement agreement.
- How much the market price reflects hidden diplomatic progress unavailable in the bounded package.

### Reasons to pass / stay small
- The bundle explicitly says blockers require new research, especially on official extension confirmation and talks timing.
- This contract is mechanics-sensitive, so generic signs of de-escalation are insufficient.
- The market is materially above bounded fair value, but the missing evidence sits directly on the decisive crux.

### What would change my mind
- Explicit bilateral official confirmation of extension talks or a reached extension would move fair value meaningfully higher.
- Multiple top-tier reports of a finalized no-gap extension deal would improve readiness substantially.
- Renewed hostilities, a failed second round, or public rejection of extension by either side would move fair value lower.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet intentionally distinguishes a broad geopolitical Yes lean from contract-level execution readiness: the unresolved issue is not whether diplomacy exists, but whether it converts into a qualifying public extension on time.

## Notes for downstream evaluator

An extension is still somewhat more likely than not because the ceasefire remains intact and mediators are active, but the market's 70.5% confidence is too high relative to the strict no-gap official-confirmation mechanics and the absence of any actual bilateral extension announcement.
