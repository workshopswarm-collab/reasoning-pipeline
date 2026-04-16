---
type: source_note
case_key: case-20260414-3691b692
dispatch_id: dispatch-case-20260414-3691b692-20260414T170231Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-3691b692 | risk-manager
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance API, Polymarket rules page, CoinDesk technical context
source_type: mixed
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=7 ; https://polymarket.com/event/bitcoin-above-on-april-16 ; https://www.coindesk.com/markets/2026/04/14/here-are-key-bitcoin-price-levels-to-watch-as-the-rally-gathers-steam
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [bitcoin, btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, bitcoin, resolution-mechanics, price-levels]
---

# Summary

This source set establishes the contract mechanics and the immediate price context for the April 16 BTC > 72,000 market. The direct resolution surface is Binance BTC/USDT 1-minute candle close at 12:00 ET on 2026-04-16. Current spot context already sits materially above the strike, but the risk question is whether that cushion can survive two more days and a specific one-minute observation window.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16, using the final candle "Close" price, and resolves Yes only if that close is higher than 72,000.
- Binance API on 2026-04-14 showed BTCUSDT spot around 74,729.43.
- Recent Binance daily candles show BTC closing above 72,000 on 2026-04-09, dipping below on 2026-04-11, then rebounding sharply to 74,417.99 on 2026-04-13, which demonstrates meaningful two-day volatility.
- CoinDesk contextual reporting on 2026-04-14 describes BTC above 74,000 with 75,000 as a near-term volatility release point, implying that movement can accelerate in either direction around current levels.

## Evidence directly stated by source

- Direct / authoritative for resolution mechanics: Polymarket rules page text naming Binance BTC/USDT 1m candle close at 12:00 ET as the governing source of truth.
- Direct / authoritative for price context: Binance ticker and kline API outputs.
- Contextual: CoinDesk notes BTC at four-week highs above 74,000 and highlights 75,000 as a level where hedging flows may amplify moves.

## What is uncertain

- Binance public web UI was not cleanly machine-readable through web fetch, so API outputs were used as the direct exchange data surface for current price context while the Polymarket rules page supplies the explicit resolution wording.
- The eventual resolving candle is two days away; path volatility between now and 12:00 ET April 16 remains the main uncertainty.
- CoinDesk's market-structure interpretation is useful context, but it is not itself a resolution source and should not be overweighted.

## Why this source may matter

The market trades at an extreme implied probability, so the central risk-manager task is not discovering whether BTC is currently above 72,000; it is checking whether the contract mechanics or path volatility could still defeat a high-confidence Yes view.

## Possible impact on the question

These sources support a Yes lean because BTC is already roughly 3.8% above the strike with two days remaining. But they also support discounting certainty below the market's 90% because the contract depends on a specific exchange, a specific one-minute close, and a narrow time window in an asset that recently moved from above 73k to below 71k within days.

## Reliability notes

- Binance API is high-value direct price evidence for current context, though not a forward settlement.
- Polymarket rules are high-value for contract interpretation but are not themselves the final observed candle.
- CoinDesk is a useful secondary contextual source with lower authority than either Binance data or the market rules page.
