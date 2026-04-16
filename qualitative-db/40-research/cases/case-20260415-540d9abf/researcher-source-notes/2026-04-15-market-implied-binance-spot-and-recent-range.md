---
type: source_note
case_key: case-20260415-540d9abf
dispatch_id: dispatch-case-20260415-540d9abf-20260415T234706Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: solana
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle close above 80 on April 19, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Binance API spot and recent candles
source_type: exchange API
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-540d9abf/researcher-analyses/2026-04-15/dispatch-case-20260415-540d9abf-20260415T234706Z/personas/market-implied.md]
tags: [binance, spot-price, klines, recent-range, verification]
---

# Summary

This source note captures direct Binance pricing evidence used to test whether the market's ~90% probability for SOL > 80 at Apr 19 noon ET looks broadly efficient.

## Key facts extracted

- Binance spot ticker for SOLUSDT was 84.87 at fetch time on Apr 15.
- Binance 24h stats showed lastPrice 84.86, low 82.65, high 85.83.
- Recent 1d candles over the prior week showed daily closes mostly in the low-to-mid 80s, with only one close near 81.53 and none below 80 in the returned sample.
- The recent 1m candles fetched around the same time also clustered near 84.84-84.87.

## Evidence directly stated by source

From Binance ticker/24hr endpoints at fetch time:
- last/spot price about 84.86-84.87
- 24h low 82.65
- 24h high 85.83

From Binance 1d klines sample:
- recent daily closes in sample: 83.33, 84.83, 84.93, 81.53, 86.51, 83.72, 84.86

## What is uncertain

- Current spot and recent history do not directly settle the Apr 19 noon print; they are contextual evidence only.
- Crypto can move sharply over several days, so recent range evidence supports but does not guarantee the market view.
- API timestamps are in exchange-standard Unix milliseconds and require mapping to ET for final settlement interpretation.

## Why this source may matter

If the market prices >80 at around 90% while Binance spot is already near 84.9 and recent lows stayed materially above 80, then the market's confidence is at least understandable. The market appears to be pricing that SOL has a modest cushion above the strike rather than needing a major rally.

## Possible impact on the question

This evidence supports the view that the market is probably incorporating a simple but strong fact pattern: SOL is already above the strike by about 6%, and recent Binance trading has not been threatening 80. That makes a noon Apr 19 close above 80 plausibly likely, though not certain.

## Reliability notes

High-quality direct exchange data for current and recent prices. Strong for context and verification, but still not a direct settlement print for Apr 19 noon ET.