---
type: source_note
case_key: case-20260406-6e955d27
dispatch_id: dispatch-case-20260406-6e955d27-20260406T051514Z
analysis_date: 2026-04-06
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: binance
topic: bitcoin-above-66k-on-april-6
question: Will the price of Bitcoin be above $66,000 on April 6?
driver:
date_created: 2026-04-06T01:19:00-04:00
source_name: Binance BTCUSDT API and Polymarket market rules
source_type: primary-plus-contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10&endTime=1775491440000 ; https://polymarket.com/event/bitcoin-above-on-april-6
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [binance, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260406-6e955d27/researcher-analyses/2026-04-06/dispatch-case-20260406-6e955d27-20260406T051514Z/personas/catalyst-hunter.md]
tags: [resolution-source, binance, polymarket, btc]
---

# Summary

This source bundle establishes both the governing settlement mechanic and the live pre-resolution setup for the case. Polymarket rules explicitly say the market resolves using the Binance BTC/USDT 1-minute candle at 12:00 ET on April 6, using the candle's final Close price. Binance live price shortly after 01:15 ET was about 69,176.49, and recent 1-minute candles around that time were all comfortably above 66,000.

## Key facts extracted

- Polymarket rules name Binance BTC/USDT 1-minute candles as the source of truth for settlement.
- The relevant settlement observation is the 12:00 ET candle on April 6, 2026.
- The threshold is strictly whether the final Close is higher than 66,000.
- Binance ticker at fetch time showed BTCUSDT price 69,176.49.
- Recent Binance 1-minute klines around 05:09Z-05:18Z (01:09-01:18 ET) were all around 69.1k, materially above the threshold.
- Polymarket market snapshot showed the 66,000 line trading around 98.6% Yes / 1.5% No.

## Evidence directly stated by source

- Polymarket directly states the resolution source and contract wording.
- Binance API directly states current spot price and recent 1-minute OHLCV values for BTCUSDT.

## What is uncertain

- The market does not resolve until the noon ET 1-minute candle closes, so several hours of intraday price movement remain.
- Current spot and recent candles do not guarantee the noon candle close.
- The fetched klines were a contextual live check, not the final settlement candle.

## Why this source may matter

This is the core evidence bundle for a narrow-resolution crypto threshold market. It provides both the authoritative settlement surface and a direct live market-state check on how much buffer currently exists versus the threshold.

## Possible impact on the question

The evidence strongly supports a high Yes probability because BTC is currently well above 66,000 and the contract uses a single clear authoritative source. The remaining decision-relevant question is whether any near-term catalyst or risk event could drive a drop of more than roughly 4.6% before noon ET.

## Reliability notes

- Binance is the named authoritative source for settlement, so source-of-truth reliability for mechanics is high.
- Polymarket is reliable for contract wording and current market pricing, but not the settlement source itself.
- Independence between these two surfaces is medium: Polymarket rules reference Binance, while Binance provides the actual price data.