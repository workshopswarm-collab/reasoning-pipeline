---
type: source_note
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close be above 70000 on 2026-04-20?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and trading page rule target
source_type: primary market data / resolution source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
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
downstream_uses: []
tags: [binance, btcusdt, primary-source, resolution-source, crypto]
---

# Summary

Binance is the governing source of truth for this market. On 2026-04-15, Binance spot BTCUSDT price was about 74,066, materially above the 70,000 threshold. Recent daily klines show BTC has spent much of the last 1-2 weeks above 70,000, which makes a five-day-ahead noon close above 70,000 a high-probability but not riskless event.

## Key facts extracted

- Binance API ticker on 2026-04-15 returned BTCUSDT spot price `74066.28000000`.
- The market resolves using the Binance BTCUSDT 1-minute candle at `12:00 ET` on 2026-04-20, specifically the final `Close` price.
- Recent daily closes from Binance:
  - 2026-04-10: 72,962.70
  - 2026-04-11: 73,043.16
  - 2026-04-12: 70,740.98
  - 2026-04-13: 74,417.99
  - 2026-04-14: 74,131.55
  - 2026-04-15: ~74,044 intraday from downloaded daily series
- In the last 90 Binance daily candles, 46/90 daily closes were above 70,000 and 59/90 daily highs were above 70,000.
- In the last 10 daily candles before the run, 9/10 daily highs were above 70,000 and 8/10 daily closes were above 70,000.

## Evidence directly stated by source

- Current BTCUSDT price level on Binance is above 70,000.
- Binance provides the exact market-specific instrument and data family used for settlement.
- Recent Binance candles indicate BTC has recently traded and often closed above 70,000.

## What is uncertain

- The market settles on one exact one-minute close at noon ET on 2026-04-20, not on current price, daily high, or daily close.
- API pulls here verify current/recent spot regime but do not directly verify the future one-minute settlement print.
- Weekend/macro volatility or exchange-specific dislocations could still push the one-minute close below 70,000.

## Why this source may matter

This is the primary source because the contract explicitly settles on Binance BTCUSDT. It anchors both the threshold comparison and the operational details that all conditions must satisfy.

## Possible impact on the question

Because BTC is currently about 5.8% above the threshold and has recently spent many daily closes above 70,000, the base-rate starting point should be meaningfully above 50%. But the exact one-minute/noon/ET condition keeps the probability below certainty.

## Reliability notes

- High credibility for settlement mechanics and current spot data.
- Independence is limited because Binance is both price source and settlement source; a separate contextual source is still useful for triangulation rather than settlement.
- Exchange-specific operational issues remain a residual risk because settlement is exchange-specific rather than cross-exchange averaged.