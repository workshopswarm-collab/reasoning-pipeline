---
type: source_note
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market listing / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-31d67ba1/researcher-analyses/2026-04-15/dispatch-case-20260415-31d67ba1-20260415T185542Z/personas/variant-view.md]
tags: [polymarket, contract-rules, resolution-source, market-implied-probability]
---

# Summary

Polymarket lists the April 17 BTC threshold ladder and shows the $70,000 contract trading around 97.2%, implying an extreme consensus that Binance BTC/USDT will still close above 70,000 on the noon ET 1-minute candle on April 17. The rules make the decisive object very specific: Binance BTC/USDT, 1-minute candle, 12:00 ET, final close price, with exchange-specific precision.

## Key facts extracted

- The specific contract asks whether Bitcoin will be above $70,000 on April 17.
- Market-implied probability on the page for the 70,000 threshold is about 97.2%.
- Resolution uses the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 17.
- The decisive field is the candle's final "Close" price, not intraminute high, low, midpoint, or another exchange's price.
- Price precision is determined by the source as displayed by Binance.

## Evidence directly stated by source

- The page explicitly states: "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- The page explicitly names Binance BTC/USDT as the resolution source.
- The page displays the live threshold ladder, with 70,000 trading at roughly 97%.

## What is uncertain

- Polymarket's web page is not itself the exchange source of truth for the eventual closing print.
- The page does not itself explain the operational mapping from ET-noon wording to Binance API timestamp/query behavior.
- Displayed prices can move after capture; the 97.2% figure is a snapshot.

## Why this source may matter

It defines the contract mechanics and the market's current consensus baseline. For this case the variant angle is less about macro bitcoin direction than about whether traders may be underweighting narrow settlement mechanics and exchange-specific timing/operational details.

## Possible impact on the question

This source pushes toward a high-Yes baseline but also highlights the key path for a contrarian argument: if anything breaks the simple "spot is way above 70k" story, it will likely be through exact settlement mechanics rather than broad price direction.

## Reliability notes

Reliable for contract wording and observed market price snapshot; not authoritative for the final April 17 noon candle itself.