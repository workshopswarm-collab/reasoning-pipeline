---
type: source_note
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416-2ab48f50-20260416T002737Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 74000?
driver: reliability
date_created: 2026-04-15
source_name: Binance API and CoinGecko spot context
source_type: exchange market data + independent contextual aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: mildly supportive
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416-2ab48f50-20260416T002737Z/personas/catalyst-hunter.md]
tags: [binance, coingecko, spot-price, intraday]
---

# Summary

Recent live price context places BTC above the contract threshold as of the research time, but only by a modest margin. Binance spot showed BTCUSDT around 74,793.86, while CoinGecko independently showed bitcoin around 74,699 USD. Recent Binance daily candles show BTC closed 74,809.99 on April 14 after trading as high as 75,425, indicating the threshold is near current spot rather than far out of range.

## Key facts extracted

- Binance ticker price at research time: 74,793.86 BTCUSDT.
- CoinGecko simple price endpoint at roughly the same time: 74,699 USD.
- Recent Binance daily closes moved from 70,740.98 on April 11 to 74,417.99 on April 12, 74,131.55 on April 13, and 74,809.99 on April 14.
- Binance 1-minute recent klines show price trading in the 74,5xx to 74,79x area immediately before note creation.

## Evidence directly stated by source

- Binance ticker endpoint returned: {"symbol":"BTCUSDT","price":"74793.86000000"}.
- CoinGecko endpoint returned: {"bitcoin":{"usd":74699}}.
- Binance daily klines show a recent regime around and above the target threshold.

## What is uncertain

- These are snapshots, not predictive sources.
- CoinGecko is contextual because the contract settles specifically on Binance BTC/USDT, not a blended market price.
- The threshold can be crossed or lost by routine intraday volatility before noon ET on April 17.

## Why this source may matter

This source establishes the immediate starting state and indicates that the market is pricing a near-coinflip to modest edge event around current spot rather than an extreme move. It also supports the catalyst view that absent a fresh macro shock, simple mean reversion around current spot may dominate.

## Possible impact on the question

If BTC remains in the recent 74k-75k regime into late morning ET on April 17, Yes is favored. If a negative macro or risk-off catalyst hits before the noon settlement minute, the small buffer above 74k can disappear quickly.

## Reliability notes

Binance is highly relevant because it is the exact settlement venue, though live exchange data is only a snapshot. CoinGecko provides a useful independent check that Binance is not wildly idiosyncratic at research time, but it is secondary to Binance for this contract.
