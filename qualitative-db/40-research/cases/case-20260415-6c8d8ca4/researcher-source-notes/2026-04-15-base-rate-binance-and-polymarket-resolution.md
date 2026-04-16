---
type: source_note
case_key: case-20260415-6c8d8ca4
dispatch_id: dispatch-case-20260415-6c8d8ca4-20260415T084705Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Polymarket contract page
source_type: exchange-api-and-market-rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=14 ; https://polymarket.com/event/bitcoin-above-on-april-17
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
downstream_uses: []
tags: [binance, polymarket, resolution, btc]
---

# Summary

This note captures the two most decision-relevant source surfaces for this case: the contract-resolution wording on Polymarket and current/recent BTCUSDT price levels from Binance, the named settlement source.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET on 2026-04-17** has a final **Close** strictly higher than 72,000.
- The contract is specifically about **Binance BTC/USDT**, not other exchanges or BTC/USD pairs.
- Current Polymarket market price for the 72,000 line is about **0.81** (81%).
- Binance ticker price fetched on 2026-04-15 showed **74,041.95** for BTCUSDT.
- Binance daily klines for the last 14 days show BTC closing below 72,000 on Apr 2-5 and above 72,000 on Apr 7-15 except Apr 12, with recent closes: Apr 13 **74,417.99**, Apr 14 **74,131.55**, Apr 15 intraday ticker **74,041.95**.
- Recent daily range shows BTC has been capable of multi-thousand-dollar swings within a day, including Apr 12 low close near **70,740.98** after prior stronger levels.

## Evidence directly stated by source

- Direct resolution mechanics: exact timestamp, exact exchange/pair, exact candle field, and strict inequality threshold.
- Direct current/recent price context from Binance, which is more relevant than other exchanges because Binance is also the governing source.

## What is uncertain

- Daily candles do not tell us the exact noon ET 1-minute close on Apr 17.
- The Binance public pages/APIs used here do not alone guarantee there will be no exchange-specific outage, settlement-data revision, or sudden two-day drawdown.
- Current price being ~2.8% above threshold does not imply stability through the resolution minute.

## Why this source may matter

These are the core sources needed to evaluate both contract mechanics and base-rate price distance. The case is not just “Will BTC trade above 72k around then?” but “Will Binance BTCUSDT 12:00 ET 1-minute close on Apr 17 settle above 72k?”

## Possible impact on the question

The source set supports a moderately bullish outside-view read because BTC is already above 72k with only about two days remaining, but it also flags nontrivial path risk because BTC has recently shown the ability to move several percent over one to two sessions.

## Reliability notes

- Binance is the named settlement source, so it is the highest-value primary source for this contract.
- Polymarket’s contract page is authoritative for the resolution wording but not for the actual final settlement price itself.
- Evidence independence is only moderate because both sources concern the same market setup rather than independent causal data; a broader contextual source is still useful for checking whether current BTC levels reflect a broader recognized market state.