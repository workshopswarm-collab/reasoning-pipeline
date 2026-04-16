---
type: source_note
case_key: case-20260414-4d440738
dispatch_id: dispatch-case-20260414-4d440738-20260414T195302Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the price of Bitcoin be above $68,000 on April 20?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance BTCUSDT API plus Polymarket rules page
source_type: primary_market_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=14 ; https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4d440738/researcher-analyses/2026-04-14/dispatch-case-20260414-4d440738-20260414T195302Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution-source, timing-risk]
---

# Summary

This source note captures the contract mechanics and the most relevant direct market data from the stated resolution venue. The contract resolves on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on 2026-04-20, using the final close price of that candle, not an average and not another exchange.

## Key facts extracted

- Polymarket rules explicitly say resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20.
- The relevant number is the candle's final **Close** price, and "Yes" requires that close to be **higher than 68,000**.
- Binance exchange metadata shows BTCUSDT is an active trading pair with a price tick size of 0.01, so the precision threshold is effectively cent-level in quote terms.
- Binance spot data on 2026-04-14 showed BTCUSDT around 74.2k, materially above the 68k strike.
- Binance daily closes from 2026-04-01 through 2026-04-14 were above 68k on 11 of 14 days; the last close was about 74.25k.
- Recent daily closes indicate BTC has spent the last week mostly in the 70k-74k range after briefly trading in the high 60ks earlier in April.

## Evidence directly stated by source

- Polymarket rules page states the exact settlement mechanic and source of truth.
- Binance API directly reports the current BTCUSDT price and recent historical candles on the same venue the contract references.

## What is uncertain

- The source does not itself answer where BTC will be at exactly 12:00 ET on 2026-04-20.
- The rules page does not clarify edge cases like a Binance outage at resolution time beyond saying the source is the price currently available on Binance.
- The daily candles are contextual; actual resolution is on a single 1-minute candle, so intraday path risk remains.

## Why this source may matter

This is the governing source-of-truth pair for the contract: Polymarket defines what counts, and Binance provides the venue-specific price history and current level. Together they anchor both contract interpretation and the base-rate distance from the strike.

## Possible impact on the question

The direct source evidence supports a high probability of "Yes" because BTCUSDT is currently ~9% above the 68k threshold with several days remaining. But it also highlights the main risk-manager objection: the market settles on one exact one-minute close, so a broad bearish move, event shock, or venue-specific dislocation at that exact timestamp could still flip the outcome.

## Reliability notes

- Polymarket is authoritative for contract wording; Binance is authoritative for the referenced price series.
- Independence between these two sources is low in the usual journalistic sense, but that is acceptable here because one defines the contract and the other is the designated resolution venue.
- This source pair is highly reliable for resolution mechanics but only moderately informative for future price direction.
