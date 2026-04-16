---
type: decision_packet
case_key: case-20260415-fc70b9f6
dispatch_id: dispatch-case-20260415-fc70b9f6-20260415T072610Z
question: "Will the price of Bitcoin be above $72,000 on April 16?"
market_id: 7da0bb87-594f-4bdb-a7ae-fddfc3f0f8bd
external_market_id: 0xee2d4eeeae30d06342d630e97c23ff423da2e542cbfb30a8ce252b9f47ccc9e3
market_slug: bitcoin-above-72k-on-april-16
platform: polymarket
market_title: "Will the price of Bitcoin be above $72,000 on April 16?"
source_decision_handoff_path: qualitative-db/40-research/cases/case-20260415-fc70b9f6/synthesizer-agent/decision-handoff.md
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260415-fc70b9f6/synthesizer-agent/syndicated-finding.md
source_light_refresh_brief_path:
refresh_mode:
recommended_side: YES
trade_authorization: watch_only
position_policy: hold_only
decision_readiness: ready
fair_value_low: 0.74
fair_value_high: 0.79
fair_value_mid: 0.765
market_reference_price: 0.8
edge_mid_vs_market_pct_points: -3.5
independent_verification_quality: medium
compressed_toward_market_applied: false
decision_confidence: medium
valid_until: 2026-04-16T07:39:51.903912+00:00
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
- Primary crux: Bitcoin is still more likely than not to close above $72,000 on the April 16 12:00 ET Binance minute because directly checked Binance levels were around 73.6k-73.7k, but an exact one-minute settlement with only a modest cushion leaves enough path-dependent downside risk that 0.80 is not clearly cheap.
- One-sentence rationale: Yes remains the base case because Binance BTC/USDT was directly observed above $72,000, but with only a modest cushion and a one-minute settlement rule, the fair value stays around 0.765 and the correct posture at 0.80 is watch-only rather than authorized.

## Why this is the right action / no-action call

Directional truth and execution readiness diverge here: likely Yes, but not at this price and not without a fresher venue-specific check.

## Valuation

- Fair value low: 0.74
- Fair value high: 0.79
- Fair value midpoint: 0.765
- Market reference price: 0.8
- Edge vs market (percentage points): -3.5
- Independent verification quality: `medium`
- Compressed toward market applied: `false`
- Compression reason: Bounded evidence already reflects direct Binance observations and a narrow one-minute settlement framework; the remaining discount comes from unresolved short-horizon path risk rather than generic uncertainty compression.

## Action bands

Define deterministic bands on the market-implied true-probability axis.

- `max_enter`
  - `min_p:` 0
  - `max_p:` 0.68
  - `target_exposure_fraction:` 0
  - `notes:` Would require a much cheaper price and still a fresh Binance check near settlement.
- `scaled_enter`
  - `min_p:` 0.68
  - `max_p:` 0.74
  - `target_exposure_fraction:` 0
  - `notes:` Potential value zone only if same-venue price state remains comfortably above strike.
- `hold`
  - `min_p:` 0.74
  - `max_p:` 0.79
  - `target_exposure_fraction:` 0
  - `notes:` Current bounded fair-value zone; maintain non-authorized hold-only posture.
- `trim`
  - `min_p:` 0.79
  - `max_p:` 0.88
  - `target_exposure_fraction:` 0
  - `notes:` Above fair value for a one-minute settlement contract with live path risk.
- `exit`
  - `min_p:` 0.88
  - `max_p:` 1
  - `target_exposure_fraction:` 0
  - `notes:` Avoid or exit at rich prices because minute-level downside tail dominates remaining edge.

## Execution semantics

- Price axis: `market_implied_true_prob`
- Price source: `market_snapshot_quote`
- Rebalance threshold fraction: 0.1
- Allow auto reversal: `false`
- Quote staleness seconds: 300
- Valid until: 2026-04-16T07:39:51.903912+00:00
- Time horizon: 

## Risk controls

- Max position size (% bankroll): 0.02
- Max additional exposure (% bankroll): 0.01
- Max single order (% bankroll): 0.005
- Slippage tolerance (bps): 100
- Liquidity minimum depth: 0
- Correlation bucket limit (% bankroll): 0.05
- Confidence level: `medium`
- Portfolio constraints: Do not add fresh exposure without a materially better price or a fresher direct Binance check closer to settlement., Treat exact-minute Binance settlement risk as economically decisive for this contract., Hold-only posture is appropriate unless the market cheapens materially or new venue-specific evidence arrives.

## Invalidation

### Thesis breakers
- Direct Binance BTC/USDT trades drift back toward 72k before the fixing window.
- A sharp crypto selloff or Binance-specific dip develops into the settlement minute.
- Evidence emerges that the operative Binance settlement surface differs from the assumed one-minute close mechanics.

### Market structure breakers
- Market pricing moves materially without corresponding spot support, changing the value case.
- Binance API or chart behavior near settlement raises venue-specific execution concerns.

### Time breakers
- A fresh direct Binance observation closer to Apr 16 12:00 ET should supersede this packet.
- The actual Apr 16 12:00 ET Binance candle close fully resolves and obsoletes this judgment.

### Reversal conditions
- Upgrade only if price becomes materially cheaper relative to the same directional fair value or if a fresh pre-fix Binance check shows a larger cushion.
- Downgrade toward forbidden or lower fair value if BTC loses cushion or volatility rises into settlement.
- Do not auto-reverse from this packet.

## Epistemic status

### Key uncertainties
- The true probability of a >2% intraday downswing into the exact settlement minute.
- Whether market participants already have fresher Binance-specific information than the bounded package.
- How much the modest current cushion protects against one-minute wick or venue-specific weakness.

### Reasons to pass / stay small
- The current price is near or slightly above bounded fair value for this exact-minute contract.
- Single-minute settlement path risk remains substantial relative to the claimed edge.
- No fresh direct Binance observation exists near the actual fixing window.

### What would change my mind
- A fresh Binance check near the fixing window showing sustained trade materially above 72k would move me closer to market.
- A move back toward 72k or heightened volatility would lower fair value materially.
- A materially cheaper market price with unchanged Binance cushion would create a cleaner edge.

### Decision quality
- `good_not_clean`

## Audit checks

- Market baseline respected: `true`
- Action bias check passed: `true`
- Self-preservation bias check passed: `true`
- Additional notes: Directional truth and execution readiness diverge here: likely Yes, but not at this price and not without a fresher venue-specific check.

## Notes for downstream evaluator

Bitcoin is still more likely than not to close above $72,000 on the April 16 12:00 ET Binance minute because directly checked Binance levels were around 73.6k-73.7k, but an exact one-minute settlement with only a modest cushion leaves enough path-dependent downside risk that 0.80 is not clearly cheap.
