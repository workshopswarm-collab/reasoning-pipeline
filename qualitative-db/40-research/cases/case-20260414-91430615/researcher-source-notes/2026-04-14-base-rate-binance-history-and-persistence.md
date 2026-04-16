---
type: source_note
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 70000?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT daily and noon-ET 1m klines; local persistence calculations
source_type: primary_data_plus_derived_analysis
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=120
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-91430615/researcher-analyses/2026-04-14/dispatch-case-20260414-91430615-20260414T235247Z/personas/base-rate.md]
tags: [binance, daily-klines, base-rate, persistence, threshold]
---

# Summary

Recent Binance history supports a generally favorable outside view for BTC staying above 70,000 over a short horizon, but not quite as favorable as the market’s 90% implies. The key base-rate distinction is that persistence is high when BTC is already meaningfully above 70,000, but weaker when it is only modestly above the threshold.

## Key facts extracted

- From the last 120 Binance daily closes, 76 closed above 70,000 (63.3%).
- From the last 30 daily closes, 15 were above 70,000 (50.0%).
- From the last 14 daily closes, 8 were above 70,000 (57.1%).
- Looking across the 120-day sample, when a day closed above 70,000, the close 4 days later was still above 70,000 in 59 of 72 cases (81.9%).
- Restricting to starts only slightly above threshold (daily close between 70,000 and 74,200), the close 4 days later remained above 70,000 in 10 of 21 cases (47.6%).
- Recent noon-ET 1-minute BTCUSDT closes on Binance for 2026-04-08 through 2026-04-13 were: 71,329.98; 72,342.21; 72,476.00; 72,865.57; 70,860.00; 71,902.91, with only 2026-04-07 below threshold at 68,187.74.

## Evidence directly stated by source

- The Binance daily and 1-minute kline endpoints directly provide the historical close levels.

## What is uncertain

- The persistence calculations are derived from a short recent sample and may reflect one regime rather than a durable long-run base rate.
- Daily-close persistence is an imperfect proxy for the exact contract, which is one specific noon-ET 1-minute candle, though the recent noon-ET sample suggests the proxy is directionally reasonable.

## Why this source may matter

This source gives the main outside-view prior for whether a BTC price already above 70,000 is likely to remain above that threshold four days later.

## Possible impact on the question

The historical frequency argues against an extreme bearish base-rate call. But it also suggests some caution against blindly accepting a 90% market if one uses broader recent persistence rather than momentum-heavy narrative framing. A disciplined base-rate estimate likely belongs below the market but still comfortably above 50%.

## Reliability notes

High reliability for the underlying Binance price history. Moderate reliability for the derived persistence inference because it is sample-dependent and uses daily closes as a proxy for the precise noon-ET one-minute settlement mechanic.
