---
type: research_case
case_key: case-20260414-8dcead65
case_id: 640f94e6-19b4-4be6-9cf9-ae2043ef470e
market_id: d57c986f-d265-4622-bad7-78ce1c10a3f2
platform: polymarket
external_market_id: 0x5687ed31630b7f74c281562c52cf56ea1385fd249688c71eba96b62a6e8a8c26
slug: bitcoin-above-70k-on-april-15
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 15?

## Case identity
- case_key: `case-20260414-8dcead65`
- case_id: `640f94e6-19b4-4be6-9cf9-ae2043ef470e`
- market_id: `d57c986f-d265-4622-bad7-78ce1c10a3f2`
- platform: `polymarket`
- external_market_id: `0x5687ed31630b7f74c281562c52cf56ea1385fd249688c71eba96b62a6e8a8c26`
- slug: `bitcoin-above-70k-on-april-15`

## Market context
- current_price: `0.979`
- closes_at: `2026-04-15T12:00:00-04:00`
- resolves_at: `2026-04-15T12:00:00-04:00`

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
