---
type: source_note
case_key: case-20260414-e15c72fe
dispatch_id: dispatch-case-20260414-e15c72fe-20260414T193100Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1m candle close above 70000 on 2026-04-20?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance BTCUSDT API + Polymarket rules page
source_type: primary_market_data_and_contract_surface
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=30
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-e15c72fe/researcher-analyses/2026-04-14/dispatch-case-20260414-e15c72fe-20260414T193100Z/personas/base-rate.md]
tags: [binance, btcusdt, polymarket-rules, source-note, base-rate]
---

# Summary

This source note captures the two most important direct surfaces for this market: the Polymarket contract wording and Binance BTC/USDT pricing data, which is also the stated resolution source.

## Key facts extracted

- Polymarket says the market resolves Yes if the Binance BTC/USDT 1 minute candle for **12:00 ET** on **2026-04-20** has a final **Close** price above **70,000**.
- The market is explicitly about **Binance BTC/USDT**, not other exchanges or other BTC pairs.
- Recent Binance BTC/USDT spot price at research time was roughly **74.25k**.
- In the last 30 daily Binance candles available through the API, **15 of 30** daily closes were above 70k.
- The most recent daily closes were mostly above 70k, with only one recent dip below in the last seven closes sampled.
- Sampled recent 1-minute candles from Binance show the API timestamps are in UTC; noon ET on the resolution date corresponds to **16:00 UTC** assuming EDT remains in effect on April 20, 2026.

## Evidence directly stated by source

From the Polymarket rules page:
- resolution is determined by the Binance BTC/USDT 1-minute candle
- the relevant field is the candle's final Close
- the relevant time is 12:00 ET on the named date

From Binance API outputs obtained during this run:
- latest ticker price was 74251.30 USDT
- last 30 daily candles included 15 closes above 70000
- recent daily sequence remains centered above the threshold, though not without volatility

## What is uncertain

- The contract settles on a single 1-minute close at a specific future timestamp, not on the daily close or spot level at research time.
- A six-day horizon in BTC is long enough for a macro or crypto-specific drawdown to push price below 70k by the relevant minute.
- Binance website rendering could differ from API presentation format, though both should reflect the same underlying BTC/USDT market data.

## Why this source may matter

This is the core direct-evidence pair for the case: it tells us exactly what must happen for Yes to resolve, and it shows the current and recent level of the underlying asset on the named venue.

## Possible impact on the question

These sources support an outside-view leaning toward Yes because BTC/USDT is currently several thousand dollars above the threshold and recent closes have been above 70k about half the time over the last month, with a stronger share in the very recent subset. But because settlement depends on one exact future minute rather than a broader window, the contract remains materially vulnerable to short-horizon volatility.

## Reliability notes

- Binance is the stated source of truth, so it is authoritative for settlement mechanics here.
- Polymarket's own rules page is authoritative for contract interpretation.
- The Binance API is highly relevant as a direct market-data surface, but this case still has some operational / interpretation risk because the contract references the website candle display rather than the API endpoint explicitly.