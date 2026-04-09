---
type: source_note
case_key: case-20260407-42a10bc6
dispatch_id: dispatch-case-20260407-42a10bc6-20260407T014927Z
analysis_date: 2026-04-07
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: case-20260407-42a10bc6 | market-implied
question: Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-07 close above 68000?
driver: reliability
date_created: 2026-04-06
source_name: Binance BTCUSDT API + Polymarket rules page
source_type: primary-plus-contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=3 ; https://polymarket.com/event/bitcoin-above-on-april-7
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [bitcoin, binance]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-42a10bc6/researcher-analyses/2026-04-07/dispatch-case-20260407-42a10bc6-20260407T014927Z/personas/market-implied.md]
tags: [binance, polymarket, btcusdt, source-of-truth, timezone]
---

# Summary

This note combines the governing market rules from Polymarket with direct Binance API checks relevant to the settlement source. The core takeaway is that the contract is mechanically simple but time-sensitive: the governing candle is the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-07, which maps to 16:00 UTC because New York is on EDT (UTC-4) on that date.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT 1-minute candle for "12:00 in the ET timezone (noon)" on the specified date, using the final Close price.
- The rule text names Binance BTC/USDT specifically and excludes other exchanges and pairs.
- A timezone conversion check shows 2026-04-07 12:00 America/New_York = 2026-04-07 16:00 UTC.
- Binance exchange metadata shows BTCUSDT is an active trading symbol and price precision includes cents via `tickSize` 0.01, which matches the contract statement that source precision governs settlement precision.
- Direct Binance spot ticker check during research showed BTCUSDT around 68,526.79, i.e. modestly above the 68,000 threshold.
- A direct historical kline request for the target future minute returned an empty array at research time, confirming the candle was not yet available and that the question remained unresolved.
- Recent live 1-minute klines from Binance were active and normal, indicating no immediate evidence of feed outage or symbol interruption.

## Evidence directly stated by source

- Polymarket explicitly states the resolution source and condition: Binance BTC/USDT 1-minute candle close above 68,000 at 12:00 ET.
- Binance API directly provides current BTCUSDT spot price, exchange metadata, and recent 1-minute klines.

## What is uncertain

- The actual 16:00 UTC / 12:00 ET candle close was not yet observable at research time.
- Intraday crypto volatility could move BTC below 68,000 by the governing close even if spot is above it now.
- There is some implementation ambiguity in Binance naming conventions because API klines are timestamped in UTC; the contract language references ET. The cleanest interpretation is to map noon ET to the UTC minute beginning at 16:00:00Z.

## Why this source may matter

It directly defines both the settlement mechanism and the most relevant live context for whether the threshold is likely to be cleared. For this market, Binance is not just a contextual exchange source; it is the governing source of truth.

## Possible impact on the question

These checks support a moderately bullish reading relative to the 68,000 threshold because live Binance spot was already above the line by roughly $527 during research. But because settlement depends on one exact future 1-minute close rather than the broader daily range, the margin is not so wide that the outcome should be treated as near-certain.

## Reliability notes

- Primary rule source quality: high for contract interpretation, though Polymarket page fetch is a web rendering rather than API docs.
- Primary market data source quality: high because Binance is the named settlement source and its public API surfaces align with the rule mechanics.
- Independence is limited because both the live-price and settlement-source checks point back to Binance; this is acceptable here because the market itself is directly governed by Binance.
- Main residual risk is not source credibility but timing/label interpretation around which UTC minute corresponds to 12:00 ET.