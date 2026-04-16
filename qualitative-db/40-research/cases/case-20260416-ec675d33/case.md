---
type: research_case
case_key: case-20260416-ec675d33
case_id: 1bef66f8-862e-4189-952c-8691d348e1ba
market_id: 796b4cfe-3528-418b-81e3-fd10fd74838d
platform: polymarket
external_market_id: 0x0b48d5d3b00735aa0fa83d1d2d18eb11ef397efba02edf50cdb78681944192eb
slug: bitcoin-above-72k-on-april-20
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $72,000 on April 20?

## Case identity
- case_key: `case-20260416-ec675d33`
- case_id: `1bef66f8-862e-4189-952c-8691d348e1ba`
- market_id: `796b4cfe-3528-418b-81e3-fd10fd74838d`
- platform: `polymarket`
- external_market_id: `0x0b48d5d3b00735aa0fa83d1d2d18eb11ef397efba02edf50cdb78681944192eb`
- slug: `bitcoin-above-72k-on-april-20`

## Market context
- current_price: `0.845`
- closes_at: `2026-04-20T12:00:00-04:00`
- resolves_at: `2026-04-20T12:00:00-04:00`

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
