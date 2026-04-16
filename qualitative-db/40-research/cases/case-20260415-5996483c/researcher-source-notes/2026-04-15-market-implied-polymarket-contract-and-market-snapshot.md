---
type: source_note
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market_contract
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: supportive
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-5996483c/researcher-analyses/2026-04-15/dispatch-case-20260415-5996483c-20260415T193222Z/personas/market-implied.md
tags: [polymarket, contract, source-of-truth, market-implied]
---

# Summary

This source establishes both the live market pricing context and the governing contract mechanics. It is the primary source for the market-implied baseline and for what must happen for this contract to resolve Yes.

## Key facts extracted

- The assigned leg is the `70,000` threshold for `Apr 20, 2026`.
- The fetched market snapshot showed the `70,000` outcome trading around `92%`, with buy prices displayed around `93¢` for Yes and `9¢` for No at fetch time.
- The market rules state the contract resolves Yes only if the `Binance BTC/USDT` `1-minute` candle for `12:00 ET` on Apr 20 has a final `Close` price `higher than` 70,000.
- The resolution source is explicitly Binance with `BTC/USDT`, `1m`, and `Candles` selected.
- The rule is close-based, not touch-based, and exchange/pair-specific, not a broad BTC spot average.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The fetched page is a rendered market page snapshot, not a direct API export, so displayed prices should be treated as point-in-time contextual evidence rather than a full order-book record.
- The page does not itself show the underlying Binance candle path or a historical series for the Apr 20 noon ET candle because that event has not happened yet.

## Why this source may matter

It defines the exact settlement mechanism and confirms that the market is pricing a very high probability for Yes despite the contract being narrow: a single exchange, single pair, single 1-minute close, and specific timezone.

## Possible impact on the question

This source supports a strong default prior toward Yes because traders are pricing the leg above 0.89. But it also creates a mechanism-specific caution: the market is not asking whether BTC trades above 70k at any time before Apr 20, only whether the Binance BTC/USDT noon ET 1-minute close on Apr 20 is above 70k.

## Reliability notes

Primary source for contract wording and current market-implied probability. Strong for mechanism and baseline; weaker for independent verification of whether the market price is efficient.