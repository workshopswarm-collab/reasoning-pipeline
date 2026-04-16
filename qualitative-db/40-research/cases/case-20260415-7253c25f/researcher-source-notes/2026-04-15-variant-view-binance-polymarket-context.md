---
type: source_note
case_key: case-20260415-7253c25f
dispatch_id: dispatch-case-20260415-7253c25f-20260415T220737Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-21 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API and Polymarket rules page
source_type: primary+market-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7253c25f/researcher-analyses/2026-04-15/dispatch-case-20260415-7253c25f-20260415T220737Z/personas/variant-view.md]
tags: [binance, polymarket, resolution-source, btc]
---

# Summary

This note captures the governing settlement mechanics and direct market context for the April 21 BTC > 72k contract.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 21, 2026.
- The market resolves Yes only if that candle's final Close is higher than 72,000; otherwise No.
- The rules explicitly exclude other exchanges and other trading pairs.
- Binance direct API spot data on 2026-04-15 showed BTCUSDT around 74,983.51.
- Binance 1-day klines for the prior 10 sessions showed BTC closing above 72,000 on several recent days, but with daily closes as low as 68,853.66 and 70,740.98 within the same window.

## Evidence directly stated by source

From the Polymarket rules page:
- resolution source is Binance BTC/USDT
- timeframe is the 12:00 ET 1-minute candle on the named date
- threshold test is strictly whether final Close is higher than 72,000
- price precision follows Binance source precision

From Binance API data:
- current BTCUSDT spot price at check time was 74,983.51
- recent daily closes over the last 10 days included substantial variation, roughly 68.9k to 75.0k

## What is uncertain

- The direct spot/ticker price on 2026-04-15 does not itself settle the market; the relevant print is a single 1-minute close six days later.
- Daily klines are contextual only; they do not reveal the exact probability distribution for the April 21 noon ET 1-minute close.
- The Binance web candle interface was named as the resolution surface, while the API was used here as a direct contextual verification of current pricing and recent realized volatility.

## Why this source may matter

The rules page is the governing interpretation source. The Binance API data is direct exchange data from the same venue family and shows that current price is already comfortably above 72k, while recent realized moves are still large enough that a drop back below 72k by the settlement minute remains plausible.

## Possible impact on the question

These sources support a pro-Yes baseline because BTC is already above the strike, but they also support a variant caution against treating an 80% market price as trivial: the contract is path-independent and hinges on one specific minute print at noon ET on April 21, so short-horizon volatility and any exchange-specific dislocation still matter.

## Reliability notes

- Polymarket rules page is highly relevant and effectively authoritative for contract mechanics.
- Binance API is direct exchange data and high credibility for market context, though not the exact stated settlement surface.
- Independence is only moderate because both sources are tightly linked to the same contract/exchange setup rather than fully independent macro analysis.
