---
type: source_note
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-structure
entity: ethereum
topic: ethereum-above-2300-on-april-17
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2300?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules page plus Binance ETHUSDT API context
source_type: primary_and_contextual
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/variant-view.md]
tags: [polymarket, binance, resolution, price-context, eth]
---

# Summary

This note combines the governing contract language from Polymarket with current Binance ETHUSDT price context relevant to the April 17 noon ET resolution.

## Key facts extracted

- Polymarket says the market resolves **Yes** if the Binance ETH/USDT **1-minute candle for 12:00 ET** on April 17 has a final **Close** above 2300.
- The market is specifically about **Binance ETH/USDT**, not other exchanges or other pairs.
- The assignment current market price was 0.725, implying roughly **72.5%** for Yes at run start.
- Binance spot ticker during this run showed ETHUSDT around **2333.19**.
- Binance recent daily candles show ETH has recently traded both above and below 2300, with notable range: one recent day closed 2322.44 after printing as high as 2415.50, and the latest daily context available in the API set showed a close near 2333.99.
- Binance exchange info shows ETHUSDT is an active trading pair and the price filter tick size is **0.01**, so threshold precision should be interpreted to cents.

## Evidence directly stated by source

- Polymarket rules explicitly define the governing source of truth and the exact candle/timeframe.
- Binance ticker and kline endpoints directly state current and recent exchange prices for ETHUSDT.

## What is uncertain

- The exact final noon-ET one-minute close on April 17 is still unknown at analysis time.
- The Polymarket web page displayed a 64-65% quote for the 2300 line in fetched page text, while assignment metadata provided 0.725; this likely reflects timing drift between snapshots rather than a contract ambiguity.
- Binance exchangeInfo uses UTC server time, so analysts still need to map noon ET on April 17 to **16:00 UTC** correctly.

## Why this source may matter

This is the source set that actually governs the contract mechanics and gives the most decision-relevant current price context. It matters more than broad crypto commentary because the contract is a narrow timestamp-and-exchange question.

## Possible impact on the question

The combination supports a view that Yes is favored because spot is already above 2300, but it also highlights the main neglected risk: the contract needs **all** of the following to hold simultaneously — Binance ETHUSDT, the correct minute, the final close, and a print strictly above 2300. A modest intraday dip at exactly noon ET would still resolve No even if ETH trades above 2300 for most of the surrounding period.

## Reliability notes

- Polymarket rules are the best primary source for contract interpretation, though the public page can show stale visible prices relative to assignment metadata.
- Binance API endpoints are direct contextual price sources and more reliable than third-party price aggregators for this contract.
- The evidence is reasonably strong but not yet settlement-complete because the decisive candle does not exist yet.