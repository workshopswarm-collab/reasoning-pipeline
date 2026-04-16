---
type: source_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: spot-market-context
entity: binanaliases: [Binance Exchange]ge]
topic: eth-spot-context-vs-2200-threshold
question: Is the 2200 threshold materially below prevailing ETH spot context one day before resolution?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot API, Coinbase ticker API, CoinGecko simple price API
source_type: exchange/API market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: []
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/variant-view.md]
tags: [binance, coinbase, coingecko, eth, price-context, verification]
---

# Summary

Independent spot references all placed ETH materially above the 2200 threshold during the verification pass, implying a substantial cushion but not eliminating one-day downside or exchange-specific resolution risk.

## Key facts extracted

- Binance spot ticker showed ETHUSDT around 2355.63.
- Recent Binance 1-minute klines clustered around 2353.88 to 2355.62 during the check.
- Coinbase ETH-USD ticker showed about 2356.06 at nearly the same time.
- CoinGecko simple price showed ETH around 2354.66.
- The market therefore sat roughly 7% above the 2200 threshold during this pass.

## Evidence directly stated by source

- Binance ticker API returned `{"symbol":"ETHUSDT","price":"2355.63000000"}`.
- Binance recent klines showed consecutive 1-minute closes above 2353.
- Coinbase ticker returned `"price":"2356.06"`.
- CoinGecko returned `{"ethereum":{"usd":2354.66,...}}`.

## What is uncertain

- These are contemporaneous checks from April 16, not the actual April 17 12:00 ET settle minute.
- Coinbase and CoinGecko are contextual validation only; they do not govern settlement.
- A large crypto move over less than 24 hours is plausible, especially around macro or crypto-specific risk events.

## Why this source may matter

It confirms the market is not pricing 95% solely on vague narrative; the spot cushion is real and visible across independent feeds. It also supports the variant-view framing that the remaining risk is mostly timestamp-specific downside or Binance-specific execution/printing risk rather than a dispute over the current level.

## Possible impact on the question

The spot cushion supports a high Yes probability. The main way to disagree with a 95.5% market price is to argue that the crowd may still underweight one-day downside tails or the narrowness of the exact noon Binance close condition.

## Reliability notes

High recency and reasonably strong independence for contextual cross-checking: Binance is the settlement-relevant source; Coinbase and CoinGecko reduce risk that a single broken feed is misleading. Independence is medium rather than high because all sources reflect the same underlying global ETH market.