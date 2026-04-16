---
type: source_note
case_key: case-20260414-d5888900
dispatch_id: dispatch-case-20260414-d5888900-20260414T143228Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-14 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules for "Bitcoin above ___ on April 14?"
source_type: market rules / platform page
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-d5888900/researcher-analyses/2026-04-14/dispatch-case-20260414-d5888900-20260414T143228Z/personas/variant-view.md]
tags: [source-note, polymarket, market-rules, resolution]
---

# Summary

This source establishes the market-implied baseline and the operative contract wording. The market page showed the 70,000 outcome priced at effectively 100% (assignment current_price 0.9995), and the rules specify a very narrow settlement mechanic tied to Binance BTC/USDT, 1-minute candles, and the 12:00 ET candle's final close.

## Key facts extracted

- The relevant threshold for this case is 70,000.
- The assignment listed current_price as 0.9995, implying a market baseline of 99.95% for Yes.
- The market page itself also displayed the 70,000 line as 100% at fetch time.
- Resolution is not based on generic BTC spot price; it is based specifically on Binance BTC/USDT.
- Resolution is not based on intraminute highs/lows; it depends on the final close of the 12:00 ET 1-minute candle.
- The date is April 14, 2026, and the page references 12:00 PM ET / noon.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The fetched market page is not itself the final authoritative settlement event; it is the contract/rules surface.
- The page does not independently prove the final 12:00 ET candle close; it only defines how that should be determined.
- The page does not clarify every edge-case scenario around temporary chart/UI discrepancies versus API/database availability, so operational interpretation still matters.

## Why this source may matter

This is the governing source for what counts. The case is date-sensitive and narrow-resolution, so correctly interpreting the contract is at least as important as having a general view on BTC direction.

## Possible impact on the question

This source sharply limits what could invalidate an obvious "Yes": basically only a contract-mechanics issue, a Binance-specific data anomaly, or an unexpectedly massive BTC price collapse into the noon ET close.

## Reliability notes

Strong for contract wording and market-implied baseline, but not sufficient alone for the actual price outcome because it is not the independent underlying settlement data source.