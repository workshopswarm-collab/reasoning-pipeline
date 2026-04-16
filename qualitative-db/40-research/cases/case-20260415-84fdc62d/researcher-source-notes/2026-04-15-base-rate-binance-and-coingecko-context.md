---
type: source_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 70000?
driver: reliability
date_created: 2026-04-15
source_name: Binance market data plus CoinGecko spot context
source_type: exchange API and secondary market data
source_url: https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [binance, coingecko, spot, base-rate, context]
---

# Summary

Recent direct market context strongly favors a yes resolution because BTC is already well above 70k with several days remaining, but the outside-view caution is that a five-day crypto drawdown of more than 5% is not rare enough to ignore.

## Key facts extracted

- Binance 5-minute average price on 2026-04-15 was about 74.3k.
- CoinGecko simple price showed BTC around 74.4k, which cross-checks the broad market level independently.
- Binance daily candles for the previous 10 days were all above 68k, and most recent daily closes were above 70k.
- In the last 60 Binance daily closes, 23 were above 70k (38.3%), while the last 30 days were above 70k 50% of the time.
- The recent regime is stronger than the 60-day base rate, but not so dominant that a sub-70k print within five days is implausible.

## Evidence directly stated by source

- Binance API returns current BTCUSDT pricing and daily candles directly from the exchange named in the contract.
- CoinGecko independently reports BTC spot around the same level, supporting that Binance is not a one-off stale print.

## What is uncertain

- Daily closes are only a rough base-rate proxy for a specific 12:00 ET one-minute close.
- Short-horizon realized volatility between now and April 20 could still move the market materially.
- CoinGecko is contextual only; it is not the governing source for settlement.

## Why this source may matter

It provides both the current cushion above 70k and a rough outside-view frequency check for how persistent above-70k trading has been in the recent regime.

## Possible impact on the question

The current price level supports yes, but the base-rate evidence argues against treating 86% as automatic. A drop from ~74.3k to below 70k by noon ET April 20 would require a move of roughly 5.8% or more, which is meaningful but not extraordinary in Bitcoin.

## Reliability notes

Binance is high-quality for direct contract-relevant price context because it is the named venue. CoinGecko is a useful independent cross-check on spot regime, but secondary for settlement and only moderately informative for the exact resolution candle.