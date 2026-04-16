---
type: source_note
case_key: case-20260415-75a50190
dispatch_id: dispatch-case-20260415-75a50190-20260415T205116Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-75a50190 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page and Binance BTCUSDT API spot context
source_type: primary_market_rules + direct_exchange_api
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-75a50190/researcher-analyses/2026-04-15/dispatch-case-20260415-75a50190-20260415T205116Z/personas/risk-manager.md]
tags: [source-note, polymarket, binance, contract-mechanics, btc]
---

# Summary

This source note captures the governing contract mechanics from the Polymarket market page plus a direct check of live Binance BTC/USDT API pricing context. Together they are sufficient to establish the source of truth, timing convention, and the rough current distance of spot price from the $72,000 threshold.

## Key facts extracted

- Polymarket rules state the market resolves to "Yes" if the Binance 1-minute candle for BTC/USDT at **12:00 ET (noon)** on **April 21, 2026** has a final **Close** price strictly **higher than 72,000**.
- The rules also state the resolution source is Binance BTC/USDT with **1m** candles selected, and that the market is specifically about **Binance BTC/USDT**, not other exchanges or trading pairs.
- The wording is multi-condition: all of the following must be true for Yes:
  1. correct date: April 21, 2026
  2. correct time bucket: 12:00 ET / noon
  3. correct venue and pair: Binance BTC/USDT
  4. correct field: final 1-minute candle **Close**
  5. strict inequality: Close must be **greater than** 72,000
- Direct Binance API spot-context check on 2026-04-15 showed BTCUSDT around **74,857.01** with recent 1-minute closes in the **74.8k** area.

## Evidence directly stated by source

From the Polymarket rules page:

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From the direct Binance API check:

- `ticker/price?symbol=BTCUSDT` returned `74857.01000000`
- recent `klines?symbol=BTCUSDT&interval=1m&limit=5` returned minute closes clustered around `74802` to `74857`

## What is uncertain

- This source note does not independently establish where BTC will trade at noon ET on April 21; it only establishes contract mechanics and current spot context.
- The API check is not itself the officially cited Polymarket surface for settlement, which points to the Binance trading interface / candle chart. But the API is a highly relevant direct Binance surface for contextual verification.
- Short-horizon crypto price path risk over the next six days remains material.

## Why this source may matter

- It is the governing source-of-truth surface for contract interpretation.
- It removes a common resolution trap: this is not a general BTC price question and not an end-of-day close question; it is one specific Binance minute candle close at noon ET.
- It shows current spot is already several thousand dollars above the threshold, which supports a positive directional lean while still leaving room for volatility-driven failure.

## Possible impact on the question

- The contract mechanics favor a straightforward interpretation with low wording ambiguity.
- Current spot context makes the threshold look reachable and currently in-the-money, but the real risk is path/timing risk by the exact settlement minute rather than broad long-term BTC direction.
- The main downside case is not contract ambiguity; it is BTC retracing below 72,000 by the precise settlement minute on Binance.

## Reliability notes

- Polymarket rules page is the authoritative market contract source for what counts.
- Binance API is a direct exchange source for current BTC/USDT context, though not the exact UI surface named in the rules.
- Evidence independence is only medium because both sources are tightly linked to the same market mechanism rather than independent macro/fundamental analysis.