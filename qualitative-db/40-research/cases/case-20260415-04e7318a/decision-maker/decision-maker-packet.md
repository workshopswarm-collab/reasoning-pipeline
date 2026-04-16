---
type: decision_packet
case_key: case-20260415-04e7318a
dispatch_id: dispatch-case-20260415-04e7318a-20260415T145259Z
question: "Will the price of Bitcoin be above $70,000 on April 20?"
market_id: 551a0230-0ffb-42cc-9103-4bea5dc0cb4e
external_market_id: 0x73f9d7c48acbeefbe93bdcdc747947e2e8573945f11720617290fe672bf997d2
market_slug: bitcoin-above-70k-on-april-20
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 20?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-04e7318a/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-04e7318a/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.8
fair_value_high: 0.85
fair_value_mid: 0.825
market_reference_price: 0.87
edge_mid_vs_market_pct_points: -4.5
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T15:02:48.087829+00:00
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
- Primary crux: Bitcoin is still more likely than not to close above $70,000 on the April 20 noon ET Binance minute because same-venue spot around 74.1k leaves a meaningful cushion, but the market at 0.87 is still somewhat too confident for a five-day, single-minute threshold where a normal 5-6% drawdown can still decide the contract.
- One-sentence rationale: BTC is still more likely than not to finish above $70,000 on the April 20 Binance noon minute, but with fair value closer to 0.825 than the 0.87 market and meaningful five-day path risk still live, the disciplined output remains watch-only rather than an authorized Yes trade.

## Why this is the right action / no-action call

This remains a high-probability but slightly overconfident crypto threshold market: directional Yes survives, execution value does not.

## Valuation

- Fair value low: 0.8
- Fair value high: 0.85
- Fair value midpoint: 0.825
- Market reference price: 0.87
- Edge vs market (percentage points): -4.5
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Fresh same-venue checks support the Yes baseline and reduce room for a large bearish fade, but no strong independent volatility model justifies closing the gap to the market's high-80s pricing.

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
  - `max_p:` 0.85
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.85
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
- Valid until: 2026-04-16T15:02:48.087829+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current price., Treat exact-minute Binance settlement risk as the dominant execution constraint even in a favorable spot regime., Reopen only if market cheapens materially or later same-venue checks show the cushion holding with reduced downside risk.

## Invalidation

### Thesis breakers
- BTC loses cushion and trades back toward 71k-70k on Binance before the Apr 20 fixing window.
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
- A move back toward the low-71k or 70k area would lower fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This remains a high-probability but slightly overconfident crypto threshold market: directional Yes survives, execution value does not.

## Notes for downstream evaluator

Bitcoin is still more likely than not to close above $70,000 on the April 20 noon ET Binance minute because same-venue spot around 74.1k leaves a meaningful cushion, but the market at 0.87 is still somewhat too confident for a five-day, single-minute threshold where a normal 5-6% drawdown can still decide the contract.
