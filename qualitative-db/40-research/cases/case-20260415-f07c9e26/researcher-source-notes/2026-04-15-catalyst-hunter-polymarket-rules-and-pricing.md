---
type: source_note
case_key: case-20260415-f07c9e26
dispatch_id: dispatch-case-20260415-f07c9e26-20260415T013036Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-pricing, daily-close]
---

# Summary

This source establishes the exact contract mechanics and the current market-implied baseline for the 72,000 threshold outcome.

## Key facts extracted

- The 72,000 line is trading around 91%, implying a market baseline near 0.905 to 0.91 for Yes.
- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final close above 72,000.
- The resolution source is Binance BTC/USDT with 1m candles selected.
- The market is explicitly about Binance BTC/USDT, not other exchanges or pairs.
- Precision is determined by the decimals shown by the source.

## Evidence directly stated by source

- Contract wording names Binance as the governing source of truth.
- The contract requires all of the following for Yes: correct exchange/pair, correct one-minute interval, correct ET noon timestamp, and close strictly higher than 72,000.

## What is uncertain

- The page is not itself the authoritative settlement source; it points to Binance.
- The web page reflects current pricing but could move quickly before close.

## Why this source may matter

This is the contract-definition surface, so it determines what evidence counts and what timing matters.

## Possible impact on the question

It makes the question mostly a narrow time-specific price-path problem rather than a broad daily-average or cross-exchange Bitcoin question. It also highlights operational/interpretation risk around the exact candle timestamp and venue.

## Reliability notes

Useful and necessary for contract interpretation, but not sufficient alone for settlement because it references Binance as the resolution authority.