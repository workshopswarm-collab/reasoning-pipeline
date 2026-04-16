---
type: source_note
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-f29db686 | market-implied
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page and rules for Bitcoin above 74,000 on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-implied, source-of-truth]
---

# Summary

The Polymarket market page gives both the current market-implied probability and the contract mechanics. The relevant line is the 74,000 strike at roughly 61%, with rules tying resolution specifically to the Binance BTC/USDT 12:00 ET one-minute candle close on Apr. 17.

## Key facts extracted

- The 74,000 line was quoted around 61% on the market page.
- The market title is for Apr. 17 and resolves at 12:00 PM ET.
- Resolution is based on the Binance BTC/USDT 1-minute candle for `12:00` ET, using the final `Close` price.
- The threshold is strict: the close must be higher than 74,000, not equal to it.
- The contract is exchange-specific: Binance BTC/USDT, not another venue or pair.

## Evidence directly stated by source

- Current market-implied probability is about 0.605 to 0.61.
- Governing source of truth is Binance BTC/USDT 1-minute candle close at noon ET on Apr. 17.

## What is uncertain

- The fetched market page is web-rendered content and not a dedicated raw API export.
- The page did not independently validate whether market price had changed seconds later.
- The page itself does not explain how daylight saving or UI timezone conversion edge cases would be handled beyond saying ET.

## Why this source may matter

This source defines both the thing being priced and how it will be settled. It is indispensable for avoiding false comparisons against the wrong time, exchange, instrument, or condition.

## Possible impact on the question

It anchors the market-implied baseline and sharply narrows the operational question: the trade is not about where BTC is in general tomorrow, but about whether Binance BTC/USDT closes one specific one-minute candle above 74,000 at 12:00 ET.

## Reliability notes

- High relevance because it is the contract page itself.
- Medium-high reliability for rules and current displayed probability, but the final settlement still depends on the linked Binance source rather than Polymarket prose alone.
