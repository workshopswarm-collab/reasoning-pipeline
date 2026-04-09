---
type: source_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: crypto
subdomain: spot-market-resolution
entity: ethereum
topic: case-20260409-21554cf3 | catalyst-hunter
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-09 close above 2100?
driver: reliability
date_created: 2026-04-09T03:40:00-04:00
source_name: Binance spot API market data plus Binance kline endpoint documentation
source_type: exchange-api-docs-and-live-market-data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/catalyst-hunter.md]
tags: [binance, ethusdt, resolution-source, candle-verification, api]
---

# Summary

Binance's own spot API documentation confirms that `/api/v3/klines` returns 1-minute candles identified by open time, with `startTime` and `endTime` interpreted in UTC even if a `timeZone` parameter is supplied. Live Binance ETH/USDT market data around 03:37-03:39 ET on 2026-04-09 showed ETH/USDT near 2183.45-2183.50, about 3.98% above the 2100 threshold, with the 24h low still at 2162.00 and the last 180 one-minute closes staying in a tight 2176.13-2188.50 range.

## Key facts extracted

- Binance docs: `GET /api/v3/klines` is the relevant candle endpoint and candle bars are uniquely identified by open time.
- Binance docs: `startTime` and `endTime` are always interpreted in UTC.
- Noon America/New_York on 2026-04-09 converts to 2026-04-09 16:00:00 UTC, or Unix ms `1775750400000`.
- Live Binance ETH/USDT ticker at research time printed `2183.50000000`.
- Binance 24h stats at research time printed high `2270.55`, low `2162.00`, last `2183.50`, 24h change `-2.887%`.
- Binance depth snapshot showed immediate bid/ask around `2183.44` / `2183.45`.
- Binance 180-minute sample around research time showed last close `2183.45`, min `2176.13`, max `2188.50`; that range is only about 0.57%.

## Evidence directly stated by source

- Binance documentation directly states the kline endpoint mechanics and UTC handling.
- Binance live API directly states the current ETH/USDT spot price, order book, and 24h range.

## What is uncertain

- The actual resolving 12:00 ET candle is still in the future at research time, so no source can directly settle the market yet.
- The Polymarket rule text points users to the Binance web chart UI, while this note relies on Binance's official API as the closest auditable direct market-data surface before resolution.
- A large macro or crypto-specific catalyst between 03:40 ET and 12:00 ET could still move ETH materially.

## Why this source may matter

This is the closest direct source-of-truth surface because the contract explicitly resolves off Binance ETH/USDT 1-minute candle closes. The Binance API/docs also let later reviewers audit the timezone conversion and exact candle logic instead of relying on a visual chart screenshot.

## Possible impact on the question

At research time, ETH had roughly an 83.5-dollar buffer over 2100 and had not traded below 2162 in the prior 24 hours, so the live exchange data supports a high-probability Yes lean absent a fresh downside catalyst.

## Reliability notes

- Primary-source quality is high because the data and docs come from Binance itself.
- Independence is limited because price, depth, and candle data are all from the same venue, but that is acceptable here because the market explicitly resolves to Binance.
- I attempted exact future-candle retrieval for `startTime=1775750400000`, but as expected the endpoint returned no data because the relevant candle had not opened yet.
