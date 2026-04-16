---
type: source_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260416-989964fe | market-implied
question: Will the Binance ETH/USDT 12:00 ET one-minute candle close on 2026-04-17 be above 2200?
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko Ethereum USD spot and 1-day market chart
source_type: secondary market data aggregator
source_url: https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd ; https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=1
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: market-implied
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/market-implied.md]
tags: [crypto, ethereum, coingecko, crosscheck]
---

# Summary

CoinGecko cross-checks the broad ETH/USD level at roughly 2354.45 and shows the prior day trading mostly in the low-to-mid 2300s, which supports the idea that Binance trading above 2200 is not an exchange-specific outlier.

## Key facts extracted

- CoinGecko simple price endpoint returned Ethereum at 2354.45 USD.
- The one-day market chart values shown in the fetched output were mostly around 2312 to 2336 during the visible portion, indicating ETH traded consistently above 2200 through the sampled period.
- The cross-check level was within about 1.2 dollars of the Binance ETHUSDT spot quote at fetch time, suggesting no meaningful discrepancy in the broad market reference level.

## Evidence directly stated by source

- Direct quoted ETH/USD spot and recent intraday price samples.

## What is uncertain

- CoinGecko is not the settlement source, so it cannot resolve the contract.
- The chart endpoint is a sampled aggregator feed rather than the exact Binance noon ET minute close.

## Why this source may matter

It provides an independent contextual check that the Binance level is aligned with the broader market and that ETH has not recently been hovering near the 2200 threshold.

## Possible impact on the question

The cross-check makes the extreme Yes price more credible because the threshold is not merely barely in the money; ETH appears to be trading meaningfully above it across venues and through the recent day.

## Reliability notes

- Good for contextual cross-verification, but weaker than Binance for contract settlement.
- Independence is moderate because CoinGecko aggregates market data rather than reproducing Binance rules text.
- Useful mainly to verify that the market is not relying on a stale or isolated exchange print.