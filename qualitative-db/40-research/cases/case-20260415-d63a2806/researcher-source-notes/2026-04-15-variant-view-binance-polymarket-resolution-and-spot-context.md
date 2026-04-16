---
type: source_note
case_key: case-20260415-d63a2806
dispatch_id: dispatch-case-20260415-d63a2806-20260415T175526Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance noon-ET close threshold mechanics and current BTC/USDT spot context
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event rules page plus Binance public API spot and kline endpoints
source_type: primary_and_governing_with_market_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-d63a2806/researcher-analyses/2026-04-15/dispatch-case-20260415-d63a2806-20260415T175526Z/personas/variant-view.md
tags: [source-note, polymarket, binance, btc, resolution]
---

# Summary

This source note captures the contract’s governing mechanics and a current spot-context check from Binance. The market resolves on the **final close** of the Binance BTC/USDT **12:00 ET** one-minute candle on 2026-04-17, not on an intraday high, cross-exchange print, or general daily close.

## Key facts extracted

- Polymarket rules state Yes resolves only if the Binance BTC/USDT **1-minute candle for 12:00 ET on Apr 17** has a final **Close** price higher than **72,000**.
- The assignment-time market price for this leg is **0.835**, implying about **83.5%**.
- A UTC conversion check puts the relevant candle at **2026-04-17 16:00:00 UTC**.
- Binance public API spot check on 2026-04-15 shows BTC/USDT around **74,121-74,122**, already roughly **2.9% above** the 72,000 threshold.
- Binance 24h stats show a session range of roughly **73,514 to 74,815** and a 24h change of about **-0.83%**, which implies ordinary volatility could still move BTC across the threshold before the decisive noon-ET minute.
- Recent hourly klines in the prior ~48 hours include trading above **76,000** and multiple hours in the **74k-75k** area, suggesting the current setup is comfortably above the line but not immune to multi-percent swings.
- CoinGecko hourly price series independently places BTC around **74.1k** at the time of checking, broadly corroborating Binance-level context.

## Evidence directly stated by source

- Direct from Polymarket rules: the contract is about the Binance BTC/USDT **close** for a single specified 1-minute candle.
- Direct from Binance API: current BTCUSDT last price and recent kline / 24h range values.

## What is uncertain

- The event has **not yet occurred**; no governing 2026-04-17 12:00 ET candle exists yet.
- Current spot levels do not prove the final noon-ET close two days later.
- Public web fetch of Binance’s trading UI did not produce a readable extracted page, so the durable proof here relies on Binance API market data plus the explicit Polymarket rule text.

## Why this source may matter

This is the key mechanism source. The contract is narrow and date-sensitive: many intuitive bullish facts about Bitcoin are irrelevant unless they bear on the final Binance 12:00 ET one-minute close on Apr 17.

## Possible impact on the question

The source set supports a bullish baseline because BTC is already trading materially above 72,000, but it also sharpens the variant caution: the contract is not a touch market and not a generic “BTC stays strong” market. A brief downside move exactly into the decision minute would still resolve No.

## Reliability notes

- Polymarket rules page is the clearest governing source for contract interpretation.
- Binance API is a strong primary market-data source for current context, though the exact settlement proof will still require the specific 2026-04-17 12:00 ET candle after it exists.
- CoinGecko is only contextual / corroborative, not the governing source of truth.