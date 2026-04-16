---
type: source_note
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-8a0619b6 | base-rate
question: Will the price of Bitcoin be above $70,000 on April 18?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-18
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/base-rate.md]
tags: [polymarket, contract-rules, resolution-source, binance]
---

# Summary

This source provides the market-implied baseline and the governing contract mechanics. It says the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 18, using the final close price, with price precision determined by Binance's displayed decimal precision.

## Key facts extracted

- The specific threshold market in question is the $70,000 line for April 18.
- The visible market-implied probability on the page was about 90% for "above 70,000."
- Resolution is not based on daily close, intraday high, or another exchange.
- Resolution depends on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone, specifically the final close.
- The page explicitly says this is about Binance BTC/USDT, not other exchanges or pairs.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- The visible market state showed the 70,000 contract trading around 90% Yes.

## What is uncertain

- The fetched page is a rendered market page, not itself the final settlement dataset.
- The exact displayed probability can move intraday before resolution.
- The page does not itself explain whether Binance API timezone handling exactly mirrors the chart UI, so Binance docs are still needed as a verification pass.

## Why this source may matter

This is the governing source for contract wording and the direct source of the market-implied baseline. For a date-specific, rule-sensitive market, it is mandatory because small wording details materially change what counts.

## Possible impact on the question

The contract is narrower than a generic "BTC above 70k on April 18" interpretation. A strict noon-ET 1-minute close on Binance makes the event less likely than a looser daily-high or end-of-day formulation, which matters for judging whether 90% is too high.

## Reliability notes

Polymarket is authoritative for the market's own wording, but not for the underlying Binance data itself. Reliability for contract interpretation is high; reliability for the final outcome requires confirmation from Binance data or Binance documentation.