---
type: source_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-669935fa | market-implied
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Polymarket market description for will-bitcoin-reach-76k-april-13-19
source_type: market rules / primary resolution source description
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/market-implied.md]
tags: [polymarket, binance, rules, resolution-source, btc]
---

# Summary

The Polymarket contract text says this market resolves Yes if any Binance BTC/USDT 1-minute candle during April 13-19 ET has a final High at or above $76,000, and resolves No otherwise. It explicitly excludes other exchanges and other pairs.

## Key facts extracted

- Market question: `Will Bitcoin reach $76,000 April 13-19?`
- Contract description states the market resolves Yes if any Binance 1-minute BTC/USDT candle from 12:00 AM ET on Apr 13 through 11:59 PM ET on Apr 19 has a final `High` >= 76,000.
- Contract description states the resolution source is Binance BTC/USDT high prices with 1-minute candles.
- Contract description says prices from other exchanges, other trading pairs, or other spot markets do not count.
- Live market data embedded on the page showed outcome prices of `['1','0']`, lastTradePrice `0.999`, bestBid `0.999`, bestAsk `1` for the $76k contract at fetch time.

## Evidence directly stated by source

- `This market will immediately resolve to "Yes" if any Binance 1-minute candle for BTC/USDT during the date range specified in the title ... has a final "High" price equal to or greater than the price specified in the title.`
- `The resolution source for this market is Binance ... with the chart settings on "1m" candles selected on the top bar.`
- `Prices from other exchanges, different trading pairs, or spot markets will not be considered`.

## What is uncertain

- The web page snapshot is not itself the final settlement notice; it is a live market page.
- The embedded market price near 100% indicates the market believes the condition has effectively been met or is all but certain, but price alone is not proof.
- The page extract did not expose the exact 1-minute candle that first crossed $76,000.

## Why this source may matter

This is the governing contract language and therefore the key source-of-truth surface for what counts. It sharply narrows the evidence standard to Binance BTC/USDT 1-minute highs within the stated ET window.

## Possible impact on the question

If Binance printed any qualifying 1-minute high at or above $76,000 during the window, the contract should resolve Yes regardless of other exchange prices. That makes exchange-specific verification more important than broad BTC spot commentary.

## Reliability notes

High reliability for contract interpretation because this is the market's own description. Moderate limitation: a live page snapshot is not identical to the eventual settlement record, so a separate verification pass against Binance price data is still appropriate.