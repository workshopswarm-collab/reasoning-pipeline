---
type: source_note
case_key: case-20260415-b4a49d1b
dispatch_id: dispatch-case-20260415-b4a49d1b-20260415T000939Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-b4a49d1b | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 70000 on April 20, 2026?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-implied, source-note]
---

# Summary

This source note captures the live market-implied baseline and the stated contract mechanics for the April 20 BTC above-70000 market.

## Key facts extracted

- The specific threshold market in scope was trading around 86 cents Yes / 16 cents No on the fetched page, consistent with the assignment's `current_price: 0.86`.
- Resolution is based on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone on April 20, 2026.
- The market resolves Yes only if that candle's final Close price is strictly higher than 70000.
- The page explicitly says this is about Binance BTC/USDT, not other exchanges or other pairs.
- Price precision is determined by the source's displayed decimal places.

## Evidence directly stated by source

- Polymarket page listed the 70000 line at roughly 85% and the trade buttons at 86 cents Yes / 16 cents No.
- Rules text: "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- Rules text: "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."

## What is uncertain

- The public HTML capture does not itself expose the exact 12:00 ET future candle; it only provides the rules and current market odds.
- The page does not independently verify Binance UI accessibility or any edge-case handling beyond the written rules.

## Why this source may matter

This is the governing contract surface for the bet. It defines the threshold, the source of truth, the exact pair, the relevant timeframe, and the strict comparison operator.

## Possible impact on the question

It makes the key question narrower than generic "Bitcoin above 70k on April 20" phrasing: all of the following must hold for Yes: (1) Binance spot BTC/USDT remains the governing market, (2) the relevant candle is the one-minute candle at 12:00 ET/noon on April 20, and (3) the final close is strictly above 70000.

## Reliability notes

The contract page is authoritative for market wording but not itself the eventual price-settlement source. Reliability for the contract mechanics is high; reliability for the underlying BTC price level is indirect because that must come from Binance at resolution time.
