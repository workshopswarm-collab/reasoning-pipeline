---
type: source_note
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-60e5e883 | market-implied
question: Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [market-implied finding, evidence map]
tags: [polymarket, contract-rules, resolution-source, price-ladder]
---

# Summary

This source establishes both the live market-implied probability for the $70,000 threshold and the governing resolution mechanics.

## Key facts extracted

- The relevant line for this run is **70,000**, trading around **93%** Yes on 2026-04-14.
- The market resolves **Yes** if the **Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-17** has a final **Close** price **higher than 70,000**.
- It resolves **No** otherwise.
- The source-of-truth is specifically **Binance BTC/USDT**, not another exchange or pair.
- Precision is determined by the number of decimals shown in the source.
- The same event page shows neighboring strikes: 72k around 77%, 74k around 51%, 76k around 24%, implying the market is centered in the low-to-mid 74k region rather than barely above 70k.

## Evidence directly stated by source

- Explicit settlement source: Binance.
- Explicit timing window: 12:00 PM ET on Apr 17.
- Explicit test condition: final 1-minute candle close must be higher than 70,000.
- Explicit market pricing for the strike ladder.

## What is uncertain

- The page itself is not the settlement data source; it only states what the source-of-truth will be.
- The ladder odds are live market prices and can move.

## Why this source may matter

This is the direct contract/rules source. It is necessary to avoid using the wrong exchange, wrong time window, or wrong condition such as intraday high rather than 1-minute close.

## Possible impact on the question

The contract mechanics are favorable to the Yes side because the current spot reference is materially above 70k and the entire strike ladder suggests the market sees 70k as well in-the-money, but the narrow timing and exchange-specific close create nonzero operational and timing risk.

## Reliability notes

Good for contract interpretation and current market price; not sufficient by itself for underlying BTC price evidence because it is derivative of trader beliefs rather than direct exchange data.
