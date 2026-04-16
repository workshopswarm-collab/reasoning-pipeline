---
type: source_note
case_key: case-20260415-572502e1
dispatch_id: dispatch-case-20260415-572502e1-20260415T124520Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: btc
topic: case-20260415-572502e1 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for bitcoin-above-on-april-16
source_type: market-rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: risk-manager
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, market-rules, binance, btc]
---

# Summary
This source defines the contract mechanics and the governing source of truth. For this market, the key risk is not broad Bitcoin direction alone, but whether Binance BTC/USDT prints a 1-minute candle close above 72000 at exactly 12:00 ET on April 16.

## Key facts extracted
- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on April 16 has a final Close price higher than 72000.
- The resolution source is Binance, specifically the BTC/USDT chart with 1m candles selected.
- The contract is exchange-specific and pair-specific; other exchanges or BTC/USD feeds do not govern resolution.
- Price precision is determined by the decimals shown by the source.
- The visible market price for the 72000 line was about 90% at fetch time, consistent with assignment current_price 0.895.

## Evidence directly stated by source
The market page explicitly states the resolution mechanism, time reference, exchange, pair, and metric (final 1-minute candle close).

## What is uncertain
- The public market page does not itself show the eventual Binance settlement candle; that must be checked at resolution.
- The page does not explain any Binance UI/data latency edge case beyond naming Binance as source.
- The wording says 12:00 in ET timezone and uses the 1-minute candle close, so one must map the exact noon ET minute correctly and not confuse intraminute prints with the final close.

## Why this source may matter
This is the governing source-of-truth surface. It determines what all other contextual evidence means and defines the main operational failure mode: BTC can trade above 72000 generally yet still resolve No if the relevant Binance minute closes at or below 72000.

## Possible impact on the question
This source makes the market more fragile than a generic "is BTC above 72k tomorrow" framing. Resolution depends on all of the following holding: correct date, correct noon ET timing, correct exchange/pair, and final candle close > 72000.

## Reliability notes
High reliability for contract interpretation because it is the market's own rules page. Lower usefulness for directional forecasting because it is not a market-data source for the future resolving print.
