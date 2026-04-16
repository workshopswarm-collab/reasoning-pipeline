---
type: evidence_map
case_key: case-20260415-04e7318a
dispatch_id: dispatch-case-20260415-04e7318a-20260415T145259Z
research_run_id: 0f9d20de-246d-4bd3-b08a-bcd8680925fc
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
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
downstream_uses: ["risk-manager-finding"]
tags: ["evidence-map", "bitcoin", "polymarket", "timing-risk"]
---

# Summary

The evidence leans Yes because Binance BTC/USDT is currently above the threshold by a meaningful margin, but the edge is less robust than the 87% market price suggests because the contract settles on a single narrow one-minute close at noon ET.

## Question being evaluated

Whether the Binance BTC/USDT 1-minute candle for April 20, 2026 at 12:00 ET will have a final close above 70,000.

## Current lean

Lean Yes, but with more fragility and timing risk than the market-implied probability appears to price.

## Prior / starting view

Starting view from price alone: likely Yes because spot is materially above threshold. Starting risk-manager concern: an extreme market price on a narrow snapshot market may underprice timing/path risk.

## Evidence supporting the claim

- Binance live spot around 74,163.71 on April 15.
  - Source: researcher-source-notes/2026-04-15-risk-manager-binance-live-price-check.md
  - Why it matters causally: the market only needs BTC to hold above 70k, not rally from below.
  - Direct or indirect: direct current-state evidence from the named settlement venue.
  - Weight: high.

- Recent Binance 1-minute closes all clustered around 74.1k during the verification pass.
  - Source: same source note.
  - Why it matters causally: shows no immediate discrepancy between spot and kline close behavior on the venue that matters for settlement.
  - Direct or indirect: direct current-state evidence.
  - Weight: medium.

- Polymarket rules specify a clean and relatively unambiguous resolution path: Binance BTC/USDT, 1m candle, 12:00 ET, final close.
  - Source: researcher-source-notes/2026-04-15-risk-manager-polymarket-rules-binance-resolution.md
  - Why it matters causally: reduces contract ambiguity and keeps the main question on price/timing rather than interpretive rule risk.
  - Direct or indirect: direct contract evidence.
  - Weight: medium.

## Evidence against the claim

- The contract resolves on a single one-minute close at noon ET rather than a daily average or end-of-day mark.
  - Source: Polymarket rules note.
  - Why it matters causally: a narrow snapshot increases path dependence and the chance of a miss despite generally bullish price action.
  - Direct or indirect: direct contract evidence.
  - Weight: high.

- The threshold buffer is only about 5.6% below current spot.
  - Source: derived from live Binance spot check.
  - Why it matters causally: BTC can move 5-6% in far less than five days; the cushion is helpful but not overwhelming.
  - Direct or indirect: direct arithmetic from current venue price.
  - Weight: high.

- The market price at 0.87 embeds high confidence despite limited evidence beyond current spot level.
  - Source: market page + live price comparison.
  - Why it matters causally: extreme pricing on short-horizon snapshot contracts can underweight volatility and timing tails.
  - Direct or indirect: interpretive.
  - Weight: medium.

## Ambiguous or mixed evidence

- Coingecko simple price check returned roughly 74,133 USD for bitcoin, broadly consistent with Binance but not settlement-authoritative.
- Consistency across sources supports the current price picture, but not the future snapshot outcome.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: whether a roughly 4.1k cushion with five days remaining deserves something near 87% or something modestly lower because of BTC volatility and single-minute timing risk.

## Key assumptions

- Current BTC level is not a transient spike likely to reverse below 70k by April 20 noon ET.
- Binance venue-specific data at settlement will remain straightforward and usable.
- No major macro or crypto-specific shock occurs before the snapshot.

## Key uncertainties

- Short-horizon BTC volatility between now and April 20.
- Whether weekend or pre-noon Monday trading introduces a fast downside move near the snapshot.
- Whether a venue-specific operational issue could complicate final close observation, even if the rule source is otherwise clear.

## Disconfirming signals to watch

- BTC trades back below 72k or especially below 70k before the event.
- Sharp risk-off move across crypto or broader markets.
- Signs of exchange-specific operational disruption around Binance market data.

## What would increase confidence

- BTC holding above 73k through the weekend.
- Additional direct Binance checks on April 19-20 showing stable trading well above threshold.
- Lower realized volatility into the settlement window.

## Net update logic

The run starts with a bullish baseline because current spot is already materially above the threshold on the named settlement venue. Risk review does not overturn that direction, but it meaningfully trims confidence because the contract is a narrow snapshot and BTC can move enough in five days to erase the current cushion. So the correct lean is still Yes, but not as confidently as the market implies.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with emphasis on timing/path-risk discount rather than a directional bearish thesis.