---
type: source_note
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 be above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / market snapshot
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, market-implied-probability, binance]
---

# Summary

This source provides the governing market wording, resolution mechanics, and the current market-implied probability for the 70,000 threshold outcome.

## Key facts extracted

- The market resolves based on the **Binance BTC/USDT 1-minute candle for 12:00 ET (noon) on April 20, 2026**.
- The relevant value is the candle's **final Close** price, not intraminute high, low, or other exchange prices.
- The market states explicitly that it uses **Binance**, not other exchanges or pairs.
- The visible market snapshot on 2026-04-15 showed the **70,000** outcome around **92%-93%**, consistent with assignment `current_price: 0.895` but a bit higher in the fetched live page snapshot.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- The page snapshot showed the 70,000 line trading around 92%-93%.

## What is uncertain

- The fetched HTML is a snapshot, not a guaranteed final API value for the current market price.
- Polymarket page text does not by itself prove what the Binance close will be on April 20.
- The page snapshot does not show a complete historical path for the 70,000 contract.

## Why this source may matter

This is the primary source for the contract mechanics and the cleanest available statement of what counts for resolution. It is also the main source for the market-implied baseline.

## Possible impact on the question

It sharply narrows the relevant risk surface: what matters is not whether bitcoin trades above 70,000 somewhere, nor whether another exchange prints above it, but whether the specific Binance BTC/USDT **12:00 ET one-minute close** on April 20 finishes above 70,000.

## Reliability notes

- High relevance for market rules; medium-high credibility for contract interpretation.
- Less suitable for independent contextual validation because it is the market venue itself.
- Requires independent exchange/context checks to avoid circular reasoning.