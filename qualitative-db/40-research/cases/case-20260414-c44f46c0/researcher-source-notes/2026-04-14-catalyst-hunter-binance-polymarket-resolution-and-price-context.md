---
type: source_note
case_key: case-20260414-c44f46c0
dispatch_id: dispatch-case-20260414-c44f46c0-20260414T185449Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-19 resolution mechanics and current price context
question: Will the price of Bitcoin be above $68,000 on April 19?
driver: liquidity
date_created: 2026-04-14
source_name: Polymarket market page and Binance BTCUSDT API/source reference
source_type: market rules page plus exchange API
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin, binance]
related_drivers: [liquidity, operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-c44f46c0/researcher-analyses/2026-04-14/dispatch-case-20260414-c44f46c0-20260414T185449Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, resolution, btc-price, catalyst-calendar]
---

# Summary

This note captures the contract mechanics and near-term price context for the April 19 BTC > 68k market. The key direct facts are that resolution depends specifically on the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 19, and that as of April 14 Binance spot is already materially above the threshold.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 19 has a final close strictly higher than 68,000.
- The source of truth is Binance, not a composite index and not another exchange or BTC/USD pair.
- Price precision is whatever Binance displays for the source candle.
- The Polymarket page showed the 68,000 line trading around 95.5% Yes at fetch time.
- Binance public API returned BTCUSDT last price of 74,093.41 on 2026-04-14 during this run.
- Binance daily candles over the prior week show closes between roughly 70.7k and 74.4k, i.e. consistently above 68k.

## Evidence directly stated by source

From Polymarket rules:
- Yes requires the Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date to close above the strike.
- Resolution is tied to Binance candle data specifically.

From Binance API responses gathered during this run:
- Current BTCUSDT spot was 74,093.41.
- Recent daily closes remained above 68,000.

## What is uncertain

- The exact April 19 12:00 ET candle is still five days away, so short-horizon volatility could still pull BTC below 68k by the settlement minute.
- Market-moving macro or crypto-specific headlines could still trigger a large downside move before resolution.
- Binance front-end rendering could differ cosmetically from API formatting, though the contract points to Binance as the governing venue and the broad price level is unambiguous.

## Why this source may matter

This is the governing source-of-truth surface plus the most relevant direct price context. It defines the exact conditions that all must hold for a Yes resolution and anchors how far BTC currently sits above the threshold.

## Possible impact on the question

The note supports a high Yes probability because BTC is already ~6k above the line and has recently closed above it consistently, but it also clarifies the path dependency: only the noon ET Binance 1-minute close on April 19 matters, so near-term catalysts that could trigger a sharp drawdown remain the real risk.

## Reliability notes

- Polymarket rules page is authoritative for contract wording but not settlement itself; settlement references Binance as the venue-level truth source.
- Binance API is a strong direct contextual source for current price and recent realized range.
- Evidence independence is moderate rather than high because the contract itself references Binance and the contextual price series is also from Binance, though this is appropriate for a venue-specific market.