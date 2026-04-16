---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: polymarket contract rules and live market-implied probability
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on April 20, 2026?
driver:
date_created: 2026-04-15
source_name: Polymarket market page for Bitcoin above 70000 on April 20
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/market-implied.md
tags: [polymarket, contract-rules, market-implied, btc]
---

# Summary

The Polymarket market page shows the current Yes price around 94 cents for the 70,000 threshold and states the governing rule clearly: resolution depends on the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20, 2026, specifically whether the final close is higher than 70,000.

## Key facts extracted

- The relevant threshold market is the 70,000 line for April 20.
- The displayed market-implied probability is about 93-94% Yes.
- The rule is close-based, not touch-based.
- The governing source is Binance BTC/USDT with 1m candles selected.
- The relevant candle is the 12:00 ET candle on the date in the title.
- The contract requires the final close price to be higher than 70,000, not equal to it.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance..."
- Market display shows the 70,000 contract around 93-94% Yes.

## What is uncertain

- The Polymarket page is not itself the governing source for the eventual BTC price; it only states the rule and current market pricing.
- Web extraction captures the displayed odds but not a time-series path or order-book depth.

## Why this source may matter

This is the primary source for contract interpretation and for the market-implied baseline. It determines what conditions all must hold for Yes: correct venue, correct pair, correct timestamp, correct timezone, correct candle interval, and a final close strictly above 70,000.

## Possible impact on the question

It fixes the mechanism and removes common misreads. A researcher cannot treat this like a generic spot-price question or a touch/high market. Because the displayed price is already extreme, any disagreement with the market would require stronger evidence than usual.

## Reliability notes

Strong for contract wording and visible market-implied odds. Weaker as evidence about where BTC will actually trade at resolution, since the page aggregates beliefs rather than proving future price behavior.
