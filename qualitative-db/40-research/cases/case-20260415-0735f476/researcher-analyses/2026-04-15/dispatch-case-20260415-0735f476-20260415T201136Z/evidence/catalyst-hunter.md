---
type: evidence_map
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: 2a0c6709-c154-45ed-8889-fdeae1614d67
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: threshold-close-markets
entity: bitcoin
topic: "BTC above 70k on April 20 noon ET"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 20 close above 70000?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["threshold-distance"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-catalyst-hunter-polymarket-rules-and-market-snapshot.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-catalyst-hunter-binance-and-coingecko-price-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "btc", "polymarket", "noon-close", "threshold"]
---

# Summary
The evidence currently nets to a high-probability Yes lean, but not one as extreme as the market price, because the contract depends on one precise future Binance minute close rather than a general multi-day price regime.

## Question being evaluated
Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 20, 2026 close above 70,000?

## Current lean
Lean Yes with moderate confidence.

## Prior / starting view
Starting view was that a 93-94% market price might be somewhat too confident because single-timestamp close markets keep residual timing risk alive even when spot is already above the threshold.

## Evidence supporting the claim
- Binance spot around 74.6k on April 15, roughly 6.5% above the threshold.
  - Source: Binance ticker / avg price / 1m klines source note.
  - Causal relevance: gives a meaningful current buffer.
  - Directness: direct to settlement venue, though not direct to final outcome.
  - Weight: high.
- Recent Binance daily candles show multiple consecutive closes above 70k and highs up to ~76k.
  - Source: Binance 1d klines source note.
  - Causal relevance: suggests the market is not barely clinging to the threshold.
  - Directness: direct to venue context.
  - Weight: medium-high.
- CoinGecko cross-check around 74.7k with mild positive 24h change.
  - Source: CoinGecko source note.
  - Causal relevance: reduces risk that Binance is a major outlier.
  - Directness: indirect/contextual.
  - Weight: medium.

## Evidence against the claim
- Settlement is one specific noon ET minute close, not a touch or average over a window.
  - Source: Polymarket rules source note.
  - Causal relevance: preserves timing/path risk.
  - Directness: direct contract evidence.
  - Weight: high.
- There are still about 4.5 days before resolution.
  - Source: case timing + rules.
  - Causal relevance: enough time for a macro or crypto risk-off move to erase the buffer.
  - Directness: direct.
  - Weight: medium-high.
- Fear & Greed Index reading of 23 (Extreme Fear) suggests sentiment backdrop is not euphoric and leaves room for sharp downside moves.
  - Source: Alternative.me fetch.
  - Causal relevance: contextual reminder that volatility regime may still be fragile.
  - Directness: indirect.
  - Weight: low-medium.

## Ambiguous or mixed evidence
- Lack of a specific scheduled bullish catalyst cuts both ways: there is no obvious forced upside trigger, but there also may be no single obvious negative event.
- Recent positive spot level may simply reflect transient strength and does not guarantee the exact noon ET print stays above the line.

## Conflict between inputs
There is no major factual conflict. The main disagreement is weighting-based: how much probability penalty should remain for a precise-timestamp close market despite a sizable current buffer.

## Key assumptions
- BTC remains comfortably above 70k into the final observation window.
- Binance remains a reliable and representative settlement venue.
- No major adverse macro/crypto shock arrives before noon ET April 20.

## Key uncertainties
- Whether weekend or macro volatility compresses the current buffer.
- Whether the noon ET print lands during a transient dip even if the broader regime remains bullish.

## Disconfirming signals to watch
- Spot sliding toward low-72k/high-71k before April 20.
- Rising realized volatility with repeated failed bounces.
- Binance-specific weakness relative to other major venues.

## What would increase confidence
- Additional daily closes above ~73k.
- Continued Binance 1m/5m pricing stability above ~72k into April 19-20.
- Independent high-quality news/context confirming no imminent macro shock.

## Net update logic
The direct venue price evidence is enough to support Yes as the base case. What keeps the estimate below the market is not broad bearishness but contract mechanics: a single future minute close leaves residual timing risk that a simple “BTC is already above 70k” argument can understate.

## Suggested downstream use
Use as forecast update and orchestrator synthesis input, with emphasis on exact contract mechanics and timing-risk discount.