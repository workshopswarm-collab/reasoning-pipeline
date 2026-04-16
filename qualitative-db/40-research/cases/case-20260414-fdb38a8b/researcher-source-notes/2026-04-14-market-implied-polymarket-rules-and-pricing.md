---
type: source_note
case_key: case-20260414-fdb38a8b
dispatch_id: dispatch-case-20260414-fdb38a8b-20260414T180238Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-fdb38a8b | market-implied
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market rules / prediction market
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, market-rules, contract-interpretation, market-implied]
---

# Summary

Polymarket shows the 72,000 line trading around 81¢ Yes / 22¢ No on the market page, consistent with the assignment’s `current_price: 0.815`. The rules specify that resolution depends on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, using the final close price, with price precision determined by Binance.

## Key facts extracted

- The market-implied probability for “above 72,000” is about 81.5% from the assignment and about 81% on-page.
- Related ladder prices on the same page show roughly:
  - above 70,000: ~94%
  - above 72,000: ~81%
  - above 74,000: ~57%
  - above 76,000: ~31%
- Rules state resolution is based on the Binance BTC/USDT 1-minute candle close at 12:00 ET on the specified date.
- The market is specifically about Binance BTC/USDT, not other exchanges or pairs.

## Evidence directly stated by source

- The crowd market already prices 72k as a fairly likely but not near-certain outcome.
- The market ladder implies a distribution centered somewhere in the low-to-mid 74k area for the target timestamp.
- Contract wording makes exact source, pair, and timing operationally important.

## What is uncertain

- The web-fetched page is a live snapshot and may lag or differ slightly from the assignment snapshot.
- On-page prices are not themselves settlement evidence; they are market beliefs.

## Why this source may matter

This is the direct source for both the market-implied baseline and the contract interpretation. It clarifies what the market is assuming and what exact observation decides the payout.

## Possible impact on the question

This source strongly supports using the live 81.5% probability as the baseline prior. It also narrows the research task to whether that probability looks efficient given Binance price context and the remaining time to the exact settlement minute.

## Reliability notes

High reliability for market odds and contract wording. Not independent evidence of the future outcome, but indispensable for baseline and rules interpretation.