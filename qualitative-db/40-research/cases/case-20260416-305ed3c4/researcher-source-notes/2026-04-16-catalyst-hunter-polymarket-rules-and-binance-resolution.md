---
type: source_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: prediction-markets
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: Will the price of Ethereum be above $2,200 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules for ethereum-above-on-april-17
source_type: market-rules-page
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [catalyst-hunter.md]
tags: [source-note, polymarket, resolution-rules, binance]
---

# Summary

This source defines the contract mechanics and source of truth. It says the market resolves "Yes" if the Binance ETH/USDT 1-minute candle for 12:00 ET on Apr. 17 has a final close strictly higher than 2200; otherwise "No". It also specifies Binance as the governing resolution source and notes that price precision is whatever Binance displays.

## Key facts extracted

- Resolution depends on the Binance ETH/USDT 1-minute candle, not a broader ETH reference price.
- The relevant candle is the 12:00 ET candle on Apr. 17, 2026.
- The contract condition is strictly greater than 2200, not greater-than-or-equal.
- The listed resolution surface is Binance ETH/USDT with 1m candles selected.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for ETH/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the ETH/USDT 'Close' prices currently available at https://www.binance.com/en/trade/ETH_USDT with '1m' and 'Candles' selected on the top bar."
- "Price precision is determined by the number of decimal places in the source."

## What is uncertain

- The public market page is not itself the final Binance candle display, so a second-source verification of Binance timing/mechanics is still useful.
- The page does not itself explain Binance API timestamp conventions; that needs contextual verification.

## Why this source may matter

It is the governing contract/rules surface, so it determines what counts, what does not count, and the relevant deadline/timezone.

## Possible impact on the question

This source makes the case mainly a near-term price-path and timing question: ETH only needs to remain above 2200 on Binance at the exact noon ET candle close on Apr. 17.

## Reliability notes

High reliability for contract wording and source-of-truth identification because it is the market’s own rules page. Lower value for independent price discovery because it is not the underlying exchange record itself.