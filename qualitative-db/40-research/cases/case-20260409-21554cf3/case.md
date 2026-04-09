---
type: research_case
case_key: case-20260409-21554cf3
case_id: c6ca2b6c-e255-413a-9016-cf903afa4360
market_id: 81a24229-d313-44a2-9e5e-246895601af7
platform: polymarket
external_market_id: 0x34b2b7b84d4e65cb8a61df3ca88871acdb93c8fb7500f912b9e02687317627fb
slug: ethereum-above-2100-on-april-9
status: active
generated_by: orchestrator
---

# Will the price of Ethereum be above $2,100 on April 9?

## Case identity
- case_key: `case-20260409-21554cf3`
- case_id: `c6ca2b6c-e255-413a-9016-cf903afa4360`
- market_id: `81a24229-d313-44a2-9e5e-246895601af7`
- platform: `polymarket`
- external_market_id: `0x34b2b7b84d4e65cb8a61df3ca88871acdb93c8fb7500f912b9e02687317627fb`
- slug: `ethereum-above-2100-on-april-9`

## Market context
- current_price: `0.9515`
- closes_at: `2026-04-09T12:00:00-04:00`
- resolves_at: `2026-04-09T12:00:00-04:00`

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
