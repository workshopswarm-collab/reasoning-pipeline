---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-2cb747e6 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API and Polymarket market page
source_type: primary-plus-market-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
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
downstream_uses: [risk-manager-finding]
tags: [binance, polymarket, resolution-check, timing]
---

# Summary

This source note captures the governing resolution mechanics and a live spot-price verification for the April 16 BTC > 72,000 market.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final Close above 72,000.
- The relevant settlement timestamp is 2026-04-16 12:00 ET, which converts to 2026-04-16 16:00 UTC.
- Binance spot via API during this run was approximately 74,187 to 74,204 BTCUSDT.
- Binance recent 1-minute data showed BTC trading in a tight band around ~74.0k-74.3k in the last hour, while the last 24 hours ranged roughly 73,514 low to 74,786.72 high.

## Evidence directly stated by source

- Polymarket directly states the governing source of truth is Binance BTC/USDT with 1m candles and that the decisive field is the final candle Close for 12:00 ET.
- Binance directly states current spot price and recent candle closes through its public API endpoints.

## What is uncertain

- This source set does not itself determine where BTC will trade at 2026-04-16 16:00 UTC.
- The Polymarket page is market context rather than an official exchange rulebook, though it is the direct market contract surface traders rely on.
- Intraday crypto volatility means current spot being above 72,000 does not guarantee the settlement-minute close remains above 72,000.

## Why this source may matter

It establishes both the exact contract mechanics and the current distance from the threshold. That is the critical foundation for risk analysis in a date-sensitive, rule-sensitive market.

## Possible impact on the question

The market is currently in-the-money by roughly $2.2k, so a Yes resolution is favored. The main residual risk is path risk over the next ~27.5 hours: a sufficient selloff, exchange-specific divergence, or a sharp move exactly into the noon ET settlement minute could still flip the result.

## Reliability notes

- Binance API is the strongest direct source for price and candle mechanics relevant to this contract.
- Polymarket market text is the strongest direct source for how this specific prediction market will resolve.
- Independence is moderate rather than high because both sources refer to the same underlying exchange for settlement, but that is appropriate here because the contract explicitly depends on Binance.