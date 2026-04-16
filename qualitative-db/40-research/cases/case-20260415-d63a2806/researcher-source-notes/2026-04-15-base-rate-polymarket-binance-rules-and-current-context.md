---
type: source_note
case_key: case-20260415-d63a2806
dispatch_id: dispatch-case-20260415-d63a2806-20260415T175526Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: BTC above 72,000 on April 17 noon ET via Binance 1-minute close
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 17, 2026 close above 72,000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance/CoinGecko current price context
source_type: mixed-primary-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, coingecko, btc, threshold-market]
---

# Summary

This note captures the governing resolution mechanics from the Polymarket market page plus current BTC price context from Binance and CoinGecko.

## Key facts extracted

- The market page shows the 72,000 line priced at about 83%, matching the assignment current_price of 0.835 closely enough for analysis.
- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, 2026 has a final Close above 72,000.
- The rule is close-based, not touch-based, and specifically tied to Binance BTC/USDT rather than other exchanges or pairs.
- Current spot context on April 15 around the time of research was about 74.1k on Binance BTCUSDT and about 74.1k on CoinGecko BTC/USD.
- CoinGecko hourly data for the prior day showed BTC trading mostly in the high-73k to mid-74k range, indicating the market is currently above the threshold with roughly two days remaining.

## Evidence directly stated by source

From Polymarket rules:
- Yes if the Binance 1 minute candle for BTC/USDT 12:00 in ET on the specified date has a final Close price higher than the threshold.
- Resolution source is Binance with 1m candles selected.
- Price precision is determined by the source.

From current market surfaces:
- Polymarket page displayed 72,000 outcome around 83%.
- Binance API returned BTCUSDT price 74148.00000000.
- CoinGecko simple price returned bitcoin at 74136 USD.

## What is uncertain

- This source set does not directly prove where BTC will be at exactly 12:00 ET on April 17.
- CoinGecko is contextual only; it is not the governing source.
- Short-dated crypto prices can move materially within two days, so current above-threshold status is informative but not dispositive.

## Why this source may matter

This source set establishes the governing mechanism and current state. The most important distinction is that this is a close-above market at a single minute, not a touch/high market. That materially lowers Yes probability relative to nearby-threshold touch contracts.

## Possible impact on the question

If BTC remains near current levels, Yes is favored because the threshold is about 2.9% below current price. But because the market uses a single-minute close on Binance at noon ET on April 17, ordinary crypto volatility and timing risk still matter.

## Reliability notes

- Polymarket market page is the primary contract/rules source and is the most important source used.
- Binance API current ticker and recent klines are high-quality contextual evidence for current market state, though not themselves the literal settlement screenshot.
- CoinGecko provides an independent contextual cross-check and modestly improves evidence independence.
- Evidence independence is medium: Polymarket and Binance are distinct surfaces for rules vs trading state, while CoinGecko is independent but still derivative of broad market pricing.