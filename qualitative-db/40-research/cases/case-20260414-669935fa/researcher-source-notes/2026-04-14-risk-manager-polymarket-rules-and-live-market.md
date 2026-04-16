---
type: source_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: tokens
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Polymarket market page and embedded rules text for will-bitcoin-reach-76k-april-13-19
source_type: primary_market_rules
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, binance, resolution]
---

# Summary

This note captures the market-implied probability and the governing source-of-truth mechanics from the Polymarket event page itself. For this contract, the key risk question is not broad BTC direction alone but whether a qualifying Binance BTC/USDT 1-minute candle high prints during the exact ET date window.

## Key facts extracted

- Assignment current_price is `0.9995`, implying a market-implied probability of about 99.95% for the $76,000 threshold contract.
- The Polymarket page embeds the rules text stating the market resolves Yes if **any Binance 1-minute candle for BTC/USDT** during the title date range has a final **High** greater than or equal to the threshold price in the title.
- The embedded rules text also states the date range is interpreted as **from 12:00 AM ET on Apr 13, 2026 through 11:59 PM ET on Apr 19, 2026**.
- The embedded rules text identifies Binance BTC/USDT 1-minute chart highs as the resolution source.

## Evidence directly stated by source

- The event page is the governing contract surface for the market.
- Resolution is based on Binance BTC/USDT 1-minute candle highs, not daily closes, not CoinGecko averages, and not prices from another exchange.
- The contract is a touch-style threshold market: one qualifying 1-minute high is enough for Yes.

## What is uncertain

- The readable page fetch itself did not expose a clean machine-readable market state for the specific sub-contract beyond the assignment metadata.
- The page text alone does not prove whether a qualifying $76,000 Binance print has already occurred.
- There remains small residual risk of page-versus-feed mismatch, chart display discrepancy, or other implementation ambiguity until resolution infrastructure reflects the qualifying print.

## Why this source may matter

This is the governing source of truth for how the contract settles. In a narrow weekly threshold-touch market, rules precision matters more than generic market commentary.

## Possible impact on the question

If a Binance BTC/USDT 1-minute high at or above $76,000 occurs within the ET date window, the market should resolve Yes regardless of later BTC weakness. If it does not occur, the contract resolves No even if other exchanges print above $76,000.

## Reliability notes

High reliability for contract interpretation because this is the market’s own rules surface. Lower value for independent factual verification of whether the threshold has already printed, since the page itself is not a live audited trade log.