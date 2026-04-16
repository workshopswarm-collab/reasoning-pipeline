---
type: source_note
case_key: case-20260414-b6293fe0
dispatch_id: dispatch-case-20260414-b6293fe0-20260414T001837Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: will-bitcoin-reach-74000-april-13-19
question: Will Bitcoin reach $74,000 April 13-19?
date_created: 2026-04-14
source_name: Binance daily OHLC + Coinbase spot + Polymarket event page
source_type: exchange_data_and_market_rules
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-b6293fe0/researcher-analyses/2026-04-14/dispatch-case-20260414-b6293fe0-20260414T001837Z/personas/variant-view.md]
tags: [btc, price-verification, polymarket, resolution-context]
---

# Summary

This note verifies that BTC already traded above $74,000 during the April 13-19 window and that the Polymarket market is a highest-price-hit style ladder market rather than a weekly close market.

## Key facts extracted

- Binance daily candles for the relevant recent period show BTC/USDT highs of 73,434 and then 73,790 before moving to a later daily candle that opened at 72,962.71 and traded to a high above 74,000.
- Coinbase spot API at time of check returned BTC-USD spot of 74,370.945.
- The Polymarket event page for "What price will Bitcoin hit April 13-19?" presents multiple outcome levels such as "↑ 74,000" and describes the market as resolving based on which price level Bitcoin hits during the period.

## Evidence directly stated by source

- Binance API response included daily OHLC rows with a visible progression into the low-74k area during the target week.
- Coinbase API returned current BTC-USD spot above 74k.
- Polymarket page text states the market has multiple possible outcomes and references the rules section for how outcomes are determined.

## What is uncertain

- The exact Polymarket rule text was not cleanly extracted from page HTML, so this note relies on the event-page framing plus the contract title and outcome ladder rather than a fully parsed rules block.
- Binance uses BTCUSDT, while Coinbase uses BTC-USD; that is good contextual verification but not guaranteed to be the exact governing settlement source.
- The exact timestamp of first crossing 74k inside the weekly interval was not separately reconstructed from intraday candles because the core question is only whether 74k was reached at any point.

## Why this source may matter

This is the core factual verification surface for the case. It checks both the market framing and the underlying price action.

## Possible impact on the question

If BTC is already trading above 74k on major exchange feeds during the listed week, then the market should be overwhelmingly likely to resolve in favor of the 74k-or-higher threshold having been reached, unless the governing source-of-truth uses a materially different venue/method or the contract has an unusual exclusion.

## Reliability notes

- Binance and Coinbase are strong contextual market-data sources, but they are not automatically the contract's settlement authority.
- Polymarket is the governing source for contract framing and rules, but the fetched page text did not expose the full rules block cleanly.
- Evidence independence is medium: exchange price feeds are partly correlated but still provide useful cross-checking that the threshold was plainly reached on major venues.