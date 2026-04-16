---
type: source_note
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules for Bitcoin above 70000 on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [risk-manager.md, risk-manager.sidecar.json, risk-manager.md]
tags: [source-note, polymarket, contract-rules, binance, btc]
---

# Summary

This source is the governing market contract surface. It provides the current market-implied baseline and the exact resolution mechanics that matter more than generic BTC price talk.

## Key facts extracted

- The relevant outcome is "70,000" with Buy Yes around 97.2%, matching the assignment current_price of 0.97.
- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 PM ET on April 17, 2026 has a final Close price strictly higher than 70,000.
- The source of truth is Binance BTC/USDT with 1m Candles selected.
- Price precision is determined by the decimals shown in the source.
- The market is exchange-specific: Binance BTC/USDT, not other exchanges or pairs.

## Evidence directly stated by source

- Resolution is based on a single minute close, not intraday high, daily close, or other exchange composite.
- The timing window is ET noon on the specified date.
- The threshold condition is strictly greater than 70,000.

## What is uncertain

- The page itself does not provide the future Binance print, only the rule.
- It does not clarify operational contingencies beyond the stated source-of-truth language.
- The scraped page duplicates some text and should not be treated as a precision market-data source; it is primarily a contract source.

## Why this source may matter

This is the primary source for contract interpretation. The risk in this case is less about whether BTC is generally strong and more about whether a very specific Binance 1-minute close at a specified ET timestamp ends above the threshold.

## Possible impact on the question

The contract wording reduces ambiguity about what must happen: all of the following must hold for Yes — correct date, correct timezone mapping, correct exchange/pair, correct 1-minute candle, and final Close strictly above 70,000. Any miss on those conditions resolves No.

## Reliability notes

Strong for contract mechanics and current market pricing; not sufficient by itself for probability estimation because it is not an independent source on likely BTC path behavior over the next two days.