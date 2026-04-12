---
type: research_case
case_key: case-20260411-6669dcdb
case_id: 14a14232-490c-4977-8612-adffbf4f85c6
market_id: 0f1963df-4f17-446a-8848-47ca3ff7f2f9
platform: polymarket
external_market_id: 0xe80d5ca4e27b7796254fac4889351f248b0b4de774a90993c812da7f05604718
slug: bitcoin-above-72k-on-april-11
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $72,000 on April 11?

## Case identity
- case_key: `case-20260411-6669dcdb`
- case_id: `14a14232-490c-4977-8612-adffbf4f85c6`
- market_id: `0f1963df-4f17-446a-8848-47ca3ff7f2f9`
- platform: `polymarket`
- external_market_id: `0xe80d5ca4e27b7796254fac4889351f248b0b4de774a90993c812da7f05604718`
- slug: `bitcoin-above-72k-on-april-11`

## Market context
- current_price: `0.7125`
- closes_at: `2026-04-11T12:00:00-04:00`
- resolves_at: `2026-04-11T12:00:00-04:00`

## Description
This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".

The resolution source for this market is Binance, specifically the BTC/USDT "Close" prices currently available at https://www.binance.com/en/trade/BTC_USDT with "1m" and "Candles" selected on the top bar.

Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs.

Price precision is determined by the number of decimal places in the source.

## Case surfaces
- `researcher-swarm-current.md` = latest/current researcher swarm pointers
- `timeline.md` = programmatic lifecycle summary
- `researcher-source-notes/` = case-level source provenance across researcher analyses
- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only researcher analysis generations
