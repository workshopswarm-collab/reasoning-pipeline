---
type: source_note
case_key: case-20260415-572502e1
dispatch_id: dispatch-case-20260415-572502e1-20260415T124520Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Polymarket contract page
source_type: primary_market_and_resolution_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=24 ; https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-572502e1/researcher-analyses/2026-04-15/dispatch-case-20260415-572502e1-20260415T124520Z/personas/variant-view.md]
tags: [binance, polymarket, resolution, btc]
---

# Summary

This source note combines the governing contract wording from the Polymarket market page with direct Binance market data used to anchor the live price context and verify how the resolution source should be interpreted.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle for `12:00` in ET timezone on April 16, using the final `Close` price.
- The threshold is strict: the final close must be **higher than** 72,000; equal to 72,000 would resolve No.
- The market is specifically about Binance BTC/USDT, not a broader BTC/USD composite or another exchange.
- Live Binance ticker at research time was about 74,353 USDT.
- Binance 24-hour hourly candles showed BTC/USDT holding mostly in the upper-73k to mid-75k range during the prior day, with no touch near 72k in the retrieved window.

## Evidence directly stated by source

From the Polymarket rules page:
- resolution source is Binance BTC/USDT with 1m candles
- relevant candle is `12:00` ET on the named date
- settlement uses the candle `Close`
- price precision is whatever Binance shows

From Binance API data:
- spot BTCUSDT at research time: 74353.04
- recent 1h candles over the prior 24h were roughly between 73,514 and 76,038 on the retrieved window

## What is uncertain

- The exact final 12:00 ET minute close for April 16 obviously does not yet exist.
- Polymarket’s web page is authoritative for the contract text, but final practical observability may depend on Binance UI/API consistency at settlement time.
- A direct future-query check of the exact 2026-04-16 12:00 ET candle is not yet possible; the attempted API query for that future minute returned an empty array, which is expected and confirms no premature data exists.

## Why this source may matter

This is the core source set for the case because the contract is narrow and date-specific. The main risk is not broad Bitcoin direction alone, but whether Binance’s specific noon-ET 1-minute close stays above the threshold.

## Possible impact on the question

At research time, the direct source context supports a Yes lean because spot is materially above 72k and recent trading range is also above 72k. The main variant-view implication is that the market’s ~89.5% probability may still be somewhat overconfident because a narrow one-minute, exchange-specific, future-time close is more fragile than a broad “BTC stays above 72k generally” interpretation.

## Reliability notes

- Binance API is the best direct operational proxy for the stated source of truth and is high-value evidence for live price context.
- Polymarket contract text is the governing interpretation source for what counts.
- These two sources are not fully independent, but together they define both the contract mechanics and the relevant live state.