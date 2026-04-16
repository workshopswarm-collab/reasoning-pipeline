---
type: source_note
case_key: case-20260414-b6293fe0
dispatch_id: dispatch-case-20260414-b6293fe0-20260414T001837Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin-weekly-hit-price
entity: btc
topic: case-20260414-b6293fe0 | risk-manager
question: Will Bitcoin reach $74,000 April 13-19?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page / embedded market JSON
source_type: market rules and market state
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin, polymarket]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, resolution-source, binance, market-state]
---

# Summary

This source establishes the governing source of truth and current market state for the contract. The embedded market JSON on the Polymarket event page states that the market resolves "Yes" if any Binance BTC/USDT 1-minute candle during Apr 13-19 ET has a final **High** price greater than or equal to 74,000.

## Key facts extracted

- The assigned market `will-bitcoin-reach-74k-april-13-19` was active as of 2026-04-14 00:14Z.
- Outcome prices embedded in the page showed `Yes` around `0.9995` and `No` around `0.0005` at extraction time.
- The contract description says the market resolves immediately to "Yes" if any Binance BTC/USDT 1-minute candle during the specified ET date range has a final `High` price `>= 74,000`.
- The description explicitly says prices from other exchanges, different pairs, or spot markets do not count.
- The same event page showed sibling markets in the weekly ladder, including `Will Bitcoin reach $72,000 April 13-19?`, already marked resolved `Yes`, which is directionally consistent with the threshold ladder.

## Evidence directly stated by source

- Resolution source: Binance BTC/USDT.
- Resolution field: 1-minute candle `High` price.
- Time window: Apr 13 12:00 AM ET through Apr 19 11:59 PM ET.
- Current market-implied probability from the displayed price was effectively ~99.95%.

## What is uncertain

- The market page is not itself the canonical Binance print; it is the venue publishing rules and current prices.
- The embedded JSON proves what Polymarket says it will use, but not by itself that Binance actually printed 74,000+ during the window.
- The page also showed a proposed resolution object for the 74k threshold, which is consistent with a hit, but the key operational point is still the underlying Binance print and the contract rules.

## Why this source may matter

This is the governing source for contract interpretation. In a narrow, date-specific price-touch market, risk analysis depends first on what exactly counts as a hit and which venue is authoritative.

## Possible impact on the question

This sharply lowers source-of-truth ambiguity: the relevant question is not whether Bitcoin broadly traded above 74k somewhere, but whether Binance BTC/USDT printed a qualifying 1-minute high in the specified ET window.

## Reliability notes

High reliability for contract wording and market-implied odds because this is the venue hosting the contract. Lower reliability as standalone proof of the underlying price event, so it needs an external verification pass against Binance or an independent market-data source.