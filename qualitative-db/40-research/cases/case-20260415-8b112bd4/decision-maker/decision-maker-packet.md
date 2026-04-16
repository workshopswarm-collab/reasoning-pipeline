---
type: decision_packet
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
question: "Will the price of Bitcoin be above $70,000 on April 16?"
market_id: b5021d2c-0b79-403b-a5df-3221dc962905
external_market_id: 0x24c9d39348a3ca9f3464ac85ac14826cd40c25fb2f4baf545602f1208baaf16c
market_slug: bitcoin-above-70k-on-april-16
platform: polymarket
market_title: "Will the price of Bitcoin be above $70,000 on April 16?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-8b112bd4/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-8b112bd4/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.94
fair_value_high: 0.97
fair_value_mid: 0.955
market_reference_price: 0.985
edge_mid_vs_market_pct_points: -3.0
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T15:40:02.960170+00:00
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
- Primary crux: Bitcoin is still very likely to close above $70,000 on the April 16 noon ET Binance minute because current same-venue spot remains in the mid-73k range with a multi-thousand-dollar cushion, but the market at 0.985 is too close to certainty for a one-day, exact-minute crypto settlement where a 5% downside move or badly timed wick can still decide the contract.
- One-sentence rationale: BTC is still very likely to finish above $70,000 on the April 16 Binance noon minute, but with fair value closer to 0.955 than the 0.985 market and nonzero one-day exact-minute downside risk still live, the disciplined output remains watch-only rather than an authorized Yes trade.

## Why this is the right action / no-action call

This is a very high-probability but still slightly overconfident crypto threshold market: directional Yes survives, execution value does not.

## Valuation

- Fair value low: 0.94
- Fair value high: 0.97
- Fair value midpoint: 0.955
- Market reference price: 0.985
- Edge vs market (percentage points): -3.0
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Fresh same-venue and cross-venue context support a very high-probability Yes view, but exact-minute downside-tail risk and lack of near-settlement verification still keep fair value below the market's near-certainty.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0.0
  - `max_p:` 0.88
  - `target_exposure_fraction:` 0.0
  - `notes:` Would require a much cheaper price and still fresh same-venue confirmation.
- `scaled_enter`
  - `min_p:` 0.88
  - `max_p:` 0.94
  - `target_exposure_fraction:` 0.0
  - `notes:` Potential value zone only if the large spot cushion persists and volatility remains contained.
- `hold`
  - `min_p:` 0.94
  - `max_p:` 0.97
  - `target_exposure_fraction:` 0.0
  - `notes:` Bounded fair-value zone; maintain watch-only hold posture.
- `trim`
  - `min_p:` 0.97
  - `max_p:` 0.99
  - `target_exposure_fraction:` 0.0
  - `notes:` Above fair value for a one-minute settlement contract with nonzero one-day downside tail.
- `exit`
  - `min_p:` 0.99
  - `max_p:` 1.0
  - `target_exposure_fraction:` 0.0
  - `notes:` Avoid or exit at extreme prices because exact-minute downside tail still matters despite the large cushion.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T15:40:02.960170+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure at the current price., Treat exact-minute Binance settlement risk as the dominant execution constraint even with a large current cushion., Reopen only if market cheapens materially or a fresher near-settlement Binance check shows the cushion holding with subdued volatility.

## Invalidation

### Thesis breakers
- BTC loses cushion materially and trades back toward 71k-70k on Binance before the Apr 16 fixing window.
- A major downside crypto, macro, or exchange-specific shock materially raises the probability of a sub-70k settlement minute.
- Binance-specific settlement-surface or operational issues emerge near resolution.

### Market structure breakers
- Market reprices materially without corresponding same-venue spot deterioration, changing the value comparison.
- Binance microstructure or liquidity behavior near the fixing window becomes abnormal.

### Time breakers
- A fresh direct Binance observation closer to Apr 16 12:00 ET should supersede this packet before any action.
- The actual Apr 16 12:00 ET Binance 1-minute close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to fair value or if later pre-fix Binance checks show the cushion still large with reduced downside risk.
- Downgrade if BTC loses cushion or if downside volatility or catalyst risk increases.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a 5%+ one-day downside move or noon-minute wick landing exactly on the settlement candle.
- Whether overnight and U.S.-morning conditions remain calm into the fixing window.
- How much exact-minute Binance microstructure deserves additional discount despite the large current cushion.

### Reasons to pass / stay small
- The current market price is above bounded fair value.
- This is still a one-minute single-venue settlement contract where path risk matters more than broad BTC direction.
- The remaining edge is small and not strong enough to justify authorization at near-certainty pricing.

### What would change my mind
- A fresh Binance check near settlement still showing BTC comfortably above 72k-73k with calm volatility would move me somewhat closer to market.
- A move back toward 71k-72k would reduce fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: This is a very high-probability but still slightly overconfident crypto threshold market: directional Yes survives, execution value does not.

## Notes for downstream evaluator

Bitcoin is still very likely to close above $70,000 on the April 16 noon ET Binance minute because current same-venue spot remains in the mid-73k range with a multi-thousand-dollar cushion, but the market at 0.985 is too close to certainty for a one-day, exact-minute crypto settlement where a 5% downside move or badly timed wick can still decide the contract.
