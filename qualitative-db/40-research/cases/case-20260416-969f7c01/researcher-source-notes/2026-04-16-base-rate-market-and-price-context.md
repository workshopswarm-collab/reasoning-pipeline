---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-price-threshold-markets
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-17 close above 2200?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules page plus cross-check ETH spot context
source_type: mixed-primary-and-context
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, eth, price-threshold]
---

# Summary

This note captures the governing market mechanics and a simple cross-check of current ETH price context. The direct question is not whether ETH trades above $2,200 somewhere, but whether Binance's ETH/USDT 1-minute candle labeled 12:00 in ET on April 17, 2026 ends with a final close above 2200.

## Key facts extracted

- Polymarket's rules specify the market resolves Yes if the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 has a final close strictly higher than 2200.
- The specified source of truth is Binance ETH/USDT, not another exchange and not an ETH/USD pair.
- Price precision is whatever Binance displays in the source.
- Polymarket page showed the 2200 strike trading around 95% at research time.
- Search/web fetch cross-checks from Binance result snippets and CoinMarketCap context indicated ETH/USDT spot was roughly in the mid-2300s during the research window, comfortably above 2200.
- CoinMarketCap context also showed recent daily closes around 2244.53 on Apr 10, 2284.77 on Apr 11, 2192.47 on Apr 12, 2370.30 on Apr 13, 2322.58 on Apr 14, 2359.15 on Apr 15, and about 2352 on Apr 16.

## Evidence directly stated by source

Direct from Polymarket rules page:
- Yes requires the Binance 1-minute ETH/USDT candle at 12:00 ET on the named date to have a final close higher than the strike.
- Binance is the resolution source.
- This is specifically ETH/USDT on Binance, not other venues.

Direct from CoinMarketCap converter/history page:
- ETH/USDT was approximately 2354 at fetch time on Apr 16, 2026.
- Daily ETH/USDT history over the prior week was mostly above 2200, with one listed daily close slightly below 2200 on Apr 12.

## What is uncertain

- The fetch stack could not reliably extract the live Binance page, so Binance price context here is from search snippet plus the contract's own rules, not a clean scraped Binance chart.
- Daily closes from a contextual source are not the same as the exact Binance 12:00 ET 1-minute close required for settlement.
- Crypto can move materially within less than 24 hours, so the current cushion above 2200 does not eliminate path risk.

## Why this source may matter

The rules page is the governing source for how the market resolves. The contextual price checks matter because they show the strike is below contemporaneous spot, making Yes the base-rate-favored outcome absent a sharp downside move before noon ET on Apr 17.

## Possible impact on the question

These sources push toward a high Yes probability because the relevant asset is currently trading well above the strike and the contract uses a single minute close rather than a broader average. That said, the single-minute structure creates some fragility if ETH sells off hard into the resolution window.

## Reliability notes

- Polymarket rules page is the highest-value source here because it governs the contract mechanics.
- CoinMarketCap is contextual rather than authoritative for settlement, but adequate for independent spot-level cross-checking.
- Evidence independence is moderate: the contract source and price-context source are distinct, but both reflect the same underlying market.
- The main remaining ambiguity is live Binance extraction and the exact ET-to-candle mapping, not the threshold itself.
