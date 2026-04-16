---
type: source_note
case_key: case-20260415-75a50190
dispatch_id: dispatch-case-20260415-75a50190-20260415T205116Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for "Bitcoin above ___ on April 21?"
source_type: market rule page
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-75a50190/researcher-analyses/2026-04-15/dispatch-case-20260415-75a50190-20260415T205116Z/personas/variant-view.md]
tags: [polymarket, contract-rules, resolution-source, binance, btc]
---

# Summary

This source is the governing market-rule surface for the case. It matters because the question is not a generic BTC spot-price forecast; it is specifically about the final close of the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 21, 2026.

## Key facts extracted

- The market resolves Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on April 21, 2026 has a final Close price higher than 72,000.
- The market resolves No otherwise.
- The resolution source is Binance, specifically the BTC/USDT chart with 1m and Candles selected.
- The relevant pair is BTC/USDT on Binance, not other exchanges or other BTC pairs.
- Precision is determined by the number of decimals shown by the source.
- The displayed market price for the 72,000 line was about 80-81%, consistent with the assignment snapshot current_price 0.78.

## Evidence directly stated by source

Directly stated on the market page:
- resolution depends on the Binance BTC/USDT 1-minute candle close
- the timestamp is 12:00 in ET timezone
- the threshold comparison is strictly higher than the named price
- source-of-truth exchange/pair are specified narrowly

## What is uncertain

- The web capture does not independently verify how Binance labels that minute internally beyond the rule text itself.
- The market page does not itself provide the future April 21 candle, so it cannot settle the substantive price outcome today.
- Intraday path dependence between now and resolution remains unknown.

## Why this source may matter

This is the authoritative contract-mechanics source. Any forecast that ignores the exact exchange, pair, minute bucket, timezone conversion, or strict-greater-than condition risks answering the wrong question.

## Possible impact on the question

The rule text slightly weakens naive confidence in a simple "BTC probably stays above 72k" framing because the contract is sensitive to one exact exchange, one exact pair, and one exact minute close at noon ET. That introduces timestamp and microstructure risk even if the broader BTC trend remains constructive.

## Reliability notes

High reliability for contract interpretation because this is the market’s own governing rule page. Lower relevance for the actual future outcome because it does not contain predictive evidence about the April 21 price path; it only specifies what counts and what does not count.