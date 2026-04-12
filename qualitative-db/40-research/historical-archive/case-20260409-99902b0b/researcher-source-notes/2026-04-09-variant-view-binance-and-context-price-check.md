---
type: source_note
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
analysis_date: 2026-04-09
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-10
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-10 be above 70000?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance BTCUSDT spot and 1m kline check with independent spot context
source_type: exchange-api-plus-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-09
credibility: high
recency: very-high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-99902b0b/researcher-analyses/2026-04-09/dispatch-case-20260409-99902b0b-20260409T203957Z/personas/variant-view.md]
tags: [binance, btc, spot-price, verification, date-specific-market]
---

# Summary

This note records the direct Binance price check and one additional independent price-context pass used for the April 10 BTC > 70,000 market.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT spot price `72361.70000000` on 2026-04-09.
- Binance 1-minute kline endpoint returned the latest sampled closes clustered around `72361.70` to `72392.38`, indicating BTCUSDT was trading materially above 70,000 during the research window.
- CoinGecko simple price endpoint returned Bitcoin at `72390` USD.
- Coinbase spot endpoint returned BTC-USD at `72380.625`.
- Cross-exchange/context prices were tightly clustered near 72.38k, reducing concern that Binance was unusually detached at the time of review.

## Evidence directly stated by source

- Binance directly states the BTCUSDT spot price and recent 1-minute candle OHLC values.
- CoinGecko and Coinbase directly state contemporaneous BTC/USD reference prices.

## What is uncertain

- The contract resolves on the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-10, not the current price on 2026-04-09.
- A move from roughly 72.36k down below 70k by the relevant noon ET candle is still possible within a day in crypto.
- Binance API outputs are highly relevant but the market wording references the Binance trading interface candle display; there is small operational/source-display ambiguity even if economically they should align.

## Why this source may matter

- It is the closest thing to a direct source-of-truth preview because the contract explicitly resolves from Binance BTC/USDT 1-minute candle closes.
- It also allows a clean distance-to-threshold check: BTC was about 2.3k above the 70k line at review time.

## Possible impact on the question

- This evidence supports a high probability of YES because the market only needs the specified future candle close to remain above a threshold that is already comfortably below the current Binance trading level.
- The main residual risk is a sharp downside move before the 12:00 ET April 10 candle close, not current mispricing around the threshold.

## Reliability notes

- Binance is the governing resolution source, so direct Binance data carries very high relevance.
- CoinGecko and Coinbase are independent contextual checks, useful for sanity-checking that Binance is not showing an anomalous level.
- Independence is not perfect because all crypto spot venues are correlated, but the contextual checks are still useful as an additional verification pass.