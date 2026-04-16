---
type: source_note
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the price of Bitcoin be above $70,000 on April 14?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance spot API plus Polymarket contract page
source_type: primary_and_contract
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT ; https://polymarket.com/event/bitcoin-above-on-april-14
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
downstream_uses: []
tags: [binance, polymarket, resolution-source, btc]
---

# Summary

This note captures the governing contract mechanics and a direct Binance price check near the relevant date. The Polymarket contract says resolution is based on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone. A same-day Binance spot API check shows BTC/USDT trading around 74.5k, well above 70k, which makes the event structurally very likely absent an abrupt pre-noon ET drawdown or a resolution-source timing mismatch.

## Key facts extracted

- Polymarket rules specify a **Yes** resolution if the Binance BTC/USDT 1-minute candle for **12:00 ET** on 2026-04-14 has a final **Close** price above 70,000.
- The market is about **Binance BTC/USDT specifically**, not other exchanges or pairs.
- Binance spot API on 2026-04-14 showed:
  - ticker price: **74545.10**
  - 5-minute average price: **74568.86901904**
- An API sanity check for current 1-minute klines returned rows timestamped in UTC, confirming Binance kline timestamps are straightforward UTC epoch milliseconds.
- Because April 14 is in daylight saving time for ET, **12:00 ET corresponds to 16:00 UTC**.

## Evidence directly stated by source

- Contract mechanics and source of truth are directly stated on the Polymarket event page.
- Binance API directly states contemporaneous BTC/USDT spot price and average price.

## What is uncertain

- The exact final 16:00 UTC / 12:00 ET 1-minute close was not yet available at research time.
- The contract page wording says to use the Binance trade UI with Candles selected, while the API verification used Binance public REST endpoints; they should align, but the UI candle remains the formal settlement surface.
- BTC can move materially in crypto markets over a few hours, so a sharp selloff before noon ET remained the main live risk.

## Why this source may matter

This is the main authoritative source set for both settlement mechanics and current state of the underlying market.

## Possible impact on the question

If BTC remains near the observed Binance levels into noon ET, the contract should resolve Yes. The main path to No would be a sharp drop below 70,000 by the specific noon ET 1-minute close or an unexpected source-of-truth / timing issue.

## Reliability notes

Polymarket is authoritative for contract wording; Binance is authoritative for the underlying price source. Independence is limited because both observations concern the same exchange-defined market, but for settlement purposes that is appropriate rather than a weakness.