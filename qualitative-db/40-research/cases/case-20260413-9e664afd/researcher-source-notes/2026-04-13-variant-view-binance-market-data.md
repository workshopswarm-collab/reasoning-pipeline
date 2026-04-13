---
type: source_note
case_key: case-20260413-9e664afd
dispatch_id: dispatch-case-20260413-9e664afd-20260413T164930Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-14 close above 70000?
driver: operational-risk
date_created: 2026-04-13
agent: Orchestrator
source_name: Binance spot API market data and symbol reference
source_type: exchange API / exchange resolution source
source_url: https://api.binance.com/api/v3/exchangeInfo?symbol=BTCUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9e664afd/researcher-analyses/2026-04-13/dispatch-case-20260413-9e664afd-20260413T164930Z/personas/variant-view.md]
tags: [binance, btcusdt, resolution-source, minute-candle]
---

# Summary

Direct Binance spot endpoints confirm the exact settlement pair exists as `BTCUSDT`, that Binance exchange timezone is `UTC`, and that BTCUSDT was trading around 72.29k-72.35k during the research window. A sampled block of the most recent 1000 one-minute candles all closed above 70,000, which strongly supports the market's bullish baseline while still leaving exact-minute path risk into the final noon-ET candle.

## Key facts extracted

- `exchangeInfo?symbol=BTCUSDT` returned the live spot symbol with exchange timezone `UTC` and status `TRADING`.
- `ticker/price?symbol=BTCUSDT` returned `72287.13000000` during the check.
- `avgPrice?symbol=BTCUSDT` returned about `72351.37868751` over the recent 5-minute window.
- Binance `serverTime` returned `1776099049653`, confirming a live exchange clock and supporting explicit UTC-to-ET timing conversion.
- A `klines?symbol=BTCUSDT&interval=1m&limit=1000` sample covered approximately `2026-04-13T00:11:00Z` to `2026-04-13T16:50:00Z` and every sampled close was above `70,000`.
- The sampled 1000-minute range was roughly `70,579.00` to `72,405.28`, with last sampled close around `72,353.39`.
- Querying the exact future resolution candle open time (`2026-04-14 16:00:00Z`, corresponding to noon ET under DST) naturally returned no data yet, which is consistent with the event still being in the future.

## Evidence directly stated by source

- `exchangeInfo` directly identifies Binance spot symbol `BTCUSDT` and exchange timezone `UTC`.
- `ticker/price` directly reported the spot price above the 70,000 threshold.
- `klines` directly reported one-minute candle closes, enabling a direct threshold-occupancy check over the recent sample.

## What is uncertain

- The final resolution minute is still in the future.
- This note does not independently prove how Polymarket would handle any later Binance correction, chart backfill, or UI/API discrepancy.
- A 1000-minute sample is strong recent context but not a formal forecast model; BTC can still move materially over ~23 hours.

## Why this source may matter

This is the closest direct evidence to the governing source of truth before resolution. It confirms pair identity, timing basis, current level versus threshold, and recent minute-level behavior on the exact venue that settles the market.

## Possible impact on the question

The direct Binance evidence makes the strongest variant case a limited one: not that the market is wrong directionally, but that it may still be a bit overconfident because the contract depends on one exact minute close tomorrow rather than today's comfortable spot margin alone.

## Reliability notes

High credibility because Binance is the named settlement source. Evidence independence is limited because all direct settlement evidence comes from the same source family, so a contextual secondary source is still useful as a sanity check rather than a replacement.
