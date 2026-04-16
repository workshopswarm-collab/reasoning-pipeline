---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: threshold-daily-close
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, rules, binance, btc]
---

# Summary

Polymarket states that this market resolves from the Binance BTC/USDT **1 minute candle for 12:00 ET on April 20**, using the candle's final **Close** price, not an intraday high and not another exchange. The event page also showed the 70,000 line trading around **94c Yes / 8c No** at fetch time, consistent with the assignment's current price of 0.93.

## Key facts extracted

- Contract condition: Yes if the Binance BTC/USDT 1-minute candle for **12:00 in ET timezone** on April 20 has a final **Close** price higher than 70,000.
- Governing source explicitly named: Binance BTC/USDT chart with **1m** candles selected.
- Price precision is determined by Binance source precision.
- Market page at fetch time displayed the 70,000 bracket around **93%-94%**.

## Evidence directly stated by source

- The market is about **Binance BTC/USDT**, not another exchange or another pair.
- The relevant observation is a **single minute close** at a specified local time.
- Other nearby thresholds on the same page imply a steep distribution centered well above 70k by April 20.

## What is uncertain

- The public market page does not itself prove what the April 20 noon ET candle will be; it only states the contract mechanics and the crowd price.
- The page does not show the final source-of-truth candle in advance, so a later direct Binance check remains required.

## Why this source may matter

This is the governing contract language. For a date-sensitive close market, the exact time, timezone, pair, and candle field matter more than generic BTC price commentary.

## Possible impact on the question

This source sharply narrows the problem. A bullish intraday or multi-exchange thesis is not sufficient; the question is whether Binance BTC/USDT remains above 70,000 exactly at noon ET on April 20 on the 1-minute closing print.

## Reliability notes

High reliability for contract interpretation and contemporaneous market price. Lower reliability for forecasting the underlying BTC path, because it is not an independent market-data source.