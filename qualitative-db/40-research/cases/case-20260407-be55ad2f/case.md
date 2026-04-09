---
type: research_case
case_key: case-20260407-be55ad2f
case_id: df38adf0-efff-4fef-9757-16c847dd1539
market_id: 314a929f-958f-4c98-8d7c-9b0ab2f4a8d4
platform: polymarket
external_market_id: 0xb3c82a8559f176ebd1fba0b82a2be00d4f5b8e8b9d151a17a1531cb54b7fb954
slug: bitcoin-above-66k-on-april-8
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $66,000 on April 8?

## Case identity
- case_key: `case-20260407-be55ad2f`
- case_id: `df38adf0-efff-4fef-9757-16c847dd1539`
- market_id: `314a929f-958f-4c98-8d7c-9b0ab2f4a8d4`
- platform: `polymarket`
- external_market_id: `0xb3c82a8559f176ebd1fba0b82a2be00d4f5b8e8b9d151a17a1531cb54b7fb954`
- slug: `bitcoin-above-66k-on-april-8`

## Market context
- current_price: `0.896`
- closes_at: `2026-04-08T12:00:00-04:00`
- resolves_at: `2026-04-08T12:00:00-04:00`

## Description
This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".

The resolution source for this market is Binance, specifically the BTC/USDT "Close" prices currently available at https://www.binance.com/en/trade/BTC_USDT with "1m" and "Candles" selected on the top bar.

Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs.

Price precision is determined by the number of decimal places in the source.

## Case surfaces
- `researcher-swarm-current.md` = latest/current researcher swarm pointers
- `timeline.md` = programmatic lifecycle summary
- `researcher-source-notes/` = case-level source provenance across analyses
- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only analysis generations
