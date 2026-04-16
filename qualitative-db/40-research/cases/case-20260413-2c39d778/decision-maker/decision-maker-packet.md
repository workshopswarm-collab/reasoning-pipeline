---
type: decision_packet
case_key: case-20260413-2c39d778
dispatch_id: dispatch-case-20260413-2c39d778-20260413T215003Z
question: "Will Vitality win IEM Rio 2026?"
market_id: case-20260413-2c39d778
external_market_id: 0xfefaf1876e4dc906d74c7c5f9241ec60edfe501a3bda4048b8722c52468e9fae
market_slug: will-vitality-win-iem-rio-2026
platform: polymarket
market_title: "Will Vitality win IEM Rio 2026?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-2c39d778/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-2c39d778/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: needs_more_research
fair_value_low: 0.58
fair_value_high: 0.68
fair_value_mid: 0.63
market_reference_price: 0.705
edge_mid_vs_market_pct_points: -7.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: low
valid_until: 2026-04-14T23:59:00-04:00
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
- Primary crux: Vitality is the deserved outright favorite, but the current 70.5% price is somewhat richer than the bounded public evidence justifies because the remaining bracket path and the true size of Vitality's form edge over the field were not cleanly independently verified.
- One-sentence rationale: Vitality is a real favorite, but because the 70.5% price is ahead of the bounded public evidence and the unresolved bracket/form questions can move the outright materially, the disciplined output is watch-only and needs-more-research rather than an authorized trade.

## Why this is the right action / no-action call

This packet intentionally distinguishes directional belief from execution readiness: the bounded package supports Vitality as favorite, but not at an auditably strong enough level to justify fresh action before the next key match.

## Valuation

- Fair value low: 0.58
- Fair value high: 0.68
- Fair value midpoint: 0.63
- Market reference price: 0.705
- Edge vs market (percentage points): -7.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: The market is information-rich and Vitality is clearly a real favorite, but unresolved uncertainty around bracket state and the extremity of their true strength edge prevents endorsing the full market price.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.25
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the case is not decision-ready despite a yes lean.
- `scaled_enter`
  - `min_p:` 0.25
  - `max_p:` 0.5
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized until bracket path and current-form edge are better verified.
- `hold`
  - `min_p:` 0.5
  - `max_p:` 0.66
  - `target_exposure_fraction:` 0
  - `notes:` Hold/watch zone; Vitality is favored but not cleanly enough for new adds.
- `trim`
  - `min_p:` 0.66
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0
  - `notes:` Avoid adding above roughly fair value given unresolved bracket and form-edge uncertainty.
- `exit`
  - `min_p:` 0.8
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at very high prices because public evidence does not support near-certainty in this field.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 7200
- Valid until: 2026-04-14T23:59:00-04:00
- Time horizon: Through the Vitality-vs-G2 catalyst and subsequent bracket progression

## Risk controls

- Max position size (% bankroll): 0.0075
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 80
- Liquidity minimum depth: 800
- Correlation bucket limit (% bankroll): 0.03
- Confidence level: `low`
- Portfolio constraints: Do not initiate new exposure from this packet because bracket-state and true-strength verification are incomplete., Reassess after the Vitality-vs-G2 match or after cleaner bracket/odds evidence becomes available., Treat tournament outrights with elite-opponent density as variance-heavy even when one team is the favorite.

## Invalidation

### Thesis breakers
- Strong independent odds, rankings, or bracket evidence show Vitality's edge over the field is materially larger than currently estimated.
- Vitality lose the G2 match or encounter a materially harder path than currently assumed.
- Another elite team shows stronger current form or an easier route than currently reflected in the bounded package.

### Market structure breakers
- The market is incorporating superior live bracket or form information unavailable in the bounded package.
- Displayed price is being distorted by thin liquidity or event-specific momentum chasing.
- Official ESL bracket or reporting updates materially change the effective outright state.

### Time breakers
- The April 14 Vitality-vs-G2 match can reprice the outright immediately.
- Subsequent bracket progression or playoff qualification should replace this packet rather than merely update it.

### Reversal conditions
- Move toward authorized yes only after cleaner independent evidence confirms both the bracket path and a truly extreme Vitality form edge.
- Move toward no if verified evidence shows a materially harder path or stronger rival form.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- How large Vitality's current true strength edge is versus the rest of the field.
- Exact remaining bracket difficulty after the next catalyst match.
- How much the market already reflects superior live information not captured in the bounded package.

### Reasons to pass / stay small
- The package explicitly says stronger verification would be preferable before high-conviction action.
- The next match is an immediate re-pricing catalyst, so current edges can decay quickly.
- The market is only moderately above bounded fair value, leaving insufficient cushion versus the unresolved information gap.

### What would change my mind
- Independent bookmaker or exchange prices near or above the current market would move me closer to market.
- Cleaner bracket evidence showing a materially easier Vitality path would raise fair value.
- Verified stronger rival form, a harder path, or a loss to G2 would move fair value materially lower.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet intentionally distinguishes directional belief from execution readiness: the bounded package supports Vitality as favorite, but not at an auditably strong enough level to justify fresh action before the next key match.

## Notes for downstream evaluator

Vitality is the deserved outright favorite, but the current 70.5% price is somewhat richer than the bounded public evidence justifies because the remaining bracket path and the true size of Vitality's form edge over the field were not cleanly independently verified.
