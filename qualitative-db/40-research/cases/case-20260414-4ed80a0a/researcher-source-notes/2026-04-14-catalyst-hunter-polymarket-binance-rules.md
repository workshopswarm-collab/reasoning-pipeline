---
type: source_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-14
source_name: Polymarket market page / embedded rules text
source_type: market rules page
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-14
credibility: medium-high
recency: current
stance: neutral
certainty: medium-high
importance: high
novelty: high
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, binance, resolution]
---

# Summary

The Polymarket event page embeds the operative resolution language for this market. The key point is that resolution depends only on Binance ETH/USDT 1-minute candle highs during the stated ET date window, not on other exchanges or generalized spot references.

## Key facts extracted

- The embedded rules text says the market resolves Yes if any Binance 1-minute ETH/USDT candle during the stated window has a final High at or above the threshold in the title.
- The rules text specifies the relevant window as from 12:00 AM ET on the first date to 11:59 PM ET on the last date.
- The rules text says the resolution source is Binance ETH/USDT High prices with 1m candles.
- The page source for the `↑ 2,400` outcome showed `outcomePrices:["1","0"]`, `closed:true`, `umaResolutionStatus:"resolved"`, and `closedTime:"2026-04-14 17:20:02+00"` when checked.
- The same page source indicates the contract is configured to resolve immediately once the threshold is hit, which matters for timing analysis.

## Evidence directly stated by source

Direct from embedded rules text recovered from page source:

- "This market will immediately resolve to \"Yes\" if any Binance 1-minute candle for ETH/USDT during the date range specified in the title (from 12:00 AM ET on the first date to 11:59 PM ET on the last) has a final \"High\" price equal to or greater than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the ETH/USDT \"High\" prices..."
- "Prices from other exchanges, different trading pairs, or spot markets will not be considered for the resolution of this market."

## What is uncertain

- I did not obtain a separately rendered rules panel from the live page UI; I extracted the embedded rules text from page HTML.
- I did not independently inspect Binance historical 1-minute candles for the exact threshold-crossing minute because the market page source already showed the relevant outcome as resolved and priced at 1.

## Why this source may matter

This is the governing source-of-truth surface for the market. It defines both what counts and what does not count. For a narrow, date-specific price-touch market, that wording is more important than general ETH spot commentary.

## Possible impact on the question

This source sharply reduces interpretation ambiguity. Once Binance ETH/USDT has printed a qualifying 1-minute high during the window, the market should resolve Yes regardless of what happens later in the week.

## Reliability notes

The source is primary for contract interpretation because it is the market host’s own rules surface, but it is not fully ideal because the readable fetch output omitted the detailed rules and I had to recover them from raw page source. Reliability for interpretation is still high enough for this case because the extracted language is specific and internally consistent with the resolved state shown on-page.