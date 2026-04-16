---
type: source_note
case_key: case-20260414-fdb38a8b
dispatch_id: dispatch-case-20260414-fdb38a8b-20260414T180238Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on April 17, 2026?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance API and market contract context
source_type: exchange-data-plus-market-rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-fdb38a8b/researcher-analyses/2026-04-14/dispatch-case-20260414-fdb38a8b-20260414T180238Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, resolution-source, timestamp-risk]
---

# Summary

This note captures the direct resolution-relevant exchange context for the April 17 BTC > 72,000 market.

## Key facts extracted

- Binance spot API returned BTCUSDT at approximately 74,759 on 2026-04-14 during this run.
- Binance 24h ticker returned last price about 74,753, 24h high about 76,038, 24h low about 72,054, and 24h change about +3.6%.
- Recent daily klines show BTC closing above 72,000 on multiple recent sessions, including around 72,963 on Apr 8, 73,043 on Apr 9, 74,418 on Apr 12, and about 74,766 in-progress on Apr 14 during this run.
- The Polymarket contract text says resolution is based specifically on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on Apr 17, using the final Close price.

## Evidence directly stated by source

- Binance API directly states current BTCUSDT spot price and recent OHLC ranges.
- Polymarket rule text directly states the governing settlement mechanism: Binance, BTC/USDT, 1m candle, 12:00 ET, final close, precision per source.

## What is uncertain

- Current spot price is not itself the settlement print; the market resolves on a single future 1-minute close on Apr 17 at noon ET.
- Binance website chart UI is the formal cited source in the contract text, while API outputs are best viewed as highly relevant contextual verification rather than the literal settlement screenshot.
- A fast move below 72,000 shortly before the resolution minute remains possible even if current spot is well above the line.

## Why this source may matter

This is the most direct evidence for both current distance from the strike and the exact operational resolution mechanism. It establishes that the market is currently in-the-money by a meaningful margin and that timing/venue risk matters more than general Bitcoin direction.

## Possible impact on the question

This source supports a high but not certain yes probability. With BTC already roughly 3.8% above the strike and with recent trading mostly above 72,000, the main remaining risk is a sharp risk-off move or Binance-specific settlement-minute distortion.

## Reliability notes

- Binance is the governing source of truth named by the contract, so source-of-truth relevance is very high.
- API access is machine-readable and recent, but the contract cites the Binance chart close specifically, so there is mild source-surface ambiguity even though both refer to Binance BTC/USDT pricing.
- Operational details like timezone conversion and final candle close handling remain important.