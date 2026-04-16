---
type: source_note
case_key: case-20260414-76e5614f
dispatch_id: dispatch-case-20260414-76e5614f-20260414T182607Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-76e5614f | risk-manager
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page plus Binance spot API/docs
source_type: primary-contract-and-primary-market-data
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: risk-manager
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, contract-interpretation, btc]
---

# Summary

This note combines the governing contract surface from Polymarket with the named resolution source and a live Binance spot check. It matters because this market is narrow, date-sensitive, and explicitly resolves on a Binance BTC/USDT 1-minute candle close at 12:00 ET on April 17 rather than on any broader BTC spot index.

## Key facts extracted

- Polymarket states the market resolves "Yes" if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close price above 72000; otherwise "No".
- The contract explicitly says the source is Binance BTC/USDT with 1m candles selected, and that other exchanges or pairs do not count.
- The Polymarket market page showed the 72000 line trading around 84 cents Yes / 19 cents No at fetch time, consistent with an implied probability near 0.83-0.84.
- Binance spot API ticker at research time showed BTCUSDT around 74603.24.
- Binance recent 1-minute klines fetched around research time were all around 74522-74573 closes, i.e. materially above 72000.
- Binance API documentation states klines are available via `/api/v3/klines`, uniquely identified by open time, and supports a `timeZone` parameter so exchange candle interpretation can be aligned with the contract's ET framing.

## Evidence directly stated by source

- Contract wording and settlement rule are directly stated by Polymarket.
- Binance docs directly state how kline data is represented and retrieved.
- Binance API directly states current ticker and recent minute-candle closes.

## What is uncertain

- The contract references the Binance UI candle, while this research used Binance public API/docs as a close proxy and verification surface; that is probably aligned but still leaves mild operational/UI-versus-API ambiguity.
- The relevant settlement candle is still about 46 hours away from research time, so current price only establishes distance from threshold, not settlement.
- BTC can move several percent in 1-2 days, so path risk remains meaningful despite current distance above 72000.

## Why this source may matter

This is the best available primary evidence set because it covers both the governing source of truth and the live market state relative to the threshold. For a narrow date-specific market, correctly understanding the exact source and time bucket is as important as directional BTC analysis.

## Possible impact on the question

The source set supports a base view that Yes is favored because current Binance BTC/USDT is ~3.6% above the threshold, but it also highlights the key risk-manager objection: the market pays only on one exact one-minute close on Binance at noon ET on April 17, so timing and venue-specific operational details can still break an otherwise bullish BTC thesis.

## Reliability notes

- Strong on direct contract interpretation and direct market-state verification.
- Independence is only medium because the contract and live data both depend on Binance as the governing venue.
- Good fit for this case because the contract explicitly names Binance, but still not a perfect substitute for the final UI candle that will settle the market.