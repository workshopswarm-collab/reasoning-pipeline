---
type: source_note
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-21 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and Binance BTCUSDT spot API
source_type: primary-market-rules-plus-resolution-source
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-bebdf03e/researcher-analyses/2026-04-15/dispatch-case-20260415-bebdf03e-20260415T221944Z/personas/variant-view.md]
tags: [polymarket, binance, resolution, btc]
---

# Summary

This source pair establishes the governing resolution mechanics and the relevant live reference level. The market resolves from the Binance BTC/USDT **1-minute candle for 12:00 ET on April 21, 2026**, using the final **Close** value, with price precision taken from Binance. A live Binance spot API check on 2026-04-15 showed BTCUSDT around **75,006**, materially above the 72,000 strike.

## Key facts extracted

- Polymarket rules specify resolution from the Binance BTC/USDT **1m candle** at **12:00 ET (noon)** on the specified date.
- The contract is about the **Close** of that one-minute candle, not intraminute high/low and not another exchange.
- Price precision is determined by the decimals in the Binance source.
- Live Binance REST API check on 2026-04-15 returned BTCUSDT around **75,006.44**.
- A live Binance 1m kline sample confirmed the API exposes the candle close explicitly as a separate field.

## Evidence directly stated by source

From the Polymarket event page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From Binance API checks performed during the run:
- `ticker/price?symbol=BTCUSDT` returned `75006.44000000`.
- `klines?symbol=BTCUSDT&interval=1m&limit=1` returned a one-minute candle whose close field was `75034.97000000`.

## What is uncertain

- The source note does not by itself establish where BTC will trade on April 21 noon ET.
- Polymarket wording references the Binance trading UI for resolution, while this run verified mechanics via the public Binance API; in normal conditions those should align, but the UI/API implementation relationship is still an operational detail worth noting.

## Why this source may matter

This is the direct source-of-truth pair for the contract: it specifies exactly **what must be true** for a Yes resolution and confirms the market is currently priced well above the strike. It also surfaces the narrow-rule sensitivity: exchange-specific price, one-minute close, ET timestamp, and close-vs-high distinction.

## Possible impact on the question

Because spot BTC on Binance is currently several thousand dollars above 72,000, the obvious baseline is that Yes should be favored. The variant angle is not that the rules are ambiguous, but that a narrow one-minute exchange-specific close still leaves room for downside variance over the next six days; traders may be slightly overconfident if they mentally substitute "BTC is above 72k now" for the stricter contract condition.

## Reliability notes

- Polymarket event page is the direct contract/rules source, so reliability for resolution mechanics is high.
- Binance public API is a highly relevant direct market data source for the referenced venue, though the exact canonical settlement path points to the Binance interface rather than the API endpoint.
- Independence between these two sources is low for market level because both ultimately center on Binance price data, but they serve different roles: rules authority and venue data verification.