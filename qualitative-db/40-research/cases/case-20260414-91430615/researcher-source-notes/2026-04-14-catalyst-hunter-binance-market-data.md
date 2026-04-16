---
type: source_note
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-91430615 | catalyst-hunter
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 70000?
date_created: 2026-04-14
source_name: Binance BTCUSDT market data API
source_type: exchange market data / primary pricing source
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
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-91430615/researcher-analyses/2026-04-14/dispatch-case-20260414-91430615-20260414T235247Z/personas/catalyst-hunter.md]
tags: [binance, market-data, resolution-source, crypto, btc]
---

# Summary

Binance is the governing resolution source for this market, so current BTC/USDT spot and recent Binance candle history are the most decision-relevant primary inputs. As of fetch time on 2026-04-14, Binance spot showed BTCUSDT at 74065.09, meaning BTC sat roughly 5.8% above the 70000 threshold with five calendar days remaining before the April 19 noon ET resolution print.

## Key facts extracted

- Binance ticker price fetch returned BTCUSDT = 74065.09000000 on 2026-04-14.
- Recent Binance daily candles show BTC/USDT closing:
  - Apr 5: 71924.22
  - Apr 6: 71069.93
  - Apr 7: 71787.97
  - Apr 8: 72962.70
  - Apr 9: 73043.16
  - Apr 10: 70740.98
  - Apr 11: 74417.99
  - Apr 12: 74141.70
- The recent daily range includes several closes above 70000 and no close below 68853.66 in the 10-candle sample returned.
- The latest sampled 1-minute candles around fetch time were all around 74046-74141, confirming the threshold is not marginal at present.

## Evidence directly stated by source

- Spot price: 74065.09.
- The most recent daily candles show BTC trading consistently above 70000 for multiple sessions into April 14.
- Recent 1-minute candles show normal intraminute fluctuation but still around 74100.

## What is uncertain

- This source does not itself tell us what the exact 12:00 ET candle on April 19 will be.
- Daily candles are UTC-based and therefore are contextual, not the actual resolution window.
- Binance API availability / market microstructure at resolution time remains an operational consideration even if Polymarket points to the Binance trading page as source of truth.

## Why this source may matter

This is the closest thing to a primary source for both current state and likely settlement mechanics. Because the contract resolves on a Binance 1-minute candle, Binance price regime and Binance-specific execution/reliability matter more than broad BTC/USD commentary from other venues.

## Possible impact on the question

This source pushes toward a high but not near-certain Yes probability: BTC is materially above 70000 right now, and recent Binance history shows sustained trading above the threshold. However, a 5-6% move in five days is still plausible in bitcoin, so the source supports Yes more than market certainty.

## Reliability notes

- High relevance because Binance is named as the resolution source.
- Strong recency because all fetches are current.
- Not fully sufficient alone because the market is date-specific and future-facing rather than already settled.
- Binance API data and Binance webpage rules should be checked together for contract interpretation confidence.