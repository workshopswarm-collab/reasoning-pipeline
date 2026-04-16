---
type: decision_packet
case_key: case-20260414-f3506e60
dispatch_id: dispatch-case-20260414-f3506e60-20260414T022039Z
question: "Will the Dravida Munnetra Kazhagam (DMK) win the most seats in the 2026 Tamil Nadu Legislative Assembly election?"
market_id: case-20260414-f3506e60
external_market_id: 0x33403f2501afbeafa3372043080e5360d714a9323b264cb76c3aaafc335304a5
market_slug: will-the-dravida-munnetra-kazhagam-dmk-win-the-most-seats-in-the-2026-tamil-nadu-legislative-assembly-election
platform: polymarket
market_title: "Will the Dravida Munnetra Kazhagam (DMK) win the most seats in the 2026 Tamil Nadu Legislative Assembly election?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260414-f3506e60/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-f3506e60/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: needs_more_research
fair_value_low: 0.67
fair_value_high: 0.74
fair_value_mid: 0.705
market_reference_price: 0.735
edge_mid_vs_market_pct_points: -3.0
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
- Trade authorization: `watch_only`
- Position policy: `hold_only`
- Decision readiness: `needs_more_research`
- Primary crux: DMK remains the likeliest single party to win the most seats because it has the strongest verified structural baseline and the contract settles on party seat count, not alliance narrative, but the market already prices a fairly strong favorite and the current bundle lacks enough late-cycle seat evidence to justify action.
- One-sentence rationale: DMK is still the likeliest single party to win the most seats, but because the market is already near the bounded fair-value range and the decisive uncertainty is unresolved constituency-level seat conversion under a fragmented opposition, the disciplined output is watch-only and needs-more-research rather than an authorized trade.

## Why this is the right action / no-action call

This packet intentionally separates a mild Yes lean from execution readiness: the structural DMK case is real, but the current bundle lacks the late-cycle seat evidence needed to treat 73.5% as clearly wrong or clearly attractive.

## Valuation

- Fair value low: 0.67
- Fair value high: 0.74
- Fair value midpoint: 0.705
- Market reference price: 0.735
- Edge vs market (percentage points): -3.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: DMK's 2021 seat dominance and incumbency justify favoritism, but thin current-cycle seat evidence and uncertainty around opposition coordination keep fair value near, but slightly below, the market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.3
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized because the case is not decision-ready.
- `scaled_enter`
  - `min_p:` 0.3
  - `max_p:` 0.55
  - `target_exposure_fraction:` 0
  - `notes:` No entry authorized until seat-conversion evidence improves materially.
- `hold`
  - `min_p:` 0.55
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0
  - `notes:` Hold/watch zone; DMK is favored but not cleanly enough verified for fresh adds.
- `trim`
  - `min_p:` 0.72
  - `max_p:` 0.85
  - `target_exposure_fraction:` 0
  - `notes:` Avoid increasing above roughly fair value given unresolved opposition-fragmentation dynamics.
- `exit`
  - `min_p:` 0.85
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Exit/avoid at expensive prices because current-cycle constituency evidence is too thin to support near-certainty.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 21600
- Valid until: 2026-04-18T23:59:00-04:00
- Time horizon: Through market close and late pre-poll seat-conversion evidence

## Risk controls

- Max position size (% bankroll): 0.005
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 80
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.03
- Confidence level: `low`
- Portfolio constraints: Do not initiate new exposure from this packet because the case remains seat-conversion-sensitive and research-incomplete., Reopen only after stronger late polling, constituency-level seat projections, or credible evidence on opposition coordination and TVK vote splitting., Treat alliance narrative and statewide mood as secondary to single-party seat mechanics in this contract.

## Invalidation

### Thesis breakers
- Credible late polling or seat projections show cleaner-than-expected anti-DMK coordination or AIADMK-led seat efficiency.
- Strong evidence emerges that TVK harms DMK more than AIADMK in constituency-level conversion.
- Late campaign reporting materially strengthens DMK's seat-conversion edge beyond the current bounded view.

### Market structure breakers
- The market is incorporating stronger local polling or field intelligence unavailable in the bounded package.
- Thin liquidity or narrative momentum is overstating or understating the displayed 0.735 quote.
- Late alliance or candidate shocks materially alter constituency-level seat conversion before market close.

### Time breakers
- Because the market closes before the reported polling date, late campaign information can quickly dominate current reasoning.
- Any credible late seat projection or polling wave should replace this packet rather than merely update it.

### Reversal conditions
- Move toward authorized yes only after stronger late evidence confirms DMK's seat-conversion edge while price remains favorable.
- Move lower if opposition coordination or TVK effects look more damaging to DMK than currently assumed.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- How TVK vote share translates into constituency-level seat effects.
- Whether anti-DMK forces coordinate efficiently enough to narrow or overturn DMK's seat edge.
- What late pre-poll evidence emerges before or near market close.

### Reasons to pass / stay small
- The bundle explicitly says blockers require new research, especially on current-cycle seat evidence.
- The market is near the bounded fair-value range, so there is not enough cushion to compensate for missing constituency-level information.
- This contract depends on seat conversion, not broad narrative momentum, and that is where the current evidence is weakest.

### What would change my mind
- Credible late polling or seat models showing DMK clearly ahead in single-party seat count would improve readiness and raise fair value modestly.
- Strong evidence of opposition consolidation or damaging TVK vote-splitting effects on DMK would lower fair value.
- Any late campaign shock materially changing constituency math would require a new packet.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet intentionally separates a mild Yes lean from execution readiness: the structural DMK case is real, but the current bundle lacks the late-cycle seat evidence needed to treat 73.5% as clearly wrong or clearly attractive.

## Notes for downstream evaluator

DMK remains the likeliest single party to win the most seats because it has the strongest verified structural baseline and the contract settles on party seat count, not alliance narrative, but the market already prices a fairly strong favorite and the current bundle lacks enough late-cycle seat evidence to justify action.
