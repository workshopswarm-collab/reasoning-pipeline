---
type: source_note
case_key: case-20260415-1e5e80f9
dispatch_id: dispatch-case-20260415T080017Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market rules page
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [variant-view.md, variant-view.sidecar.json]
tags: [polymarket, contract, resolution, source-of-truth]
---

# Summary

The Polymarket rules specify a narrow, timing-sensitive contract: Yes resolves only if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-16 has a final close strictly higher than 72,000.

## Key facts extracted

- Contract resolves from Binance, specifically BTC/USDT on the Binance chart.
- Resolution requires the `1m` candle and `Candles` display.
- The relevant candle is `12:00` in ET timezone on the specified date.
- Condition is `higher than` 72,000, not equal to 72,000.
- Price precision follows the source display.
- On the fetched market page, the 72,000 line showed approximately 83% Yes / 18% No, consistent with assignment `current_price: 0.825`.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance..."

## What is uncertain

- The public page does not itself provide the future 2026-04-16 12:00 ET close.
- The rules page does not explain edge handling for website/API discrepancies beyond naming the Binance chart surface.

## Why this source may matter

- It is the governing source for contract mechanics and resolves the main timing/source ambiguity.
- This is a narrow-resolution market, so exact wording matters materially.

## Possible impact on the question

- Makes the key variant risk obvious: the market is not about whether BTC broadly stays strong, but whether one specific minute-close on one exchange remains above 72,000 at noon ET.
- This can justify a lower probability than a casual directional BTC view would suggest.

## Reliability notes

- High credibility for contract interpretation because it is the venue’s own rules page.
- Not evidence about the eventual answer; it is evidence about what must happen for Yes to resolve.