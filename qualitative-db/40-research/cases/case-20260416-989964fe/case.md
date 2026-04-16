---
type: research_case
case_key: case-20260416-989964fe
case_id: cc0db6be-0982-44e7-b612-439278d42b88
market_id: 30172bb7-9f35-4ca6-93a4-adb8544ba07a
platform: polymarket
external_market_id: 0x99eb86c2cf41bbf90f3df2f839525c317790ad8b8024f55a80c997255e8787f7
slug: ethereum-above-2200-on-april-17
status: active
generated_by: orchestrator
---

# Will the price of Ethereum be above $2,200 on April 17?

## Case identity
- case_key: `case-20260416-989964fe`
- case_id: `cc0db6be-0982-44e7-b612-439278d42b88`
- market_id: `30172bb7-9f35-4ca6-93a4-adb8544ba07a`
- platform: `polymarket`
- external_market_id: `0x99eb86c2cf41bbf90f3df2f839525c317790ad8b8024f55a80c997255e8787f7`
- slug: `ethereum-above-2200-on-april-17`

## Market context
- current_price: `0.955`
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
