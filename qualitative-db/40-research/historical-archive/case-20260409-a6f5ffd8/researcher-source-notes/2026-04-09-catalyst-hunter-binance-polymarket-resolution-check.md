---
type: source_note
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-9
question: Will the price of Bitcoin be above $70,000 on April 9?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance BTCUSDT 1m API and Polymarket rules page
source_type: primary-plus-contextual
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, resolution, timestamp, source-note]
---

# Summary

This source note checks the direct settlement mechanics for the market. The key point is that Polymarket explicitly settles from the Binance BTC/USDT 1-minute candle labeled 12:00 ET, and 12:00 ET on 2026-04-09 converts to 16:00:00 UTC because New York is on EDT (UTC-4).

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in ET on the specified date, using the final Close price.
- 2026-04-09 12:00:00 ET converts to 2026-04-09 16:00:00 UTC.
- Binance spot klines are timestamped in UTC milliseconds.
- A Binance 1-minute kline opened at 16:00:00 UTC closes at 16:00:59.999 UTC and its close price is the settlement-relevant number for this market.
- A direct Binance API check near the relevant window showed BTCUSDT trading around 71,032.89, above the 70,000 threshold.
- The sampled recent klines around the check were all above 70,000, indicating the threshold had a buffer of roughly $1,000 at the time of verification.

## Evidence directly stated by source

- Polymarket rules: resolve to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET has a final close above the listed strike.
- Binance API output: recent BTCUSDT 1-minute candles had closes of 71,051.14, 71,093.01, 71,045.86, 71,032.88, and ticker price 71,032.89 at time of check.

## What is uncertain

- The direct API sample here was a near-resolution context check, not a saved capture of the exact 16:00:00 UTC settlement candle for this contract.
- Short-horizon crypto volatility could still move BTC below 70,000 before the settlement minute if the market has not yet resolved at the time of trading.
- Binance website UI wording uses human-readable local display conventions, but API timestamps are UTC, so timestamp alignment remains the main operational issue to verify.

## Why this source may matter

This is the governing source-of-truth surface for the contract. For a date-and-minute-specific market like this, the main edge is not macro interpretation but exact timestamp mapping and confirming what candle actually counts.

## Possible impact on the question

The source strongly supports a high Yes probability because BTC was trading comfortably above the threshold and because the main non-price risk is an operational/timestamp misread rather than economic ambiguity.

## Reliability notes

- Binance is the authoritative price source named in the contract, so source-of-truth ambiguity is low once the ET-to-UTC mapping is verified.
- Polymarket rules are a strong contextual source for contract interpretation but not the underlying settlement data itself.
- Evidence independence is medium: the rules and settlement source are distinct surfaces, but both are part of the same contract ecosystem.