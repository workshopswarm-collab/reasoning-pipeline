---
type: source_note
case_key: case-20260407-42a10bc6
dispatch_id: dispatch-case-20260407-42a10bc6-20260407T014927Z
analysis_date: 2026-04-07
persona: base-rate
domain: crypto
subdomain: exchange-market-structure
entity: binance
topic: case-20260407-42a10bc6 | base-rate
question: Will the price of Bitcoin be above $68,000 on April 7?
driver: reliability
date_created: 2026-04-06
source_name: Binance BTCUSDT API + Polymarket market rules page
source_type: primary_market_data_and_contract_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [bitcoin, binance]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-42a10bc6/researcher-analyses/2026-04-07/dispatch-case-20260407-42a10bc6-20260407T014927Z/personas/base-rate.md]
tags: [binance, btcusdt, 1m-candle, resolution-source, timezone-check]
---

# Summary

This source note captures the direct resolution source mechanics and the live Binance BTC/USDT context before the relevant noon ET candle occurs.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 7, using the final close price.
- The named source of truth is Binance BTC/USDT, not other exchanges or trading pairs.
- The target timestamp 2026-04-07 12:00 ET converts to 2026-04-07 16:00 UTC because New York is on EDT (UTC-4) on this date.
- A direct Binance kline query for startTime corresponding to 2026-04-07 16:00:00 UTC returned an empty array at research time, which is expected because the candle had not happened yet.
- Binance exchangeInfo reports exchange timezone as UTC.
- Binance spot ticker at research time showed BTCUSDT last price 68485.64.
- Binance 24h ticker at research time showed high 70351.46, low 68300.00, and last price 68485.64.
- Recent 1-minute klines immediately before research time showed BTC/USDT trading in the mid-68500s and drifting down from earlier levels.

## Evidence directly stated by source

Direct from Polymarket rules page:
- resolution source is Binance
- instrument is BTC/USDT
- time reference is 12:00 ET
- settlement field is the final 1-minute candle close
- threshold comparison is strictly higher than 68000

Direct from Binance public API:
- BTCUSDT last traded price around research time was 68485.64
- 24h range included both values materially above and near the threshold
- exchange metadata uses UTC, which matters for mapping noon ET to the correct candle

## What is uncertain

- The actual settlement candle had not yet occurred during this run.
- API output is a convenient direct surface for verification, but Polymarket text names the Binance trading page candle display as the formal resolution surface.
- Intraday BTC volatility could move the final noon ET close materially by resolution time.

## Why this source may matter

This is the core direct evidence set because the market is narrowly defined by one exchange, one pair, one one-minute candle, and a specific timezone mapping.

## Possible impact on the question

The live Binance price already being above 68000 several hours before noon ET makes a Yes outcome plausible, but not close to certain because BTC is close enough to the threshold that ordinary intraday movement could still flip the final candle close below 68000.

## Reliability notes

- Binance is the explicit settlement source, so source-of-truth ambiguity is low.
- The remaining risk is operational/interpretive rather than epistemic: making sure noon ET maps to 16:00 UTC and that the relevant candle is the one opening at 16:00 UTC and closing at 16:00:59.999 UTC.
- The direct future-candle query returning empty before 16:00 UTC is a useful verification of timing rather than a data failure.