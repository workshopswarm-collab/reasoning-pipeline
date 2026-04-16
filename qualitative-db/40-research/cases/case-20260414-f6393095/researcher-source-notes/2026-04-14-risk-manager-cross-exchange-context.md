---
type: source_note
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 70000 on April 17, 2026?
driver: reliability
date_created: 2026-04-14
source_name: CoinGecko and Coinbase BTC price cross-check
source_type: market data aggregator and exchange quote
source_url: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: medium
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [cross-check, coingecko, coinbase, price-context]
---

# Summary

This source note records an additional verification pass using non-Binance price references to confirm that the broader BTC market was also trading well above 70,000 around research time.

## Key facts extracted

- CoinGecko returned BTC at 74,078 USD.
- Coinbase spot returned BTC-USD at 74,113.445.
- These values were close to Binance BTC/USDT around 74,066, suggesting no large venue-specific dislocation at research time.

## Evidence directly stated by source

- CoinGecko API output: `{"bitcoin":{"usd":74078}}`.
- Coinbase API output: `{"data":{"amount":"74113.445","base":"BTC","currency":"USD"}}`.

## What is uncertain

- These are BTC/USD references, not Binance BTC/USDT, so they cannot settle the contract.
- Cross-venue alignment at research time does not eliminate the possibility of a later exchange-specific move or a brief noon ET wick on Apr. 17.

## Why this source may matter

It is a useful independence check against overreliance on one venue/API surface and helps test whether Binance is obviously off-market right now.

## Possible impact on the question

The cross-check modestly strengthens confidence that the current >70k margin is real rather than a Binance-specific anomaly. It does not remove the core timing/path risk of a 1-minute resolution market.

## Reliability notes

Good as contextual verification, not as source of truth. Independence from Binance is useful, but contract relevance is lower than the direct Binance source.