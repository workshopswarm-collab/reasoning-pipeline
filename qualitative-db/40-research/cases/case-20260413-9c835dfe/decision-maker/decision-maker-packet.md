---
type: decision_packet
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
question: "MicroStrategy announces >1000 BTC purchase April 7-13?"
market_id: case-20260413-9c835dfe
external_market_id: 0xdd1101f985c5649c070c0acc370e72d48a1117a2d4775fd060526771c4c38e41
market_slug: microstrategy-announces-1000-btc-purchase-april-7-13
platform: polymarket
market_title: "MicroStrategy announces >1000 BTC purchase April 7-13?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-9c835dfe/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-9c835dfe/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.93
fair_value_high: 0.985
fair_value_mid: 0.96
market_reference_price: 0.96
edge_mid_vs_market_pct_points: 0.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-13T23:59:00-04:00
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
- Decision readiness: `ready`
- Primary crux: The bounded evidence strongly indicates an official Strategy disclosure stack showing a 2026-04-13 announcement for 13,927 BTC, which is far above threshold, so the event substance appears to have happened; the only meaningful remaining risk is a narrow timestamp/source-surface settlement technicality.
- One-sentence rationale: The substance of the event appears overwhelmingly satisfied by an official 13,927 BTC April 13 disclosure, but because the remaining risk is a narrow timestamp/source-surface technicality and the market already prices 96%, the disciplined output is hold/watch-only rather than fresh entry.

## Why this is the right action / no-action call

I treated synthesis as advisory, accepted the bounded official-disclosure evidence as strong on substance, and declined to claim a live edge because independent refresh in this turn was partially impaired and did not eliminate the residual qualifying-surface ambiguity.

## Valuation

- Fair value low: 0.93
- Fair value high: 0.985
- Fair value midpoint: 0.96
- Market reference price: 0.96
- Edge vs market (percentage points): 0.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: I keep fair value near market because the event substance appears overwhelmingly satisfied, but unresolved ET timestamp and qualifying-surface technicalities still justify a non-trivial haircut from certainty and prevent claiming a clear edge.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.84
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry from this packet; if the market were this low, a fresh packet with refreshed disclosure evidence would be required.
- `scaled_enter`
  - `min_p:` 0.84
  - `max_p:` 0.92
  - `target_exposure_fraction:` 0
  - `notes:` No autonomous entry authorized because current edge is too small relative to settlement-surface ambiguity.
- `hold`
  - `min_p:` 0.92
  - `max_p:` 0.97
  - `target_exposure_fraction:` 0
  - `notes:` Hold-only zone consistent with a likely Yes that is already well priced by the market.
- `trim`
  - `min_p:` 0.97
  - `max_p:` 0.99
  - `target_exposure_fraction:` 0
  - `notes:` Trim/avoid increasing as price moves above my fair-value midpoint into the technical-risk zone.
- `exit`
  - `min_p:` 0.99
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at extreme prices because residual timestamp/source-surface technicality still prevents certainty.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 1800
- Valid until: 2026-04-13T23:59:00-04:00
- Time horizon: Same-day disclosure and settlement-confirmation window

## Risk controls

- Max position size (% bankroll): 0.015
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 40
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not initiate fresh exposure from this packet because the remaining uncertainty is a narrow settlement technicality and the market is already pricing near fair value., Existing aligned exposure may be held, but avoid adding unless a refreshed authoritative source clarifies the in-window qualifying announcement beyond current ambiguity., Refresh official disclosure timing/source evidence before any new action if the market moves materially.

## Invalidation

### Thesis breakers
- Authoritative evidence shows the qualifying official announcement was not public within the Apr 7-13 ET window.
- Resolvers reject the purchases-page disclosure stack as insufficient under market rules.
- The company corrects or withdraws the apparent 13,927 BTC disclosure.

### Market structure breakers
- A clarified market-rule interpretation requires a distinct official surface that the current disclosure stack does not satisfy.
- Current executable pricing diverges materially from the 0.96 reference, making this packet stale for action decisions.
- Later authoritative evidence materially changes the accepted announcement timestamp.

### Time breakers
- This packet expires at valid_until unless refreshed with later official confirmation or settlement-relevant clarification.
- If the market remains unresolved despite same-day official disclosure debate, re-underwrite with the latest accepted source evidence.

### Reversal conditions
- Reverse only on fresh authoritative evidence that the in-window announcement requirement was not met.
- Do not auto-reverse from this packet; require a new packet with refreshed source-of-truth evidence.
- Suspend this packet if source-surface or timing assumptions are materially contradicted by official or resolver guidance.

## Epistemic status

### Key uncertainties
- The main uncertainty is whether the official purchases-page plus linked filing/social stack cleanly counts as the qualifying announcement surface.
- The exact ET timestamp of public availability is not independently audited in the bounded bundle.
- Independent verification quality is only medium because my attempt to refresh supporting public sources was degraded by bot-detection and incomplete page extraction.

### Reasons to pass / stay small
- At 0.96, the market already prices the high-probability Yes outcome almost fully.
- The remaining risk is mostly a settlement technicality, which is hard to monetize unless one has superior source-timing verification.
- A small apparent edge can disappear entirely if resolvers adopt a narrower interpretation of qualifying announcement surface.

### What would change my mind
- Direct authoritative confirmation of the public ET timestamp and accepted official surface would raise confidence toward near-certainty.
- Evidence that the disclosure was posted outside the ET window or that resolvers reject the purchases page would lower fair value materially.
- A materially cheaper market combined with better timestamp verification could justify authorization.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: I treated synthesis as advisory, accepted the bounded official-disclosure evidence as strong on substance, and declined to claim a live edge because independent refresh in this turn was partially impaired and did not eliminate the residual qualifying-surface ambiguity.

## Notes for downstream evaluator

The bounded evidence strongly indicates an official Strategy disclosure stack showing a 2026-04-13 announcement for 13,927 BTC, which is far above threshold, so the event substance appears to have happened; the only meaningful remaining risk is a narrow timestamp/source-surface settlement technicality.
