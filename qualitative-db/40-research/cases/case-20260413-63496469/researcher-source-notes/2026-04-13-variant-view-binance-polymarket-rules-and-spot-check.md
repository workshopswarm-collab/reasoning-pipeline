---
type: source_note
case_key: case-20260413-63496469
dispatch_id: dispatch-case-20260413-63496469-20260413T173535Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-63496469 | variant-view
question: Will the price of Bitcoin be above $66,000 on April 14?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance BTCUSDT API + Polymarket market rules
source_type: primary_market_data_and_contract_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-63496469/researcher-analyses/2026-04-13/dispatch-case-20260413-63496469-20260413T173535Z/personas/variant-view.md]
tags: [binance, polymarket, contract-rules, spot-price, source-note]
---

# Summary

This source note combines the governing contract rules from Polymarket with a direct spot-data check from Binance API. Together they establish both what the market settles on and the current distance of BTC/USDT from the 66,000 threshold.

## Key facts extracted

- Polymarket says the market resolves to **Yes** if the Binance BTC/USDT **1-minute candle for 12:00 ET on April 14** has a final **Close** price **higher than 66,000**.
- The market is specifically about **Binance BTC/USDT**, not other exchanges or pairs.
- On a direct Binance API spot check performed during this run, BTC/USDT last price was **72,398.00**.
- A direct Binance 1-minute kline pull showed recent closes clustered around **72.4k-72.5k**.
- Converting the latest kline open time `1776101760000` yields **2026-04-13T17:36:00Z**, i.e. **2026-04-13 13:36 ET**, confirming the checked data is roughly **22.4 hours before** the noon-ET settlement minute.

## Evidence directly stated by source

- Polymarket rules directly state the settlement condition and governing source.
- Binance API directly states the latest BTCUSDT traded price and recent 1-minute candle closes.

## What is uncertain

- The market does **not** resolve on current spot price; it resolves on one specific later 1-minute close.
- A large adverse move before noon ET on April 14 could still push BTC/USDT below 66,000 at the relevant closing minute.
- API data confirms current distance from strike but does not by itself prove anything about realized volatility over the remaining window.

## Why this source may matter

This is the core source set for a narrow, date-sensitive contract: one source defines what counts, and the other shows where the governed price currently sits relative to the strike.

## Possible impact on the question

At ~72.4k spot versus a 66k threshold, the contract currently looks very likely to resolve Yes unless BTC falls by roughly **8.8%-9.0%** before the settlement minute. That supports a high Yes probability, but not literal certainty, because the exact settlement minute and Binance-specific print still matter.

## Reliability notes

- Polymarket is authoritative for contract wording but not for final market settlement until the event resolves.
- Binance is the explicit governing source of truth for the relevant price series.
- Evidence independence is only moderate because the contract explicitly points back to Binance; this is still acceptable here because Binance is the source-of-truth surface, not just a supporting source.
- Main residual risk is operational/interpretive rather than source credibility: timezone handling, exact candle minute, and exchange-specific print behavior.