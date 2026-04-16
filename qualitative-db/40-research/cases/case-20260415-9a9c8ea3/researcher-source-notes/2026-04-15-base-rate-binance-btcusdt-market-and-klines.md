---
type: source_note
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-16 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT ticker and 1-minute klines API
source_type: exchange data / primary market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, primary-source, btcusdt, market-data, 1m-candles]
---

# Summary

Binance is the governing source of truth for this market. Direct pulls from Binance's public API on 2026-04-15 showed BTC/USDT spot around 74.6k and the most recent 1000 one-minute closes all above 72k.

## Key facts extracted

- `api/v3/ticker/price?symbol=BTCUSDT` returned BTCUSDT spot at about 74613.32 on 2026-04-15 around 15:21 ET.
- `api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000` returned 1000 recent one-minute candles.
- In that 1000-minute sample, the minimum close was 73566.00 and the maximum close was 74703.99.
- The sample covered roughly from 2026-04-14 22:43 ET to 2026-04-15 15:22 ET.
- Every sampled close in that window was above 72000.
- Noon ET on 2026-04-16 is roughly 20.6 hours after the sample endpoint, so the contract remains live and can still be invalidated by a sufficiently large drawdown before the specific settlement minute.

## Evidence directly stated by source

- Binance API directly provided the current BTCUSDT price.
- Binance API directly provided timestamped one-minute OHLCV candles for BTCUSDT.
- The data directly supports that BTC traded materially above 72k through the sampled recent window.

## What is uncertain

- The exact one-minute close that will govern settlement is the 12:00 ET candle on 2026-04-16, which had not occurred yet at research time.
- The public API queried is a machine-readable source from Binance, while the contract language points to the Binance trading interface with `1m` and `Candles` selected; these should normally align, but the contract technically names the website surface.
- It is still possible for BTC to fall more than ~3.5% before noon ET on Apr 16.

## Why this source may matter

This is the primary evidence because the market explicitly resolves from Binance BTC/USDT one-minute close data. It directly establishes both the relevant source-of-truth venue and the current margin above the threshold.

## Possible impact on the question

The source strongly supports a high probability of `Yes` because BTC is currently far above 72k and has remained above that threshold throughout the most recent ~16.7 hours sampled. It does not settle the contract early, but it gives a strong outside-view anchor that a >3% downside move by the exact settlement minute is required for `No`.

## Reliability notes

High credibility for venue-specific price data. Main limitation is surface-matching: the contract names the Binance UI candle close, while the API was used as a direct verification proxy. Operational alignment risk appears low but not literally zero.