---
type: source_note
case_key: case-20260416-5baa54ee
dispatch_id: dispatch-case-20260416-5baa54ee-20260416T032738Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page plus Binance API price context
source_type: market rules page + exchange API
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-5baa54ee/researcher-analyses/2026-04-16/dispatch-case-20260416-5baa54ee-20260416T032738Z/personas/base-rate.md]
tags: [source-note, polymarket, binance, resolution]
---

# Summary

This note captures the governing contract mechanics from the Polymarket market page and a contextual Binance API spot/daily-price check used to assess whether a >$70,000 close at noon ET on April 20 is structurally plausible rather than already settled.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET (noon)** on **2026-04-20** has a final **Close** price **higher than 70,000**.
- The market is specifically tied to **Binance BTC/USDT**, not another exchange or USD reference.
- Price precision is whatever Binance displays in the source.
- The live Polymarket market price for the 70,000 threshold was about **94%** at fetch time.
- Binance public API checks on 2026-04-15/16 showed BTC/USDT trading materially above 70,000 and recent daily closes around the low 70k range, which supports a high prior for remaining above 70,000 over a four-day horizon but does not settle the exact noon candle.

## Evidence directly stated by source

From the Polymarket rules page:
- Resolution source is Binance BTC/USDT with 1m candles selected.
- The decisive observation is the **12:00 ET** candle close on the date named in title.
- All material conditions must hold together: right exchange, right pair, right timestamp, right candle field, and price strictly higher than threshold.

From Binance API context:
- Recent BTC/USDT prices and daily closes were above 70,000 during the research window.

## What is uncertain

- The Polymarket page is not itself the final settlement print; it only states the governing rule.
- Daily closes and spot checks do not guarantee the exact 12:00 ET 1-minute close on 2026-04-20.
- Binance API context here is supportive, not settlement-grade for the exact contract condition.

## Why this source may matter

The market is narrow, date-sensitive, and exchange-specific. Contract interpretation is therefore central. The rules page identifies the source of truth and the exact timestamp logic, while Binance price context shows whether the threshold is far in/out of the money during the research period.

## Possible impact on the question

These sources support a high-probability Yes view because BTC was already above the threshold with only a short time remaining, but they also constrain the claim: the contract only pays Yes if Binance BTC/USDT remains above 70,000 on the exact noon ET 1-minute close on April 20.

## Reliability notes

- Polymarket rules page is authoritative for contract mechanics but not for the future outcome.
- Binance is the authoritative settlement source named by the contract.
- The Binance API checks are direct exchange data, but only contextual because they are not the exact settlement candle yet.
- Evidence independence is moderate: one source defines the rule, another source family (Binance API) gives live price context.