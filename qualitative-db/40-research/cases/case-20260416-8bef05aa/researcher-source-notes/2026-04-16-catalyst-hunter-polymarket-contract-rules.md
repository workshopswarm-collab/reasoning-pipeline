---
type: source_note
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Polymarket contract mechanics for Apr 21 BTC above 72000 market
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-21 close above 72000?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page and rules text
source_type: market rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/catalyst-hunter.md
tags: [polymarket, rules, source-note, binance, close-market]
---

# Summary

The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 in ET on Apr 21 has a final close price strictly higher than 72,000. It is a close-above market for one exact minute, not a touch market and not a broader daily-close market.

## Key facts extracted

- The threshold in this contract is 72,000.
- The governing time is 12:00 in the ET timezone on Apr 21, 2026.
- The governing metric is the final close of the Binance BTC/USDT 1-minute candle for that exact minute.
- The contract resolves from Binance BTC/USDT candles, not from other exchanges or other BTC pairs.
- Price precision is determined by the decimals shown on the source.

## Evidence directly stated by source

- The rules explicitly say: resolve Yes if the Binance 1-minute candle for BTC/USDT 12:00 in ET has a final close higher than the threshold.
- The rules explicitly say the source is Binance with BTC/USDT, 1m candles selected.

## What is uncertain

- The fetched page text does not itself prove what Binance will display on Apr 21; it only establishes the contract mechanics.
- The page text available via fetch does not independently verify the exact UI behavior at settlement.

## Why this source may matter

This is the primary resolution-mechanics source. It determines what counts, what does not count, and which exact minute and venue matter.

## Possible impact on the question

The source sharply narrows the relevant catalyst frame. Many broad bullish Bitcoin narratives matter only insofar as they keep Binance BTC/USDT above 72,000 specifically into the noon-ET minute on Apr 21. Intraday path above 72,000 before then is not sufficient by itself.

## Reliability notes

- High reliability for contract mechanics because this is the market page itself.
- Source-of-truth ambiguity is low to medium rather than zero because the market page delegates final settlement to the Binance candle surface, which is a separate but clearly named governing source.