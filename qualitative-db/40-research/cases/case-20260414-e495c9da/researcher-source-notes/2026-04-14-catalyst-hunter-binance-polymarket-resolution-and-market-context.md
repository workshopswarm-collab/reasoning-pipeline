---
type: source_note
case_key: case-20260414-e495c9da
dispatch_id: dispatch-case-20260414-e495c9da-20260414T191806Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the price of Bitcoin be above $70,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance spot API docs plus live BTCUSDT market data, cross-checked against Polymarket market rules
source_type: primary_plus_market_context
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-e495c9da/researcher-analyses/2026-04-14/dispatch-case-20260414-e495c9da-20260414T191806Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, resolution, timing, btc]
---

# Summary

This note combines the governing market rules from Polymarket with Binance's documented kline mechanics and a live BTCUSDT snapshot to establish what exactly must happen for the market to resolve Yes and how far spot BTC is from the threshold with five days left.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 19 has a final Close price above 70,000.
- Polymarket explicitly says the market is about Binance BTC/USDT, not other exchanges or pairs.
- Binance spot API docs describe `/api/v3/klines` as the kline/candlestick endpoint and define the close price field in the kline response.
- Binance docs note kline intervals can be interpreted in a supplied timezone, while startTime/endTime remain UTC.
- Live Binance fetch at research time showed BTCUSDT last price about 74,267.18.
- Binance 24h ticker showed high about 76,038 and low about 72,599.9 over the prior 24h window.

## Evidence directly stated by source

- The resolution source of truth is Binance BTC/USDT 1m candle close at 12:00 ET on April 19.
- The relevant contract is a strict threshold test: close price must be higher than 70,000, not equal.
- Binance kline output includes a defined close price field and timestamped minute bars.
- Recent spot trading has remained materially above 70,000 during the observed 24h window.

## What is uncertain

- The live fetch is only a current snapshot, not a guarantee of the April 19 noon ET close.
- Polymarket references the Binance web chart UI, while my verification used Binance API docs and live API endpoints rather than the exact UI view.
- No single upcoming scheduled macro release was confirmed from web search because search tooling failed during this run.

## Why this source may matter

This is the core source set for contract interpretation and for the most immediate catalyst framing. If BTC is already more than 4,000 above the threshold and the recent 24h low is still above 70,000 by roughly 2,600, then the relevant near-term catalysts are less about a gradual grind higher and more about whether a sharp downside shock can force BTC back below 70,000 exactly at the noon ET minute close on April 19.

## Possible impact on the question

This source set pushes the case toward Yes unless a discrete downside catalyst emerges before resolution. It also narrows the causal question: the market is not asking whether BTC stays strong generally, but whether Binance BTCUSDT specifically closes the noon ET minute above 70,000 on April 19.

## Reliability notes

- Strong on contract mechanics because Polymarket states the resolution rule directly.
- Strong on price mechanics because Binance docs define the kline endpoint and close field.
- Moderate on catalyst calendar coverage because this note is mostly contract-and-market-state focused rather than event-calendar exhaustive.
- Independent enough for this case because the rule source and the price-mechanics source are distinct surfaces, though both ultimately rely on Binance for final settlement.