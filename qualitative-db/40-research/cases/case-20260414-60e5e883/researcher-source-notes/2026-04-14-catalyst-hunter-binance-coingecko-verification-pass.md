---
type: source_note
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-60e5e883 | catalyst-hunter
question: Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 70000?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT live ticker, 1m klines, 1d klines, with CoinGecko cross-check
source_type: primary exchange data + secondary contextual cross-check
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: live
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [catalyst-hunter finding, catalyst-hunter evidence map, catalyst-hunter assumption note]
tags: [binance, coingecko, verification-pass, btcusdt, catalyst-calendar]
---

# Summary

This note documents the catalyst-hunter verification pass using the governing Binance venue plus an independent contextual cross-check. The core takeaway is that BTC is currently trading around 74.3k, leaving roughly a 6.2% cushion over the 70k strike with about three days remaining, but the contract still hinges on one exact Binance 1-minute close at noon ET on April 17.

## Key facts extracted

- Binance ticker returned **BTCUSDT = 74,318.38** during the verification pass.
- Recent Binance 1-minute closes were **74,307.79**, **74,330.20**, **74,310.87**, **74,338.36**, and **74,318.38**, showing no immediate stress around the threshold.
- Recent Binance daily closes were approximately **71,069.93**, **71,787.97**, **72,962.70**, **73,043.16**, **70,740.98**, **74,417.99**, and current around **74,318.38**.
- Recent seven-day Binance lows included **70,466.00**, **70,505.88**, and **70,566.99**, which are above or only marginally below the strike neighborhood; the market is not currently trading near 70k.
- CoinGecko cross-check returned **BTC/USD ≈ 74,346**, broadly consistent with Binance.
- The contract time maps cleanly to **2026-04-17 12:00 ET = 2026-04-17 16:00 UTC**.

## Evidence directly stated by source

- Binance directly reports the settlement pair's current price and recent 1-minute / 1-day candles.
- CoinGecko independently corroborates the broad BTC spot level.

## What is uncertain

- None of these checks settle the actual noon ET April 17 candle.
- A macro risk-off move, crypto-specific liquidation cascade, or exchange-specific print at the exact minute could still produce a No despite current spot being safely above 70k.

## Why this source may matter

For a date-specific BTC threshold market, the most relevant near-term catalyst is often simply whether any identifiable event is likely to push BTC several thousand dollars before the exact resolution minute. This verification pass suggests no obvious scheduled catalyst currently dominates the path more than ordinary crypto volatility and broad risk sentiment.

## Possible impact on the question

The evidence supports a high Yes probability, but not a near-certainty much above the low 90s. The live cushion is meaningful, yet the contract's narrow timing window means path risk still matters.

## Reliability notes

High for direct price level and recent range because Binance is the governing resolution source. Medium for forecasting because the note uses current state rather than future settlement data. CoinGecko improves contextual independence but is not the settlement source.