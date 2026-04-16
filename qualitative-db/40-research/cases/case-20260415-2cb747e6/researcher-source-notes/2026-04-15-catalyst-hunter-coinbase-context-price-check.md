---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Coinbase BTC-USD spot API
source_type: exchange_market_data_context
source_url: https://api.coinbase.com/v2/prices/BTC-USD/spot
source_date: 2026-04-15
credibility: medium-high
recency: intraday
stance: neutral
certainty: medium-high
importance: medium
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [coinbase, btcusd, contextual-check, cross-exchange]
---

# Summary

A same-session Coinbase spot API check returned BTC/USD around 74.25k, broadly consistent with Binance BTC/USDT trading near 74.23k.

## Key facts extracted

- Coinbase API returned `{"data":{"amount":"74254.72","base":"BTC","currency":"USD"}}` during this run.
- The Coinbase spot read was within roughly $25 of the Binance spot/API check.

## Evidence directly stated by source

- A second major venue also showed BTC trading comfortably above the 72k threshold during this research pass.

## What is uncertain

- Coinbase is not the settlement source.
- BTC/USD on Coinbase is not identical to BTC/USDT on Binance, so this is contextual rather than dispositive evidence.

## Why this source may matter

It serves as the extra verification pass required by the extreme market probability and date-sensitive contract. It helps check whether Binance’s reading is idiosyncratic or whether the broader market is similarly above the strike.

## Possible impact on the question

This lowers concern that the Binance-above-72k reading is a venue-specific anomaly. It does not materially change the thesis but slightly increases confidence in the current above-strike state.

## Reliability notes

- Independent venue and API, useful for cross-checking.
- Contextual only, since settlement still depends solely on Binance BTC/USDT.