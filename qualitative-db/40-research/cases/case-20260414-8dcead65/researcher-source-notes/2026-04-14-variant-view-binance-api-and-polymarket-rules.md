---
type: source_note
case_key: case-20260414-8dcead65
dispatch_id: dispatch-case-20260414-8dcead65-20260414T160342Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-15 be above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance API klines and ticker; Polymarket market rules page
source_type: exchange-api-and-market-rules
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8dcead65/researcher-analyses/2026-04-14/dispatch-case-20260414-8dcead65-20260414T160342Z/personas/variant-view.md]
tags: [binance, polymarket, resolution-source, btc]
---

# Summary

This note captures the governing market mechanics from Polymarket and a direct Binance API verification pass on current BTC/USDT levels and recent 1-minute candles.

## Key facts extracted

- Polymarket rules say the market resolves based on the Binance BTC/USDT **1-minute candle for 12:00 ET** on 2026-04-15, specifically the candle's final **Close** price.
- The threshold is strictly **higher than 70,000**; equal to 70,000 would not be enough.
- Binance current spot/ticker at retrieval time was about **75,456.46**.
- Recent Binance 1-minute klines around 2026-04-14 16:00 UTC (12:00 ET) were in the **75.3k-75.5k** area.
- A direct API pull of the last 1000 one-minute candles showed a **minimum close of 74,054.21**, with **zero** closes at or below 70,000 in that retrieved sample.
- 2026-04-15 12:00 ET converts to **2026-04-15 16:00:00 UTC**.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected..."

From Binance API checks:
- `ticker/price` returned BTCUSDT around 75,456.46.
- `avgPrice` returned ~75,441.73 over the prior 5 minutes.
- Recent `klines` around 16:00 UTC showed closes near 75.3k-75.5k.
- The retrieved 1000-candle sample had no closes at or below 70,000.

## What is uncertain

- The market resolves on tomorrow's noon ET candle, not today's price.
- The 1000-candle sample is only a recent window, not a full historical regime study.
- A sudden macro or exchange-specific shock could still push BTC below 70,000 before the resolution minute.
- There is some operational ambiguity between the Binance website chart UI named in the rules and Binance API data, though they should normally align.

## Why this source may matter

This is the most direct combination of governing contract mechanics plus the most relevant live underlying reference market. It establishes both what must happen for the contract to resolve Yes and how much room currently exists above the 70,000 threshold.

## Possible impact on the question

The direct evidence strongly favors Yes because BTC/USDT is trading several thousand dollars above the threshold with less than a day remaining. The main variant-view caution is not that spot is near 70,000; it is that an ultra-high market probability can still underweight timing-specific crash risk, Binance-specific dislocation, or exact-candle operational issues.

## Reliability notes

- Polymarket is authoritative for contract wording but not final underlying price data.
- Binance is the stated source of truth for resolution, so its BTC/USDT candle surface is authoritative for settlement.
- Evidence independence is only medium because both the direct live checks come from Binance-related surfaces, but that is acceptable here because Binance is the governing source of truth.
- The main residual risk is not source credibility but source-of-truth implementation detail at the exact resolution minute.