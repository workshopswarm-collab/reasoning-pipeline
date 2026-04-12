---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-11
persona: variant-view
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-72k-on-april-11
question: Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-11 close above 72000?
driver: reliability
date_created: 2026-04-11
source_name: Polymarket market page and rules text
source_type: market contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-11
source_date: 2026-04-11
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/variant-view.md]
tags: [polymarket, rules, resolution, btcusdt]
---

# Summary

The market resolves using the Binance BTC/USDT 1-minute candle for 12:00 ET on April 11, specifically the candle's final close price, with price precision determined by Binance source decimals. That contract wording makes timing and source interpretation more important than broad Bitcoin narrative.

## Key facts extracted

- Resolution condition is whether the Binance 1-minute candle for BTC/USDT at `12:00` in ET has a final close above `72,000`.
- Resolution source is Binance, specifically the BTC/USDT close prices visible on the Binance trading page with `1m` and `Candles` selected.
- The rules emphasize this is not about other exchanges or other trading pairs.
- Price precision is determined by the number of decimals in the source.
- Market page at fetch time showed the 72,000 line trading around `90.8%` Yes / `9.6%` No.

## Evidence directly stated by source

Direct rules text from the market page states:
- `This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title.`
- `The resolution source for this market is Binance, specifically the BTC/USDT "Close" prices currently available at https://www.binance.com/en/trade/BTC_USDT with "1m" and "Candles" selected on the top bar.`

## What is uncertain

- The wording `12:00 in the ET timezone` can create a timing-audit need because Binance natively timestamps many feeds in UTC; researchers should map noon ET to 16:00 UTC on this date.
- The rules reference the website chart rather than the API explicitly, leaving mild source-of-truth ambiguity about UI-versus-API parity or later corrections.

## Why this source may matter

This is the contract-defining source. It determines what counts, what pair matters, what timeframe matters, and which exact candle is governing.

## Possible impact on the question

This source narrows the real uncertainty. The main live question is not generic Bitcoin direction but whether BTC/USDT on Binance stays above 72,000 into the exact noon-ET minute close.

## Reliability notes

Very high relevance because it defines the contract. It is not independent from the market itself, so it should be paired with direct Binance data and at least one extra verification pass on timing/mechanics.