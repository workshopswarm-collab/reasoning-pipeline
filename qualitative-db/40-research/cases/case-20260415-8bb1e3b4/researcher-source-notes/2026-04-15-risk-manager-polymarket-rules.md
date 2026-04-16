---
type: source_note
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-8bb1e3b4 | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market-rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8bb1e3b4/researcher-analyses/2026-04-15/dispatch-case-20260415-8bb1e3b4-20260415T150551Z/personas/risk-manager.md]
tags: [polymarket, rules, resolution, binance, timing-risk]
---

# Summary

This source defines the actual contract mechanics. The market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 20, using the final Close price, and requires that close to be higher than $70,000.

## Key facts extracted

- Resolution is not based on daily close, intraday high, or another exchange.
- Governing source of truth is Binance BTC/USDT with 1m Candles selected.
- Relevant datapoint is the final "Close" for the 12:00 ET candle on April 20, 2026.
- Market price on review showed the $70,000 line around 87%-88% implied probability.
- Precision depends on Binance source decimals.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT 'Close' prices... with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The public market page does not itself show the future resolving candle; it only specifies how it will be checked.
- The page does not discuss operational contingencies if Binance UI/data presentation changes, though the source-of-truth intent is still clear.

## Why this source may matter

This is the governing contract source. It sharply narrows the question to one exchange, one pair, one minute, one timezone label, and one field (Close). That creates timing and microstructure risk not captured by broader BTC spot narratives.

## Possible impact on the question

The contract is easier to lose than a casual "BTC above 70k that day" phrasing suggests. A thesis based only on BTC staying generally above 70k is insufficient; it must survive a specific 12:00 ET one-minute close on Binance.

## Reliability notes

High reliability for contract interpretation because this is the primary market rules page. Lower value for underlying price prediction beyond showing crowd-implied probability.