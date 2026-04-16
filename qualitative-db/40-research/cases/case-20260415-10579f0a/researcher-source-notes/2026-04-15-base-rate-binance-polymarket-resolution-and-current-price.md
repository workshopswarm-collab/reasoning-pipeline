---
type: source_note
case_key: case-20260415-10579f0a
dispatch_id: dispatch-case-20260415-10579f0a-20260415T184424Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT 1m market data API plus Polymarket market rules page
source_type: primary_and_resolution_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, resolution, btc, direct-source]
---

# Summary

This note captures the direct source-of-truth surface for the contract and the current Binance BTC/USDT price context relevant to a short-horizon base-rate view.

## Key facts extracted

- Polymarket rules state the market resolves to Yes if the Binance BTC/USDT 1 minute candle for 12:00 ET on 2026-04-17 has a final Close price higher than 70,000.
- The rules explicitly say the source is Binance BTC/USDT, not other exchanges or trading pairs.
- Binance public API on 2026-04-15 returned BTCUSDT spot price around 74,340.
- Binance recent 1m klines also showed closes around 74.2k-74.34k during the check.
- A 60-day daily-kline pull showed BTC daily closes above 70,000 for most recent days, including approximately 74,418 on 2026-04-13, 74,131.55 on 2026-04-14, and 74,339.99 on 2026-04-15 at query time.

## Evidence directly stated by source

- Polymarket direct rule text: Yes resolves only if the Binance 1 minute candle for BTC/USDT at 12:00 ET on the specified date has a final Close price higher than the strike.
- Binance ticker/klines directly state current exchange price and recent 1m candle closes for BTCUSDT.

## What is uncertain

- The Binance trade page itself did not extract cleanly via fetch, so the API was used as a direct Binance surface rather than the browser page.
- Current price does not guarantee the noon ET close on 2026-04-17.
- Short-horizon crypto volatility could still push BTC below 70,000 by the settlement minute.

## Why this source may matter

It directly pins down the contract mechanics and the governing exchange/source, while also showing the current spot level is already materially above the 70,000 threshold.

## Possible impact on the question

If BTC remains in its recent range, a noon ET close above 70,000 is more likely than not and likely favored heavily. The main residual risk is a sufficiently sharp selloff before the specific settlement minute.

## Reliability notes

- Binance is the named settlement source, so it is authoritative for this contract.
- Polymarket market page is authoritative for the contract wording but not for the eventual price itself.
- Evidence independence is not high because both the rule check and price check revolve around the same settlement stack, but this is acceptable for a narrow exchange-settled contract.