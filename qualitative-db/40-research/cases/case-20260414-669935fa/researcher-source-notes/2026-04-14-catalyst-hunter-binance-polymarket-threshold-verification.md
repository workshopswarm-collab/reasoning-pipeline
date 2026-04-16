---
type: source_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-669935fa | catalyst-hunter
question: Will Bitcoin reach $76,000 April 13-19?
driver: liquidity
date_created: 2026-04-14
source_name: Polymarket rules plus Binance BTCUSDT verification
source_type: contract rules plus exchange market data
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [liquidity, macro, sentiment]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, catalyst, verification, btc]
---

# Summary

The key timing catalyst for this market appears to have already occurred. Polymarket's own rule framing points to Binance BTC/USDT 1-minute highs during Apr 13-19 ET as the governing trigger, and Binance market data already shows a print above $76,000 on Apr 14.

## Key facts extracted

- The governing contract language, as preserved in the market-implied source note, says this resolves Yes if any Binance BTC/USDT 1-minute candle during Apr 13-19 ET has a final High at or above $76,000.
- Binance 24-hour ticker data on 2026-04-14 reported `highPrice = 76038.00`.
- A separate Binance hourly-kline verification found the 2026-04-14 14:00 UTC candle had a high of `76038.00`.
- CoinGecko's sampled 7-day/30-day aggregated series remained below $76,000 in sampled observations, implying the move may have been brief or exchange-specific rather than a broad persistent spot regime change.

## Evidence directly stated by source

- Polymarket rule note: any Binance 1-minute BTC/USDT high >= 76,000 in the stated window resolves Yes.
- Binance ticker and kline data: highPrice / hourly high = 76038.00.

## What is uncertain

- This note does not archive the exact first qualifying 1-minute candle, only higher-level Binance data that implies one existed.
- The Polymarket public fetch path is not a perfect contract transcript, though it is still the best available governing-source surface in this run.
- A brief wick above threshold does not imply bullish follow-through for BTC broadly; it only matters for this contract's narrow resolution condition.

## Why this source may matter

This is the most decision-relevant catalyst check for the contract: whether the threshold-triggering event already happened. It matters more than macro commentary because the contract is path-dependent and exchange-specific.

## Possible impact on the question

If the Binance print is valid and the rule note is accurate, the decisive catalyst has already occurred and the remaining timeline mostly concerns administrative settlement rather than market repricing on fundamentals.

## Reliability notes

High relevance and high practical credibility because the evidence aligns the market rule with exchange data. Independence is moderate rather than high because both strands ultimately point back to Binance, but this is still stronger than using the live market price alone.