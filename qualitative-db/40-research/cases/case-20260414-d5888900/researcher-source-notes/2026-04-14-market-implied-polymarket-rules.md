---
type: source_note
case_key: case-20260414-d5888900
dispatch_id: dispatch-case-20260414-d5888900-20260414T143228Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-d5888900 | market-implied
question: Will the price of Bitcoin be above $70,000 on April 14?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules for bitcoin-above-on-april-14
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-d5888900/researcher-analyses/2026-04-14/dispatch-case-20260414-d5888900-20260414T143228Z/personas/market-implied.md]
tags: [polymarket, contract-rules, resolution-source, binance]
---

# Summary

This source establishes the contract mechanics and governing source of truth. It says the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on 2026-04-14 has a final close above 70,000. It also states that Binance trading-pair data, not another exchange or pair, governs settlement.

## Key facts extracted

- Resolution depends on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone.
- The relevant field is the candle's final close price.
- Threshold is strictly higher than 70,000.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."

## What is uncertain

- The public web page is clear on rules but does not itself expose the historical noon ET candle value in the fetched text.
- Binance API history availability around the exact target minute appears limited or incomplete in live verification, so final settlement still depends on the exchange interface/data source named in the contract.

## Why this source may matter

This is the governing contract source, so it defines both the timing and the exact data source. For a date-sensitive crypto market, contract interpretation matters almost as much as the price level itself.

## Possible impact on the question

This source strongly supports a high Yes probability because the current live market page shows the 70,000 line priced at roughly 100%, consistent with BTC trading well above the threshold. But the source matters most because it limits settlement to a specific exchange, pair, timestamp, and field.

## Reliability notes

Primary source for contract mechanics. High reliability for what counts. Not independently sufficient for the actual historical noon close, but authoritative for the resolution rule.