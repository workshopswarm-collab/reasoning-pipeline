---
type: source_note
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-de71fc13 | market-implied
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-13 close above 68000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket event rules page
source_type: market rules / contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-13
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, contract-interpretation, settlement]
---

# Summary

The Polymarket event page specifies that resolution depends on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 13, using the final close price, and that the price must be higher than 68,000 for a Yes resolution.

## Key facts extracted

- The market resolves Yes if the Binance 1-minute candle for BTC/USDT `12:00` in ET has a final close above 68,000.
- Otherwise it resolves No.
- The resolution source is Binance, specifically the BTC/USDT chart with `1m` and `Candles` selected.
- The market is explicitly about Binance BTC/USDT, not other exchanges or other pairs.
- Price precision is determined by the number of decimals in the source.
- The market page showed the 68,000 line trading at roughly `99.7%` / `current_price 0.929` in assignment context, i.e. an extreme Yes prior.

## Evidence directly stated by source

- Contract mechanics require all of the following for Yes: correct date, noon ET candle, Binance venue, BTC/USDT pair, 1-minute timeframe, and final close strictly above 68,000.
- The governing source of truth is Binance.

## What is uncertain

- The web-fetched page is a scraped representation of the UI, not the live interactive trading chart itself.
- The exact current displayed price on the market page may move between retrieval and final settlement.
- The rules do not by themselves answer whether BTC will remain above 68k; they only define what must be true for settlement.

## Why this source may matter

This source is necessary to interpret the contract correctly and prevent category errors such as relying on Coinbase, a daily close, or a different time window.

## Possible impact on the question

It sharply narrows the relevant evidence set to Binance BTC/USDT at noon ET. That makes live Binance price evidence much more important than broader crypto commentary.

## Reliability notes

- Primary for contract interpretation: yes.
- Independent from Binance price data: yes, because it comes from the market venue rather than the exchange.
- Main limitation: it defines settlement but does not itself provide the final answer before noon ET.