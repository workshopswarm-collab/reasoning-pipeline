---
type: source_note
case_key: case-20260416-66f6f47e
dispatch_id: dispatch-case-20260416-66f6f47e-20260416T141457Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin-threshold-daily-close
entity: btc
topic: Binance BTC/USDT spot level and contract resolution mechanics for Apr 21 noon ET close-above-72000 market
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21 close above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance spot API + Polymarket market rules page
source_type: primary_market_and_resolution_sources
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-66f6f47e/researcher-analyses/2026-04-16/dispatch-case-20260416-66f6f47e-20260416T141457Z/personas/catalyst-hunter.md
tags: [source-note, binance, polymarket, btc, resolution-source]
---

# Summary

This note captures the governing resolution mechanics and the current/very recent Binance BTC/USDT price context relevant to the Apr 21 noon ET close-above-72000 contract.

## Key facts extracted

- Polymarket rules state the market resolves **Yes** if the Binance BTC/USDT **1-minute candle for 12:00 ET on Apr 21** has a final **Close** above 72000.
- The market is **not** about touch/high, not about another exchange, and not about a daily close.
- Binance ticker spot fetched on 2026-04-16 showed BTCUSDT at **73608.41**.
- Binance daily candles for Apr 7-Apr 16 show BTC trading mostly above 72000 recently, with daily highs of **74900** on Apr 13, **76038** on Apr 14, and **75425** on Apr 15.
- Daily closes from Binance were **74417.99** on Apr 13, **74131.55** on Apr 14, and **74809.99** on Apr 15.
- Apr 16 intraday ticker remained above the 72000 threshold at fetch time, but final contract settlement depends only on the **Apr 21 12:00 ET 1-minute close**.

## Evidence directly stated by source

- From Polymarket rules: resolution source is Binance BTC/USDT with "1m" and "Candles" selected; winning condition is final Close higher than the specified threshold.
- From Binance API: ticker price 73608.41000000 at fetch time.
- From Binance daily kline data: BTC has recently traded in a roughly 70.5k-76.0k range over the last 10 daily candles.

## What is uncertain

- Whether BTC remains above 72000 specifically at **Apr 21 12:00 ET**.
- Whether any macro or crypto-specific event between now and then causes a directional move of more than ~2%.
- Whether Binance-specific print at that minute diverges materially from broader spot consensus.

## Why this source may matter

This is the core direct-evidence package for the case: it identifies the exact settlement mechanism and shows current threshold distance on the governing venue.

## Possible impact on the question

The direct source package supports a baseline leaning Yes because BTC is currently above 72000 on the governing venue and has spent multiple recent sessions above that level. But because the contract is a **single-minute close at a fixed future timestamp**, not a touch market, the main remaining risk is a modest drawdown into Apr 21 noon ET.

## Reliability notes

- Polymarket rules page is the authoritative contract wording surface available to traders.
- Binance is the governing source of truth for the actual settlement print.
- Binance API is stronger for current context than secondary market commentary because it uses the exact venue/pair named in the rules.
- This does **not** itself prove the Apr 21 settlement print; it only verifies mechanism and current threshold context.
