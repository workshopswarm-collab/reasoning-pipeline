---
type: source_note
case_key: case-20260416-dfb8f85e
dispatch_id: dispatch-case-20260416-dfb8f85e-20260416T140232Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: binance-btcusdt-market-state
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-21 close above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance spot/API market data
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-dfb8f85e/researcher-analyses/2026-04-16/dispatch-case-20260416-dfb8f85e-20260416T140232Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, spot-price, resolution-source]
---

# Summary

This note captures the directly relevant exchange data from Binance, which is also the governing resolution venue for the contract.

## Key facts extracted

- Binance BTC/USDT last traded around 73,797 on 2026-04-16 during the research run.
- Binance 24h high was 75,425 and 24h low was 73,309.85.
- Binance 5-minute average price endpoint returned roughly 73,705.
- Recent 1-minute klines around the run time showed closes in the 73,650-73,791 range.

## Evidence directly stated by source

- `ticker/price`: BTCUSDT price `73790.89000000`.
- `avgPrice`: 5-minute average `73705.21631255`.
- `ticker/24hr`: last price `73797.25000000`, high `75425.00000000`, low `73309.85000000`, weighted average `74557.38195997`.
- `klines?interval=1m&limit=5`: recent one-minute closes of approximately 73,651; 73,729; 73,697; 73,656; 73,791.

## What is uncertain

- This is only a current-state snapshot, not a forecast.
- The market resolves on the 12:00 ET one-minute candle on 2026-04-21, so interim prices can drift materially.
- Binance UI candle display and API data should normally align, but the contract language specifically points users to the Binance trading interface.

## Why this source may matter

The contract explicitly resolves using Binance BTC/USDT 1-minute candle close data, so Binance is both the market-state source and the source of truth for settlement mechanics.

## Possible impact on the question

Current Binance spot trading above 72,000 by ~1,800 with recent intraday trading above 75,000 suggests the hurdle is close enough to spot that a moderate selloff over the next five days could still flip the market, but the current level gives the yes side an initial buffer.

## Reliability notes

High reliability for current exchange-state facts and contract relevance, because Binance is the specified resolution venue. Lower reliability for broader forecasting beyond the current snapshot because this source does not itself explain why price should stay above 72,000 through resolution.