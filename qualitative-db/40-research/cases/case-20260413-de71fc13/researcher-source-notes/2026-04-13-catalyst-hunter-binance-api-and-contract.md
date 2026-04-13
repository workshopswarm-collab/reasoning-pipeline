---
type: source_note
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-13
question: Will the Binance BTC/USDT 1m candle for 2026-04-13 12:00 ET close above 68000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance spot API + Polymarket contract page
source_type: primary_market_data_and_contract
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-de71fc13/researcher-analyses/2026-04-13/dispatch-case-20260413-de71fc13-20260413T130158Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, resolution-source, settlement-mechanics, timing]
---

# Summary

The governing contract says this market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-13, using the candle's final Close price. Direct Binance API checks confirm BTC/USDT traded around 71.1k in the latest available 1-minute candles visible at research time, comfortably above 68k, but the exact 12:00 ET candle was not yet retrievable from the public API during this run.

## Key facts extracted

- Polymarket contract text explicitly defines the source of truth as Binance BTC/USDT with 1m candles, using the 12:00 ET candle's final Close price.
- Binance spot API `exchangeInfo` confirms BTCUSDT is an active trading pair and the price tick size is 0.01, so precision is not a meaningful issue versus a 68000 threshold.
- Binance API `time` returned server time `1776085526524`, which corresponds to 2026-04-13 13:05:26 UTC.
- Binance API `klines?symbol=BTCUSDT&interval=1m&limit=5` returned latest visible candles with closes between 71117.98 and 71139.49.
- A direct query for the exact 2026-04-13 12:00 ET candle (`startTime=1776096000000`, which is 16:00 UTC) returned no candle yet during this run.
- Additional targeted checks showed data available for 08:00 ET and 09:00 ET, but not yet for 10:00 ET onward, implying either API availability lag, retention/access quirks for future timestamps relative to available exchange data, or a mismatch between visible server-time freshness and requested historical window.

## Evidence directly stated by source

- Direct contract language from Polymarket: resolution is based on Binance BTC/USDT 1m candle close at 12:00 ET.
- Direct Binance kline outputs show latest available close values above 71k.
- Direct Binance API absence of the exact target candle at research time means the market is not directly settled by the authoritative minute yet from this interface.

## What is uncertain

- Why the exact target minute was unavailable despite the assignment timestamp being after market close in ET.
- Whether Binance web UI would already show the relevant candle while public API access still lagged or truncated.
- Whether the missing later-hour candles reflect data-delay, endpoint behavior, or another operational/access quirk.

## Why this source may matter

This is the primary evidence set for both contract mechanics and the eventual authoritative settlement condition. It is also the main reason the directional view is extremely high-confidence while still not literally 100% from direct settlement evidence at the instant of research.

## Possible impact on the question

Because all visible direct Binance prices during the run are materially above 68000, the market's very high Yes pricing looks directionally justified. The only meaningful residual risk is settlement-surface/timing ambiguity around the exact ET-noon candle retrieval, not underlying price level risk.

## Reliability notes

- Binance is the explicit governing source of truth for settlement, so source authority is high.
- The public API outputs are machine-readable and direct.
- Reliability caveat: the exact target minute was not retrievable during this run, so there is an operational-access ambiguity even though the observed price level is far above the threshold.