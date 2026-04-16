---
type: source_note
case_key: case-20260415-58166133
dispatch_id: dispatch-case-20260415-58166133-20260415T083617Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API klines for BTCUSDT 1m
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, 1m-candles, source-note]
---

# Summary

Direct Binance kline data shows BTC/USDT trading around $74.0k at approximately 04:28-04:37 ET on 2026-04-15, comfortably above the $72,000 threshold that will matter for the April 16 noon ET resolution candle. This does not settle the market, but it establishes that the market is pricing from a spot level already materially above the strike.

## Key facts extracted

- Binance 1-minute klines fetched from the spot API for `BTCUSDT`.
- Returned timestamps map to 2026-04-15 08:28-08:37 UTC, which is 04:28-04:37 ET.
- Observed closes in the sample ranged from 73,972.48 to 74,133.57.
- Latest sampled close in the fetch was 74,112.01.

## Evidence directly stated by source

- Each kline contains open time, OHLC, volume, and close time for a 1-minute BTC/USDT candle.
- The sampled candles were all above 72,000 on close.

## What is uncertain

- This sample is only a short recent window and not the settlement candle.
- The market resolves specifically on the Binance 1-minute candle labeled 12:00 ET on 2026-04-16, so the relevant question is whether BTC stays above 72,000 through the next roughly 31.5 hours.
- API output here is contextual evidence; the contract text points traders to the Binance trading interface candle close as the practical resolution surface.

## Why this source may matter

It is the most direct available primary pricing source connected to the contract’s stated source of truth. It helps bound how far BTC would need to fall for the market to fail.

## Possible impact on the question

Because BTC was already about 2.7%-3.0% above the strike during the research window, the variant bearish case needs a plausible mechanism for a >$2,000 decline before noon ET on April 16, rather than merely mild drift lower.

## Reliability notes

- High relevance because Binance BTC/USDT 1-minute candles are explicitly named in the contract.
- Slight source-of-truth caveat: Polymarket’s text references the Binance website candle display rather than the API endpoint directly, though both should normally reflect the same underlying market data.
- Good for contextual verification, not final settlement until the specific resolution minute is observed.