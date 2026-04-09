---
type: source_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
analysis_date: 2026-04-06
persona: catalyst-hunter
domain: crypto
subdomain: ethereum
entity: Ethereum
topic: ethereum price threshold market resolution mechanics and observed high
question: Will Ethereum reach $2,200 March 30-April 5?
driver: exchange-specific settlement mechanics
date_created: 2026-04-06T01:38:00Z
source_name: Polymarket market page + Binance API ETHUSDT 1m klines
source_type: primary + direct resolution source
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-march-30-april-5
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [Ethereum, Binance, Polymarket]
related_drivers: [resolution mechanics, exchange-specific price source]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/personas/catalyst-hunter.md]
tags: [primary-source, settlement-source, binance, ethusdt, 1m-candle]
---

# Summary

The key direct evidence is unusually strong for this case because the market page itself specifies the exact resolution rule and exchange source, and Binance provides the relevant ETH/USDT 1-minute candle data directly. The market resolves Yes only if any Binance 1-minute ETH/USDT candle during Mar 30 00:00 ET through Apr 5 23:59 ET has a final High at or above 2200. A direct pull of Binance 1-minute klines across that ET window showed a maximum high of 2167.85, so the threshold was not reached on the governing source.

## Key facts extracted

- Polymarket states the market resolves Yes only if any Binance 1-minute candle for ETH/USDT in the title date range has a final High equal to or above 2200.
- Polymarket states the resolution source is Binance ETH/USDT with the chart set to 1m candles.
- Polymarket explicitly says prices from other exchanges, different trading pairs, or spot markets will not be considered.
- Binance ETHUSDT 1-minute kline data for the full ET window Mar 30 00:00 through Apr 5 23:59 showed:
  - maximum observed 1-minute high: 2167.85
  - timestamp of max high: 2026-04-01 13:03 ET
  - threshold hit status: false
- Spot/context checks from Binance 24h ticker, Kraken ticker, and CoinGecko market data all showed ETH trading around 2116-2118 at the time of verification, consistent with the threshold remaining unhit late in the window.

## Evidence directly stated by source

From the Polymarket market page:
- "This market will immediately resolve to \"Yes\" if any Binance 1-minute candle for ETH/USDT during the date range specified in the title ... has a final \"High\" price equal to or greater than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the ETH/USDT \"High\" prices ... with the chart settings on \"1m\" candles selected on the top bar."
- "Prices from other exchanges, different trading pairs, or spot markets will not be considered."

## What is uncertain

- The web-fetched Polymarket page is a readable extract rather than a signed rules document, but it is the direct market surface and aligns with Binance’s directly queryable kline endpoint.
- Binance UI wording about "final High" could in theory differ subtly from API presentation, but for finalized historical 1-minute candles the API and chart should ordinarily align.
- There is always a small implementation risk if Polymarket applies a hidden override or clarification, but nothing observed suggests that here.

## Why this source may matter

This source pair directly answers the otherwise ambiguous contract-mechanics question. It resolves the flagged issue about whether the source of truth is CEX vs DEX vs a broader spot/index composite and whether "reach" means touch on any venue. Here, only Binance ETH/USDT 1-minute highs count.

## Possible impact on the question

Material and decisive. If the direct Binance 1-minute high never reached 2200 in the defined ET window, the outcome should be No regardless of DEX prints, other CEX prices, or narrative catalysts.

## Reliability notes

- Primary source quality: high. The market page defines the resolution rule.
- Direct evidence quality: high. Binance API exposes the exact 1-minute kline series used for the relevant pair.
- Independence: medium. Polymarket and Binance are not independent on the core point because Polymarket delegates to Binance; contextual price checks from Kraken and CoinGecko are independent but non-governing.
- Main residual risk is interpretation/implementation rather than factual price observation.
