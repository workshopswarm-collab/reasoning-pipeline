---
type: evidence_map
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
research_run_id: b6903382-0d33-43ef-b410-c752a884fa22
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "BTC above 72000 at Apr 21 noon ET"
question: "Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21, 2026 close above 72000?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["threshold-close mechanics"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-source-notes/2026-04-16-base-rate-binance-and-polymarket-rules.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/base-rate.md"]
tags: ["evidence-map", "btc", "threshold-close", "polymarket"]
---

# Summary

This is a moderately favorable Yes setup because BTC is already well above 72000, but the contract is narrower than a generic bullish BTC view: only the single 12:00 ET one-minute Binance close on Apr 21 counts.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21, 2026 close above 72000?

## Current lean

Lean Yes.

## Prior / starting view

Outside-view baseline for a date-specific single-minute close market should be lower than the base rate for "trades above 72k at some point" because path dependency and exact timing matter.

## Evidence supporting the claim

- BTC/USDT was around 73944 during the run; that is ~2.7% above the threshold. Direct contextual evidence; high weight.
- Binance daily closes from Apr 13-15 were all above 74000, and Apr 10-11 were also above 72000. Direct contextual evidence; high weight.
- In the most recent 10 daily candles, 8 closes were above 72000. Direct contextual evidence; medium-high weight.
- In the last 60 daily candles, 10 closes were above 72000, but the recent regime is much stronger than the full 60-day sample. Direct contextual/base-rate evidence; medium weight.

## Evidence against the claim

- The market settles on one exact minute close, not a daily close and not an intraday high. Mechanism-based counterweight; high weight.
- Bitcoin routinely moves multiple percent over a few days; a 2.7% cushion is meaningful but not decisive over a five-day horizon. Contextual evidence; high weight.
- Apr 12 closed below 72000 despite nearby days above it, showing the threshold can be lost quickly even in the current regime. Direct contextual evidence; medium weight.

## Ambiguous or mixed evidence

- Recent regime strength may persist through Apr 21, but crypto is volatile enough that short-horizon continuation and mean reversion are both plausible.
- Market price at 70.5% may partly reflect crowd calibration from recent levels, but could still underweight the contract's single-minute timing risk.

## Conflict between inputs

- No major factual conflict. The main tension is weighting-based: recent above-threshold persistence pushes Yes up, while the narrow resolution mechanic pushes it back down.

## Key assumptions

- BTC remains in roughly the current price regime through Apr 21 rather than suffering a >3% drawdown into noon ET.
- Binance BTC/USDT remains the clean governing source without operational anomaly.

## Key uncertainties

- Exact BTC level around Apr 21 noon ET.
- Whether volatility over the next several days is trend-continuation or regime reversal.

## Disconfirming signals to watch

- Sustained trade back below 72000 before Apr 21.
- Sharp macro/risk-off move that compresses BTC by several percent.
- Any sign of contract/source ambiguity around Binance candle timestamping, though current rules seem fairly clear.

## What would increase confidence

- Continued daily/hourly closes above 72000 through Apr 19-20.
- Market stabilization above the mid-73k area into the settlement window.

## Net update logic

The outside view starts below a naive spot-price extrapolation because exact-time close contracts are stricter than generic trend bets. Recent Binance closes materially above 72000 move the estimate clearly above 50%, but not all the way to certainty because a single adverse 3-4% move before Apr 21 noon ET would be enough to lose.

## Suggested downstream use

Use as forecast update input and as an audit trail for why the base-rate view is somewhat below the bullish recent-price narrative while still leaning Yes.