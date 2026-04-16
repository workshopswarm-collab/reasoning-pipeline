---
type: source_note
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-70k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and market rules
source_type: market rules / settlement source
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [base-rate finding, assumption note]
tags: [polymarket, rules, resolution, source-of-truth]
---

# Summary

The Polymarket event page clearly states the resolution mechanics and current market-implied price for the 70000 threshold outcome.

## Key facts extracted

- The relevant outcome is "70,000" for April 16, 2026.
- Market price on the event page during this pass was about 98.6 cents Yes / 1.5 cents No, consistent with the assignment current_price of 0.985.
- The contract resolves Yes if the Binance BTC/USDT one-minute candle for 12:00 in the ET timezone on the specified date has a final close price higher than 70000.
- The contract is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the number of decimals in the source.

## Evidence directly stated by source

- Governing source of truth is Binance BTC/USDT with 1m candles selected.
- Material condition is strict inequality: higher than 70000, not equal to 70000.
- Time reference is noon ET on April 16.

## What is uncertain

- The web page is not itself the settlement source; it is the contract-definition source pointing to Binance.
- The page does not explain in more detail how daylight savings or exact Binance UI labeling maps to ET, so practical interpretation still requires a timing audit.

## Why this source may matter

This source defines what counts. Because the market is date-sensitive and rule-sensitive, the contract wording matters almost as much as the underlying BTC level.

## Possible impact on the question

The rules narrow the question from a general "BTC above 70k tomorrow" intuition to one exact minute, one exchange, one pair, and one strict comparison. That reduces some false confidence while still leaving the basic directional view driven by current spot distance from the threshold.

## Reliability notes

Best available contract-definition source. High value for rule interpretation, but not independent from the market itself. It should be paired with Binance data for the evidence floor.