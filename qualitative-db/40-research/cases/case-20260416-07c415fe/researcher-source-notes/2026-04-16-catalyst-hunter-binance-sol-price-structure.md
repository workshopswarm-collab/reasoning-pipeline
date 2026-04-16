---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: tokens
entity: sol
topic: sol-above-80-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 80?
driver: reliability
date_created: 2026-04-15T23:22:00-04:00
source_name: Binance API SOLUSDT spot data
source_type: exchange market data
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=20
source_date: 2026-04-16
credibility: high
recency: high
stance: bullish-above-80
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-07c415fe/researcher-analyses/2026-04-16/dispatch-case-20260416-07c415fe-20260416T031541Z/personas/catalyst-hunter.md]
tags: [binance, spot-price, catalyst-calendar, resolution-source]
---

# Summary

Binance spot data is both the market's governing resolution source and the strongest direct evidence base for this case. As of late 2026-04-15 / early 2026-04-16 ET, SOL/USDT was trading about 85.43 on Binance, well above the 80 threshold, and daily closes since 2026-04-03 have all been above 80 except for the 2026-04-12 close at 81.53, still comfortably above the strike.

## Key facts extracted

- Binance ticker price at retrieval: 85.43 for SOLUSDT.
- Daily closes from 2026-04-03 through 2026-04-16 were: 80.40, 80.83, 81.89, 80.03, 85.56, 82.57, 83.33, 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, 85.39.
- 72 recent hourly closes were all above 80.
- Recent 72-hour range from Binance hourly data was roughly 81.73 to 87.29.
- The market resolves on the Binance 1-minute candle close at 12:00 ET on 2026-04-19, so intraday spot behavior near that timestamp is what matters rather than daily settlement on other venues.

## Evidence directly stated by source

- Binance API reported current SOLUSDT price near 85.43.
- Binance kline data showed sustained trading above 80 over recent days and hours.

## What is uncertain

- A three-day crypto drawdown could still take SOL below 80 by the exact noon ET resolution candle.
- Binance API spot snapshots do not by themselves prove what the exact 12:00 ET one-minute candle on 2026-04-19 will be.

## Why this source may matter

This is the highest-value source because Binance is the explicit source of truth for settlement. It also gives the best direct read on whether the current cushion above 80 is large or fragile.

## Possible impact on the question

Sustained trading in the mid-80s makes a Yes resolution more likely than the market's already-high 92% baseline, unless a material crypto-wide risk-off move hits before Sunday noon ET.

## Reliability notes

- High credibility for direct pricing because Binance is the named settlement venue.
- Lower usefulness for catalysts beyond price path itself; this source describes realized trading, not upcoming news triggers.
