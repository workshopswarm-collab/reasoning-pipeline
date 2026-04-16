---
type: source_note
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-91430615 | market-implied
question: Will the price of Bitcoin be above $70,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page for bitcoin-above-on-april-19
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, market-rules, market-implied, bitcoin]
---

# Summary

This source establishes both the market-implied baseline and the governing contract mechanics. It shows the $70,000 outcome trading around 90-91% Yes on April 14 and states that resolution depends on the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on April 19.

## Key facts extracted

- The specific market asks whether Bitcoin will be above $70,000 on April 19.
- The displayed probability for the $70,000 outcome is about 90% (the page also shows a 91c Yes quote).
- Resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on the target date.
- The deciding field is the final candle "Close" price, and it must be higher than $70,000.
- The market explicitly says Binance BTC/USDT is the source, not other exchanges or other trading pairs.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- The event page displays the $70,000 line around 90-91% Yes.

## What is uncertain

- The page does not explain why traders assign 90% odds.
- The page display can lag or round; exact market-implied probability should be treated as approximately 0.90 rather than exact to the basis point.
- The page does not by itself show whether Binance API output will perfectly match front-end candle display formatting at resolution time, though the source of truth is clear enough.

## Why this source may matter

It is the governing source for how the market settles and the direct source for the market-implied prior being evaluated.

## Possible impact on the question

This source is necessary to avoid analyzing the wrong instrument, wrong timestamp, or wrong settlement rule. It narrows the question to one exact exchange, one exact pair, one exact minute, and one exact threshold.

## Reliability notes

Useful and necessary for contract interpretation, but it is also the market itself, so it is not independent evidence about where BTC will trade. It should be paired with direct Binance pricing/context sources.