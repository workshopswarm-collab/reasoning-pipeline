---
type: research_case
case_key: case-20260413-63496469
case_id: 30a4e286-820a-4f6a-9828-4e056ceaf63c
market_id: 702781b5-47f2-4e94-a638-a67213619a3e
platform: polymarket
external_market_id: 0x1c2f06de72ad9ecd9a25babc2a908302261686659d642c9d369946ce0d1bfdd3
slug: bitcoin-above-66k-on-april-14
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $66,000 on April 14?

## Case identity
- case_key: `case-20260413-63496469`
- case_id: `30a4e286-820a-4f6a-9828-4e056ceaf63c`
- market_id: `702781b5-47f2-4e94-a638-a67213619a3e`
- platform: `polymarket`
- external_market_id: `0x1c2f06de72ad9ecd9a25babc2a908302261686659d642c9d369946ce0d1bfdd3`
- slug: `bitcoin-above-66k-on-april-14`

## Market context
- current_price: `0.957`
- closes_at: `2026-04-14T12:00:00-04:00`
- resolves_at: `2026-04-14T12:00:00-04:00`

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
