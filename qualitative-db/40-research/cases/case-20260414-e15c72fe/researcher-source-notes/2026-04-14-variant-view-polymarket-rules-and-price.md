---
type: source_note
case_key: case-20260414-e15c72fe
dispatch_id: dispatch-case-20260414-e15c72fe-20260414T193100Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-e15c72fe | variant-view
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-e15c72fe/researcher-analyses/2026-04-14/dispatch-case-20260414-e15c72fe-20260414T193100Z/personas/variant-view.md]
tags: [polymarket, contract-rules, settlement-source, timing]
---

# Summary

Polymarket's market page gives both the current market-implied probability for the $70k threshold and the controlling resolution mechanics. The key point is that this is not a broad "Bitcoin above $70k by April 20" contract; it resolves off the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on April 20.

## Key facts extracted

- The $70,000 line was trading around 85% on the market page at retrieval.
- Resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 20, 2026.
- The relevant datapoint is the final candle "Close" price, not intra-minute highs/lows.
- The source of truth is Binance, not another exchange or BTC/USD pair.
- Price precision follows the decimals shown in the source.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The web fetch did not expose a historical chart path for the exact future candle; it only exposed the market rules and current prices.
- Polymarket page output alone does not say anything about expected BTC path between now and April 20 beyond crowd pricing.

## Why this source may matter

This is the governing contract surface. It defines the precise timing window, venue, and price field that all must line up for a Yes resolution.

## Possible impact on the question

Because the market is narrow and date-specific, misreading the resolution mechanics could easily create false confidence. A trader can be directionally bullish BTC and still lose if Binance BTC/USDT closes below 70,000 exactly at the noon ET 1-minute candle.

## Reliability notes

High reliability for rules and current market price because this is the contract venue itself. It is not independent evidence on BTC fundamentals or path probability.