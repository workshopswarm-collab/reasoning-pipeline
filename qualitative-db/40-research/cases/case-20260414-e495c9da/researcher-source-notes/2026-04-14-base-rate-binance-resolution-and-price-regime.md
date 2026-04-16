---
type: source_note
case_key: case-20260414-e495c9da
dispatch_id: dispatch-case-20260414-e495c9da-20260414T191806Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-e495c9da | base-rate
question: Will the price of Bitcoin be above $70,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance BTCUSDT market rules and recent BTCUSDT pricing
source_type: exchange market data / resolution source
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=15
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: base-rate
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, resolution-source, btcusdt, daily-close]
---

# Summary
Binance is the governing source of truth for this contract, and recent Binance BTC/USDT daily closes show BTC already trading materially above $70,000 on most recent days before the April 19 noon ET resolution point.

## Key facts extracted
- Contract resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 19, using the final Close price.
- Binance recent daily closes (UTC) were approximately:
- 2026-04-05: close 69034.18, range 66611.66-69136.20
- 2026-04-06: close 68853.66, range 68300.00-70351.46
- 2026-04-07: close 71924.22, range 67732.01-72761.00
- 2026-04-08: close 71069.93, range 70707.23-72857.00
- 2026-04-09: close 71787.97, range 70466.00-73145.00
- 2026-04-10: close 72962.70, range 71426.15-73434.00
- 2026-04-11: close 73043.16, range 72513.09-73790.00
- 2026-04-12: close 70740.98, range 70505.88-73137.24
- 2026-04-13: close 74417.99, range 70566.99-74900.00
- 2026-04-14: close 74346.05, range 73795.47-76038.00
- Binance 5-minute average price during collection was 74337.90.
- Recent Binance closes were above 70,000 on 8 of the last 10 reported daily sessions in this pull.

## Evidence directly stated by source
- Binance API returned BTCUSDT OHLCV data with close values above 70,000 on Apr 7-14 except Apr 5-6.
- The current average price feed was above 74,000 during collection.

## What is uncertain
- Daily closes are not the settlement minute; the contract resolves on the specific 12:00 ET one-minute close on Apr 19.
- Intraday volatility between now and resolution could still push the final resolving minute below 70,000.
- API data here is a proxy for recent regime level; it does not itself settle the market until the target date and minute.

## Why this source may matter
This is the most important source because the contract explicitly uses Binance BTC/USDT as settlement authority. It also directly shows whether the current price regime is already comfortably above the threshold.

## Possible impact on the question
This source strongly supports a high Yes probability from an outside-view perspective: when the governing exchange is already trading around 74k several days before settlement, a sub-70k print at the exact target minute requires a nontrivial drawdown or shock over a short horizon.

## Reliability notes
High reliability for contract interpretation and recent price level because Binance is the named settlement venue. Remaining risk is not data quality but path dependence: the exact resolving minute can differ from recent daily closes.
