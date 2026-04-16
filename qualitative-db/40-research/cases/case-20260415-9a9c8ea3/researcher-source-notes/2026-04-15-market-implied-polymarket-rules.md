---
type: source_note
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-9a9c8ea3 | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market-rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-9a9c8ea3/researcher-analyses/2026-04-15/dispatch-case-20260415-9a9c8ea3-20260415T192028Z/personas/market-implied.md]
tags: [polymarket, rules, source-note]
---

# Summary

The Polymarket rules define a narrow, date-sensitive contract: the outcome depends only on the final close price of the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-16, and it must be strictly higher than 72,000.

## Key facts extracted

- Resolution is based on the Binance BTC/USDT market only.
- The relevant observation window is the 1-minute candle for `12:00` in ET on the date in the title.
- The market resolves Yes only if the final close is higher than `72,000`.
- Other exchanges or trading pairs do not count.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

- The rules specify the source of truth.
- The rules specify the time zone and minute.
- The rules specify a strict `higher than`, not `higher than or equal to`, threshold.

## What is uncertain

- The page text does not itself explain any rare exchange-outage or retroactive-correction edge case beyond pointing to Binance as the source.

## Why this source may matter

This is the governing contract source. For a date-sensitive crypto threshold market, resolution mechanics are material, so this source determines what must be true for a Yes outcome.

## Possible impact on the question

This source narrows the analysis to three material conditions: (1) Binance BTC/USDT specifically, (2) the noon ET 1-minute candle on 2026-04-16, and (3) a final close above 72,000. That reduces noise from other exchanges and from intraday highs/lows outside the settlement minute.

## Reliability notes

- High credibility as the contract-defining market page.
- Not independent from the market itself, so it governs rules but does not independently verify the underlying future price path.
