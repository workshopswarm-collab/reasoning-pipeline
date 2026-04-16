---
type: source_note
case_key: case-20260414-3691b692
dispatch_id: dispatch-case-20260414-3691b692-20260414T170231Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on April 16, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance public market data API (BTCUSDT ticker and klines)
source_type: primary_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: bullish-above-72k
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, primary-source, market-data]
---

# Summary

Direct Binance API checks on April 14 show BTC/USDT trading materially above 72,000, making the variant case less about directional price prediction and more about whether the market is underpricing contract/mechanics or short-horizon drawdown risk.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT spot price `74734.66` on the check.
- Recent 1-minute Binance candles around the check were all in the mid-74,000s.
- Recent 1-day Binance candles showed closes above 72,000 on April 10, 11, 13, and intraday trading above 74,000 on April 14.
- The April 13 daily candle reached a high of 74,900 and closed 74,417.99.
- The April 14 daily candle, still in progress at the time of check, had traded as high as 76,038.

## Evidence directly stated by source

- Current Binance BTCUSDT price was above the market strike by roughly 2,700 points.
- Binance historical kline data confirms BTC has recently sustained trading and closes above the 72,000 threshold.

## What is uncertain

- The market resolves on the 12:00 ET one-minute candle close on April 16, not on current spot or daily close.
- A sharp risk-off move, exchange-specific dislocation, or intraday reversal could still push the noon ET close below 72,000.
- API output is direct but does not itself tell us the exact noon ET candle that will exist on April 16.

## Why this source may matter

This is the governing exchange named in the contract, so it is the most important direct source for current state and for verifying that the contract refers to Binance BTC/USDT rather than a generic BTC index.

## Possible impact on the question

This source supports a high probability of YES because the market only needs Binance BTC/USDT to remain above 72,000 at a single specified minute two days from now, and current direct exchange pricing sits comfortably above that level.

## Reliability notes

- High relevance because Binance is the named resolution source.
- Moderate limitation because this was checked through the public API rather than the exact web chart UI named in the market text; still, both should reflect the same Binance market data family.
- For this case, the main remaining uncertainty is path risk into the exact resolution minute, not source identity.