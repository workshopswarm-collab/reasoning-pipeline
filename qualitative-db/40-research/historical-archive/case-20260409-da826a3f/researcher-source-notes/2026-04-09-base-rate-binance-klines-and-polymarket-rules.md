---
type: source_note
case_key: case-20260409-da826a3f
dispatch_id: dispatch-case-20260409-da826a3f-20260409T211410Z
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: btc-daily-close
entity: btc
topic: bitcoin-above-68k-on-april-10
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-10 close above 68000?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance spot API market-data docs and Polymarket market rules
source_type: primary-plus-resolution-context
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data ; https://polymarket.com/event/bitcoin-above-on-april-10
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-da826a3f/researcher-analyses/2026-04-09/dispatch-case-20260409-da826a3f-20260409T211410Z/personas/base-rate.md]
tags: [binance, polymarket, resolution-mechanics, timezone]
---

# Summary

This source note records the two key direct surfaces for this case: Polymarket’s own rule text and Binance’s spot market-data documentation for 1-minute klines.

## Key facts extracted

- Polymarket says the market resolves from the Binance BTC/USDT 1-minute candle for **12:00 ET** on the date in the title, using the candle’s final **Close** price.
- Polymarket explicitly says the source is Binance BTC/USDT, not other exchanges or pairs.
- Binance’s spot API docs for `GET /api/v3/klines` and `GET /api/v3/uiKlines` say:
  - klines are uniquely identified by **open time**
  - `timeZone` can be provided so kline intervals are interpreted in that timezone rather than UTC
  - `startTime` and `endTime` are still interpreted in **UTC regardless of `timeZone`**
- ET on 2026-04-10 is EDT (`UTC-4`), so **12:00 ET = 16:00 UTC**.
- During this run, spot BTC/USDT was approximately **72.3k**, materially above the 68k strike, making the base-rate path favor “Yes” absent a large same-day selloff.

## Evidence directly stated by source

- Polymarket rules directly state the governing contract mechanics.
- Binance docs directly state the kline endpoint behavior, including timezone handling and identification by open time.

## What is uncertain

- The public docs do not by themselves prove whether Polymarket staff will visually inspect the Binance web UI candle versus query the API, though the contract language points to Binance candles generally and the API behavior is strongly consistent with the chart mechanics.
- This note does not establish the final 2026-04-10 12:00 ET candle close; it only clarifies how that candle should be identified and why the current state makes “Yes” a high-probability base-rate outcome.

## Why this source may matter

This market is mostly about **resolution mechanics and timing alignment** rather than deep macro thesis. The important failure mode is mis-mapping the ET candle to the wrong UTC minute or misunderstanding whether the relevant candle is the one opened at 12:00 ET.

## Possible impact on the question

These sources strongly reduce rule/timing ambiguity. Once 12:00 ET is mapped to 16:00 UTC and the candle is understood as the 1-minute bar opened at 12:00 ET, the key remaining uncertainty is simply whether BTC can fall below 68k by then.

## Reliability notes

- Binance API docs are the best direct technical source for how Binance klines are indexed and how timezone conversion works.
- Polymarket’s own market page is the authoritative source for the market’s stated settlement rule.
- The two sources are not fully independent, but they address different layers: contract wording versus exchange data mechanics.
