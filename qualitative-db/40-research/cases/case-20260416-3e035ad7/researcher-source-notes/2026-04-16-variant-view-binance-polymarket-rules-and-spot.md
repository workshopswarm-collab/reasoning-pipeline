---
type: source_note
case_key: case-20260416-3e035ad7
dispatch_id: dispatch-case-20260416-3e035ad7-20260416T043505Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 70000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules page plus Binance spot/API checks
source_type: market rules + exchange direct data
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-3e035ad7/researcher-analyses/2026-04-16/dispatch-case-20260416-3e035ad7-20260416T043505Z/personas/variant-view.md]
tags: [source-note, polymarket, binance, resolution]
---

# Summary

This note captures the direct resolution mechanics from Polymarket and a direct spot/API check from Binance. The combined takeaway is that the contract is mechanically simple but timing-sensitive: it resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-17, and current Binance spot was already around 74.98k roughly 35.4 hours before that candle.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 17 has a final close strictly higher than 70,000.
- The rules specify Binance BTC/USDT, not other exchanges or other trading pairs.
- Price precision is determined by the source.
- Current market price on the assigned contract was about 0.9915, implying about 99.15% Yes.
- Direct Binance ticker check returned BTCUSDT at 74,975.57 on 2026-04-16 00:37 ET.
- A direct Binance kline check for recent 1-minute candles showed contemporaneous closes around 74.9k.
- Time conversion check: the relevant resolution minute is 2026-04-17 12:00 ET = 2026-04-17 16:00 UTC because the date is in EDT.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From direct Binance API observations:
- ticker endpoint returned BTCUSDT 74,975.57.
- recent 1m klines were also clustered near 74.9k.

## What is uncertain

- The contract settles on a future minute, not the current price, so a large downside move before noon ET Apr. 17 could still flip the market to No.
- Binance direct future-candle query for the target minute naturally returned no data yet because the minute had not happened.
- The rules page does not separately spell out outage/fallback handling on the fetched page excerpt, so operational edge cases remain low-probability but not totally specified in this note.

## Why this source may matter

This is the governing source-of-truth surface plus a direct exchange-level spot check. It establishes both the exact contract mechanics and the starting distance from the threshold.

## Possible impact on the question

Because spot was already nearly 5k above the threshold with only about 35 hours left, the market's extreme Yes pricing is directionally understandable. The main residual risk is not interpretive ambiguity but a sufficiently large BTC drawdown or an operational/source edge case before the specific noon ET candle.

## Reliability notes

- Polymarket rules are the relevant contract-definition source, so credibility is high for mechanics.
- Binance is the named settlement source, so its direct data is authoritative for price reference.
- Independence is only medium because Polymarket itself points to Binance, but this is appropriate for a rule-driven market.
- Remaining ambiguity is mostly about operational edge cases, not about the basic threshold test.