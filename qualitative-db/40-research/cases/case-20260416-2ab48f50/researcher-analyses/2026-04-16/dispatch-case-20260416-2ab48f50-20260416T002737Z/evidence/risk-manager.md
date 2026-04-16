---
type: evidence_map
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416-2ab48f50-20260416T002737Z
research_run_id: 66676d1a-96dc-4c2a-b777-5644bc3cf0cb
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416T002737Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "threshold-market", "timing-risk"]
---

# Summary

Net evidence favors Yes, but only modestly. The key risk is that the market resolves on one exact future Binance minute close, so a small current cushion does not justify high confidence.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for April 17 at 12:00 ET have a final Close above 74,000?

## Current lean

Cautious Yes.

## Prior / starting view

A threshold market with BTC already near or above the strike should start slightly above 50%, but narrow time-specific resolution creates material path risk.

## Evidence supporting the claim

- Binance direct price context: BTCUSDT traded around 74,770 at capture time, above the 74,000 threshold. Direct evidence. High relevance, medium weight.
- Recent Binance 1m candles showed BTC holding in the mid-74k area rather than barely touching the strike. Direct evidence. Medium relevance, medium weight.
- CoinGecko 2-day context showed BTC trading in a roughly 73.8k to 75.5k range, so 74,000 is a plausible hold level rather than an outlier target. Contextual evidence. Medium relevance, modest weight.
- Polymarket adjacent strikes were internally coherent: 72k priced much higher and 76k much lower, with 74k in the middle. Contextual market-structure evidence. Medium relevance, modest weight.

## Evidence against the claim

- The strongest disconfirming consideration is timing fragility: Yes requires one exact future minute close on Binance, not a daily average or any intraday touch. Direct contract-interpretation risk. High weight.
- BTC is volatile enough that a modest decline from current levels could put the settlement minute below 74,000 even if the broader trend remains healthy. Contextual evidence. High weight.
- CoinGecko context implies the recent range comfortably includes sub-74k outcomes, so the threshold is not safely beneath the market. Contextual evidence. Medium weight.

## Ambiguous or mixed evidence

- Current spot being above the strike is directionally positive but can be overread; for a volatile asset with a one-minute-close resolution, current price is only a partial signal.
- CoinGecko confirms broad context independently, but because it is not Binance it cannot resolve venue-specific microstructure questions.

## Conflict between inputs

There is little direct conflict between inputs. The main disagreement is interpretive: whether a current price above the strike should justify something near the market's 61% or a more cautious estimate because of path dependence.

## Key assumptions

- Current Binance strength has some persistence into the specified settlement window.
- No material exchange-specific anomaly changes the meaning of the relevant minute close.
- BTC remains in the recent range rather than breaking sharply lower.

## Key uncertainties

- Overnight macro or crypto-specific risk-off moves.
- Exact path into the noon ET minute.
- Venue-specific print behavior at resolution time.

## Disconfirming signals to watch

- Binance BTCUSDT losing 74,000 decisively before the resolution window.
- Adjacent strike pricing weakening sharply at 74k while downside strikes remain firm.
- Elevated market-wide volatility into the settlement window.

## What would increase confidence

- Continued Binance trading comfortably above 74,500 closer to resolution.
- Evidence that the market is holding above 74,000 across multiple hours rather than only brief spikes.
- Additional exchange-independent context showing broad crypto risk appetite still supportive.

## Net update logic

The case starts slightly bullish because BTC is already above the strike, but risk management pushes the estimate down from an easy extrapolation because the contract is narrow and timing-sensitive. That leaves a modest Yes edge rather than a strong one.

## Suggested downstream use

Use as Orchestrator synthesis input and as a caution against over-weighting spot-above-strike observations in narrow-resolution crypto markets.