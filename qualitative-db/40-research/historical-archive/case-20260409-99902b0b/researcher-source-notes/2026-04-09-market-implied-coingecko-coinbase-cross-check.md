---
type: source_note
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: market-data-and-information-infrastructure
entity: coingecko
topic: case-20260409-99902b0b | market-implied
question: Will the price of Bitcoin be above $70,000 on April 10?
driver: liquidity
date_created: 2026-04-09
source_name: CoinGecko and Coinbase BTC price cross-check
source_type: market-data aggregator + exchange ticker
source_url: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd
source_date: 2026-04-09
credibility: medium-high
recency: live
stance: neutral
certainty: medium-high
importance: medium
novelty: low
agent: market-implied
related_entities: [coingecko, coinbase, btc, bitcoin]
related_drivers: [liquidity]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-99902b0b/researcher-analyses/2026-04-09/dispatch-case-20260409-99902b0b-20260409T203957Z/personas/market-implied.md]
tags: [cross-check, btc, spot-price, contextual]
---

# Summary

Independent contextual price references broadly matched Binance around the assignment time: CoinGecko showed Bitcoin at $72,390 and Coinbase showed BTC-USD at $72,380.62. This reduces the chance that Binance was showing an idiosyncratic outlier near the threshold.

## Key facts extracted

- CoinGecko simple price endpoint returned Bitcoin USD price `72390`.
- Coinbase ticker endpoint returned BTC-USD price `72380.62` at `2026-04-09T20:40:32Z`.
- Both external references were within about $30 of each other and within about $27 of Binance spot.

## Evidence directly stated by source

- CoinGecko response: `{"bitcoin":{"usd":72390}}`.
- Coinbase response included `"price":"72380.62"` and timestamp `"2026-04-09T20:40:32.088024429Z"`.

## What is uncertain

- Neither source is the governing resolution source for this contract.
- CoinGecko is an aggregator, so methodology and venue mix differ from Binance BTC/USDT.
- Coinbase is BTC-USD rather than Binance BTC/USDT, so stablecoin basis and venue-specific microstructure differences remain possible.

## Why this source may matter

These sources provide an independence check against venue-specific noise or a stale Binance reading. If all major references cluster around the same price well above $70,000, the market's high yes price looks more plausibly efficient.

## Possible impact on the question

This cross-check modestly strengthens the yes case by confirming Bitcoin was broadly trading around $72.38k-$72.39k, not barely above $70k. It does not settle the contract but supports the idea that the market is pricing a real cushion rather than a razor-thin edge.

## Reliability notes

- Good contextual verification value.
- Lower settlement authority than Binance.
- Independence is partial rather than perfect because crypto pricing across venues is highly correlated.