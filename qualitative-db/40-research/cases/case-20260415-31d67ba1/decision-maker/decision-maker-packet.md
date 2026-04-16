---
type: decision_packet
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
question: "Will the price of Bitcoin be above $70,000 on April 17?"
market_id: 02f818d5-3451-482c-ba4b-0a663270e680
external_market_id: 0x80281108ecd458d73c9e0eafe0946a91645d98771f1326e565657b6f8dcc00e6
market_slug: bitcoin-above-70k-on-april-17
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 17?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-31d67ba1/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-31d67ba1/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.93
fair_value_high: 0.95
fair_value_mid: 0.94
market_reference_price: 0.97
edge_mid_vs_market_pct_points: -3.0
independent_verification_quality: medium
compressed_toward_market_applied: true
decision_confidence: medium
valid_until: 2026-04-16T19:07:16.400934+00:00
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
- Primary crux: Bitcoin is still very likely to close above $70,000 on the April 17 noon ET Binance minute because fresh same-venue pricing around 74.4k leaves a large cushion, but the market at 0.97 is still a bit too confident for a one-minute, single-venue crypto settlement where a routine 5-6% selloff or venue-specific anomaly can still decide the outcome.
- One-sentence rationale: BTC is still very likely to finish above $70,000 on the April 17 Binance noon minute, but with fair value closer to 0.94 than the 0.97 market and residual exact-minute downside tail still live, the disciplined output remains watch-only rather than an authorized Yes trade.

## Why this is the right action / no-action call

This is a very high-probability but still slightly overconfident crypto threshold market: strong directional Yes, weak execution value.

## Valuation

- Fair value low: 0.93
- Fair value high: 0.95
- Fair value midpoint: 0.94
- Market reference price: 0.97
- Edge vs market (percentage points): -3.0
- Independent verification quality: `medium`
- Compressed toward market applied: `true`
- Compression reason: Fresh Binance spot well above strike supports a very high-probability Yes view, but residual path-dependent downside and exact-minute implementation risk still keep fair value below the 0.97 market.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.88
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price and still refreshed same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.88
  - `max_p:` 0.93
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if BTC remains comfortably above 70k and no new downside catalyst appears.
- `hold`
  - `min_p:` 0.93
  - `max_p:` 0.95
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.95
  - `max_p:` 0.98
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a one-minute settlement contract with residual short-horizon tail risk.
- `exit`
  - `min_p:` 0.98
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at extreme prices because exact-minute downside tail still matters despite the favorable spot cushion.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T19:07:16.400934+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current price., Treat exact-minute Binance settlement risk as the dominant execution constraint even with a large spot cushion., Reopen only if market cheapens materially or if a fresher near-settlement Binance check still shows a large cushion with no emerging catalyst risk.

## Invalidation

### Thesis breakers
- BTC loses substantial cushion and trades back toward 71k-70k on Binance before the Apr 17 fixing window.
- A downside macro, crypto, regulatory, or exchange-specific shock materially raises the probability of a sub-70k settlement minute.
- Binance-specific pricing, liquidity, or operational issues emerge near resolution.

### Market structure breakers
- Market reprices materially again without corresponding same-venue spot deterioration, changing the value comparison.
- Binance microstructure or settlement-surface behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 17 12:00 ET should supersede this packet before any action.
- The actual Apr 17 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if later pre-fix Binance checks show the cushion still large with reduced downside risk.
- Downgrade if BTC loses cushion or if downside volatility or catalyst risk increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a 5-6% downside move or wick landing on the exact settlement minute over the next ~48 hours.
- Whether an unobserved late catalyst emerges before the fixing window.
- How much additional discount exact-minute Binance implementation risk deserves at very high market prices.

### Reasons to pass / stay small
- The current market price is above bounded fair value.
- This is still a one-minute single-venue settlement contract where tail risk matters more than broad BTC direction.
- The remaining edge is weak and not robust enough to justify authorization.

### What would change my mind
- Later same-venue checks showing BTC still comfortably above 72k-73k into the final hours would move me slightly closer to market.
- A move back toward 70k-71k would reduce fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a very high-probability but still slightly overconfident crypto threshold market: strong directional Yes, weak execution value.

## Notes for downstream evaluator

Bitcoin is still very likely to close above $70,000 on the April 17 noon ET Binance minute because fresh same-venue pricing around 74.4k leaves a large cushion, but the market at 0.97 is still a bit too confident for a one-minute, single-venue crypto settlement where a routine 5-6% selloff or venue-specific anomaly can still decide the outcome.
