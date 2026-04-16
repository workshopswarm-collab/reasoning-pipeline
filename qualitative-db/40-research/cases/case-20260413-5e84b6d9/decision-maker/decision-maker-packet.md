---
type: decision_packet
case_key: case-20260413-5e84b6d9
dispatch_id: dispatch-case-20260413-5e84b6d9-20260413T210605Z
question: "Will Rumen Radev be the next prime minister of Bulgaria after the 2026 parliamentary election?"
market_id: case-20260413-5e84b6d9
external_market_id: 0xd75a9de8f60669a0b891d713902dcfee64dcf88471c49dd76f39fd1ac34c016b
market_slug: will-rumen-radev-be-the-next-prime-minister-of-bulgaria-after-the-2026-parliamentary-election
platform: polymarket
market_title: "Will Rumen Radev be the next prime minister of Bulgaria after the 2026 parliamentary election?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260413-5e84b6d9/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-5e84b6d9/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: forbidden
position_policy: flat
decision_readiness: needs_more_research
fair_value_low: 0.5
fair_value_high: 0.72
fair_value_mid: 0.61
market_reference_price: 0.9035
edge_mid_vs_market_pct_points: -29.3
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
- Primary crux: Radev is a plausible favorite to become the next non-caretaker PM, but the market's 90.35% price is far too confident relative to the publicly auditable evidence because no independently verified coalition whip-count or partner commitment shows he is already near-locked for formal investiture.
- One-sentence rationale: Radev may well be the favorite, but because the 90.35% market price is not supported by independently verified coalition-path evidence and the contract hinges on formal non-caretaker investiture, the disciplined output is forbidden and needs-more-research rather than an executable anti-market trade.

## Why this is the right action / no-action call

This packet intentionally separates directional disagreement with the market from trade authorization: the public case against 90%+ is meaningful, but not yet clean enough to overcome the explicit coalition-path verification gap.

## Valuation

- Fair value low: 0.5
- Fair value high: 0.72
- Fair value midpoint: 0.61
- Market reference price: 0.9035
- Edge vs market (percentage points): -29.3
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Although the bounded synthesis midpoint is 0.68, the lack of directly verified coalition-path evidence and the possibility that the market embeds stronger local information justify a cautious downward but not aggressively maximal anti-market valuation.

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
  - `notes:` No entry authorized until coalition-path evidence is directly verified.
- `hold`
  - `min_p:` 0.5
  - `max_p:` 0.7
  - `target_exposure_fraction:` 0
  - `notes:` Flat while Radev remains plausible but not sufficiently verified as the dominant investiture path.
- `trim`
  - `min_p:` 0.7
  - `max_p:` 0.85
  - `target_exposure_fraction:` 0
  - `notes:` Flat; avoid leaning against high confidence without cleaner coalition evidence.
- `exit`
  - `min_p:` 0.85
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Flat/forbidden at extreme prices because public evidence does not support near-certainty, but verification is too incomplete for execution.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.15
- Allow auto reversal: `false`
- Quote staleness seconds: 14400
- Valid until: 2026-04-17T23:59:00-04:00
- Time horizon: Post-election coalition formation through first formal non-caretaker PM swearing-in

## Risk controls

- Max position size (% bankroll): 0.0
- Max additional exposure (% bankroll): 0.0
- Max single order (% bankroll): 0.0
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 1000
- Correlation bucket limit (% bankroll): 0.03
- Confidence level: `low`
- Portfolio constraints: No new exposure is authorized from this packet because the decisive coalition-path evidence is missing., Reopen only after direct evidence on coalition arithmetic, partner commitments, or authoritative post-election government-formation reporting is available., Do not treat a large gap versus market as sufficient when the market may embed local information on elite bargaining not visible in the bounded package.

## Invalidation

### Thesis breakers
- Authoritative Bulgarian reporting or official party statements show Radev has secured a governing coalition or dominant support for investiture.
- Another leader emerges with a clearer coalition path than Radev.
- Evidence shows Radev is not the operative PM candidate for the relevant bloc or compromise coalition.

### Market structure breakers
- The market is embedding local coalition intelligence not present in the bounded package.
- Thin liquidity or event-driven speculation is distorting the displayed 0.9035 quote.
- Resolution timing or interpretation around swearing-in versus pre-resolution reporting changes the effective executable meaning of the market.

### Time breakers
- Election results and immediate coalition negotiations can change this probability rapidly.
- Any post-election seat distribution or formal coalition announcement should replace this packet rather than merely update it.

### Reversal conditions
- Move toward authorized yes only after direct coalition-path verification materially improves.
- Move toward no if verified evidence shows another leader has the clearer path to formal swearing-in.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- Whether Radev actually has a secured or near-secured governing coalition.
- Which parties would back or block a Radev-led government after the election.
- How much the 90.35% market price reflects local information on coalition bargaining unavailable in the bounded package.

### Reasons to pass / stay small
- The package explicitly says blockers require new research and coalition arithmetic is unresolved.
- At 90%+, the market is pricing near-lock confidence that is not publicly auditable from the bounded evidence.
- This is a coalition-formation contract, so hidden elite bargaining information can matter more than generic public narratives.

### What would change my mind
- Authoritative post-election reporting or party statements showing Radev has the numbers for investiture.
- Verified seat distribution and coalition commitments making Radev the dominant formal swearing-in path.
- Evidence that another coalition leader or compromise candidate is more likely to become the first non-caretaker sworn PM.

### Decision quality
- `not_ready`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This packet intentionally separates directional disagreement with the market from trade authorization: the public case against 90%+ is meaningful, but not yet clean enough to overcome the explicit coalition-path verification gap.

## Notes for downstream evaluator

Radev is a plausible favorite to become the next non-caretaker PM, but the market's 90.35% price is far too confident relative to the publicly auditable evidence because no independently verified coalition whip-count or partner commitment shows he is already near-locked for formal investiture.
