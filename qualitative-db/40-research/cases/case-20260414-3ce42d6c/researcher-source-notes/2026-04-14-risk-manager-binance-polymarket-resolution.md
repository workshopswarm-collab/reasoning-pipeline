---
type: source_note
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-14 be above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market rules + Binance Spot API kline docs and live query
source_type: primary-plus-verification
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ce42d6c/researcher-analyses/2026-04-14/dispatch-case-20260414-3ce42d6c-20260414T130958Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution-mechanics, date-sensitive]
---

# Summary

The market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-14, with a Yes outcome only if the final Close is strictly higher than 70,000. Polymarket names Binance web chart candles as the governing source of truth. As an additional verification pass, Binance Spot REST kline documentation confirms 1-minute klines are database-backed and can be queried with UTC timestamps plus an optional `timeZone` parameter for interval interpretation. A live REST query at the relevant future timestamp returned an empty array, which is consistent with the noon ET candle not having occurred yet at research time rather than with any contract defect.

## Key facts extracted

- Polymarket rule text says resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone.
- The condition is strict: the final Close must be higher than 70,000, not equal to 70,000.
- Price precision is determined by the source.
- Binance Spot API documentation states `GET /api/v3/klines` returns kline/candlestick bars and that `timeZone` can be used so intervals are interpreted in a specified timezone, while `startTime` and `endTime` remain UTC.
- Live query to Binance Spot ticker returned BTCUSDT around 74,544.7 during research time, materially above 70,000.
- Live query to the specific future noon-ET minute returned `[]`, as expected before that candle exists.
- Historical control queries for prior dates returned normal kline payloads, supporting that the empty result is a timing artifact rather than a broken endpoint.

## Evidence directly stated by source

- Polymarket directly states the contract mechanics and governing source.
- Binance docs directly state kline endpoint behavior, parameter semantics, and that klines are database-backed.

## What is uncertain

- The contract references the Binance website chart as source of truth rather than explicitly the public REST API, so there is a small implementation-surface ambiguity if UI and API were to diverge temporarily.
- Intraday price could still move below 70,000 before noon ET despite being far above it during research time.

## Why this source may matter

This is the core contract-interpretation source and the main verification source for operational resolution mechanics. For a narrow date-and-time market, this is more important than broader Bitcoin narratives.

## Possible impact on the question

These sources support a high-probability Yes lean, but they also define the main residual risk correctly: not “Is BTC generally strong?” but “Will the Binance BTC/USDT 12:00 ET one-minute close still be above 70,000 at settlement?”

## Reliability notes

- Polymarket rules are authoritative for contract mechanics.
- Binance API docs are authoritative for API semantics but are one step removed from the UI chart explicitly named in rules.
- Live Binance queries provide useful verification but do not themselves settle the market before the relevant candle exists.
- Evidence independence is medium because both key inputs point back to Binance as the ultimate price source.