---
type: evidence_map
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
research_run_id: 3eab7d72-befe-4af0-8b7b-4a47e2c13916
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle close be above 70000 on 2026-04-20?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "crypto", "bitcoin", "binance"]
---

# Summary

The net evidence supports Yes, but less strongly than the market price suggests. Current spot and recent Binance history make above-70k the base case, while the narrow one-minute noon ET settlement condition and normal BTC volatility keep the event meaningfully short of certainty.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-20 have a final close strictly above 70,000?

## Current lean

Lean Yes.

## Prior / starting view

Starting from an outside view, a five-day-ahead threshold bet should rarely deserve near-certainty unless the strike is comfortably out of range or the asset is unusually stable. BTC is not unusually stable, so an 88% market probability needs verification rather than acceptance.

## Evidence supporting the claim

- Binance spot on 2026-04-15 was about 74,066.
  - Source: Binance API source note.
  - Why it matters: gives roughly 5.8% cushion above the strike.
  - Direct/indirect: direct to current price regime, indirect to settlement.
  - Weight: high.

- Recent daily Binance closes were mostly above 70,000.
  - Source: Binance API source note.
  - Why it matters: shows the threshold is inside the recent trading regime, not a tail level.
  - Direct/indirect: indirect to noon settlement but still strong context.
  - Weight: medium-high.

- Last 90 Binance daily candles had 46 closes above 70,000 and 59 highs above 70,000.
  - Source: Binance API source note.
  - Why it matters: outside-view anchor says 70,000 has been a common zone recently.
  - Direct/indirect: contextual/base-rate.
  - Weight: medium.

- Contract uses Binance BTCUSDT specifically, matching the exchange where current spot was checked.
  - Source: Polymarket rules note plus Binance source note.
  - Why it matters: reduces cross-venue mapping risk.
  - Direct/indirect: direct for resolution mechanics.
  - Weight: medium.

## Evidence against the claim

- The contract is narrow: one exact one-minute close at noon ET on one future date.
  - Source: Polymarket rules note.
  - Why it matters: localized volatility can produce No even in an otherwise bullish regime.
  - Direct/indirect: direct to settlement mechanics.
  - Weight: high.

- BTC remains volatile enough that a 5-6% cushion is useful but not decisive over five days.
  - Source: Binance 30d realized-vol proxy and recent daily range behavior.
  - Why it matters: a typical adverse move can erase the margin.
  - Direct/indirect: contextual.
  - Weight: medium-high.

- Extreme market pricing itself is a caution signal.
  - Source: Polymarket price 0.88.
  - Why it matters: near-extreme probabilities can underweight contract narrowness and exchange-specific execution risk.
  - Direct/indirect: contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- 90-day frequency statistics are informative but imperfect because this contract is about one minute at a specific future time, not daily closes.
- Current BTC strength may persist, but crypto weekend/news flows can reprice quickly.

## Conflict between inputs

There is no major factual conflict. The disagreement is mostly weighting-based: how much confidence should current spot and recent regime justify versus the narrow one-minute settlement risk?

## Key assumptions

- BTC remains in roughly the current price regime through April 20.
- Binance remains operationally normal at the settlement timestamp.

## Key uncertainties

- Whether BTC can hold above 70,000 through any weekend volatility.
- Whether noon ET on the resolution date is a benign print rather than a local dip.

## Disconfirming signals to watch

- Daily close back below 70,000 before April 20.
- Sharp increase in intraday volatility with repeated sub-70k dips.
- Binance-specific price dislocation or operational issue.

## What would increase confidence

- Continued daily closes above 72-73k into April 19.
- Cross-exchange spot staying tightly aligned with Binance while BTC remains above the strike.

## Net update logic

The outside view starts below the market because BTC threshold bets with exact minute-based settlement should not casually be treated as near-certain. Current spot around 74k and recent repeated closes above 70k move the estimate strongly toward Yes, but not all the way to the market's 88% because the contract can fail on ordinary volatility without any thesis-level regime change.

## Suggested downstream use

Use this as forecast update input and as an auditable explanation for why base-rate supports Yes but with a haircut relative to the market.