---
type: source_note
case_key: case-20260415-89d9685e
dispatch_id: dispatch-case-20260415-89d9685e-20260415T181939Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules plus Binance BTCUSDT API surfaces
source_type: primary-and-contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-89d9685e/researcher-analyses/2026-04-15/dispatch-case-20260415-89d9685e-20260415T181939Z/personas/variant-view.md]
tags: [source-note, polymarket, binance, btc]
---

# Summary

This note captures the contract mechanics and the most relevant direct market-state context for the case: Polymarket says the outcome resolves from the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-16, and Binance API spot data on 2026-04-15 shows BTC/USDT trading around 74.2k, materially above the 72k strike.

## Key facts extracted

- Polymarket rule text says the market resolves to Yes if the Binance 1-minute candle for BTC/USDT at 12:00 PM ET on the specified date has a final Close price higher than 72000.
- Polymarket explicitly says the source is Binance BTC/USDT with 1m candles, not another exchange or pair.
- Time conversion check: 2026-04-16 12:00 PM America/New_York equals 2026-04-16 16:00:00 UTC.
- Binance ticker endpoint returned BTCUSDT spot around 74199.45 on 2026-04-15.
- Binance recent 1-minute klines fetched on 2026-04-15 showed closes mostly in the 74257 to 74350 range over the sampled recent window.

## Evidence directly stated by source

- Direct resolution wording from Polymarket identifies both the governing source and the exact candle construct.
- Direct Binance API outputs show current BTCUSDT spot and recent 1-minute closes substantially above 72000.

## What is uncertain

- The contract resolves on a future minute candle, so current price being above 72000 does not settle the outcome.
- A sharp drawdown before 12:00 PM ET on 2026-04-16 could still push the resolving close below 72000.
- API spot/ticker and recent klines are contextual evidence, not the final resolving candle itself.

## Why this source may matter

It provides both the authoritative contract mechanics and the most decision-relevant current state: the governing exchange/pair/timeframe and the fact that BTC is presently trading with a buffer of roughly 2.2k above the strike.

## Possible impact on the question

This source supports a high Yes probability, but also highlights the key variant risk: even a seemingly comfortable buffer can be erased in under a day in crypto, so market confidence should be tested against short-horizon realized volatility rather than only current level.

## Reliability notes

- Polymarket rules are the governing settlement description for this market, so reliability for contract interpretation is high.
- Binance API is a direct exchange surface and high quality for contemporaneous price context.
- Independence is limited because both pieces are tightly linked to the same settlement setup rather than offering broad independent causal evidence.
- Main residual risk is not source credibility but future price movement between now and the resolving minute.
