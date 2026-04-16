---
type: source_note
case_key: case-20260415-6c8d8ca4
dispatch_id: dispatch-case-20260415-6c8d8ca4-20260415T084705Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on April 17 above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and market rules
source_type: market page / rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6c8d8ca4/researcher-analyses/2026-04-15/dispatch-case-20260415-6c8d8ca4-20260415T084705Z/personas/risk-manager.md]
tags: [polymarket, rules, market-implied-probability, resolution-source]
---

# Summary

This source provides the current market-implied price for the 72,000 strike and the governing contract wording for how the market resolves.

## Key facts extracted

- The 72,000 contract was trading around 81% / 82¢ at fetch time.
- The market resolves on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17.
- The deciding field is the final candle "Close" price, not intraday high, low, VWAP, or another exchange.
- Resolution is specific to Binance BTC/USDT and not other exchanges or trading pairs.
- Price precision is determined by the source display.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."

## What is uncertain

- The page is a market interface rather than the authoritative data source itself; it states the rules but does not settle the outcome until the relevant Binance candle exists.
- The interface showed both 81% and 82¢ style values; small display rounding may exist.
- The exact Binance UI behavior at settlement time is not independently verified from the web page alone.

## Why this source may matter

It locks the contract mechanics and prevents thesis drift into broader BTC price narratives that are not actually resolution-relevant.

## Possible impact on the question

This source makes the key risk-manager issue explicit: all bullish macro/contextual evidence only matters insofar as it raises the probability that Binance BTC/USDT specifically prints a final 12:00 ET 1-minute close above 72,000 on April 17.

## Reliability notes

Useful and necessary for contract interpretation, but not sufficient alone for the price outlook because it is the market venue describing its own rules rather than the final settlement print itself.