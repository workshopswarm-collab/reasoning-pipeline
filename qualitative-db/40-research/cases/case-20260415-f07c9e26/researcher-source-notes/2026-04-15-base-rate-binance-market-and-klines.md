---
type: source_note
case_key: case-20260415-f07c9e26
dispatch_id: dispatch-case-20260415-f07c9e26-20260415T013036Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT market data and Polymarket rules page
source_type: exchange_market_data_plus_market_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-f07c9e26/researcher-analyses/2026-04-15/dispatch-case-20260415-f07c9e26-20260415T013036Z/personas/base-rate.md]
tags: [binance, polymarket, resolution-source, minute-candle, base-rate]
---

# Summary

This source note captures the direct resolution mechanics from the Polymarket market page and the relevant direct Binance price surfaces used for a base-rate view.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT 1 minute candle for 12:00 in ET on April 16, using the final Close price.
- The contract is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Around research time, Binance spot BTC/USDT last price was 74,663.59.
- Binance 24h range at research time was 73,795.47 to 76,038.00, meaning spot was already comfortably above the 72,000 threshold.
- A direct timestamp check on recent Binance 1m klines showed exchange timestamps mapping cleanly to America/New_York time, so the target observation is the candle opening at 12:00 ET on 2026-04-16, with the reported close for that minute governing resolution.
- Using recent Binance daily closes as a rough base-rate reference, among the last 58 days where BTC daily close was above 72,000, the next day also closed above 72,000 on 54 occasions (93.1%). Among the last 52 days where daily close was above 74,000, the next day closed above 72,000 on all 52 occasions. This is not the exact contract metric, but it is a useful outside-view stability check.

## Evidence directly stated by source

- Polymarket rules explicitly identify Binance BTC/USDT 1m candle close at 12:00 ET as the source of truth.
- Binance direct market data reports current spot and 24h range directly.

## What is uncertain

- Binance public API surfaces used here are not the exact same chart UI named in the Polymarket rules, though they are exchange-native and materially consistent with the stated source.
- The daily-close persistence check is only an approximation for the exact noon-minute contract and should be treated as contextual base-rate evidence, not direct settlement evidence.
- Extreme overnight volatility could still drag BTC below 72,000 by the target minute even from the current mid-74k level.

## Why this source may matter

This is the highest-value source set for the case because it combines the governing contract mechanics with direct exchange-native pricing and a quick persistence check on analogous short-horizon states.

## Possible impact on the question

Because the contract only asks whether Binance BTC/USDT remains above 72,000 at one specified minute, the fact that current Binance spot is roughly 2.7% above the threshold and recent analogous next-day states usually persist supports a high-probability Yes view, though not certainty.

## Reliability notes

- Primary settlement mechanics source quality: high.
- Exchange-native spot data quality: high.
- Independence across the two components is only medium because both depend on the same market venue and contract design.
- Best use is direct for resolution mechanics and current level; contextual for persistence/base-rate inference.
