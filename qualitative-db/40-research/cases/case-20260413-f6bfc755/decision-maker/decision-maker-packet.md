---
type: decision_packet
case_key: case-20260413-f6bfc755
dispatch_id: dispatch-case-20260413-f6bfc755-20260413T152336Z
question: "Will \\\"Thrash\\\" be the top US Netflix movie this week?"
market_id: case-20260413-f6bfc755
external_market_id: 0xf0298a9e3948374a4c3341f5b286f6f99a6bd6bd960c455bf8bb355c2eff358c
market_slug: will-thrash-be-the-top-us-netflix-movie-this-week
platform: polymarket
market_title: "Will \"Thrash\" be the top US Netflix movie this week?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-f6bfc755/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-f6bfc755/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: NONE
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.62
fair_value_high: 0.8
fair_value_mid: 0.71
market_reference_price: 0.9
edge_mid_vs_market_pct_points: -19.0
independent_verification_quality: low
compressed_toward_market_applied: false
decision_confidence: low
valid_until: 2026-04-14T23:59:00Z
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
- Primary crux: The bounded bundle does not provide independently verified evidence that Thrash actually led the unpublished 4/6/26-4/12/26 US Netflix week, while the market is pricing extreme confidence at 0.90, so the evidence-quality gap is too large to support an execution-quality decision.
- One-sentence rationale: Because the governing Netflix chart for the target week is still unpublished and the bundle provides no strong independent evidence explaining a 90% market price, the disciplined output is to stay flat and wait for the actual source of truth.

## Why this is the right action / no-action call

I preserve the bounded provisional estimate around 0.71 as a pre-publication expectation, but I do not consider it execution-usable given low independent verification quality, explicit reopen-recommended status, and the absence of direct title-specific evidence for the unresolved week.

## Valuation

- Fair value low: 0.62
- Fair value high: 0.8
- Fair value midpoint: 0.71
- Market reference price: 0.9
- Edge vs market (percentage points): -19.0
- Independent verification quality: `low`
- Compressed toward market applied: `false`
- Compression reason: No further compression helps because the problem is not overprecision in the estimate; it is that the decisive title-specific chart evidence for the unpublished week is absent, leaving the market's unseen-information signal unverified.

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
  - `notes:` Zero-exposure band because the decisive target-week evidence is missing.
- `hold`
  - `min_p:` 0.4
  - `max_p:` 0.6
  - `target_exposure_fraction:` 0
  - `notes:` Zero-exposure band; no autonomous hold/add decision is justified before publication.
- `trim`
  - `min_p:` 0.6
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0
  - `notes:` Zero-exposure band because market confidence cannot be audited against the unpublished governing chart.
- `exit`
  - `min_p:` 0.8
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Zero-exposure band; remain flat until the governing Netflix update prints and title mapping is confirmed.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 3600
- Valid until: 2026-04-14T23:59:00Z
- Time horizon: Pre-publication through the expected 2026-04-14 Netflix US Top 10 publication

## Risk controls

- Max position size (% bankroll): 0.0
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `low`
- Portfolio constraints: Do not trade from this packet because the target-week chart evidence is unpublished and independently unverified., Require the Netflix Tudum US movie chart for 4/6/26-4/12/26 or equivalently authoritative confirmation before authorizing any exposure., Keep target exposure at zero until title mapping and actual weekly rank are observed on the governing source.

## Invalidation

### Thesis breakers
- The 2026-04-14 Netflix Tudum US movie chart publishes and shows Thrash clearly below #1.
- The chart publishes and shows a different title at #1, eliminating the pre-publication uncertainty.
- Credible evidence emerges that Thrash was not eligible or is titled differently than the market assumes for the governing chart.

### Market structure breakers
- A clarified market-rule interpretation changes how title mapping to the Netflix chart is handled.
- The governing Tudum update is delayed or unavailable long enough to shift settlement expectations materially.
- Evidence appears that the market's 0.90 price was tied to information not reflected in public pre-publication sources, requiring a new review after release.

### Time breakers
- This packet should not be used after valid_until without the actual target-week Netflix update.
- Once the chart publishes, this pre-publication uncertainty packet should be replaced with a new post-publication decision immediately.

### Reversal conditions
- No reversal logic applies because this packet authorizes no position.
- A new packet is required after chart publication or equivalent authoritative confirmation.
- Do not auto-reverse from flat based on this packet.

## Epistemic status

### Key uncertainties
- Whether Thrash actually led the unpublished 4/6/26-4/12/26 US Netflix week.
- Whether the market's extreme confidence reflects accurate unofficial tracking or simply overconfident speculation.
- Whether the eventual Netflix chart label will map cleanly to the market's exact title string.

### Reasons to pass / stay small
- The decisive governing chart has not yet published, so the strongest possible evidence is still unavailable.
- Independent verification quality is explicitly low, which is insufficient for acting against or with an extreme market price confidently.
- This is a classic case where the market may have unseen information, but the bounded public bundle does not justify trusting that signal enough to trade.

### What would change my mind
- The 2026-04-14 Netflix Tudum US movie Top 10 update showing Thrash at #1 would make the case decision-ready in favor of Yes.
- The update showing another film at #1 would make the case decision-ready against Thrash.
- Authoritative title-specific evidence that Thrash launched in-window and dominated US viewing would increase confidence materially even before chart publication.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: I preserve the bounded provisional estimate around 0.71 as a pre-publication expectation, but I do not consider it execution-usable given low independent verification quality, explicit reopen-recommended status, and the absence of direct title-specific evidence for the unresolved week.

## Notes for downstream evaluator

The bounded bundle does not provide independently verified evidence that Thrash actually led the unpublished 4/6/26-4/12/26 US Netflix week, while the market is pricing extreme confidence at 0.90, so the evidence-quality gap is too large to support an execution-quality decision.
