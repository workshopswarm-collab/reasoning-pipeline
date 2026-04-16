---
type: source_note
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Polymarket rule surface for Apr 17 BTC above 74000 market
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on Apr 17 close above 74000?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market_rules_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15T22:55:00-04:00
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, market-rules, settlement, binance]
---

# Summary

The Polymarket rule surface makes this a narrow, date-sensitive Binance settlement mechanics case: the relevant condition is the **final close** of the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on Apr 17, and that close must be **higher than 74000**.

## Key facts extracted

- Current market price for the 74000 outcome was shown around 73% on the fetched page.
- The page states the market resolves Yes if the Binance 1-minute candle for BTC/USDT at 12:00 in the ET timezone on the specified date has a final close price higher than the threshold.
- It also states the market is about Binance BTC/USDT, not other exchanges or trading pairs.
- Price precision is governed by the source.

## Evidence directly stated by source

- Governing source: Binance BTC/USDT candles.
- Governing condition: the final 1-minute candle close at 12:00 ET on Apr 17.
- Multi-condition implication: both timing and exchange/pair matching matter; being above 74000 before or after the exact minute does not by itself settle the contract.

## What is uncertain

- The page fetch is a readable snapshot and not a signed archival rule export.
- The exact candle-to-timezone implementation is still operationally sensitive at settlement time and should be checked directly on the governing source if the event is close.

## Why this source may matter

This source defines what counts. It is the contract interpretation anchor and prevents confusion with touch/high markets or with broader BTC prices.

## Possible impact on the question

The rules make this meaningfully less permissive than a touch market. That pushes against overconfidence even though BTC is already above 74000 before resolution.

## Reliability notes

- High reliability for contract wording and current market-implied probability.
- Still depends on Binance as the actual settlement source, so final proof must come from the governing venue, not only from the market page.