---
type: source_note
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: Binance noon-close threshold mechanics and current BTC/USDT distance above $70k
question: Will the Binance BTC/USDT 12:00 PM ET one-minute candle close on 2026-04-20 be above $70,000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance BTCUSDT API surfaces
source_type: primary_and_governing_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [bitcoin, btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/catalyst-hunter.md
tags: [source-note, polymarket, binance, btc, resolution-mechanics]
---

# Summary

This source note captures the governing contract mechanics from the Polymarket market page and the directly checked Binance BTCUSDT price surfaces relevant to the April 20 noon ET close-above-$70,000 question.

## Key facts extracted

- Polymarket rules state the market resolves **Yes** if the **Binance BTC/USDT 1 minute candle for 12:00 PM ET on April 20** has a final **Close** price **higher than $70,000**.
- The rules explicitly say this is about **Binance BTC/USDT**, not other exchanges or other BTC pairs.
- The rules explicitly frame the market as a **close** market, not a touch/high market.
- Current market snapshot on the Polymarket page showed the **$70,000 line trading around 88%-89% Yes**, consistent with assignment `current_price: 0.87`.
- Direct Binance API spot check on 2026-04-15 showed BTCUSDT around **$73,989**.
- Direct Binance API daily candles for the prior week showed BTCUSDT daily highs mostly in the **$73k-$76k** range, including **$76,038** on 2026-04-14.

## Evidence directly stated by source

From the Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."

From direct Binance API checks:
- current BTCUSDT spot/ticker price was about **73989.52** on 2026-04-15.
- recent daily candle data showed BTC remained materially above the 70k threshold over the last several sessions.

## What is uncertain

- The contract resolves on a **specific minute close at 12:00 PM ET on 2026-04-20**, not the current price and not a daily close.
- Binance UI and API presentation details can differ from third-party contextual sites, so the governing proof still must be taken from the Binance resolution surface at the relevant time.
- Short-horizon crypto volatility could still move BTC below 70k by the decisive minute.

## Why this source may matter

This source is the governing mechanics check and the main direct evidence that the contract is currently deep in-the-money on price level, while still subject to a date-and-time-specific close condition.

## Possible impact on the question

The combination of explicit close-style mechanics and BTC currently trading nearly $4,000 above the threshold supports a high Yes probability, but not certainty. The main remaining question is whether any catalyst or volatility shock forces BTC below 70k exactly at the settlement minute.

## Reliability notes

- Polymarket rules page is the authoritative contract-language source for what counts.
- Binance is the explicitly named governing resolution source.
- Direct API checks are highly relevant context for present state, but they do **not** settle the contract early because the decisive minute has not occurred yet.
