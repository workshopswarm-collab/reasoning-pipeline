---
type: evidence_map
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
research_run_id: d1f43a18-4dc3-4fce-a34f-09d4b152afea
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-68-000-on-april-20
question: "Will the price of Bitcoin be above $68,000 on April 20?"
driver:
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-79281f9a/researcher-analyses/2026-04-15/dispatch-case-20260415-79281f9a-20260415T202526Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "market-implied"]
---

# Summary

This map nets the case for respecting the market’s strong Yes bias against the main reasons not to fully endorse a 97% probability.

## Question being evaluated

Will Binance BTC/USDT print a final 1-minute candle Close above 68,000 for the 12:00 ET minute on April 20, 2026?

## Current lean

Yes is favored by a wide margin, but the market may be somewhat overconfident at 97.15%.

## Prior / starting view

Starting from the live market prior, the default stance was that Yes should be very likely unless contract wording, timing mechanics, or venue-specific issues introduced more risk than the price implied.

## Evidence supporting the claim

- Binance spot/current-klines check shows BTCUSDT around 74.6k.
  - direct source note: 2026-04-15-market-implied-binance-polymarket-price-check.md
  - matters because current level is about 6.6k above strike.
  - direct for present state, indirect for April 20 settlement.
  - weight: high.

- Polymarket contract wording is straightforward and names Binance BTCUSDT 1m Close at 12:00 ET.
  - direct source note: 2026-04-15-market-implied-binance-polymarket-price-check.md
  - matters because low interpretation ambiguity makes market aggregation more trustworthy.
  - direct for resolution mechanics.
  - weight: high.

- CoinGecko external context check roughly matches Binance.
  - direct source note: 2026-04-15-market-implied-coingecko-context-check.md
  - matters because it reduces concern about single-venue anomaly or stale read.
  - indirect/contextual.
  - weight: medium.

## Evidence against the claim

- The contract resolves on one exact one-minute close several days from now, not on current spot.
  - matters because path risk remains real even when spot is well above strike.
  - direct contract/timing risk.
  - weight: medium-high.

- BTC can move >9% over several days during risk-off shocks.
  - matters because the cushion to strike, while large, is not impossibly large for crypto.
  - indirect/base-rate style evidence rather than directly observed in this run.
  - weight: medium.

- Binance-specific operational or price-dislocation risk could matter near the minute even if broader market remains healthier.
  - matters because contract is venue-specific.
  - indirect but structurally relevant.
  - weight: low-medium.

## Ambiguous or mixed evidence

- Cross-venue agreement helps today, but it does not strongly constrain where Binance will print at the exact settlement minute.
- Market confidence itself is informative, but extreme probabilities can also reflect complacency if traders are anchoring too heavily to current spot.

## Conflict between inputs

There is little factual conflict among sources. The main disagreement is weighting-based: how much to discount a comfortable current spot cushion for several days of crypto volatility and exact-minute settlement risk.

## Key assumptions

- BTC remains in roughly the current trading regime through April 20.
- No major venue-specific dislocation occurs on Binance near noon ET on April 20.
- The relevant price reference is the final close of the 12:00 ET minute, not an average or neighboring minute.

## Key uncertainties

- Short-horizon volatility over the next ~4.5 days.
- Event/news risk affecting crypto broadly.
- Whether Binance-specific prints diverge materially from broader BTC spot near settlement.

## Disconfirming signals to watch

- BTC moving toward or below low-70k before April 20.
- Sharp increase in downside volatility.
- Signs of Binance-specific operational issues or unusual price dispersion.

## What would increase confidence

- Continued stability above ~72k into the last 24 hours.
- Additional confirmation that Binance BTCUSDT remains aligned with broader spot.
- No major market-moving macro/crypto shock before the resolution window.

## Net update logic

The evidence keeps the lean strongly on Yes because current spot is far above strike and the settlement rule is clean. The main reason not to fully match 97.15% is that crypto can still move enough in several days for exact-minute settlement risk to matter. So the net update is: agree with the market directionally, but shade modestly below its extremity.

## Suggested downstream use

Use as an input for orchestrator synthesis and for checking whether other personas are being insufficiently market-respecting or, conversely, whether they identify a concrete downside catalyst strong enough to justify a larger discount to the live price.