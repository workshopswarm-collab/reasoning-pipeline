---
type: source_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: spot-market-thresholds
entity: ethereum
topic: Binance ETH/USDT governing source spot check before Apr 17 noon ET resolution
question: Will the Binance ETH/USDT 1-minute candle close at 12:00 ET on Apr 17, 2026 be above 2200?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance Spot API ETHUSDT 1m klines and ticker
source_type: primary_market_data
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=5
source_date: 2026-04-16T14:33:00Z
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/catalyst-hunter.md
tags: [binance, ethusdt, governing-source, threshold-market, 1m-candle]
---

# Summary

Direct governing-source spot check from Binance API shows ETH/USDT trading above the 2200 threshold on Apr 16 around 10:30-10:33 ET, but this does **not** settle the contract because the market resolves on the specific Binance 1-minute candle close at 12:00 ET on Apr 17.

## Key facts extracted

- Binance ticker returned `2299.70000000` for `ETHUSDT`.
- Recent Binance 1-minute klines at 14:30-14:33 UTC (10:30-10:33 ET) had closes of approximately `2298.80`, `2297.96`, `2297.97`, and `2299.70`.
- The threshold is only about 100 points below current Binance spot, or roughly 4.3%.
- Because Binance is a 24/7 venue, there is no overnight market-close gap between now and resolution.

## Evidence directly stated by source

- The market's governing venue, Binance, currently prices ETH/USDT above 2200.
- The Binance feed used for resolution can be queried directly and is behaving normally in this spot check.
- Short-horizon realized volatility over even a few minutes is enough to move ETH by multiple dollars; being ~100 points above threshold one day before resolution is directionally supportive but not dispositive.

## What is uncertain

- The contract settles on the **final close** of the Binance 1-minute candle stamped 12:00 ET on Apr 17, not on the current price, current high, or any other venue.
- A rapid drawdown of more than ~4% before the settlement minute remains plausible in crypto.
- This spot check does not by itself prove the exact timezone labeling on the Binance UI used by Polymarket, though the assignment text specifies ET/noon and Binance 1m candles.

## Why this source may matter

This is the clearest direct evidence for the governing source of truth and for the current distance-from-threshold. It materially constrains how bearish one can be one day before expiry.

## Possible impact on the question

This source pushes probability upward because ETH is currently well above the line on the exact settlement venue. It does not eliminate downside risk, but it means the market only needs ETH to avoid a >4% drop by the settlement minute.

## Reliability notes

- High credibility for current spot price because Binance is the explicit resolution venue.
- Limited settlement completeness: current Binance price is direct evidence about starting state, not direct proof of the Apr 17 12:00 ET close.
- Important verification distinction: the event is **not yet verified** because settlement time has not arrived, not because the governing surface is unavailable.