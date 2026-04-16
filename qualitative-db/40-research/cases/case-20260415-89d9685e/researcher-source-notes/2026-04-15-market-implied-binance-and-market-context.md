---
type: source_note
case_key: case-20260415-89d9685e
dispatch_id: dispatch-case-20260415-89d9685e-20260415T181939Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-89d9685e | market-implied
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Polymarket rules page
source_type: primary-plus-contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-89d9685e/researcher-analyses/2026-04-15/dispatch-case-20260415-89d9685e-20260415T181939Z/personas/market-implied.md]
tags: [binance, polymarket, source-note, market-implied]
---

# Summary

The governing market resolves on the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-16, and the live Binance spot reference checked during this run was about 74.2k, roughly 2.2k above the 72k threshold. Polymarket showed the 72k contract around 94% Yes, implying the crowd sees only a modest chance of a >2.2k drop before the resolution minute.

## Key facts extracted

- Polymarket rules specify the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 16 has a final Close above 72,000.
- The market is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Binance ticker API during this run returned BTCUSDT at 74,200.00.
- Recent Binance 1-minute klines fetched during this run showed BTCUSDT trading in a narrow band around 74,200-74,280.
- CoinGecko spot context during the same window showed bitcoin around 74,266 USD, broadly confirming that Binance was not an outlier print.

## Evidence directly stated by source

- Binance ticker endpoint returned `{ "symbol": "BTCUSDT", "price": "74200.00000000" }`.
- Binance 1-minute klines endpoint returned recent closes around 74,242.54, 74,268.26, 74,279.12, 74,214.96, and 74,199.99.
- Polymarket page stated the exact resolution logic and displayed the 72,000 line near 94% Yes.

## What is uncertain

- This note does not prove where BTC will be at exactly 12:00 ET on Apr 16; it only establishes the current cushion versus the threshold and the exact contract mechanics.
- Short-horizon crypto volatility could erase a ~3% cushion in less than a day.
- Exchange-specific microstructure or brief exchange-specific dislocations could matter because Binance BTC/USDT is the sole source of truth.

## Why this source may matter

This is the key source set for a date-sensitive price-threshold contract: it establishes the source of truth, the relevant pair, the exact timing condition, and the current distance from the strike that the market is pricing.

## Possible impact on the question

The combination of exact contract mechanics plus a current Binance price above 74k supports the market’s high-Yes stance. The main remaining question is not interpretation of the rules but whether sub-day BTC volatility is large enough to push the Binance 12:00 ET Apr 16 close below 72k.

## Reliability notes

- Binance is the explicit settlement source, so it is authoritative for resolution even if not necessarily perfect as a market-wide price reference.
- Polymarket’s rules page is authoritative for contract wording but not for the eventual settlement print itself.
- CoinGecko is a useful contextual cross-check rather than a settlement source.
- Independence is only moderate because both crypto price surfaces ultimately reflect the same underlying market environment.