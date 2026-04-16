---
type: decision_packet
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
market_id: case-20260413-07f0191d
external_market_id: 0xe54223c75f0b8675afaccc099f9cf21fb8877a4f3b72c1064f6d284ef8723fbc
market_slug: will-gerb-udf-gerb-sds-finish-second-in-the-2026-bulgarian-parliamentary-election
platform: polymarket
market_title: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-07f0191d/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-07f0191d/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: NO
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.1
fair_value_high: 0.35
fair_value_mid: 0.22
market_reference_price: 0.96
edge_mid_vs_market_pct_points: -74.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: low
valid_until: 2026-04-16T23:59:00-04:00
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
- Primary crux: The bounded package makes 0.96 on GERB-SDS finishing second look far too high because accessible outside-view evidence still points to GERB-SDS being more plausibly first than second, but the missing direct late-cycle domestic polling and official-source verification are too material to authorize execution.
- One-sentence rationale: Even though the bounded package suggests 0.96 on GERB-SDS finishing second is probably far too high because GERB-SDS may still be more likely first than second, the missing direct late-cycle polling and official-source verification are too material to justify an executable trade, so the correct output is forbidden and needs-more-research.

## Why this is the right action / no-action call

This packet intentionally refuses action despite a large apparent anti-market edge because the package itself marks the case as reopen-recommended and the unresolved verification gap sits directly on the decisive crux.

## Valuation

- Fair value low: 0.1
- Fair value high: 0.35
- Fair value midpoint: 0.22
- Market reference price: 0.96
- Edge vs market (percentage points): -74.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: The apparent mispricing is extremely large, but the selected bundle explicitly identifies unresolved late-polling and official-source gaps, so valuation is kept conservative and non-executable rather than maximally anti-market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.2
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the case is not decision-ready.
- `scaled_enter`
  - `min_p:` 0.2
  - `max_p:` 0.4
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized until late-polling and official-source blockers are resolved.
- `hold`
  - `min_p:` 0.4
  - `max_p:` 0.6
  - `target_exposure_fraction:` 0
  - `notes:` Flat while the decisive race-structure uncertainty remains unresolved.
- `trim`
  - `min_p:` 0.6
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0
  - `notes:` Flat; apparent overpricing alone is insufficient without cleaner verification.
- `exit`
  - `min_p:` 0.8
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat/forbidden at extreme prices because evidence quality is not strong enough to support execution.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.15
- Allow auto reversal: `false`
- Quote staleness seconds: 21600
- Valid until: 2026-04-16T23:59:00-04:00
- Time horizon: Through election day counting and official final seat ranking

## Risk controls

- Max position size (% bankroll): 0.0
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.03
- Confidence level: `low`
- Portfolio constraints: No new exposure is authorized from this packet because the case remains research-incomplete., Reopen only after direct verification of late domestic polling, official reporting pathways, and party-label mapping., Do not convert apparent anti-market edge into execution without cleaner confirmation of first-versus-second race structure.

## Invalidation

### Thesis breakers
- Multiple independent late Bulgarian polls directly show GERB-SDS running second rather than first.
- Credible domestic reporting or preliminary official counts make GERB-SDS clearly more likely second than first.
- Party-label or coalition-taxonomy issues show the market subject is materially different from the analyzed GERB-SDS baseline.

### Market structure breakers
- The market is incorporating fresher local information unavailable in the bounded package, especially around late polling or exit polls.
- Official seat-allocation or reporting conventions materially alter the apparent first-versus-second ordering.
- Displayed price is being driven by thin or distorted market structure rather than informed probability.

### Time breakers
- Late pre-election polls or election-night preliminary counts can quickly dominate all current reasoning.
- Any materially new polling or official reporting should trigger a replacement packet rather than a small update.

### Reversal conditions
- Move toward authorization only after direct late-polling and official-source verification resolves the current blockers.
- Reverse the directional view if verified evidence shows GERB-SDS is in fact the modal second-place finisher.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether recent domestic Bulgarian polling materially contradicts the accessible outside-view evidence.
- Whether direct CIK or domestic reporting would validate a PB-first/GERB-second structure.
- How much the 0.96 market price reflects fresher local information unavailable in the bounded package.

### Reasons to pass / stay small
- The selected bundle explicitly says blockers require new research.
- A huge apparent edge against a 0.96 market requires stronger verification than is present here.
- The decisive uncertainty is exactly the first-versus-second ordering, and that is where the package is weakest.

### What would change my mind
- Direct late Bulgarian polls from multiple independent sources showing GERB-SDS running second in seats or votes.
- Strong exit polling, preliminary official counts, or credible domestic reporting indicating GERB-SDS is trailing one bloc but ahead of the rest.
- Clean official/settlement mapping that removes remaining party-label ambiguity and confirms the market subject unambiguously.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet intentionally refuses action despite a large apparent anti-market edge because the package itself marks the case as reopen-recommended and the unresolved verification gap sits directly on the decisive crux.

## Notes for downstream evaluator

The bounded package makes 0.96 on GERB-SDS finishing second look far too high because accessible outside-view evidence still points to GERB-SDS being more plausibly first than second, but the missing direct late-cycle domestic polling and official-source verification are too material to authorize execution.
