---
type: decision_packet
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
question: "Will the price of Bitcoin be above $70,000 on April 20?"
market_id: 551a0230-0ffb-42cc-9103-4bea5dc0cb4e
external_market_id: 0x73f9d7c48acbeefbe93bdcdc747947e2e8573945f11720617290fe672bf997d2
market_slug: bitcoin-above-70k-on-april-20
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 20?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-84fdc62d/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-84fdc62d/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.8
fair_value_high: 0.86
fair_value_mid: 0.83
market_reference_price: 0.875
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T13:08:04.774832+00:00
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
- Primary crux: Bitcoin is still more likely than not to close above $70,000 on the April 20 noon ET Binance minute because current spot in the mid-74k area leaves a real cushion above strike, but the market at 0.875 is already pricing this five-day, single-minute, single-venue threshold too confidently given ordinary BTC drawdown risk and unresolved settlement-minute fragility.
- One-sentence rationale: BTC is still more likely than not to finish above $70,000 on the April 20 Binance noon minute, but with fair value closer to 0.83 than the 0.875 market and meaningful five-day path risk still live, the disciplined output remains watch-only rather than an authorized Yes trade.

## Why this is the right action / no-action call

This is a high-probability but still overconfident crypto threshold market: directionally Yes, weak execution value at the quoted price.

## Valuation

- Fair value low: 0.8
- Fair value high: 0.86
- Fair value midpoint: 0.83
- Market reference price: 0.875
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Fresh same-venue spot and rule verification support the Yes baseline and reduce room for a large bearish fade, but exact-minute Binance microstructure and normal five-day BTC volatility still keep fair value below market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.72
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price and still refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.72
  - `max_p:` 0.8
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if BTC remains comfortably above 70k and downside regime stays benign.
- `hold`
  - `min_p:` 0.8
  - `max_p:` 0.86
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.86
  - `max_p:` 0.92
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a one-minute settlement contract with meaningful five-day path dependence.
- `exit`
  - `min_p:` 0.92
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at very rich prices because exact-minute downside tail dominates residual uncertainty.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T13:08:04.774832+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current price., Treat exact-minute Binance settlement risk as the dominant execution constraint even in a favorable spot regime., Reopen only if market cheapens materially or later same-venue checks show the cushion holding into the weekend with calmer downside risk.

## Invalidation

### Thesis breakers
- BTC loses cushion and trades back toward 70k-72k on Binance before the Apr 20 fixing window.
- A major downside crypto or macro catalyst materially raises the probability of a sub-70k settlement minute.
- Binance-specific weakness or settlement-surface issues emerge ahead of the resolving minute.

### Market structure breakers
- Market reprices materially without corresponding same-venue spot deterioration, changing the value comparison.
- Binance operational or microstructure issues emerge near settlement.

### Time breakers
- A fresh direct Binance observation closer to Apr 20 12:00 ET should supersede this packet before any action.
- The actual Apr 20 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if later pre-fix Binance checks show a still-strong cushion with reduced downside risk.
- Downgrade if BTC loses cushion or if downside volatility or catalyst risk increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a 5-6% pullback landing exactly on the settlement minute.
- Whether the market already embeds fresher venue-specific information than the bounded package contains.
- How much Binance-specific microstructure deserves additional discount versus broad spot context.

### Reasons to pass / stay small
- The current market price is above bounded fair value.
- This is a one-minute single-venue settlement contract where path risk matters more than broad BTC direction.
- The edge is modest and not robust enough to justify authorization.

### What would change my mind
- Later same-venue checks showing BTC still comfortably above 72k into Apr. 18-19 would move me somewhat closer to market.
- A move back toward the low-72k or 70k area would lower fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a high-probability but still overconfident crypto threshold market: directionally Yes, weak execution value at the quoted price.

## Notes for downstream evaluator

Bitcoin is still more likely than not to close above $70,000 on the April 20 noon ET Binance minute because current spot in the mid-74k area leaves a real cushion above strike, but the market at 0.875 is already pricing this five-day, single-minute, single-venue threshold too confidently given ordinary BTC drawdown risk and unresolved settlement-minute fragility.
