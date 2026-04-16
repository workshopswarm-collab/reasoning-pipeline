---
type: source_note
case_key: case-20260415-9c95ce3a
dispatch_id: dispatch-case-20260415-9c95ce3a-20260415T173129Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 PM ET 1-minute candle on 2026-04-17 close above 72000?
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
agent: base-rate
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-9c95ce3a/researcher-analyses/2026-04-15/dispatch-case-20260415-9c95ce3a-20260415T173129Z/personas/base-rate.md]
tags: [binance, polymarket, resolution-source, price-level, timing]
---

# Summary
This note captures the governing resolution mechanics and current price context for the Apr. 17 BTC > 72k market.

## Key facts extracted
- Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 PM ET on Apr. 17, using the final candle close.
- The contract is exchange-specific: Binance BTC/USDT, not other exchanges or pairs.
- Current Polymarket price for the 72,000 line was approximately 82-83% Yes at fetch time.
- Binance spot BTC/USDT fetched around 74.1k on Apr. 15.
- Recent Binance daily data show BTC moved above 72k on intraday highs in 9 of the last 11 trading days, and closed above 72k on 5 of the last 11 daily candles in the Apr. 5-15 sample.

## Evidence directly stated by source
- Polymarket rules explicitly say resolution is based on the Binance 1-minute BTC/USDT candle at 12:00 ET on the specified date, with close price determining outcome.
- Binance ticker/API directly reports current BTCUSDT spot price and recent klines.

## What is uncertain
- The exact Apr. 17 12:00 ET candle is still in the future.
- The market page is a good source for rules and current odds, but final settlement still depends on Binance’s displayed/source close at the relevant minute.
- Daily or hourly bars are contextual only; they do not directly settle the contract.

## Why this source may matter
This is the main source-of-truth pair for a date-specific crypto threshold market: Polymarket defines the rule and Binance provides the actual resolution datapoint.

## Possible impact on the question
Because current spot is already materially above 72k and recent realized range has spent substantial time above the threshold, the base rate for being above 72k two days later at one specified minute is favorable but not close to certain. The single-minute noon ET condition still leaves room for a sizable downside swing or intraday reversal.

## Reliability notes
- Binance API is high-quality for current and historical exchange-specific price context, though API outputs are contextual unless they exactly match the settlement candle queried at settlement time.
- Polymarket market page is authoritative for contract wording but not for the final settled price itself.
- Independence is moderate: the two sources cover different roles (rules vs price source), which is good, but both remain tightly linked to the same market structure.