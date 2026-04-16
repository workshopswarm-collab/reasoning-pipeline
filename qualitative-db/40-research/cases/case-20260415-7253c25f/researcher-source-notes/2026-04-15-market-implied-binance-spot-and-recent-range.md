---
type: source_note
case_key: case-20260415-7253c25f
dispatch_id: dispatch-case-20260415-7253c25f-20260415T220737Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: reliability
date_created: 2026-04-15
source_name: Binance API spot price and recent daily/hourly candles
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7253c25f/researcher-analyses/2026-04-15/dispatch-case-20260415-7253c25f-20260415T220737Z/personas/market-implied.md]
tags: [binance, btcusdt, spot, price-data]
---

# Summary

Direct Binance market data on Apr 15 showed BTC/USDT near 74,947 and recent daily candles mostly above 72,000, with one notable daily close below 72,000 on Apr 12 before price rebounded above 74,000.

## Key facts extracted

- Binance ticker price fetched: 74,947.39 BTC/USDT.
- Recent daily closes:
  - Apr 09: 71,787.97
  - Apr 10: 72,962.70
  - Apr 11: 73,043.16
  - Apr 12: 70,740.98
  - Apr 13: 74,417.99
  - Apr 14: 74,131.55
  - Apr 15: 74,947.39 at fetch time
- Recent 72-hour hourly closes ranged roughly from 70,680.7 to 75,525.94, with last around 74,947.4.

## Evidence directly stated by source

- Binance API directly returned current BTCUSDT price and historical kline values.

## What is uncertain

- This is not the exact April 21 12:00 ET settlement candle; it is only the current and recent trading context.
- Short-horizon BTC volatility remains meaningful, so current spot being comfortably above 72,000 does not guarantee the April 21 noon ET close will stay above that threshold.

## Why this source may matter

Because Binance BTC/USDT is the explicit source of truth for settlement, direct Binance data is the most relevant primary evidence for whether the market’s ~80% pricing is reasonable.

## Possible impact on the question

Current spot being almost 3,000 above the threshold, plus several recent closes above 72,000 after a brief dip, supports the view that an 80% Yes price is not obviously overextended. It also highlights the main disconfirming mechanism: BTC can still move several thousand dollars within days.

## Reliability notes

High reliability for direct exchange pricing and recent realized ranges. Independence versus settlement is high because this is the same venue/pair family the contract references, though that also means it is not a separate external viewpoint; it is direct market-state evidence.