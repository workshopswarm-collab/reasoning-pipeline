---
type: source_note
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: prediction-markets
entity: ethereum
topic: ethereum-above-2300-on-april-17
question: Will the Binance ETH/USDT 1-minute candle for 2026-04-17 12:00 ET close above 2300?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules page
source_type: market-rules
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/personas/variant-view.md]
tags: [polymarket, rules, settlement, binance, timing]
---

# Summary

Rule check on the market page to identify the exact contract condition, governing source of truth, and timing semantics.

## Key facts extracted

- Market resolves Yes if the Binance 1-minute candle for ETH/USDT at `12:00` in ET on the specified date has a final close price higher than 2300.
- Otherwise the market resolves No.
- Resolution source is Binance, specifically ETH/USDT with `1m` and `Candles` selected on the Binance trading interface.
- The market is about Binance ETH/USDT, not other exchanges or pairs.
- Price precision is determined by the number of decimal places in the source.

## Evidence directly stated by source

- The relevant condition is not daily close, not a time range, and not another exchange reference price.
- All material conditions must hold simultaneously: correct exchange, correct pair, correct 1-minute timeframe, correct ET noon minute, and close strictly above 2300.

## What is uncertain

- The rules do not explicitly clarify how ET wording maps to Binance's UTC-native market data, though the mapping itself is straightforward.
- The rules rely on the Binance interface currently available, which can create a small operational ambiguity if UI availability or display formatting becomes an issue.

## Why this source may matter

This is the governing resolution text. Any forecast that ignores the exact minute, exchange, or pair would be analyzing the wrong contract.

## Possible impact on the question

The contract is narrower than a generic "ETH above 2300 tomorrow" view. Variant risk lives in minute-specific timing and source mechanics: ETH can trade above 2300 for most of the day and still resolve No if the exact Binance noon-ET 1-minute close finishes at or below 2300.

## Reliability notes

- High credibility for contract interpretation because it is the market's own rule page.
- Not independent from the market price itself; it governs settlement rather than the probability estimate.
- Important operational ambiguity remains low-to-medium rather than zero because the UI page, not an explicit API spec, is named as the source of truth.