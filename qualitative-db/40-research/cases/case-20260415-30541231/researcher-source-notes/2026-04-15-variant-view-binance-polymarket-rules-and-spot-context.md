---
type: source_note
case_key: case-20260415-30541231
dispatch_id: dispatch-case-20260415-30541231-20260415T133406Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance API spot and kline endpoints
source_type: market rules + exchange API
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [variant-view.md, variant-view.sidecar.json]
tags: [polymarket, binance, btc, resolution-rules, source-note]
---

# Summary

This source bundle establishes the contract mechanics and gives a direct contemporaneous read on Binance BTC/USDT spot levels relative to the 72,000 strike.

## Key facts extracted

- Polymarket says the market resolves from the Binance BTC/USDT **1 minute candle for 12:00 ET on April 17**, using the candle's final **Close** value.
- The contract is specifically about **Binance BTC/USDT**, not other exchanges or other pairs.
- Current Polymarket pricing on the fetched page showed the **72,000** line at roughly **84% Yes**.
- Binance ticker API showed BTCUSDT at **74,148.65** at fetch time on 2026-04-15.
- Recent Binance 1-minute klines around fetch time were all above **74,250**, well above the strike.
- A 48-hour pull of hourly Binance klines showed **47 of the last 48 hourly closes above 72,000**, with a minimum close of **71,866.59** and latest hourly close around **74,152.00**.

## Evidence directly stated by source

- Polymarket rules directly state the governing source of truth and the exact settlement condition.
- Binance API directly states current BTCUSDT ticker price and recent candle closes.

## What is uncertain

- The market settles on one specific future minute close, so current spot levels only provide context, not direct settlement evidence.
- Binance UI presentation could matter operationally if there is any discrepancy between API data and the web chart that Polymarket references.

## Why this source may matter

The source bundle matters because this is a narrow, date-specific, rule-sensitive market where exact venue, pair, candle interval, and timezone all govern resolution. It also shows that BTC currently has meaningful cushion above 72,000, which is the main support for a high Yes probability.

## Possible impact on the question

This supports a bullish baseline because spot is currently more than $2,000 above the strike and has mostly held above 72,000 over the last two days. The variant angle is that a single noon ET minute close can still fail on short-horizon volatility or venue-specific moves even if broader market context remains bullish.

## Reliability notes

- Polymarket is authoritative for contract wording but not for the eventual Binance print itself.
- Binance is authoritative for the eventual price print, though Polymarket references the Binance web trading surface rather than the public API explicitly.
- Independence is limited because both the rules and the settlement source are tightly coupled to Binance-specific data.