---
type: evidence_map
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
research_run_id: 186adea0-afa8-450a-b2f6-69014d91ab49
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-1-minute-candle-on-2026-04-20-close-above-68000
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 68000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-79281f9a/researcher-analyses/2026-04-15/dispatch-case-20260415-79281f9a-20260415T202526Z/personas/base-rate.md"]
tags: ["evidence-map", "btc", "base-rate"]
---

# Summary

The outside-view lean is Yes because the threshold is materially below prevailing Binance spot and recent realized prices, while the remaining No paths are mostly short-horizon shock or resolution-mechanics risks.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 20, 2026 close above 68,000?

## Current lean

Lean Yes, high probability but not certainty.

## Prior / starting view

Before checking current prices and exact rules, the generic prior for a five-day BTC threshold market should be sensitive to both volatility and the distance between current spot and threshold. A threshold far below current spot should usually resolve Yes absent a material shock.

## Evidence supporting the claim

- Binance current spot around 74.6k during research.
  - Source: Binance source note.
  - Why it matters: direct settlement-venue evidence showing a roughly 6.5k cushion above the threshold.
  - Direct or indirect: direct.
  - Weight: high.

- Binance daily closes from April 7 through April 15 all above 68k.
  - Source: Binance source note.
  - Why it matters: supports regime persistence rather than one isolated spike.
  - Direct or indirect: direct.
  - Weight: high.

- CoinGecko 30-day series broadly confirms BTC trading in the same general range across venues.
  - Source: CoinGecko source note.
  - Why it matters: independent contextual check against Binance-only overfit.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- BTC is volatile enough that a 5-day drawdown of more than 6k is possible.
  - Source: inferred from recent crypto volatility plus Binance daily range behavior.
  - Why it matters: the contract settles on one minute, so timing risk is concentrated.
  - Direct or indirect: contextual.
  - Weight: medium-high.

- Contract is exchange- and minute-specific.
  - Source: Polymarket rules note.
  - Why it matters: even if broad BTC sentiment remains positive, a venue-specific wick or brief selloff at noon ET can still produce No.
  - Direct or indirect: direct on contract mechanics.
  - Weight: medium.

## Ambiguous or mixed evidence

- Market-implied probability near 97% may reflect correct pricing, but it also leaves little room for operational or volatility tails.
- BTC strength can persist for days, but crypto can also gap sharply on macro, regulatory, or liquidation-driven news.

## Conflict between inputs

There is no major factual conflict across sources. The main disagreement is weighting-based: how much probability to assign to sharp short-horizon downside or micro-timing risk despite the current cushion above 68k.

## Key assumptions

- Current trading regime broadly persists into April 20.
- Binance remains a usable and representative settlement source.
- No large idiosyncratic shock hits BTC before the settlement minute.

## Key uncertainties

- Short-horizon crypto volatility over the next five days.
- Whether a noon ET one-minute close can briefly dip below a level that broader daily context would suggest is safe.
- Any late-breaking exchange-specific or contract-interpretation issue.

## Disconfirming signals to watch

- BTC losing 72k and then 70k before the weekend.
- A sharp macro risk-off move with crypto leading downside.
- Binance-specific price dislocations or outages.

## What would increase confidence

- Continued Binance closes above 72k into April 18-19.
- Additional independent context showing stable cross-exchange pricing and no major risk catalyst.
- Clean confirmation of the noon ET timing and final-candle handling from settlement practice.

## Net update logic

The initial outside-view leaned Yes if the threshold was materially below spot. Direct Binance data strengthened that lean because the cushion is large and persistent, while the contract rules clarified that residual risk is not about general direction alone but about one exact exchange-minute print. That keeps the estimate high but below the market.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the base-rate lane stayed constructive but not fully at the market extreme.