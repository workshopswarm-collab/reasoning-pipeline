---
type: source_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-13
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-13 close above 70000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance BTCUSDT market data API and Polymarket market page
source_type: primary_market_data_plus_market_contract
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=240
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, source-note, candle-resolution, timing]
---

# Summary

This note captures the governing source-of-truth mechanics and immediate price context for the April 13 BTC > 70,000 market. The key point is that resolution depends specifically on the Binance BTC/USDT 1-minute candle labeled 12:00 ET, not on a daily close, not on another exchange, and not on a broader intraday average.

## Key facts extracted

- Polymarket rules state the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET has a final Close above 70,000.
- Polymarket also states Binance BTC/USDT is the resolution source, with 1m candles selected.
- Binance public API was reachable during research and returned live BTCUSDT market data.
- Binance server time during research was 1776088369173 ms, which corresponds to 2026-04-13 13:52:49 UTC, showing the market had not yet reached the 16:00 UTC candle that corresponds to 12:00 ET.
- Recent Binance BTCUSDT trade context during research showed ticker price around 71,415.16.
- The last 240 one-minute candles fetched during research showed last close 71,372.35, first close 70,769.92, net gain about 0.85%, mean absolute one-minute move about 0.036%, and max absolute one-minute move about 0.516%.

## Evidence directly stated by source

- From Polymarket market page: resolution is based on the Binance BTC/USDT 12:00 ET 1-minute candle close.
- From Binance API: BTCUSDT was trading above 70,000 during the research window and Binance data endpoints were functioning.

## What is uncertain

- The exact noon ET candle close was not yet available during research because the relevant candle had not occurred.
- Binance web UI language around timezone display was not independently fetched in a clean way, so the strongest verification comes from converting 12:00 ET to 16:00 UTC and matching that to Binance API timestamps.
- No single scheduled macro release was identified from the limited contextual pass; the dominant near-term catalyst is broad BTC intraday risk sentiment and any sudden tape shock before noon ET.

## Why this source may matter

This is the governing direct source for settlement and the best available live context for whether the market is likely to finish above or below the threshold.

## Possible impact on the question

Because BTC was already meaningfully above 70,000 several hours before the relevant candle, the threshold looked favorable to Yes absent a sharp intraday drawdown. The main remaining risk was path risk between the research time and the 12:00 ET candle close.

## Reliability notes

- Binance API is a high-credibility direct market-data source for this contract because Binance is the named source of truth.
- Polymarket market page is a high-credibility contract-definition source for resolution mechanics.
- Evidence independence is only moderate because both sources are tightly linked to the same market mechanism rather than independent analytic views.
- This note is strong on resolution mechanics and live level checking, but weaker on broader catalyst calendar context.