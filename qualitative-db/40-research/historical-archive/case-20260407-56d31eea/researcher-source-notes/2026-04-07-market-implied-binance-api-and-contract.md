---
type: source_note
case_key: case-20260407-56d31eea
dispatch_id: dispatch-case-20260407-56d31eea-20260407T023203Z
analysis_date: 2026-04-07
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: binance
topic: case-20260407-56d31eea | market-implied
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-07 close above 66000?
driver: operational-risk
date_created: 2026-04-06
source_name: Binance spot API klines plus Polymarket market rules
source_type: exchange-api-and-market-rules
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [bitcoin, binance]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-56d31eea/researcher-analyses/2026-04-07/dispatch-case-20260407-56d31eea-20260407T023203Z/personas/market-implied.md]
tags: [binance, btcusdt, candle-close, resolution-source]
---

# Summary

This note captures the governing resolution mechanics and a direct verification pass on Binance BTC/USDT pricing shortly before the market resolves.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-07, specifically the final `Close` price.
- The rule is explicit that the source is Binance BTC/USDT, not other exchanges or pairs.
- Binance API documentation states `GET /api/v3/klines` returns kline/candlestick bars and that each bar includes open time and close price.
- A live Binance API check around the time of research showed BTCUSDT spot price around 68.56k.
- Recent 1-minute klines fetched directly from Binance showed closes around 68.56k-68.59k, materially above the 66k threshold.

## Evidence directly stated by source

From the Polymarket contract page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices..."

From Binance API docs:
- `GET /api/v3/klines` returns candlestick bars.
- The response contains close price and allows a `timeZone` parameter; start/end times remain UTC.

Live Binance API outputs observed during this run:
- ticker price: 68557.00000000, then 68565.33000000 on repeat check.
- recent 1m klines without timezone parameter closed at 68580.00, 68580.01, 68592.59, 68561.29, 68565.33.
- recent 1m klines with `timeZone=-4` returned matching same-range prices, supporting the ET interpretation check.

## What is uncertain

- The market resolves on the specific 12:00 ET candle, not on the spot price at research time.
- Bitcoin can move materially before noon, though the current buffer over 66k is about 2.5k.
- The exact UI-displayed candle and API-returned final close should normally align, but the rule text names the Binance trading UI surface rather than the API endpoint directly.

## Why this source may matter

This is the core direct evidence set because it establishes both the source of truth and the live distance from the threshold using the same exchange and pair named in the contract.

## Possible impact on the question

If Binance BTC/USDT remains near observed levels into noon ET, the market should resolve Yes. The main remaining risk is an intraday drop of more than roughly 3.7% before the relevant minute closes.

## Reliability notes

- High credibility for settlement mechanics because the contract text is explicit.
- High credibility for live spot context because the data is pulled directly from Binance.
- Moderate implementation ambiguity remains because Polymarket cites the Binance chart UI rather than spelling out an API query, but the underlying series should be the same unless there is a display or timing discrepancy.