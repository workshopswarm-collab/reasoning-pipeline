---
type: source_note
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-d9ca8ddf | base-rate
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rule text for Bitcoin above $72,000 on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract, market-implied-probability, resolution-rules]
---

# Summary

This source establishes the market-implied probability and the operative contract language. It is not the final resolution source, but it is the authoritative source for how Polymarket says the contract should settle.

## Key facts extracted

- The event page showed the 72,000 threshold trading at about 93% Yes at fetch time.
- The title/date indicate the relevant observation window is April 17, 2026.
- The rule text says the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone (noon) on the specified date has a final Close above 72,000.
- The source-of-truth named by the market is Binance BTC/USDT with 1m candles selected.
- The rule text also says the market is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by Binance's displayed decimal precision.

## Evidence directly stated by source

- Direct evidence on contract mechanics: yes.
- Direct evidence on current market pricing: yes.
- Direct evidence on whether BTC will actually be above 72,000 on April 17: no.

## What is uncertain

- The event page itself is not the final settlement print; the actual settlement observation depends on the Binance 12:00 ET 1-minute candle close on April 17.
- The page does not itself provide the April 17 settlement candle in advance.
- The market page does not clarify edge handling beyond the posted rules, so execution issues or chart-interface differences would still need Binance-side verification if settlement became disputed.

## Why this source may matter

The source defines all material conditions for a Yes resolution and shows that the market is pricing the outcome as highly likely. Because the market is at an extreme probability, this source also triggers the need for an extra verification pass.

## Possible impact on the question

It anchors the comparison point: any researcher view should explain whether ~93% is justified given current BTC level, time remaining, and the exact Binance 12:00 ET close condition.

## Reliability notes

- Strong for contract wording because it is the market's own published rule text.
- Only moderate as a pricing snapshot because quotes can move.
- Not independent from the market itself; it should be paired with an external price/context source.
