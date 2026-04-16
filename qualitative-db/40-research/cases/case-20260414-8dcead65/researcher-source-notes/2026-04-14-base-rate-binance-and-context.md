---
type: source_note
case_key: case-20260414-8dcead65
dispatch_id: dispatch-case-20260414-8dcead65-20260414T160342Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-15 be above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance API and Polymarket market page with CoinGecko contextual cross-check
source_type: mixed_primary_contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8dcead65/researcher-analyses/2026-04-14/dispatch-case-20260414-8dcead65-20260414T160342Z/personas/base-rate.md]
tags: [binance, polymarket, bitcoin, btc, resolution-source]
---

# Summary

This note captures the direct resolution surface and a contextual spot-price cross-check for the April 15 BTC > 70,000 market.

## Key facts extracted

- Binance BTCUSDT spot ticker at fetch time showed `75461.49`.
- Recent Binance 1-minute klines fetched immediately around the same time showed closes of roughly `75399.99`, `75439.68`, `75468.62`, `75469.03`, and `75469.04`.
- Polymarket's market page states the market resolves from the Binance BTC/USDT 1-minute candle for `12:00 ET` on the specified date, using the final `Close` price, with price precision determined by Binance.
- CoinGecko simple price endpoint showed bitcoin around `75459` USD at roughly the same time, broadly consistent with Binance spot.

## Evidence directly stated by source

- Binance ticker endpoint directly states the current BTCUSDT price.
- Binance klines endpoint directly states recent 1-minute open/high/low/close data.
- Polymarket rules directly state the governing contract condition: Binance BTC/USDT, 1-minute candle, 12:00 ET, final close above 70,000.
- CoinGecko directly states a contemporaneous BTC/USD spot level useful as contextual confirmation rather than settlement.

## What is uncertain

- This does not directly settle the April 15 noon ET outcome because the market resolves on tomorrow's specific 12:00 ET candle, not today's current price.
- CoinGecko is not the settlement source and may differ slightly from Binance BTC/USDT due to exchange and pair differences.
- The Binance public web UI fetch was not cleanly readable through the tool, so contract interpretation relies on Polymarket's quoted rules plus Binance API data rather than the exact UI candle panel.

## Why this source may matter

The key base-rate question is whether BTC being materially above 70,000 with less than a day to resolution makes a sub-70,000 noon close tomorrow unusual enough that a 97.9% implied probability is justified. Direct Binance price data matters more than generalized crypto commentary because the contract is mechanically tied to Binance's own 1-minute close.

## Possible impact on the question

These sources support a high-probability Yes view because the current direct resolution venue level is about 7.8% above the threshold, leaving substantial buffer for ordinary intraday volatility over the next day. They do not eliminate the possibility of a sharp drawdown before noon ET tomorrow.

## Reliability notes

- Primary settlement relevance: high for Binance API price and kline endpoints, though the contract references the Binance trading interface's displayed 1-minute candle close rather than the API explicitly.
- Contract interpretation relevance: high for the Polymarket market rules page.
- Contextual independence: medium because CoinGecko aggregates market prices and is not independent of crypto spot conditions generally, but it is independent of Binance's exact UI and helps check that the fetched level is not obviously anomalous.