---
type: source_note
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: polymarket-rules-and-market-baseline
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7d14e3a4/researcher-analyses/2026-04-15/dispatch-case-20260415-7d14e3a4-20260415T231343Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, baseline, resolution]
---

# Summary

The Polymarket market page provides the contract mechanics and the current market-implied baseline. For the 72,000 strike on April 19, the page showed approximately 87% for "Yes" and specified that resolution depends on the Binance BTC/USDT 1-minute candle at 12:00 ET on the target date.

## Key facts extracted

- The market outcome for 72,000 on April 19 was displayed around `87%`.
- The contract resolves to "Yes" if the Binance BTC/USDT 1-minute candle for `12:00 ET` on the target date has a final close strictly higher than `72,000`.
- The rules explicitly specify Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the source.

## Evidence directly stated by source

- Current market baseline around 87%.
- Exact timing condition: 12:00 ET on April 19.
- Exact instrument/source condition: Binance BTC/USDT 1-minute candle close.
- Strict threshold logic: close must be higher than 72,000.

## What is uncertain

- The market page is a trading surface and can reflect stale snippets or UI duplication; it should be treated as authoritative for the listed contract text but not as an independent price source for BTC itself.
- The page does not explain fallback behavior for exchange outages or data display anomalies; that is a minor operational ambiguity.

## Why this source may matter

This is the governing contract text and current market-implied baseline. It defines what all material conditions are and what source of truth controls resolution.

## Possible impact on the question

This source frames the entire analysis: the question is not whether BTC is generally strong by April 19, but whether Binance BTC/USDT specifically prints a 12:00 ET 1-minute close above 72,000 on that date.

## Reliability notes

- High relevance because it is the contract page itself.
- High authority for contract wording and market-implied price.
- Lower value as independent evidence on underlying BTC direction, since it is not an external price-data source.