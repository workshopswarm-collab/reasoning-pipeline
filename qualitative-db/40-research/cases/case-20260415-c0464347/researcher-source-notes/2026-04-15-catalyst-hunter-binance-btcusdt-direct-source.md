---
type: source_note
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API BTCUSDT ticker and 1m klines
source_type: primary_direct_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-c0464347/researcher-analyses/2026-04-15/dispatch-case-20260415-c0464347-20260415T011958Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, direct-source, resolution-mechanics, 1m-candle]
---

# Summary

Direct-source verification of the market's governing data surface. Binance public endpoints returned BTC/USDT spot price around 74.6k and recent 1-minute klines, which confirms both that BTC is currently above 70k by a meaningful margin and that the contract's resolution mechanic is a specific 1-minute Binance close rather than a broad daily or cross-exchange price.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price `74598.54000000` on 2026-04-15 UTC.
- Binance 1-minute kline endpoint returned recent 1m candles with closes clustered around 74.6k-74.7k.
- The contract-relevant data surface is capable of producing the required 1-minute close field directly.
- Current spot level is roughly 6.6% above the 70k threshold.

## Evidence directly stated by source

- Current BTCUSDT spot price on Binance is about 74.6k.
- Binance exposes 1m kline close values directly for BTCUSDT.

## What is uncertain

- This source does not itself tell us what the 12:00 ET April 20 close will be.
- API output does not independently prove Polymarket will use API rather than website-rendered candles, though both refer to Binance BTC/USDT 1m closes.
- Short-horizon crypto volatility could still move BTC below 70k by resolution.

## Why this source may matter

This is the most direct available evidence for both current level and resolution mechanics. For a narrow date-specific contract, verifying the exact exchange/pair/interval matters more than generic BTC price headlines.

## Possible impact on the question

Supports a high Yes probability because BTC currently trades materially above the threshold and the governing source is a single Binance BTC/USDT 1-minute close, not a more ambiguous cross-exchange measure.

## Reliability notes

- High credibility for direct market data.
- Independence is limited because this is also effectively the same underlying source the contract resolves against.
- Operational caveat: exchange-specific print risk or transient volatility matters more here than broad market consensus because only one minute candle close governs settlement.