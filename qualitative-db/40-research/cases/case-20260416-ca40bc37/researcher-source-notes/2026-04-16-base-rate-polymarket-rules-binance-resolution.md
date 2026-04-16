---
type: source_note
case_key: case-20260416-ca40bc37
dispatch_id: dispatch-case-20260416-ca40bc37-20260416T053546Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules page
source_type: market rules / primary contract context
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, resolution, btc]
---

# Summary

This source provides the market-specific resolution mechanics. It states that the market resolves from the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20, using the final close price, with price precision determined by Binance display precision.

## Key facts extracted

- The market resolves to Yes only if the relevant Binance BTC/USDT 1-minute candle has a final close price strictly higher than 72,000.
- The relevant timestamp is 12:00 in ET timezone on the date in the title, i.e. April 20, 2026.
- The designated source of truth is Binance BTC/USDT, not another exchange or pair.
- The page currently shows the 72,000 line trading around 84-85% Yes.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."

## What is uncertain

- The page does not itself explain how Binance's chart timezone presentation maps to API query parameters.
- It does not define fallback handling if Binance UI behavior changes, though the named source is clear enough for practical interpretation.

## Why this source may matter

This is the governing contract-context source. For a date-specific, multi-condition market, resolution mechanics matter almost as much as directional price view.

## Possible impact on the question

The forecast must answer all material conditions together: correct date, correct timezone, correct exchange/pair, correct 1-minute candle, and strict greater-than threshold.

## Reliability notes

Primary for market rules, but still benefits from an independent Binance-source check because this is a narrow-resolution contract tied to exchange-specific candle mechanics.