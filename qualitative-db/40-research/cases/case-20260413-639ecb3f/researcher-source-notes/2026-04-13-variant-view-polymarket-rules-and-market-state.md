---
type: source_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: protocols
entity: ethereum
topic: ethereum weekly hit-price market structure
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-13
source_name: Polymarket event page and embedded market metadata
source_type: market page / primary contract source
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [variant-view.md]
tags: [polymarket, rules, source-of-truth, market-implied-probability]
---

# Summary

The Polymarket event page is the governing contract/source-of-truth surface for this case and also exposes current market state for the full weekly ETH hit-price ladder. For the specific target market, the page showed "Will Ethereum reach $2,400 April 13-19?" priced around 0.785 Yes at the time of review.

## Key facts extracted

- The relevant contract asks: "Will Ethereum reach $2,400 April 13-19?"
- Resolution is immediate Yes if any Binance 1-minute ETH/USDT candle during Apr 13 12:00 AM ET through Apr 19 11:59 PM ET has final High >= 2400.
- The contract explicitly says only Binance ETH/USDT price data counts; other exchanges/pairs/spot references do not count.
- Embedded market metadata showed the weekly ladder roughly as:
  - $2,300: 0.9995 Yes
  - $2,400: 0.785 Yes
  - $2,500: 0.43 Yes
  - $2,600: 0.203 Yes
  - $2,700: 0.0855 Yes
- This means the market is pricing $2,400 as more likely than not, but still treating it as a meaningful additional move versus the near-certain $2,300 threshold.

## Evidence directly stated by source

- Resolution text from page source: the market resolves Yes if any Binance 1-minute ETH/USDT candle in the stated time window has a final High at or above the threshold.
- Resolution source named directly: Binance ETH/USDT with 1m candles.
- Market state from embedded JSON showed the $2,400 market at about 0.785 Yes and adjacent rungs at materially lower/higher probabilities.

## What is uncertain

- The page is a live market surface, so prices can move after capture.
- The public page presents live odds but does not itself provide a historical path of how traders arrived there.
- Binance chart access itself was not independently scraped here; the note relies on Polymarket’s embedded rules text for the governing source.

## Why this source may matter

This is the primary contract source for both resolution mechanics and market-implied baseline. It clarifies that the question is about a touched intraperiod high on Binance, not a weekly close or multi-exchange average. That interpretation materially lowers the difficulty of hitting $2,400 versus a close-based framing.

## Possible impact on the question

Because the contract uses any 1-minute high over a full week, modest overshoots count. That makes the threshold easier than a sustained trade-above or weekly-close condition and supports a relatively high Yes probability.

## Reliability notes

High relevance and high authority for contract interpretation. Independence is limited for price expectations because this is the market itself, not an external contextual source.