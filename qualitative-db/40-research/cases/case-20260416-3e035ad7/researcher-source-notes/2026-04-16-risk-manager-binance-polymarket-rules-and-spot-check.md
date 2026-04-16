---
type: source_note
case_key: case-20260416-3e035ad7
dispatch_id: dispatch-case-20260416-3e035ad7-20260416T043505Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 close above 70000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules page plus Binance API spot/klines check
source_type: market-rules-plus-exchange-data
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, contract-check, timing-risk]
---

# Summary

This source note captures the market contract mechanics from the Polymarket event page and a direct spot check of Binance BTCUSDT pricing and recent 1-minute candles via Binance's public API.

## Key facts extracted

- Polymarket rules state the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, 2026 has a final Close price strictly higher than 70,000.
- The rules specify Binance BTC/USDT, not other exchanges or pairs.
- The rules specify price precision is determined by the decimals shown in the source.
- Around 2026-04-16 00:37 EDT, Binance public API returned BTCUSDT spot price 75,010.00.
- Binance public API recent 1-minute klines around 04:35-04:37 UTC showed closes of 74,992.00, 74,975.58, and 75,010.00.
- CoinGecko spot check returned bitcoin USD 74,961, broadly consistent with Binance directionally though not the settlement source.

## Evidence directly stated by source

- Direct from Polymarket rules: the governing resolution source is Binance BTC/USDT 1-minute candle close at 12:00 ET on the title date.
- Direct from Binance API: BTCUSDT was trading roughly 5,000 above the 70,000 threshold at the time checked.

## What is uncertain

- Spot price one day earlier does not guarantee the 12:00 ET candle close on April 17.
- The browser-facing Binance chart is the named resolution surface; API parity is very likely but not independently guaranteed in the rules text.
- A sharp overnight or intraday crash greater than roughly 6.5% before noon ET would still flip the market to No.

## Why this source may matter

The market is extremely one-sided, so the key risk question is whether contract mechanics or timing/path dependence could still matter despite current price being comfortably above the threshold.

## Possible impact on the question

This source strongly supports Yes as the base case because BTC/USDT is materially above 70,000 and the contract is mechanically simple. It also clarifies the main failure mode: not general Bitcoin weakness in the abstract, but a sufficiently large drop by the exact Binance 12:00 ET one-minute close on April 17.

## Reliability notes

- Polymarket rules page is the direct contract source for resolution mechanics.
- Binance public API is highly relevant direct exchange data, but the exact settlement source named by the rules is the Binance chart/candle surface rather than this API endpoint.
- CoinGecko is only contextual verification, not a source of truth.