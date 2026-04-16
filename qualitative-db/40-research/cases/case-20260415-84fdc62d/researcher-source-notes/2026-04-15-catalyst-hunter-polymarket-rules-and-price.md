---
type: source_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market-rules-page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [catalyst-hunter.md, catalyst-hunter.sidecar.json]
tags: [polymarket, market-rules, resolution-source, btc]
---

# Summary
The Polymarket market page provides the live market-implied probability and the operative contract wording. For the $70,000 line on April 20, the page showed roughly 86% Yes on 2026-04-15 and specified that settlement depends on the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 20, using the final Close price.

## Key facts extracted
- The relevant threshold market is `70,000` for `Apr 20, 2026`.
- The market-implied probability observed on the page was about `86%` Yes.
- Resolution is not based on any exchange average or end-of-day close; it is based specifically on Binance BTC/USDT.
- The relevant timestamp is the `12:00` candle in Eastern Time on the specified date.
- The deciding field is the final `Close` for that 1-minute candle.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain
- The market page itself does not explain how Binance UI timezone selection maps operationally to the ET-labeled candle beyond the wording shown.
- The page provides only a snapshot of probabilities, which can move materially before resolution.

## Why this source may matter
This is the governing source for contract interpretation. It narrows the question from general BTC level to a specific exchange, pair, candle, timezone, and field.

## Possible impact on the question
Because the contract is a noon-ET one-minute-close test, intraday path and timing matter more than a generic view that BTC will be above $70k "sometime that day." This reduces ambiguity but increases sensitivity to short-term volatility and exchange-specific prints.

## Reliability notes
Useful as the authoritative contract surface for market wording, but not independently authoritative on the eventual price outcome. The rule text is direct, but price and timeline judgments need separate verification from Binance and contextual market sources.
