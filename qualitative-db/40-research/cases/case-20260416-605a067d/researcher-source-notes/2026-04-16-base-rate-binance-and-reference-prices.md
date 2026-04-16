---
type: source_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: short-dated-price-thresholds
entity: ethereum
topic: ETH/USDT price level versus April 17 noon ET close-above threshold
question: Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 have a final close above 2200?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance spot price and 1-minute klines, with Coinbase and Kraken spot cross-check
source_type: exchange data / market data APIs
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/base-rate.md
tags: [source-note, binance, coinbase, kraken, eth, threshold-market]
---

# Summary

Direct market-data checks show ETH is currently trading well above 2200 across the governing Binance venue and two contextual reference venues. That makes the outside-view starting point favorable to a Yes outcome, but the contract is a **specific timed close** on Binance at **12:00 ET on April 17**, so current spot being above 2200 does not itself settle the market.

## Key facts extracted

- Binance ticker endpoint returned `ETHUSDT` price `2295.50000000` at research time.
- Binance 1-minute klines for the latest 10 candles showed closes mostly in the 2288-2295 range, with no sign of immediate proximity to 2200.
- Coinbase spot endpoint returned ETH-USD `2295.1`.
- Kraken ticker returned ETH/USD last trade `2295.18000`.
- Cross-venue alignment suggests no obvious venue-specific price dislocation near the threshold at research time.

## Evidence directly stated by source

- Binance API directly states the current `ETHUSDT` price.
- Binance kline API directly states recent 1-minute opens/highs/lows/closes.
- Coinbase and Kraken APIs directly state contemporaneous reference spot prices.

## What is uncertain

- The contract resolves on the **final close of the Binance 1-minute candle labeled 12:00 ET on April 17**, not on the current price.
- A roughly 4% downside move over the next day remains plausible in crypto, so current distance from threshold is supportive but not definitive.
- Binance website UI accessibility via fetch was weak, so this note relies on Binance public API as a practical proxy for current market state, while the contract language still points to Binance chart candles as governing source.

## Why this source may matter

This is the most direct available evidence for the governing venue and the best immediate calibration for how much buffer ETH has above the contract threshold heading into the final day.

## Possible impact on the question

Because ETH is about 95 dollars above the threshold, the market starts from a favorable base rate for Yes. But since the event is a **timed close-above** contract rather than an intraday touch, the relevant question is whether ETH can avoid a drop of roughly 4% by noon ET tomorrow on Binance.

## Reliability notes

- Binance is the explicit governing venue in the contract, so its direct market data is high-signal.
- Coinbase and Kraken are independent contextual checks, useful for verifying that Binance is not showing an isolated aberrant print.
- Independence is moderate rather than high because all three are observing the same global crypto market regime.