---
type: source_note
case_key: case-20260415-1e5e80f9
dispatch_id: dispatch-case-20260415-1e5e80f9-20260415T080017Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-16 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot price API and Polymarket market rules page
source_type: primary_market_data_and_market_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, settlement, btc]
---

# Summary

This note captures the direct settlement mechanics from the Polymarket market page and a contemporaneous Binance BTC/USDT spot reading. Together they frame what the market is pricing: a one-day-ahead question about whether Binance BTC/USDT remains above 72,000 at the specific 12:00 ET one-minute candle close on April 16.

## Key facts extracted

- The assigned market current price is 0.825, implying about an 82.5% Yes probability for "above 72,000."
- The Polymarket rules text says resolution is based on the Binance BTC/USDT **1 minute candle for 12:00 in the ET timezone (noon)** on the specified date, using the candle's final **Close** price.
- The rules text explicitly says the source of truth is Binance BTC/USDT, not another exchange or pair.
- A direct Binance spot API pull during this run returned BTCUSDT price `73703.25000000`.
- A Binance 1-minute kline pull during this run showed recent closes around `73679.40` to `73776.45`, i.e. materially above the 72,000 strike.
- A CoinGecko BTC/USD spot pull during this run returned `73742`, broadly confirming that the broader market was also around the mid-73k area at the same time.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."

From direct Binance API pull:
- BTCUSDT last spot price during the run: `73703.25000000`.

From recent Binance 1m klines during the run:
- Recent close values included `73776.45`, `73744.73`, `73730.43`, `73679.40`, `73703.25`.

## What is uncertain

- This source does not tell us where BTC/USDT will be at exactly 12:00 ET on April 16; it only establishes present context and contract mechanics.
- The Polymarket web page is a good surface for rules text but is not itself the settlement data source.
- No volatility distribution or options-implied one-day move estimate was directly pulled in this note.

## Why this source may matter

- It cleanly defines the contract's governing condition and the relevant time window.
- It shows the market is asking about a relatively small downside buffer versus current spot: with BTC around 73.7k, the contract can still fail if BTC drops roughly 2.3% or more by the relevant candle close.
- It also highlights a small but real operational wrinkle: Binance's precise displayed candle close, with ET timing and 1m selection, is the source of truth.

## Possible impact on the question

This source supports taking the 82.5% market-implied Yes probability seriously. BTC is already above the strike by roughly 1.7k at run time, so a Yes outcome does not require further upside, only maintaining price above 72k through the specified next-day noon ET minute close. The main remaining risk is ordinary one-day BTC volatility or an exchange-specific print/operational issue at the settlement minute.

## Reliability notes

- Binance is the direct settlement source, so it is the highest-value source for this case.
- CoinGecko is only contextual cross-checking, not the governing source of truth.
- Evidence independence is moderate rather than high because contextual BTC price sources often ultimately reflect overlapping exchange data, but the settlement dependency on Binance makes Binance primary regardless.