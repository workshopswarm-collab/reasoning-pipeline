---
type: source_note
case_key: case-20260413-600f720f
dispatch_id: dispatch-case-20260413-600f720f-20260413T233138Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: prices
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-13
source_name: Binance daily klines, Coinbase daily candles, and CoinGecko market chart
source_type: contextual market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-600f720f/researcher-analyses/2026-04-13/dispatch-case-20260413-600f720f-20260413T233138Z/personas/market-implied.md]
tags: [binance, coinbase, coingecko, context, volatility, btc]
---

# Summary

Independent contextual price sources show BTC has already rallied from the high-60s to the mid/high-74s by April 13 and has recently printed daily highs in the low- to mid-74k region. That leaves only a relatively small additional move to reach 76k during the remaining week, but it has not happened yet.

## Key facts extracted

- Binance recent dailies show a rapid move from roughly `67k` to daily highs around `72.8k-73.1k` before the current day.
- Coinbase daily candle for the current day captured a high around `74,936.90` and close/open values near the high-74k / low-70k range at fetch time.
- CoinGecko market-chart data showed spot BTC around `74,768` at fetch time on 2026-04-13.
- Taken together, BTC was trading within roughly `1.5k` of the 76k threshold at the time of research.

## Evidence directly stated by source

- Binance API daily kline data directly reports recent BTC/USDT open/high/low/close levels.
- Coinbase candles directly report current and recent daily high values, including one candle high near `74,936.90`.
- CoinGecko chart data directly reports current spot price around `74,768`.

## What is uncertain

- These are contextual sources rather than the governing resolution source for the contract.
- Daily candles understate intraday path detail relative to the Binance 1-minute-high rule used for settlement.
- CoinGecko is an aggregate market-data source, not the settlement venue.

## Why this source may matter

This source set answers the key market-implied question: is 76k a remote move or a modest continuation? Given spot around mid/high-74k, the threshold is close enough that a one-week hit probability above 50% is intuitively defensible.

## Possible impact on the question

These data support the market's broad logic. The contract only needs a brief 76k print on Binance, and current spot is already near 75k. The main remaining uncertainty is whether momentum persists enough to tag the level before week-end.

## Reliability notes

- Binance is highly relevant because it is also the contract's official settlement venue.
- Coinbase provides a useful independent exchange check on the same broad price regime.
- CoinGecko is a good tertiary contextual source but less authoritative than exchange data for this contract.