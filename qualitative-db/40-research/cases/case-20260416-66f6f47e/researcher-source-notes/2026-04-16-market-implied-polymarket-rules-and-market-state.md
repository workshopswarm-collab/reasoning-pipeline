---
type: source_note
case_key: case-20260416-66f6f47e
dispatch_id: dispatch-case-20260416-66f6f47e-20260416T141457Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: btc-threshold-close
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-21 close above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market contract / primary rules surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-66f6f47e/researcher-analyses/2026-04-16/dispatch-case-20260416-66f6f47e-20260416T141457Z/personas/market-implied.md
tags: [polymarket, rules, resolution-source, binance, noon-close]
---

# Summary

This source establishes the governing contract mechanics and the live market-implied baseline relevant to the case.

## Key facts extracted

- The market resolves Yes if the **Binance BTC/USDT 1-minute candle for 12:00 ET on April 21** has a final **Close** price strictly higher than **72,000**.
- The governing source is explicitly **Binance BTC/USDT** with **1m** candles, not another exchange or trading pair.
- Price precision is determined by the source.
- The market page showed the **72,000** bracket trading around **79%-80% Yes** on fetch, which is directionally close to the assignment snapshot price of **0.705**.

## Evidence directly stated by source

- Resolution is based on a **single specific minute-close observation** rather than intraday high/low or end-of-day close.
- The event is not yet verified because the governing candle has not occurred yet; this is a future-dated contract as of 2026-04-16.
- The market page is itself a direct read on crowd pricing but not the final governing source for settlement.

## What is uncertain

- The fetched market-page snapshot showed around 79%-80% for the 72k line, while the assignment metadata gave current_price 0.705. That likely reflects time drift or quote movement rather than a rules discrepancy.
- The Polymarket page alone does not prove where Binance BTC/USDT will print at 12:00 ET on April 21.

## Why this source may matter

- It is the primary contract/rules source and therefore determines what counts.
- It also provides a direct read on how the public market is pricing the threshold.

## Possible impact on the question

- Because the rule uses **one specific one-minute close** on Binance at **noon ET**, being above 72k now is supportive but not dispositive.
- The narrow settlement mechanic means short-horizon volatility into the exact observation window is the main residual risk.

## Reliability notes

- High reliability for contract wording and live market display.
- Lower reliability for static quote persistence because the market price can move after the fetch.