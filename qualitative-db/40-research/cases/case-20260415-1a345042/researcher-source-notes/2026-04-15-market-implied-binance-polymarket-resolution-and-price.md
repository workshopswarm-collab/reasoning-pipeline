---
type: source_note
case_key: case-20260415-1a345042
dispatch_id: dispatch-case-20260415-1a345042-20260415T223206Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-1a345042 | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-21 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance BTCUSDT public market data API
source_type: primary+direct
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1a345042/researcher-analyses/2026-04-15/dispatch-case-20260415-1a345042-20260415T223206Z/personas/market-implied.md]
tags: [polymarket, binance, resolution-source, btc]
---

# Summary

This note captures the governing contract mechanics from the Polymarket market page plus a direct check that Binance public BTC/USDT price surfaces were reachable during the run.

## Key facts extracted

- Polymarket states the market resolves "Yes" if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-21 has a final close above 72,000.
- The contract is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the number of decimals in the source.
- During this run, Binance public API endpoints were reachable and returned live BTC/USDT data.
- Spot check during the run: Binance ticker price returned approximately 74,991.76, above the 72,000 threshold by about 2,991.76.
- Recent 1-minute klines were returned successfully, confirming the relevant data structure exists on the governing venue/source surface.

## Evidence directly stated by source

From the Polymarket rules page:
- resolution source is Binance BTC/USDT with 1m candles selected
- the relevant candle is the 12:00 ET candle on the title date
- the final close must be higher than 72,000 for a Yes resolution

From the Binance API check:
- ticker endpoint returned a live BTCUSDT price of 74,991.76000000
- 1-minute klines endpoint returned recent candles with standard OHLCV fields including close prices

## What is uncertain

- The market resolves on 2026-04-21 at 12:00 ET, so current spot price does not settle the market.
- Intraday BTC volatility over the next ~5.5 days could still take the noon ET close below 72,000.
- Public API availability today does not guarantee there will be no temporary Binance UI/API issues at resolution time, though the contract names Binance as source of truth.

## Why this source may matter

This is the core direct evidence set for both contract interpretation and current distance-to-threshold. It anchors the market-implied analysis in the actual resolution mechanics rather than a generic BTC price thesis.

## Possible impact on the question

The source strongly supports the market's current high Yes probability because BTC is presently several thousand dollars above the threshold and the contract only asks whether a single specified noon ET Binance close remains above 72,000.

## Reliability notes

- Polymarket is authoritative for the contract wording but not for underlying BTC price truth.
- Binance is authoritative for the contract's settlement source but remains an exchange-operated surface, so exchange-specific operational quirks remain a residual risk.
- This source pair is strong for direct mechanics and live state, but not sufficient by itself to rule out volatility over the remaining days to resolution.