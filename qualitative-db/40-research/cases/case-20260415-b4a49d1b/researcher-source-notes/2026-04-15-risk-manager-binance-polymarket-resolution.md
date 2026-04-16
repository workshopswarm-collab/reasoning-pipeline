---
type: source_note
case_key: case-20260415-b4a49d1b
dispatch_id: dispatch-case-20260415-b4a49d1b-20260415T000939Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules plus Binance market-data docs / API
source_type: primary-plus-contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
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
downstream_uses: [risk-manager-finding, risk-manager-assumption, risk-manager-evidence-map]
tags: [polymarket, binance, resolution-criteria, timing-risk]
---

# Summary

This source cluster establishes the governing contract mechanics and the practical verification surface for the market. The critical points are that settlement uses Binance BTC/USDT, the relevant datum is the 1-minute candle close for 12:00 ET on April 20, and Binance kline data are indexed by candle open time. That makes time-window interpretation a material risk item, even if the directional BTC thesis remains bullish.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on the specified date has a final Close strictly higher than 70,000.
- Polymarket states the source of truth is Binance BTC/USDT, not other exchanges or pairs.
- Binance docs state kline/candlestick bars are uniquely identified by their open time.
- Binance docs show the kline response includes the close price and supports 1m intervals.
- A direct Binance API pull returned BTCUSDT around 74,567 at fetch time, comfortably above 70,000 as current context, though not settlement evidence.
- A direct Binance kline sample pull confirmed that the 16:00 UTC 1-minute bar maps to 12:00 ET during EDT, which is the relevant settlement minute on April 20, 2026.

## Evidence directly stated by source

- From Polymarket rules: Yes requires the Binance 1-minute candle for BTC/USDT at 12:00 ET on April 20 to have a final close price higher than 70,000.
- From Polymarket rules: price precision is determined by Binance source decimals.
- From Binance docs: klines are uniquely identified by their open time.
- From Binance docs/API schema: the close price is an explicit field in the kline response.

## What is uncertain

- Polymarket references the Binance web chart surface rather than explicitly the API endpoint, so there is minor operational ambiguity if chart presentation and API display were ever inconsistent.
- The contract says “higher than” 70,000, so an exact 70,000.00 close would resolve No; that edge case is low probability but matters.
- The market is date-specific and minute-specific, so path risk between now and Apr 20 matters more than broad monthly bullishness.

## Why this source may matter

This source set is sufficient to define the governing settlement mechanism and the main operational failure mode: a bullish BTC view can still lose if price dips below 70,000 exactly at the relevant minute or if traders mentally substitute a different exchange/time interpretation.

## Possible impact on the question

These sources support a generally bullish baseline because spot BTC is currently well above 70,000, but they also justify a discount from an overly confident market price because the contract is narrow, minute-specific, exchange-specific, and strict on the threshold.

## Reliability notes

- Polymarket is authoritative for contract wording.
- Binance is authoritative for the referenced price surface and kline mechanics.
- Independence is medium rather than high because the contract explicitly depends on Binance.
- Source-of-truth ambiguity is low to medium: the governing source is clear, but minute labeling and exact threshold strictness still deserve explicit mention.