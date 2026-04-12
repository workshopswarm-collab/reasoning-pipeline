---
type: research_case
case_key: case-20260409-746679d3
case_id: b24a11ac-d7b4-4df1-89bb-c4624a69adc7
market_id: 182a7e4c-918b-419c-9547-fc5036bfa9bf
platform: polymarket
external_market_id: 0x400035edb2f06b436d7c67662962782f38f4ce3536e12e5897b9023dbc8bb2a3
slug: ethereum-above-2100-on-april-10
status: active
generated_by: orchestrator
---

# Will the price of Ethereum be above $2,100 on April 10?

## Case identity
- case_key: `case-20260409-746679d3`
- case_id: `b24a11ac-d7b4-4df1-89bb-c4624a69adc7`
- market_id: `182a7e4c-918b-419c-9547-fc5036bfa9bf`
- platform: `polymarket`
- external_market_id: `0x400035edb2f06b436d7c67662962782f38f4ce3536e12e5897b9023dbc8bb2a3`
- slug: `ethereum-above-2100-on-april-10`

## Market context
- current_price: `0.94`
- closes_at: `2026-04-10T12:00:00-04:00`
- resolves_at: `2026-04-10T12:00:00-04:00`

## Description
This market will resolve to "Yes" if the Binance 1 minute candle for ETH/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".

The resolution source for this market is Binance, specifically the ETH/USDT "Close" prices currently available at https://www.binance.com/en/trade/ETH_USDT with "1m" and "Candles" selected on the top bar.

Please note that this market is about the price according to Binance ETH/USDT, not according to other exchanges or trading pairs.

Price precision is determined by the number of decimal places in the source.

## Case surfaces
- `researcher-swarm-current.md` = latest/current researcher swarm pointers
- `timeline.md` = programmatic lifecycle summary
- `researcher-source-notes/` = case-level source provenance across researcher analyses
- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only researcher analysis generations
