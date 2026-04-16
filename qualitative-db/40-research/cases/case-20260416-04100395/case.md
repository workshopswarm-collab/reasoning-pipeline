---
type: research_case
case_key: case-20260416-04100395
case_id: d6ce2cc4-e862-4b7a-bd77-26fbbcd1f5fb
market_id: b7a0f9a1-95a0-48be-a965-a36923e72e1b
platform: polymarket
external_market_id: 0xcd0c4035e9811bdcaa8c86056d93c4c953513b912103dc12439ac23034bd3f70
slug: ethereum-above-2300-on-april-17
status: active
generated_by: orchestrator
---

# Will the price of Ethereum be above $2,300 on April 17?

## Case identity
- case_key: `case-20260416-04100395`
- case_id: `d6ce2cc4-e862-4b7a-bd77-26fbbcd1f5fb`
- market_id: `b7a0f9a1-95a0-48be-a965-a36923e72e1b`
- platform: `polymarket`
- external_market_id: `0xcd0c4035e9811bdcaa8c86056d93c4c953513b912103dc12439ac23034bd3f70`
- slug: `ethereum-above-2300-on-april-17`

## Market context
- current_price: `0.725`
- closes_at: `2026-04-17T12:00:00-04:00`
- resolves_at: `2026-04-17T12:00:00-04:00`

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
