---
type: source_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: crypto
subdomain: market-rules
entity: ethereum
topic: case-20260409-21554cf3 | catalyst-hunter
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-09 close above 2100?
driver: operational-risk
date_created: 2026-04-09T03:40:00-04:00
source_name: Polymarket market page rules for ethereum-above-2100-on-april-9
source_type: market-rule-page
source_url: https://polymarket.com/event/ethereum-above-on-april-9
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, binance, timezone]
---

# Summary

The Polymarket market page states that this market resolves Yes if the Binance ETH/USDT 1-minute candle for 12:00 in ET on 2026-04-09 has a final close above 2100, and No otherwise. It also specifies that the source is Binance ETH/USDT with 1m candles selected, and that price precision is determined by the source.

## Key facts extracted

- Resolution depends on the Binance ETH/USDT 1-minute candle for 12:00 ET.
- The deciding field is the candle's final close price.
- The threshold is strictly higher than 2100.
- The market is about Binance ETH/USDT only, not other exchanges or pairs.
- Price precision is whatever Binance shows in the source.

## Evidence directly stated by source

- The rule text directly specifies exchange, pair, timeframe, timezone framing, and close-price criterion.

## What is uncertain

- The rule page references the Binance trading UI rather than naming the API endpoint used internally for any later settlement check.
- The page does not separately explain whether the relevant candle is indexed by open time or close time; that interpretation comes from Binance's own kline docs.

## Why this source may matter

This is the governing market contract surface. Even strong exchange data is not enough without confirming what exact candle and timezone the market means.

## Possible impact on the question

The contract mechanics are simple but narrow: the right question is not "will ETH trade above 2100 at some point" but whether the Binance ETH/USDT 12:00 ET one-minute candle closes above 2100.

## Reliability notes

- High relevance because it is the contract page itself.
- Not an independent pricing source; it is a rules source.
- Main residual ambiguity is low-to-medium and centers on chart-vs-API surface choice, not on the threshold or timing itself.
