---
type: source_note
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-15 be above 72000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance BTCUSDT API spot and 1m kline check
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-395c5631/researcher-analyses/2026-04-13/dispatch-case-20260413-395c5631-20260413T221534Z/personas/variant-view.md]
tags: [binance, btcusdt, source-note, price-check]
---

# Summary

Direct exchange-source check of current BTC/USDT pricing and recent one-minute candles on Binance, the governing venue for this contract.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT at `73823.14000000`.
- Binance 1-minute klines for the five most recent minutes showed closes at approximately 73.46k, 73.58k, 73.75k, 73.85k, and 73.82k.
- Timestamp conversion showed the sampled Binance candles mapped to 2026-04-13 18:12-18:16 ET, confirming normal minute alignment relative to the contract's ET noon resolution rule.
- Current spot is already about 1.8k above the 72k strike with roughly 42 hours remaining.

## Evidence directly stated by source

- Binance API reported current BTCUSDT spot price of `73823.14000000`.
- Binance API reported recent 1-minute candle closes in the mid-73k range.

## What is uncertain

- This check does not directly observe the eventual 2026-04-15 12:00 ET candle.
- API access confirms current venue pricing and timestamp alignment, but not whether Polymarket will use the website display or any post-hoc candle revision process.
- Short-horizon crypto volatility remains material over the remaining time window.

## Why this source may matter

This is the closest available direct source to the contract's stated settlement venue and market mechanism. It materially reduces ambiguity about current distance from strike and about the ET-to-Binance candle mapping.

## Possible impact on the question

Because the governing venue is already trading materially above 72k, the default baseline is Yes unless BTC sells off by more than ~2.5% by noon ET on Apr. 15. The variant angle is not that No is likeliest, but that a 73% Yes market may still underprice path risk tied to a date-specific one-minute close and single-venue settlement.

## Reliability notes

- High credibility for current Binance venue pricing because this is Binance's own public API.
- Good directness for contract interpretation because the market explicitly references Binance BTC/USDT one-minute candles.
- Limited independence as a sole source, so paired with external spot references and Polymarket rule text.