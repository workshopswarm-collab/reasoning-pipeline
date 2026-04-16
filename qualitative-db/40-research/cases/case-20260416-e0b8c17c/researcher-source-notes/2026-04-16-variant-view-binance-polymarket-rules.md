---
type: source_note
case_key: case-20260416-e0b8c17c
dispatch_id: dispatch-case-20260416-e0b8c17c-20260416T050131Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules page and Binance BTCUSDT API surfaces
source_type: primary_and_direct
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-analyses/2026-04-16/dispatch-case-20260416-e0b8c17c-20260416T050131Z/personas/variant-view.md]
tags: [polymarket, binance, settlement, btc]
---

# Summary

This note captures the direct settlement mechanics and a live verification pass for the BTC/USDT market used by the contract. The key takeaway is that the contract is mechanically simple but operationally specific: settlement depends on the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-20, using that candle's final close price, not any broader daily close or another exchange.

## Key facts extracted

- Polymarket rules say the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on the named date has a final close strictly higher than the strike.
- The named resolution surface is Binance BTC/USDT with 1m candles selected.
- Price precision is determined by the number of decimals on the source.
- A direct Binance API check for recent 1-minute klines returned valid BTCUSDT rows and confirms the venue exposes minute-candle close data in a machine-readable way.
- A timezone conversion pass on recent klines found the 2026-04-15 12:00:00-04:00 candle and its close at 73792.01000000, confirming that mapping UTC-stamped Binance klines into America/New_York yields a distinct noon ET minute.
- A live Binance ticker check during research showed BTCUSDT around 75009.98, already materially above the 72000 threshold four days ahead of resolution.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From direct Binance API checks performed in-run:
- `api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10` returned recent 1-minute candle rows.
- `api/v3/ticker/price?symbol=BTCUSDT` returned `75009.98000000` during the run.
- `api/v3/exchangeInfo?symbol=BTCUSDT` returned symbol metadata showing BTCUSDT active/trading.

## What is uncertain

- The contract references the Binance trading UI, while this note verified the economically equivalent exchange API surface rather than the web UI candle widget itself.
- The market will settle on the final close for a future minute, so current spot level only indicates distance from threshold, not resolution certainty.
- Intraday BTC volatility over four days can still produce a move back below 72000 by the specific noon ET minute.

## Why this source may matter

This is the governing source-of-truth bundle for the case. It determines what counts, what does not count, and how the time window maps to the outcome.

## Possible impact on the question

The direct-source read reduces ambiguity around settlement mechanics and supports a high baseline Yes probability because the current Binance BTCUSDT price is already meaningfully above the threshold. The remaining risk is price-path risk into the specific April 20 noon ET minute, not contract-interpretation uncertainty.

## Reliability notes

- Polymarket rules page is the authoritative contract description for this market.
- Binance API is a direct exchange-operated source and a strong verification surface for the same underlying BTCUSDT market.
- Evidence independence is moderate rather than high because both surfaces ultimately point to the same settlement mechanism, but that is appropriate here because the main task is contract verification, not broad causal inference.
