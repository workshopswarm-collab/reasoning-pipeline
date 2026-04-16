---
type: source_note
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the price of Bitcoin be above $68,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Polymarket rules page
source_type: exchange-api-plus-market-rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: supports-yes
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-79281f9a/researcher-analyses/2026-04-15/dispatch-case-20260415-79281f9a-20260415T202526Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution-rules, timing-risk]
---

# Summary
The contract is governed by the Binance BTC/USDT 1-minute candle close for 12:00 ET on 2026-04-20, and current Binance spot context on 2026-04-15 shows BTC/USDT around 74.7k-74.9k, materially above the 68k strike.

## Key facts extracted
- Polymarket rules explicitly say the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20 has a final Close above 68,000.
- The rules explicitly name Binance BTC/USDT, not other exchanges or pairs, as the governing source of truth.
- Binance API ticker on 2026-04-15 showed BTCUSDT at 74,853.01.
- Binance 5-minute average endpoint showed 74,711.03 around 2026-04-15 20:30:46 UTC.
- Recent 1-minute klines fetched from Binance covered 20:13-20:17 UTC on 2026-04-15, with closes from 74,613.01 to 74,676.96.
- Those UTC timestamps correspond to 16:13-16:17 ET on 2026-04-15, confirming the venue is reporting in UTC while the contract resolves on an ET-labeled minute.

## Evidence directly stated by source
- Direct contract language: final 1-minute candle close at 12:00 ET on the specified date determines resolution.
- Direct exchange prices: BTC/USDT was about 6.6k-6.9k above the strike at the time checked.

## What is uncertain
- Spot price four-plus days ahead can move materially in crypto; current cushion is large but not dispositive.
- The exact Binance front-end candle display at the resolution minute could still create operational/interpretive edge risk if UI data differ transiently from API-observed candles.
- This source set does not itself explain why BTC is trading where it is; it only establishes the governing contract mechanics and current distance from strike.

## Why this source may matter
This is the primary direct evidence set because it ties the market to its settlement mechanism and gives the current state of the governing venue and pair.

## Possible impact on the question
At current levels, the market leaning heavily to Yes is directionally sensible, but the risk-manager takeaway is that the market is pricing not only direction but also high confidence that BTC will remain above 68k exactly at the noon ET resolution minute on Binance.

## Reliability notes
- High reliability for contract interpretation because Polymarket states the rules directly.
- High reliability for current spot context because Binance is the named source of truth.
- Still some operational caveat because the rules refer traders to Binance's candle display, so exact minute-close handling and ET/UTC mapping deserve explicit attention.